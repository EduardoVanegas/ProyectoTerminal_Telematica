from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QDialog, QStyle
from PyQt5.QtGui import QFont, QPixmap, QIcon, QImage
from datetime import datetime
import os

class AutoClosingDialog(QDialog):
    def __init__(self, message, timeout=2, parent=None):
        super(AutoClosingDialog, self).__init__(parent)

        self.setWindowTitle("Alert Window")
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.setWindowIcon(QIcon(QApplication.style().standardIcon(QStyle.SP_MessageBoxWarning)))
        layout = QVBoxLayout(self)
        label_alert = QLabel(message)
        font = QFont()
        font.setPointSize(15)
        label_alert.setFont(font)
        layout.addWidget(label_alert)
        QTimer.singleShot(timeout * 1000, self.accept)

class Second_Window(QWidget):
    stopSignal = pyqtSignal(bool)  # Nueva señal

    def __init__(self):
        super(Second_Window, self).__init__()
        self.OperationalWidow()
        self.image_label = QLabel(self)
        self.detected_images_manually = QLabel(self)
        self.image_label_automatic = QLabel(self)
        self.detected_images_automatic = QLabel(self)
        self.relative_path = ''
        self.ventana_emergente = QMessageBox()
        self.ventana_emergente_video = QMessageBox()
        self.label_video = QLabel(self)
        self.StopButton = QPushButton('Paro', self)#definicion del boton de paro
        self.StopButton.hide()
        self.class_video = int
        self.contador = 0#Para evitar llenar de ventanas la aplicacion
          
    def OperationalWidow(self):
        screen_size = QDesktopWidget().screenGeometry(-1)#Obtenemos el tamño de la pantalla de la pc
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())#establecemos la geometria acorde al tamaño de nuestra ventana
        self.setWindowFlag(Qt.FramelessWindowHint)#ocultamos la barre donde estabelcemos el titulo
        labelImg = QLabel(self)
        pixmap1 = QPixmap('./fondo pantalla 3.jpg')#establecemos fodo de pantalla
        scaled_images1 = pixmap1.scaled(screen_size.width(), screen_size.height())#Rezise to images user
        labelImg.setPixmap(scaled_images1)
        labelImg.setGeometry(0, 0, scaled_images1.width(), scaled_images1.height())
        #Aqui comenzamos a definir los atributos de la ventana
        self.LeftCanva()
        self.upperLeftButtons()
        self.LogoIcon()
        self.OptionsButtons()
        
    
    def upperLeftButtons(self):

        path_close = './cerrar.png'
        path_minimize = './minimizar-signo.png'
        path_return = './return.png'
        position_height_X = 30
        position_widht_X = 10

        ''' Para boton de cierre '''
        if os.path.isfile(path_close):
            with open(path_close):
                X_boton = QPushButton("", self)
                X_boton.setIcon(QIcon(path_close))
                X_boton.setFixedSize(70, 45)#establecemos el tamaño del boton close
                X_boton.setStyleSheet('background-color: transparent;')
        else:
            X_boton = QPushButton("X", self)
            X_boton.setFont(QFont('Arial', 20))
            X_boton.setFixedSize(70, 45)#establecemos el tamaño del boton close
            X_boton.setStyleSheet('background-color: transparent;')

        X_boton.move(position_widht_X, position_height_X)
        X_boton.clicked.connect(self.close)

        ''' Para boton de minimizar '''
        if os.path.isfile(path_minimize):
            with open(path_minimize):
                minimize_button = QPushButton("", self)
                minimize_button.setIcon(QIcon(path_minimize))
                minimize_button.setFixedSize(70, 45)#establecemos el tamaño del boton minimizar
                minimize_button.setStyleSheet('background-color: transparent;')
        else:
            minimize_button = QPushButton("-", self)
            minimize_button.setFont(QFont('Arial', 20))
            minimize_button.setFixedSize(70, 45)#establecemos el tamaño del boton minimizar
            minimize_button.setStyleSheet('background-color: transparent;')

        minimize_button.move((position_widht_X*10), (position_height_X))
        minimize_button.clicked.connect(self.showMinimized)

        ''' para el boton de return '''
        if os.path.isfile(path_return):
            with open(path_return):
                return_button = QPushButton(self)
                return_button.setIcon(QIcon(path_return))
                return_button.setFixedSize(70, 45)
                return_button.setStyleSheet('background-color: transparent;')
        else:
            return_button = QPushButton("<--", self)
            return_button.setFont(QFont('Arial', 20))
            return_button.setFixedSize(70, 45)
            return_button.setStyleSheet('background-color: transparent;')
        
        return_button.move((position_widht_X*20), (position_height_X))
        return_button.clicked.connect(self.returned_page)

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)#deshabilitamos los botones predeterminados de minimizar
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)#deshabilitamos los botones predeterminados de cierre

    def returned_page(self):
        from index import MainWindow
        # Crear instancia de la segunda ventana
        self.first_window = MainWindow()
        # Ocultar la ventana actual
        self.hide()
        # Mostrar la segunda ventana
        self.first_window.show()
    
    def LeftCanva(self):
        scrren_size_for_canva = QDesktopWidget().screenGeometry(-1)
        container_label = QLabel(self)
        container_label.setStyleSheet(
            '''border: 2px solid black;
               border-top-right-radius: 20px;
               border-bottom-right-radius: 20px; 
               background-color: rgba(78, 179, 207, 108;)
            '''
            )#los primero tres de rdba es el color rgb, el ultimo es alpha, o sea la transparencia
        container_label.setGeometry(0, 0, 450, scrren_size_for_canva.width())

    def LogoIcon(self):
        icon_label = QLabel(self)
        upiita_icon_logo = './upiita.png'
        with open(upiita_icon_logo):
            pixmap = QPixmap(upiita_icon_logo)
            scaled_pixmap = pixmap.scaled(300,250)
            icon_label.setPixmap(scaled_pixmap)
        icon_label.move(70,130)

    def OptionsButtons(self):
        height = 30
        width = 420
        ''' Comenzamos con el label y boton de folder '''
        label_folder = QLabel(self)
        folder_images = './folder.png'
        with open(folder_images):
            pixmap = QPixmap(folder_images)
            scaled_images_folder =pixmap.scaled(80,80)#ajustamos el tamaño de la imagen
            label_folder.setPixmap(scaled_images_folder)#aplicamos la imagen
        label_folder.move(height,width)#-desplazamos en coordenadas x,y
        #
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        folder_button = QPushButton("Abrir archivos", self)
        folder_button.setFont(QFont("Helvetica", 20))#Establecemois la fuente del boton
        folder_button.setFixedSize(285,70)#Establecemos el tamaño del boton
        folder_button.setStyleSheet(
            '''
            QPushButton {
            background-color: transparent;
            border: 2px solid black;
            border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #4D8AC6;  /* color del botón cuando el ratón está encima */
                color: black;  /* color del texto cuando el ratón está encima */
            }
            QPushButton:pressed {
                background-color: #8FBDEB;  /* color del botón cuando está presionado */
                color: black;  /* color del texto cuando está presionado */
            }
            ''')#Damos caracterisitcas al boton
        folder_button.move(int(height*4.2), width)#Desplazamos boton en coordenadas x,y
        folder_button.clicked.connect(self.Folder_actions)#Accion que tomara el boton de folder
        # layout.addWidget(folder_button)

        ''' comenzamos con el boton "inicio manual" '''
        label_start_manually = QLabel(self)
        play_images = './play-button.png'
        with open(play_images):
            pixmap_1 = QPixmap(play_images)
            scaled_play_images= pixmap_1.scaled(80,80)
            label_start_manually.setPixmap(scaled_play_images)
        label_start_manually.move(height, width+150)
        start_manually_button = QPushButton("Inicio manual",self)
        start_manually_button.setFont(QFont("Helvetica", 20))
        start_manually_button.setFixedSize(285,70)
        start_manually_button.setStyleSheet(
            '''
            QPushButton {
            background-color: transparent;
            border: 2px solid black;
            border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #4D8AC6;  /* color del botón cuando el ratón está encima */
                color: black;  /* color del texto cuando el ratón está encima */
            }
            QPushButton:pressed {
                background-color: #8FBDEB;  /* color del botón cuando está presionado */
                color: black;  /* color del texto cuando está presionado */
            }
            ''')
        start_manually_button.move(int(height*4.2), width+150)
        start_manually_button.clicked.connect(self.Start_manually_actions)#Accion que tomara el boton inicio manual

        ''' Comenzamos con el boton inicio automatico '''
        label_start_automatic = QLabel(self)
        with open(play_images):
            pixmap_2 = QPixmap(play_images)
            scaled_play_images = pixmap_2.scaled(80,80)
            label_start_automatic.setPixmap(scaled_play_images)
        label_start_automatic.move(height, width+300)
        start_automatic_button = QPushButton("Inicio automatico", self)
        start_automatic_button.setFont(QFont("Helvetica", 20))
        start_automatic_button.setFixedSize(285,70)
        start_automatic_button.setStyleSheet(
            '''
            QPushButton {
            background-color: transparent;
            border: 2px solid black;
            border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #4D8AC6;  /* color del botón cuando el ratón está encima */
                color: black;  /* color del texto cuando el ratón está encima */
            }
            QPushButton:pressed {
                background-color: #8FBDEB;  /* color del botón cuando está presionado */
                color: black;  /* color del texto cuando está presionado */
            }
            ''')
        start_automatic_button.move(int(height*4.2), width+300)
        start_automatic_button.clicked.connect(self.Start_automatic_actions)

        ''' Comenzamos con el boton de web cam '''
        label_WebCam = QLabel(self)
        with open(play_images):
            pixmap_3 = QPixmap(play_images)
            scaled_play_images = pixmap_3.scaled(80,80)
            label_WebCam.setPixmap(scaled_play_images)
        label_WebCam.move(height, width+450)
        start_web_cam_button = QPushButton("Inicio de proceso", self)
        start_web_cam_button.setFont(QFont("Helvetica", 20))
        start_web_cam_button.setFixedSize(285,70)
        start_web_cam_button.setStyleSheet(
            '''
            QPushButton {
            background-color: transparent;
            border: 2px solid black;
            border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #4D8AC6;  /* color del botón cuando el ratón está encima */
                color: black;  /* color del texto cuando el ratón está encima */
            }
            QPushButton:pressed {
                background-color: #8FBDEB;  /* color del botón cuando está presionado */
                color: black;  /* color del texto cuando está presionado */
            }
            ''')
        start_web_cam_button.move(int(height*4.2), width+450)
        start_web_cam_button.clicked.connect(self.init_web_cam)


    def Folder_actions(self):#interaccion que hago con el boton para abril el folder
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'All Files (*);;Image Files (*.jpg *.png);;Video Files (*.mp4)', options=options)#Open images and videos
        
        if file_name:
            format_images = ['png', 'jpg']
            format_video = ['mp4']
            split_path = (file_name.split('/')[-1]).split('.')[1]

            if split_path in format_images:
                self.StopButton.hide()
                pixmap = QPixmap(file_name)
                scaled_open_images = pixmap.scaled(450,450)
                self.image_label.setPixmap(scaled_open_images)
                self.image_label.adjustSize() 
                self.image_label.setStyleSheet(
                    '''border: 20px solid #E74A47;
                    ''')
                self.image_label.move(550,200)
                self.image_label.show()
                self.relative_path = file_name#Asignamos al path para que el boton de inicio automatico lo pueda leer

            elif split_path in format_video:
                self.image_label.hide()
                self.detected_images_manually.hide()
                print("Se ha abierto un video")
                self.relative_path = file_name#Asignamos al path para que el boton de inicio automatico lo pueda leer
            else:
                self.ventana_emergente.setWindowTitle("Window Warning")
                self.ventana_emergente.setText("Archivo no compatible, solo .png, .jpg, .mp4")
                self.ventana_emergente.setIcon(QMessageBox.Warning)
                self.ventana_emergente.exec_()
                self.relative_path = ''#Asignamos al path para que el boton de inicio automatico lo pueda leer
        else:
            self.ventana_emergente.setWindowTitle("Window Warning")
            self.ventana_emergente.setText("No se selecciono ningun archivo")
            self.ventana_emergente.setIcon(QMessageBox.Warning)
            self.ventana_emergente.exec_()

    @pyqtSlot(int, str)
    def handleVarChange(self, var, kind):
        self.var = var
        self.type = kind
        print(f"Clase : {var}")
        self.contador = self.contador + var
        print(f"Tipo de video {kind}")

        self.StopButton.move(1020, 810)
        self.StopButton.setFixedSize(250,85)
        self.StopButton.setFont(QFont("Helvetica", 20))
        self.StopButton.setStyleSheet(''' 
            QPushButton {
            background-color: transparent;
            border: 2px solid black;
            border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #4D8AC6;  /* color del botón cuando el ratón está encima */
                color: black;  /* color del texto cuando el ratón está encima */
            }
            QPushButton:pressed {
                background-color: #8FBDEB;  /* color del botón cuando está presionado */
                color: black;  /* color del texto cuando está presionado */
            }
        ''')
        # self.stopSignal.connect(self.th.stop)
        # self.button.clicked.connect(lambda: self.stopSignal.emit(False))
        self.StopButton.clicked.connect(self.stop_clicked)
        self.StopButton.show()
        if self.var == 0:
            pass
        elif self.var == 1 and len(kind)>1:#Para los videos que se habran
            # if self.contador % 1 == 0:
            hora_actual = datetime.now().time()
            hora_formateada = hora_actual.strftime("%H:%M:%S")[0:8]
            dialog = AutoClosingDialog(f"Producto erroneo, hora: {hora_formateada}", timeout=1, parent=self)
            dialog.show()
        elif self.var == 1 and len(kind) == 1:#Para webcam
            if self.contador % 25 == 0:
                hora_actual = datetime.now().time()
                hora_formateada = hora_actual.strftime("%H:%M:%S")[0:8]
                dialog = AutoClosingDialog(f"Producto erroneo, hora: {hora_formateada}", timeout=1, parent=self)
                dialog.show()

    @pyqtSlot(bool)
    def status(self, status):
        self.VideoStatus = status
        #print(status) #Me dice si es true o false para detener el video
        match status:
            case True:
                pass
            case False:
                self.label_video.hide()#ocultamos las ventanas al finalizar
                self.StopButton.hide()
                self.ventana_emergente_video.hide()#Si no cerramos la ventana emergente, aqui la ocultamos
                self.ventana_emergente.setWindowTitle("Success Window")#Se muestra si el proceso se ha finalizado
                self.ventana_emergente.setText("Proceso finalizado")
                self.ventana_emergente.setIcon(QMessageBox.Information)
                self.ventana_emergente.exec_()
        
    def stop_clicked(self):
        self.stopSignal.connect(self.th.stop)
        self.stopSignal.emit(False)

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label_video.setPixmap(QPixmap.fromImage(image))
       
    def Start_manually_actions(self):
        from detection import ManuallyDetection, Thread

        if self.relative_path == '':#se define para cuando no hay seleccion de imagenes
            #ocultamos labels
            self.image_label.hide()
            self.detected_images_manually.hide()
            self.ventana_emergente.setWindowTitle("Window Warning")
            self.ventana_emergente.setText("Aun no has seleccionado una imagen o video")
            self.ventana_emergente.setIcon(QMessageBox.Warning)
            self.ventana_emergente.exec_()
        else:#Cuando se haya elegido una imagen o video
            format_images = ['png', 'jpg']
            split_path = (self.relative_path.split('/')[-1]).split('.')[1]
            if split_path in format_images:
              
                obj_model = ManuallyDetection(self.relative_path)
                classes, path_predict = obj_model.getDetection()#obtenemos path y clase de la imagen

                with open(path_predict):
                    pixmap = QPixmap(path_predict)
                    scaled_predict_images = pixmap.scaled(450, 450)
                    self.detected_images_manually.setPixmap(scaled_predict_images)
                    self.detected_images_manually.adjustSize()
                    self.detected_images_manually.setStyleSheet('''
                        border: 20px solid #E74A47;
                    ''')
                self.detected_images_manually.move(1250, 200)
                self.detected_images_manually.show()
                #Muestra de las alarmas 
                match classes:
                    case 0:
                        print("La deteccion actual es \"buena\"".center(50, "-"))
                    case 1:
                        print("La deteccion actual es \"mala\"".center(50, "-"))
                        hora_actual = datetime.now().time()
                        hora_formateada = hora_actual.strftime("%H:%M:%S")[0:8]
                        self.ventana_emergente.setWindowTitle("Alert Window")
                        self.ventana_emergente.setText(f"Producto erroneo, hora: {hora_formateada}")
                        self.ventana_emergente.setIcon(QMessageBox.Warning)
                        self.ventana_emergente.exec_()
                    case _:
                        pass
            ##### AQUI EMPEZAMOS A DEFINIR LO DEL VIDEO ######
            else:
                self.contador = 0
                self.label_video.move(750,200)
                self.label_video.resize(740, 580)#Estetamaño se debe de modificar igual que en la funcio thread, en la parte de scaled
                self.label_video.setStyleSheet('''
                        border: 20px solid #E74A47;
                    ''')
                self.label_video.show()
                self.th = Thread(self.relative_path, self)
                self.th.varChanged.connect(self.handleVarChange)
                self.th.changePixmap.connect(self.setImage)
                self.th.status_cam.connect(self.status)
                self.th.start()
                self.show()
            self.relative_path = ''#Terminado lo hago nulo para que no provoque errores
                
    def Start_automatic_actions(self):
        from detection import AutomaticDetection, ManuallyDetection

        self.detected_images_manually.hide()#ocultamos el label de la prediccion cada vez que se habra otra imagen
        self.image_label.hide()
        self.label_video.hide()#ocultamos el label del video
        self.StopButton.hide()#ocultamos el boton del video

        ''' seleccionamos el folder donde vienen el conjunto de pastillas '''
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_name = QFileDialog.getExistingDirectory(self, 'Seleccione la carpeta', '', options=options)

        if folder_name:
            ''' obtenemos las lista de las imagenes que estan dentro del folder '''
            object_list = AutomaticDetection(folder_name)
            list_of_images = object_list.getListOfImagesFiles()
            # print(list_of_images)
            ''' Recorremos Todo el conjunto de imagenes '''
            for x in range(0, int(len(list_of_images)/2)):
                obj_model = ManuallyDetection(list_of_images[x])
                classes, path_predict = obj_model.getDetection()#obtenemos path y clase de la imagen
                with open(list_of_images[x]):
                    #print(path)
                    pixmap = QPixmap(list_of_images[x])
                    scaled_open_images = pixmap.scaled(450,450)
                    self.image_label_automatic.setPixmap(scaled_open_images)
                    self.image_label_automatic.adjustSize() 
                    self.image_label_automatic.setStyleSheet(
                        '''border: 20px solid #E74A47;
                        ''')
                self.image_label_automatic.move(550,200)
                self.image_label_automatic.show()
                # time.sleep(2)#dejamos por dos segundos para simular un retraso
                with open(path_predict):
                    pixmap_1 = QPixmap(path_predict)
                    scaled_predict_images_A = pixmap_1.scaled(450, 450)
                    self.detected_images_automatic.setPixmap(scaled_predict_images_A)
                    self.detected_images_automatic.adjustSize()
                    self.detected_images_automatic.setStyleSheet('''
                        border: 20px solid #E74A47;
                    ''')
                self.detected_images_automatic.move(1250, 200)
                self.detected_images_automatic.show()

                QApplication.processEvents()#Forzamos la muestra del evento de mostrar imagenes
                #Muestra de las alarmas 
                match classes:
                    case 0:
                        print("La deteccion actual es \"buena\"".center(50, "-"))
                    case 1:
                        print("La deteccion actual es \"mala\"".center(50, "-"))
                        hora_actual = datetime.now().time()
                        hora_formateada = hora_actual.strftime("%H:%M:%S")[0:8]
                        self.ventana_emergente.setWindowTitle("Alert Window")
                        self.ventana_emergente.setText(f"Producto erroneo, hora: {hora_formateada}")
                        self.ventana_emergente.setIcon(QMessageBox.Warning)
                        self.ventana_emergente.exec_()
                    case _:
                        pass

            self.image_label_automatic.hide()#ocultamos las ventanas al finalizar
            self.detected_images_automatic.hide()
            self.ventana_emergente.setWindowTitle("Success Window")#Se muestra si el proceso se ha finalizado
            self.ventana_emergente.setText("Proceso finalizado")
            self.ventana_emergente.setIcon(QMessageBox.Information)
            self.ventana_emergente.exec_()
        else:#por si no se selecciona alguna carpeta
            self.ventana_emergente.setWindowTitle("Window Warning")
            self.ventana_emergente.setText("Aun no has seleccionado la carpeta")
            self.ventana_emergente.setIcon(QMessageBox.Warning)
            self.ventana_emergente.exec_()
    
    def init_web_cam(self):
        self.label_video.hide()
        from detection import Thread
        self.label_video.move(750,200)
        self.label_video.resize(740, 580)#Estetamaño se debe de modificar igual que en la funcio thread, en la parte de scaled
        self.label_video.setStyleSheet('''
                border: 20px solid #E74A47;
            ''')
        self.label_video.show()
        self.StopButton.hide()
        self.th = Thread(0, self)
        self.th.varChanged.connect(self.handleVarChange)#Esta variable es la clase que manda yolo
        self.th.changePixmap.connect(self.setImage)#Esta clase manda el video
        self.th.status_cam.connect(self.status)
        self.th.start()
        self.show()
