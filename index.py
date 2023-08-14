from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget, QPushButton
from PyQt5.QtGui import QFont, QPixmap, QIcon
import sys
import os

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.WelcomedWindow()
        
    def WelcomedWindow(self):
        screen_size = QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())#establecemos la geometria acorde al tamaño de nuestra ventana
        self.setWindowFlag(Qt.FramelessWindowHint)#ocultamos la barre donde estabelcemos el titulo
        labelImg = QLabel(self)
        pixmap1 = QPixmap('./fondo pantalla 4.jpg')#establecemos fodo de pantalla
        scaled_images1 = pixmap1.scaled(screen_size.width(), screen_size.height())#Rezise to images user
        labelImg.setPixmap(scaled_images1)
        labelImg.setGeometry(0, 0, scaled_images1.width(), scaled_images1.height())
        self.backGroundImage()#inicializamos el recuadro detras del userImage
        self.userImage()#Iicializamos el user image
        self.upperLeftButtons()#iicializamos los botoes de cerrado y minimizar
        self.InteractiveButtons()#inicializamos el boton de inicio
    
    def backGroundImage(self):
        
        screen_size_for_frame = QDesktopWidget().screenGeometry(-1)
        container_label = QLabel(self)
        container_label.setStyleSheet(
            '''border: 2px solid black;
               border-radius: 20px;
               background-color: rgba(31, 80, 95, 196;)
            '''
            )#background-color: #B6FBF5; --> el color claro
        #background-color: rgba(78, 179, 207, 198;) --> seguda opcion
        #background-color: rgba(31, 80, 95, 196;)
        container_label.setGeometry(int(screen_size_for_frame.width()/2)-260,int(screen_size_for_frame.height()/2)-450,550,830)
        #container_label.move(int((screen_size_for_frame.width())/2), int((screen_size_for_frame.height())/2))

    def userImage(self):
        path = './images/'#Este es el path de las imagenes que se usaran en la aplicacion
        if os.path.isdir(path):
            user_images = path + 'user.png'
            try:
                with open(user_images):
                    perfil_label = QLabel(self)
                    pixmap = QPixmap(user_images)
                    scaled_images = pixmap.scaled(200,200)#Rezise to images user
                    perfil_label.setPixmap(scaled_images)
                    #screen_size_for_image = QDesktopWidget().screenGeometry(-1)
                    perfil_label.move(870, 110)#870, 110
                    perfil_label.raise_()
                    #container_label.setBuddy(perfil_label)
                    # layout.addWidget(perfil_label)

            except FileNotFoundError as e:
                print("Dosn't found the images")

    def upperLeftButtons(self):

        path_close = './cerrar.png'
        path_minimize = './minimizar-signo.png'
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

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)#deshabilitamos los botones predeterminados de minimizar
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)#deshabilitamos los botones predeterminados de cierre
        

    def InteractiveButtons(self):
        screen_size_for_button = QDesktopWidget().screenGeometry(-1)
        startSystemButton = QPushButton("Iniciar sistema",self)
        startSystemButton.setFont(QFont('Helvetica', 20))
        startSystemButton.setFixedSize(315,70)
        startSystemButton.setStyleSheet(
            '''
            QPushButton {
                background-color: #B6E1FB;
                border: 2px solid blue;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #C4DAEF;  /* color del botón cuando el ratón está encima */
                color: black;  /* color del texto cuando el ratón está encima */
            }
            QPushButton:pressed {
                background-color: #5C8DBD;  /* color del botón cuando está presionado */
                color: black;  /* color del texto cuando está presionado */
            }
            ''')
        startSystemButton.move(int(screen_size_for_button.width()/2)-150, int(screen_size_for_button.height()/2))
        startSystemButton.clicked.connect(self.secondWidow)
    
    def secondWidow(self):
        from SecondWindow import Second_Window
        # Crear instancia de la segunda ventana
        self.second_window = Second_Window()
        # Ocultar la ventana actual
        self.hide()
        # Mostrar la segunda ventana
        self.second_window.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())