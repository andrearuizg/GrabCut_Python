# -*- coding: utf-8 -*-
"""
Proyecto final, procesamiento de imagenes

@author: Andrea Ruiz, Sebastian Parrado & Pablo Mosquera
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image # Para mostrar la imagen en la interfaz GUI
from PIL import ImageTk # Para mostrar la imagen en la interfaz GUI
import cv2
import numpy as np
#import sys

###Step 1: Create The App Frame
class AppFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ###call the parent constructor
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
        
        # self.tamanio imagenes que se muestran en la interfaz. Las imagenes son cuadradas
        self.tam = 600 
        
        # Posiciones y self.tamanios de los botones
        self.btn_posx = 1240 # Posicion x del boton
        self.btn_posy = 145 # Posicion y del primer bloque de botones
        self.btn_posy2 = 675 # Posicion y del segundo bloque de botones
        self.btn_w = 110 # self.tamanio horizontal boton
        self.btn_h = 30 # self.tamanio vertical boton
        
        self.gui()
        
        self.select_reset()
        
    def gui(self):
        """
        Textos en la ventana
        """
        lbli = tk.Label(self, text=" ", font=("Arial Bold", 40)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbli.place(x=620, y=self.btn_posy, width=self.tam, height=self.tam) # Posicion y self.tamanio texto
        lbli.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        #lbli.bind('<Motion>',self.motion)
        
        lbl0 = tk.Label(self, text=" ", font=("Arial Bold", 40)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl0.place(x=0, y=0, width=1370, height=820) # Posicion y self.tamanio texto
        lbl0.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl1 = tk.Label(self, text="Proyecto final - Procesamiento de imágenes y visión", font=("Arial Bold", 35)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl1.place(x=10, y=5, width=1340, height=60) # Posicion y self.tamanio texto
        lbl1.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "Este proyecto consiste en realizar la segmentación de una imagen y ubicarla sobre un fondo, dichas imagenes se seleccionan desde  el disco duro del computador. Para ello se hace uso de los botones" 
        lbl2 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl2.place(x=10, y=60, width=1340, height=20) # Posicion y self.tamanio texto
        lbl2.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "de la derecha, con Rectangle se selecciona el área a segmentar, con Foreground y Background se marcan zonas a las que pertece respectivamente el primer plano o fondo. Finalmente, cada vez que se"
        lbl2_1 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl2_1.place(x=10, y=80, width=1340, height=20) # Posicion y self.tamanio texto
        lbl2_1.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        text = "desee, se pueden realizar iteraciones y observar el resultado en pantalla."
        lbl2_2 = tk.Label(self, text=text, font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl2_2.place(x=10, y=100, width=1340, height=20) # Posicion y self.tamanio texto
        lbl2_2.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl3 = tk.Label(self, text="Proyecto realizado por: Pablo Mosquera, Juan Sebastián Parrado y Andrea Ruiz", font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl3.place(x=10, y=740, width=1340, height=30) # Posicion y self.tamanio texto
        lbl3.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl4 = tk.Label(self, text="Imagen entrada", font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl4.place(x=10, y=120, width=600, height=25) # Posicion y self.tamanio texto
        lbl4.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl5 = tk.Label(self, text="Imagen salida", font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl5.place(x=620, y=120, width=600, height=25) # Posicion y self.tamanio texto
        lbl5.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl6 = tk.Label(self, text="Botones", font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl6.place(x=self.btn_posx, y=120, width=self.btn_w, height=25) # Posicion y self.tamanio texto
        lbl6.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        """
        Botones en la ventana
        """
        n = 0 # Hace referencia a la operacion de la posicion en y del boton 1
        btn1 = tk.Button(self, text="Select an image", bg=self.but_bg, fg=self.but_fg, command=self.select_image) # Configuracion del boton 1 (ventana, texto, colores de fondo y de letra, funcion)
        btn1.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 1
        
        n = 2 # Hace referencia a la operacion de la posicion en y del boton 2
        btn2 = tk.Button(self, text="Rectangle", bg=self.but_bg, fg=self.but_fg, command=self.select_rectangle) # Configuracion del boton 2 (ventana, texto, colores de fondo y de letra, funcion)
        btn2.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 2
        
        n = 3 # Hace referencia a la operacion de la posicion en y del boton 3
        btn3 = tk.Button(self, text="Background", bg=self.but_bg, fg=self.but_fg, command=self.select_background) # Configuracion del boton 3 (ventana, texto, colores de fondo y de letra, funcion)
        btn3.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 3
        
        n = 4 # Hace referencia a la operacion de la posicion en y del boton 4
        btn4 = tk.Button(self, text="Foreground", bg=self.but_bg, fg=self.but_fg, command=self.select_foreground) # Configuracion del boton 4 (ventana, texto, colores de fondo y de letra, funcion)
        btn4.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 4
        
        n = 5 # Hace referencia a la operacion de la posicion en y del boton 5
        btn5 = tk.Button(self, text="Iteration", bg=self.but_bg, fg=self.but_fg, command=self.select_iteration) # Configuracion del boton 5 (ventana, texto, colores de fondo y de letra, funcion)
        btn5.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 5
        
        n = 1 # Hace referencia a la operacion de la posicion en y del boton 6
        btn6 = tk.Button(self, text="Select Background", bg=self.but_bg, fg=self.but_fg, command=self.select_bg) # Configuracion del boton 6 (ventana, texto, colores de fondo y de letra, funcion)
        btn6.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 6
        
        n = 0 # Hace referencia a la operacion de la posicion en y del boton 7
        btn7 = tk.Button(self, text="Save images", bg=self.but_bg, fg=self.but_fg, command=self.select_save) # Configuracion del boton 7 (ventana, texto, colores de fondo y de letra, funcion)
        btn7.place(x=self.btn_posx, y=(self.btn_posy2+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 7
        
        n = 1  # Hace referencia a la operacion de la posicion en y del boton 8
        btn8 = tk.Button(self, text="Reset", bg=self.but_bg, fg=self.but_fg, command=self.select_reset) # Configuracion del boton 8 (ventana, texto, colores de fondo y de letra, funcion)
        btn8.place(x=self.btn_posx, y=(self.btn_posy2+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 8

        
        ###Create button
        #btn = tk.Button(self, text='askopenfilename',command=self.askopenfilename)
        #btn.pack(pady=5)
    def mouse_move(self,event):
        x = event.x#-10
        y = event.y#-self.btn_posy
        if self.flag_rect == True:
            img_temp_m = self.image_in.copy()
            self.fin_points = [x , y]
            self.img_copy = cv2.rectangle(img_temp_m, tuple(self.ini_points), tuple(self.fin_points), (0, 0, 255), 5)    
            print("inipoitns",self.ini_points)
        if self.flag_circle_fg == True and self.start == True: 
            print("Circulo fg")
            cv2.circle(self.img_copy, (x, y), 3, (255,255,255), -1)
            cv2.circle(self.mask, (x, y), 5, 1, -1)    
        elif self.flag_circle_bg == True and self.start == True: 
            print("Circulo bg")
            cv2.circle(self.img_copy, (x, y), 3, (0,0,0), -1)
            cv2.circle(self.mask, (x, y), 5, 0, -1)
        self.trans_show_images(self.img_copy,self.image_out)   
        
        #print("Mouse position: (%s %s)" % (event.x, event.y))
        
    def mouse_down(self,event):
        x = event.x#-10
        y = event.y#-self.btn_posy
        #if x>0 and y>0:
        print("Click en: (%s %s)" % (event.x, event.y))
        if self.flag_rect == True:
            self.ini_points = [x , y]
        #else:
         #   print("Fuera de imagen")
        if ((self.flag_rect == False) and ((self.flag_circle_fg == True) or (self.flag_circle_bg == True))):
            self.start = True
            print("Circulo start")
        
    def mouse_up(self,event):
        print("Suelto en: (%s %s)" % (event.x, event.y))
        x = event.x#-10
        y = event.y#-self.btn_posy
        if self.flag_rect == True:
            img_temp = self.image_in.copy()
            self.fin_points = [x , y]
            self.img_copy = cv2.rectangle(img_temp, tuple(self.ini_points), tuple(self.fin_points), (0, 0, 255), 5)
            self.mask = cv2.rectangle(self.mask, tuple(self.ini_points), tuple(self.fin_points), 3, -1)
            self.corners = self.ini_points[0],self.ini_points[1],self.fin_points[0],self.fin_points[1]
            #self.flag_rect = False
            print('Rectangulo terminado')
            #cv2.destroyWindow('image_mod')
            self.flag_rect = False
        self.start = False
        self.trans_show_images(self.img_copy,self.image_out)     
        
    def askopenfilename(self):
        ###ask filepath
        filepath = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))) # Abre el buscador de archivos

        ###if you selected a file path
        if filepath: # Verifica que se escoge un archivo y/o no se ha dado click en cancelar
            self.filepath = filepath    
        #image = cv2.imread(path) # load the image from disk
        #return image

    # Funcion de seleccionar imagen
    def select_image(self):
        print("ENTRO A SELECCIONAR IMAGEN")
        self.askopenfilename()
        self.image_in = cv2.imread(self.filepath) # load the image from disk
        self.image_in = cv2.resize(self.image_in,(self.tam,self.tam))
        self.img_copy = self.image_in.copy()
        self.img_bg = np.zeros((self.tam,self.tam,3),np.uint8)
        self.image_out = cv2.imread(self.filepath) # load the image from disk
        self.image_out = cv2.resize(self.image_out,(self.tam,self.tam))
        self.trans_show_images(self.image_in,self.image_out)
        
        self.gui()
        # self.image_in = self.askopenfilename
        # self.image_out = self.askopenfilename
    # Funcion para transformar y mostrar imagenes en GUI      
    def trans_show_images(self,image_in,image_out):
        # OpenCV represents images in BGR order; however PIL represents
  		# images in RGB order, so we need to swap the channels
        image_in = cv2.cvtColor(image_in, cv2.COLOR_BGR2RGB)
        image_out = cv2.cvtColor(image_out, cv2.COLOR_BGR2RGB)
  		# convert the images to PIL format...
        image_in = Image.fromarray(image_in)
        image_out = Image.fromarray(image_out)
  		# ...and then to ImageTk format
        image_in = ImageTk.PhotoImage(image_in)
        image_out = ImageTk.PhotoImage(image_out)
          
          # if the panels are None, initialize them
        if self.panelA is None or self.panelB is None:
            # the first panel will store our original imag
            self.panelA = tk.Label(image=image_in)
            self.panelA.image = image_in
            self.panelA.place(x=10, y=self.btn_posy, width=self.tam, height=self.tam)
            # while the second panel will store the edge map
            self.panelB = tk.Label(image=image_out)
            self.panelB.image = image_out       
            self.panelB.place(x=620, y=self.btn_posy, width=self.tam, height=self.tam)
            # otherwise, update the image panels
        else:
            # update the pannels
            self.panelA.configure(image=image_in)
            self.panelB.configure(image=image_out)
            self.panelA.image = image_in
            self.panelB.image = image_out
        
        self.panelA.bind('<Motion>',self.mouse_move)        
        self.panelA.bind('<Button-1>', self.mouse_down)
        self.panelA.bind('<ButtonRelease-1>', self.mouse_up)
    
                
    # Funcion de hacer el rectangulo
    def select_rectangle(self):
        print("HOLA")  
        self.flag_rect = True
        self.flag_circle_fg = False
        self.flag_circle_bg = False
    
    # Funcion para seleccionar fondo
    def select_background(self):
        self.flag_rect = False
        self.flag_circle_fg = False
        self.flag_circle_bg = True
        print("HOLA BG")  
    
    # Funcion para seleccionar primer plano
    def select_foreground(self):
        self.flag_rect = False
        self.flag_circle_fg = True
        self.flag_circle_bg = False
        print("HOLA FG")
    
    # Funcion para realizar iteracion
    def select_iteration(self):
        print("HOLA IT")
        self.flag_rect = False
        self.flag_circle_fg = False
        self.flag_circle_bg = False
        self.iteration()
    
    # Funcion para seleccionar imagenes del fondo
    def select_bg(self):
        print("HOLA FG sel")
        self.askopenfilename()
        self.img_bg = cv2.imread(self.filepath) # load the image from disk
        #self.image_out = cv2.imread(self.filepath) # load the image from disk
        self.img_bg = cv2.resize(self.img_bg,(self.tam,self.tam))
        #self.image_out = cv2.resize(self.image_out,(self.tam,self.tam))
        #self.trans_show_images(self.image_in,self.image_out)
        
    # Funcion para seleccionar o quitar pantalla completa
    def select_fs(self):
        #global state # variables globales usadas
        if self.state: # Si esta en pantalla completa...
            self.state = False # ... salga de pantalla completa
        else: # Si no esta en pantalla completa...
            self.state = True # ... ponga pantalla completa
        self.attributes("-fullscreen", self.state) # Ajustar el estado de la pantalla
    
    def select_save(self):
        bar = np.zeros((self.image_in.shape[0], 5, 3), np.uint8)
        res = np.hstack((self.image_in, bar, self.img_copy, bar, self.output, bar, self.image_out,bar, self.img_bg))
        cv2.imwrite('output.png', res)
        
    def iteration(self):
        cv2.grabCut(self.image_in, self.mask, None, self.BGD_model, self.FGD_model, 1, cv2.GC_INIT_WITH_MASK)
        self.mask_out = np.where((self.mask==1)|(self.mask==3), 1, 0).astype('uint8')
        self.output = cv2.bitwise_and(self.image_in, self.image_in, mask=self.mask_out)
        # #cv2.imshow('image_mod',output)
        self.mask_bg = np.where((self.mask==1)|(self.mask==3), 0, 1).astype('uint8')
        # self.img_bg = cv2.imread('lena.jpg', 1)  
        # self.img_bg = cv2.resize(self.img_bg,(self.tam,self.tam))
        output_bg = cv2.bitwise_or(self.img_bg,self.img_bg, mask=self.mask_bg)
        self.image_out = cv2.bitwise_or(output_bg,self.output)
        # cv2.imshow('image_mod',output_bg)
        self.trans_show_images(self.img_copy,self.image_out)
         
    # Funcion para cerrar la ventana
    def select_reset(self):
        self.BGD_model = np.zeros((1,65),np.float64)
        self.FGD_model = np.zeros((1,65),np.float64)
        self.ini_points , self.fin_points , self.temp_points  , self.corners = [],[],[],[]
        self.flag_rect = False #Rect = True
        self.flag_circle_fg = False
        self.flag_circle_bg = False
        self.start = False
        self.flag_rect_or_mask = True #Rect_iteration = True / mask_iteration = False
        self.initial_mask = np.zeros((self.tam,self.tam),np.uint8)
        self.mask = np.zeros((self.tam,self.tam),np.uint8)
        self.img_bg = np.zeros((self.tam,self.tam,3),np.uint8)
        self.trans_show_images(self.img_bg,self.img_bg)

###Step 2: Creating The App
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        ###call the parent constructor
        tk.Tk.__init__(self, *args, **kwargs)
            
        self.attributes("-fullscreen", True) # Pantalla completa

        ###create filepath list
        self.filepaths = []

        ###show app frame
        self.appFrame = AppFrame(self)
        self.appFrame.pack(side="top",fill="both",expand=True)
        
###Step 3: Bootstrap the app
def main():
    app = App()
    window = tk.Tk()
    """
    Configuracion de la ventana
    """
    #tk.title("Proyecto Procesamiento de Imagenes") # Titulo ventana
    #tk.geometry('1360x720') # self.tamaño ventana

    app.mainloop()

if __name__ == '__main__':
    main()