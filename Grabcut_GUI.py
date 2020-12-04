# -*- coding: utf-8 -*-
"""
Proyecto final, procesamiento de imagenes

@author: Andrea Ruiz, Sebastian Parrado & Pablo Mosquera
"""

import tkinter as tk # GUI
from tkinter.filedialog import askopenfilename # Buscar archivos en disco local
from PIL import Image # Para mostrar la imagen en la GUI
from PIL import ImageTk # Para mostrar la imagen en la GUI
import cv2 # Opencv
import numpy as np # Numpy

# App Frame
class AppFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
    
        # Variables globales
        self.image =  None  # Imagen
        self.state = True # Estado pantalla completa
        self.panelA = None # Panel A ventana
        self.panelB = None # Panel B ventana
        
        # Colores de la interfaz - Códigos de colores: https://htmlcolorcodes.com/es/
        """
        Morado
        
        self.but_bg = '#E188FD' # Fondo boton
        self.but_fg = '#55086D' # Letra boton
        self.wn_bg = '#F4E0FA'  # Fondo ventana
        self.wn_fg = '#55086D'  # Letra ventana
        """
        """
        Azul
        """
        self.but_bg = '#78CCEB' # Fondo boton
        self.but_fg = '#0B5E7D' # Letra boton
        self.wn_bg = '#E0F3FA'  # Fondo ventana
        self.wn_fg = '#0B5E7D'  # Letra ventana
        
        # Tamanio imagenes que se muestran en la GUI. Las imagenes son cuadradas
        self.tam = 600 
        
        # Posiciones y tamanios de los botones
        self.btn_posx = 1240 # Posicion x del boton
        self.btn_posy = 145 # Posicion y del primer bloque de botones
        self.btn_posy2 = 675 # Posicion y del segundo bloque de botones
        self.btn_w = 110 # Tamanio horizontal boton
        self.btn_h = 30 # Tamanio vertical boton
        
        # Funciones iniciales
        self.gui() # Función configuracion GUI
        self.select_reset() # Reiniciar variables
        
    # Funcion configuracion GUI
    def gui(self):
        """
        Textos en la ventana
        """        
        text = " " # Texto del label
        lbl0 = tk.Label(self, text=" ", font=("Arial Bold", 40)) # Configuracion label (ventana, texto, estilo y tamanio de letra)
        lbl0.place(x=0, y=0, width=1370, height=820) # Posicion y tamanio texto
        lbl0.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Proyecto final - Procesamiento de imágenes y visión" # Texto del label
        lbl1 = tk.Label(self, text=text, font=("Arial Bold", 35)) # Configuracion label (ventana, texto, estilo y tamanio de letra)
        lbl1.place(x=10, y=5, width=1340, height=60) # Posicion y tamanio texto
        lbl1.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Este proyecto consiste en realizar la segmentación de una imagen y ubicarla sobre un fondo, dichas imagenes se seleccionan desde  el disco duro del computador. Para ello se hace uso de los botones" # Texto del label
        lbl2 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion label (ventana, texto, estilo y tamanio de letra)
        lbl2.place(x=10, y=60, width=1340, height=20) # Posicion y tamanio texto
        lbl2.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "de la derecha, con Rectangle se selecciona el área a segmentar, con Foreground y Background se marcan zonas a las que pertece respectivamente el primer plano o fondo. Finalmente, cada vez que se" # Texto del label
        lbl2_1 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion label (ventana, texto, estilo y tamanio de letra)
        lbl2_1.place(x=10, y=80, width=1340, height=20) # Posicion y tamanio texto
        lbl2_1.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "desee, se pueden realizar iteraciones y observar el resultado en pantalla." # Texto del label
        lbl2_2 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y tamanio de letra)
        lbl2_2.place(x=10, y=100, width=1340, height=20) # Posicion y tamanio texto
        lbl2_2.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Proyecto realizado por: Pablo Mosquera, Juan Sebastián Parrado y Andrea Ruiz" # Texto del label
        lbl3 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y tamanio de letra)
        lbl3.place(x=10, y=740, width=1340, height=30) # Posicion y tamanio texto
        lbl3.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Imagen entrada" # Texto del label
        lbl4 = tk.Label(self, text=text, font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y tamanio de letra)
        lbl4.place(x=10, y=120, width=600, height=25) # Posicion y tamanio texto
        lbl4.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Imagen salida" # Texto del label
        lbl5 = tk.Label(self, text=text, font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y tamanio de letra)
        lbl5.place(x=620, y=120, width=600, height=25) # Posicion y tamanio texto
        lbl5.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Botones" # Texto del label
        lbl6 = tk.Label(self, text=text, font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y tamanio de letra)
        lbl6.place(x=self.btn_posx, y=120, width=self.btn_w, height=25) # Posicion y tamanio texto
        lbl6.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        """
        Botones en la ventana
        """
        n = 0 # Hace referencia a la operacion de la posicion en y del boton 1
        text = "Select an image" # Texto boton 1
        btn1 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_image) # Configuracion del boton 1 (ventana, texto, colores de fondo y de letra, funcion)
        btn1.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 1
        
        n = 2 # Hace referencia a la operacion de la posicion en y del boton 2
        text = "Rectangle" # Texto boton 2
        btn2 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_rectangle) # Configuracion del boton 2 (ventana, texto, colores de fondo y de letra, funcion)
        btn2.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 2
        
        n = 3 # Hace referencia a la operacion de la posicion en y del boton 3
        text = "Background" # Texto boton 3
        btn3 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_background) # Configuracion del boton 3 (ventana, texto, colores de fondo y de letra, funcion)
        btn3.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 3
        
        n = 4 # Hace referencia a la operacion de la posicion en y del boton 4
        text = "Foreground" # Texto boton 4
        btn4 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_foreground) # Configuracion del boton 4 (ventana, texto, colores de fondo y de letra, funcion)
        btn4.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 4
        
        n = 5 # Hace referencia a la operacion de la posicion en y del boton 5
        text = "Iteration" # Texto boton 5
        btn5 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_iteration) # Configuracion del boton 5 (ventana, texto, colores de fondo y de letra, funcion)
        btn5.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 5
        
        n = 1 # Hace referencia a la operacion de la posicion en y del boton 6
        text = "Select Background" # Texto boton 6
        btn6 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_bg) # Configuracion del boton 6 (ventana, texto, colores de fondo y de letra, funcion)
        btn6.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 6
        
        n = 0 # Hace referencia a la operacion de la posicion en y del boton 7
        text = "Save images" # Texto boton 7
        btn7 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_save) # Configuracion del boton 7 (ventana, texto, colores de fondo y de letra, funcion)
        btn7.place(x=self.btn_posx, y=(self.btn_posy2+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 7
        
        n = 1  # Hace referencia a la operacion de la posicion en y del boton 8
        text = "Reset" # Texto boton 8
        btn8 = tk.Button(self, text=text, bg=self.but_bg, fg=self.but_fg, command=self.select_reset) # Configuracion del boton 8 (ventana, texto, colores de fondo y de letra, funcion)
        btn8.place(x=self.btn_posx, y=(self.btn_posy2+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y tamanio boton 8

    # Funcion mouse - movimiento
    def mouse_move(self,event):
        x = event.x # Posicion mouse en x
        y = event.y # Posicion mouse en y 
        if self.flag_rect == True: # Opcion rectangulo seleccionada
            img_temp_m = self.image_in.copy() # Copia de la imagen original
            self.fin_points = [x , y] # Posicion actual del mouse
            self.img_copy = cv2.rectangle(img_temp_m, tuple(self.ini_points), tuple(self.fin_points), (0, 0, 255), 5) # Rectangulo de color rojo sobre la imagen
        if self.flag_circle_fg == True and self.start == True: # Opcion primer plano seleccionada
            cv2.circle(self.img_copy, (x, y), 3, (255,255,255), -1) # Circulo de color blanco sobre la imagen
            cv2.circle(self.mask, (x, y), 5, 1, -1) # Circulo en mascara de valor 1 (primer plano seguro)
        elif self.flag_circle_bg == True and self.start == True: # Opcion fondo seleccionada
            cv2.circle(self.img_copy, (x, y), 3, (0,0,0), -1) # Circulo de color negro sobre la imagen
            cv2.circle(self.mask, (x, y), 5, 0, -1) # Circulo en mascara de valor 0 (fondo seguro)
        self.trans_show_images(self.img_copy,self.image_out) # Actualizacion de imagen en los paneles de GUI
        
    # Funcion mouse - presionar     
    def mouse_down(self,event):
        x = event.x # Posicion mouse en x
        y = event.y # Posicion mouse en y 
        # print("Click en: (%s %s)" % (event.x, event.y))
        if self.flag_rect == True: # Opcion rectangulo seleccionada
            self.ini_points = [x , y] # Posicion actual del mouse
        if ((self.flag_rect == False) and ((self.flag_circle_fg == True) or (self.flag_circle_bg == True))): # Opcion primer plano y fondo seleccionadas
            self.start = True # Bandera inicio habilitada
            # print("Circulo start")
      
    # Funcion mouse - presionar   
    def mouse_up(self,event):
        x = event.x # Posicion mouse en x
        y = event.y # Posicion mouse en y 
        # print("Suelto en: (%s %s)" % (event.x, event.y))
        if self.flag_rect == True: # Opcion rectangulo seleccionada
            img_temp = self.image_in.copy() # Copia de la imagen original
            self.fin_points = [x , y] # Puntos finales del rectangulo
            self.img_copy = cv2.rectangle(img_temp, tuple(self.ini_points), tuple(self.fin_points), (0, 0, 255), 5) # Rectangulo de color rojo sobre la imagen
            self.mask = cv2.rectangle(self.mask, tuple(self.ini_points), tuple(self.fin_points), 3, -1) # Rectangulo con valor 3 (primer plano posible) en la mascara
            self.corners = self.ini_points[0],self.ini_points[1],self.fin_points[0],self.fin_points[1] # Esquinas del rectangulo realizado
            # print('Rectangulo terminado')
            self.flag_rect = False # Deshabilitar función del rectangulo
        self.start = False # Bandera inicio deshabilitada
        self.trans_show_images(self.img_copy,self.image_out) # Actualizacion de imagen en los paneles de GUI     
    
    # Funcion direccion de archivo
    def askopenfilename(self):
        filepath = askopenfilename() # Adquiere la direccion del archivo
        if filepath: # Verifica que se escoge un archivo y/o no se ha dado click en cancelar
            self.filepath = filepath # Direccion del archivo

    # Funcion de seleccionar imagen
    def select_image(self):
        # print("ENTRO A SELECCIONAR IMAGEN")
        self.askopenfilename() # Direccion del archivo
        self.image_in = cv2.imread(self.filepath) # Abrir imagen de disco
        self.image_in = cv2.resize(self.image_in,(self.tam,self.tam)) # Cambiar tamaño de imagen a tamxtam
        #self.img_copy = self.image_in.copy() # Copia de la imagen original
        self.img_bg = np.zeros((self.tam,self.tam,3),np.uint8) # Creacion de imagen de fondo con dimensiones tamxtam y color negro
        self.image_out = self.image_in.copy() # Copia de la imagen original
        self.trans_show_images(self.image_in,self.image_out) # Actualizacion de imagen en los paneles de GUI

    # Funcion para transformar y mostrar imagenes en GUI      
    def trans_show_images(self,image_in,image_out):
        image_in = cv2.cvtColor(image_in, cv2.COLOR_BGR2RGB) # Cambiar imagen de BGR (opencv) a RGB (PIL)
        image_out = cv2.cvtColor(image_out, cv2.COLOR_BGR2RGB) # Cambiar imagen de BGR (opencv) a RGB (PIL)
        image_in = Image.fromarray(image_in) # Conversion a formato PIL
        image_out = Image.fromarray(image_out) # Conversion a formato PIL
        image_in = ImageTk.PhotoImage(image_in) # Conversion a formato ImageTk
        image_out = ImageTk.PhotoImage(image_out) # Conversion a formato ImageTk
          
        if self.panelA is None or self.panelB is None: # Si los paneles están vacios, los inicializa
            # Configuracion del primer panel
            self.panelA = tk.Label(image=image_in)
            self.panelA.image = image_in
            self.panelA.place(x=10, y=self.btn_posy, width=self.tam, height=self.tam) # Posicion primer panel
            # Configuracion del segundo panel
            self.panelB = tk.Label(image=image_out)
            self.panelB.image = image_out       
            self.panelB.place(x=620, y=self.btn_posy, width=self.tam, height=self.tam) # Posicion segundo panel
        else: # Si los paneles estan creados los actualiza
            # Primer panel
            self.panelA.configure(image=image_in)
            self.panelA.image = image_in
            # Segundo panel
            self.panelB.configure(image=image_out)
            self.panelB.image = image_out
        # Eventos del mouse: Si ____ sobre el primer panel
        self.panelA.bind('<Motion>',self.mouse_move) # Mouse se mueve
        self.panelA.bind('<Button-1>', self.mouse_down) # Se presiona el mouse
        self.panelA.bind('<ButtonRelease-1>', self.mouse_up) # Se deja de presionar el mouse
    
    # Funcion de hacer el rectangulo
    def select_rectangle(self):
        # print("HOLA REC")  
        self.flag_rect = True # Bandera rectangulo habilitada
        self.flag_circle_fg = False # Bandera primer plano deshabilitada
        self.flag_circle_bg = False # Bandera fondo deshabilitada
        self.ini_points = [] # Inicializacion de puntos iniciales
    
    # Funcion para seleccionar fondo
    def select_background(self):
        # print("HOLA BG")  
        self.flag_rect = False # Bandera rectangulo deshabilitada
        self.flag_circle_fg = False # Bandera primer plano deshabilitada
        self.flag_circle_bg = True # Bandera fondo habilitada
        
    # Funcion para seleccionar primer plano
    def select_foreground(self):
        # print("HOLA FG")
        self.flag_rect = False # Bandera rectangulo deshabilitada
        self.flag_circle_fg = True # Bandera primer plano habilitada
        self.flag_circle_bg = False # Bandera fondo deshabilitada
        
    # Funcion para realizar iteracion
    def select_iteration(self):
        # print("HOLA IT")
        self.flag_rect = False # Bandera rectangulo deshabilitada
        self.flag_circle_fg = False # Bandera primer plano deshabilitada
        self.flag_circle_bg = False # Bandera fondo deshabilitada
        self.iteration() # funcion iteracion
    
    # Funcion para seleccionar imagenes del fondo
    def select_bg(self):
        # print("HOLA FG sel")
        self.askopenfilename() # Direccion del archivo
        self.img_bg = cv2.imread(self.filepath) # Carga imagen del fondo
        self.img_bg = cv2.resize(self.img_bg,(self.tam,self.tam)) # Cambia el tamaño de la imagen
    
    # Funcion para guardar imagen de salida
    def select_save(self):
        bar = np.zeros((self.image_in.shape[0], 5, 3), np.uint8) # Barra para separar imagenes
        res = np.hstack((self.image_in, bar, self.img_copy, bar, self.output, bar, self.image_out,bar, self.img_bg)) # Junta imagen original, barra, imagen original con rectangulo y mascara negra y blanca, barra, imagen segmentada, barra, imagen segmentada con fondo, barra y fondo 
        cv2.imwrite('output.png', res) # Guarda imagen de salida
    
    # Funcion de iteracion
    def iteration(self):
        cv2.grabCut(self.image_in, self.mask, None, self.BGD_model, self.FGD_model, 1, cv2.GC_INIT_WITH_MASK) # Funcion grabcut 1 iteracion con mascara
        self.mask_out = np.where((self.mask==1)|(self.mask==3), 1, 0).astype('uint8') # Si valor es 1 o 3 (primer plano), se cambia a 1 (primer plano seguro), valores de 0 y 2 (fondo) cambian a 0 (fondo seguro)
        self.output = cv2.bitwise_and(self.image_in, self.image_in, mask=self.mask_out) #  Mascara imagen de salida - imagen segmentada
        self.mask_bg = np.where((self.mask==1)|(self.mask==3), 0, 1).astype('uint8') # Si valor es 1 o 3 (primer plano), se cambia a 0, valores de 0 y 2 (fondo) cambian a 1
        output_bg = cv2.bitwise_or(self.img_bg,self.img_bg, mask=self.mask_bg) # Imagen fondo con negro en zona segmentada de la imagen segmentada
        self.image_out = cv2.bitwise_or(output_bg,self.output) # Imagen segmentada con fondo
        self.trans_show_images(self.img_copy,self.image_out) # Actualizacion de imagen en los paneles de GUI
         
    # Funcion para cerrar la ventana
    def select_reset(self):
        # Declaración de variables
        self.BGD_model = np.zeros((1,65),np.float64) # Vector modelo fondo
        self.FGD_model = np.zeros((1,65),np.float64) # Vector modelo primer plano
        self.ini_points , self.fin_points , self.temp_points  , self.corners = [],[],[],[] # Puntos y esquinas
        self.flag_rect = False # Bandera rectangulo
        self.flag_circle_fg = False # Bandera primer plano
        self.flag_circle_bg = False # Bandera fondo
        self.start = False # Bandera inicio
        self.initial_mask = np.zeros((self.tam,self.tam),np.uint8) # Mascara inicial
        self.mask = np.zeros((self.tam,self.tam),np.uint8) # Mascara
        self.img_bg = np.zeros((self.tam,self.tam,3),np.uint8) # Imagen fondo
        self.trans_show_images(self.img_bg,self.img_bg) # Actualizacion de imagen en los paneles de GUI

# App
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
            
        self.attributes("-fullscreen", True) # Pantalla completa
        self.filepaths = [] # Vector direccion de archivo

        self.appFrame = AppFrame(self)
        self.appFrame.pack(side="top",fill="both",expand=True)
        
# main
def main():
    app = App() # Aplicacion
    window = tk.Tk() #  Tkinter
    app.mainloop() # GUI

if __name__ == '__main__':
    main() # Ejecutar main