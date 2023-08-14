from ultralytics import YOLO
import cv2
import os
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage
import time

class ManuallyDetection():
    def __init__(self, source):
        self._source = source

    @property
    def source(self):
        return self._source
    @source.setter
    def source(self, source):
        self._source = source     

    def getDetection(self):
        path_founded_trained_model = 'add/pathFolder/best.pt/model/'
        currentModel = 'bestLast.pt'

        path = 'add/directory/where/save/results/'#donde se guardaran las detecciones
        
        ''' define the trained model '''
        model = YOLO(path_founded_trained_model+currentModel)

        ''' deploy the results '''
        match self._source:
            case "0":
                results = model.predict(source="0", device = 0, show = True,  stream=True) 
            case _:
                ''' read image with openCV '''
                name_result = self._source.split('/')[-1]
                name_result = name_result.split('.')[0]+'_detected'#con este nombre se guardara la carpeta de la deteccion
                img = cv2.imread(self.source)
                results = model.predict(source=img,  save=True, conf = 0.7, device = 0, stream=True, project=path, name=name_result)
        ''' get the class detection '''        
        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
        print('\n')
        list_of_images = os.listdir(path+name_result)
        if len(list_of_images) == 1:
            totally_path = path+name_result+'/'+list_of_images[0]#obtenemos el path de la imagen con prediccion
        else:
            raise Exception("More files in a totally path, check it")

        if 1 in boxes.cls.tolist():
            return 1, totally_path
        elif 0 in boxes.cls.tolist():
            return 0, totally_path
        else:
            return 2, self.source #este caso es especial puesto que si se eleva el conf, no hara detecciones y por ende no habra una imagen que regresar 
   
class AutomaticDetection():
    def __init__(self, source):
        self._source = source
        self._list_of_all_images = []
    
    @property
    def source(self):
        return self._source
    @source.setter
    def source(self, source):
        self._source = source

    @property
    def list_of_all_images(self):
        return self._list_of_all_images
    @list_of_all_images.setter
    def list_of_all_images(self, list_of_all_images):
        self._list_of_all_images = list_of_all_images
        
    
    def getListOfImagesFiles(self):
        list_of_images = os.listdir(self.source)

        for image in list_of_images:
            path = self.source +"/"+image
            self._list_of_all_images.append(path)
        
        return self._list_of_all_images
    
###Clase para video
class Thread(QThread):

    changePixmap = pyqtSignal(QImage)
    varChanged = pyqtSignal(int, str)  # Nueva señal para la variable var
    status_cam = pyqtSignal(bool)

    def __init__(self, video_path, parent=None):
        QThread.__init__(self, parent=parent)
        self._video_path = video_path
        self.running = True

    @pyqtSlot(bool)
    def stop(self, running):
        self.running = running

    def run(self):
        model = YOLO('add/pathFolder/best.pt/model/')
        cap = cv2.VideoCapture(self._video_path)
        var = 0
        '''  variables para el conteo de los fps'''
        fps_counter = 0
        start_time = time.time()
        fotogramas_count = 0
        cont_buenas = 0
        cont_malas = 0

        while cap.isOpened() and self.running:

            success, frame = cap.read()
            if success and self.running:
                ''' registro de tiempo actual '''
                end_time = time.time()
                elapsed_time = end_time - start_time
                
                results = model.predict(frame, conf = 0.3, iou = 0.8, imgsz = 864, device = 0)
                for result in results:
                    boxes = result.boxes
                if 0 in boxes.cls.tolist() and 1 not in boxes.cls.tolist():
                    print(f"Se detecto pastilla excelente".center(50, "-"))
                    var = 0
                    cont_buenas += 1
                elif 1 in boxes.cls.tolist():
                    print(f"Se detecto pastilla erronea".center(50, "-"))
                    var = 1
                    cont_malas += 1
                self.varChanged.emit(var, str(self._video_path))  # Emitir la señal con la variable var y el resultado del videopath
                annotated_frame = results[0].plot()
                rgbImage = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(740, 580, Qt.IgnoreAspectRatio)
                self.changePixmap.emit(p) # emitir la señal de video
                fps_counter += 1
                fotogramas_count += 1
                # Mostrar FPS cada segundo
                if elapsed_time >= 1:
                    fps = fps_counter / elapsed_time
                    print("FPS: ", round(fps, 2))
                    # Reiniciar variables para el próximo segundo
                    fps_counter = 0
                    start_time = time.time()
                self.status_cam.emit(self.running)# emitir la señal de status(stop button)
            else:
                self.status_cam.emit(False)#cuando acabe el while, se limpia todo y aparece mensaje
                print("Video finalizado")
                break
        print(f"Cantidad de frames del video: {fotogramas_count}".center(50,'-'))
        print(f"Cantidad de detecciones marcadas como buenas: {cont_buenas}".center(50,'-'))
        print(f"Cantidad de detecciones marcadas como malas: {cont_malas}".center(50,'-'))