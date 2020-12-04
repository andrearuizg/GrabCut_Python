# Proyecto final de Procesamiento de imágenes y visión - Segmentar imagenes usando Grabcut

Proyecto final de la materia Procesamiento de imágenes y visión de la Pontificia Universidad Javeriana

<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/output.png" alt="drawing" width="1000"/>  
</p>

La segmentación de objetos sobre una imagen es una de las aplicaciones más utilizadas por usuarios de plataformas como Adobe Photoshop. Realizar este procedimiento puede tomar un tiempo proporcional al resultado deseado; no obstante, durante el desarrollo de este proyecto, se ha realizado un programa en lenguaje Python que buscar solventar esta problemática, ofreciendo una segmentación de objetos con resultados sobresalientes. En paralelo, se ha desarrollado una interfaz gráfica con el fin de facilitar el proceso para usuarios que desconocen este lenguaje de programación. El valor agregado de esta solución, no solo yace en la interfaz mencionada sino que dentro de esta se puede colocar la imagen segmentada sobre un background ingresado por el usuario.

### Video explicativo

Presionar la imagen los redigirá al video
[<p align="center"><img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/video.png" width="500"></p>](https://youtu.be/yoFRtnh3hco)

### Instalación

Para su correcta ejecución se debe tener instalado Opencv, Tkinter y Numpy.

### Contenidos

A continuación se hará un breve resumen de los contenidos del repositorio.

| Archivo | Ubicación |
| ------ | ------ |
| Código | [/Grabcut_GUI.py](https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Grabcut_GUI.py) |
| Imagenes | [/Imagenes/img().png](https://github.com/andrearuizg/Proyecto_Final_Grabcut/tree/main/Imagenes)|
| Pruebas | [/Imagenes/Outputs](https://github.com/andrearuizg/Proyecto_Final_Grabcut/tree/main/Imagenes/Outputs)|
| Licencia | [/LICENSE](https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/LICENSE) |
| Informe | [/Informe_Proyecto_Final_Grabcut](https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Informe_Proyecto_Final_Grabcut.pdf) |
| Video | [Video explicativo](https://youtu.be/yoFRtnh3hco) |

### Desarrollo

A continuación, en las siguiente figuras se podrá observar la explicación del código desarrollado.


En la siguiente figura se puede observar la interfaz gráfica, la cual está compuesta por la imagen original (izquierda) y la imagen de salida (derecha), adicionalemnte tiene unos botones ubicados a la derecha:
- Select an image: Seleccionar imagen original desde el equipo
- Select background: Seleccionar imagen de fondo desde el equipo
- Rectangle: Agregar máscara del rectángulo para el objeto a segmentar
- Background: Agregar máscara de fondo
- Foreground: Agregar máscara de primer plano
- Iteration: Realizar iteración
- Save images: guardar imágenes (más adelante se explica como se guardan)
- Reset: Reiniciar

<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/g.png" alt="drawing" width="1000"/>  
</p>

Ahora se procede a relizar una explicación sobre un proceso realizo en la interfaz gráfica del código y los resultados obtenidos. En la siguiente imagen se observa la ventana que se abre al presionar los botones select an image o select background, con el fin de seleccionar una imagen desde el equipo.

<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/g0.png" alt="drawing" width="1000"/>  
</p>

Ahora se observa el resultado de la imagen segmentada después de haber realizado el rectángulo sobre el objeto a segmentar y una iteración.

<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/g1.png" alt="drawing" width="1000"/>  
</p>

Se procede a realizar la máscara de primer plano (blanco) y fondo (negro). 
 
<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/g2.png" alt="drawing" width="1000"/>  
</p>

Finalmente, se seleccionó una imagen de fondo desde el equipo, el cual se le agregó a la imagen segmentada.

<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/GUI/g3.png" alt="drawing" width="1000"/>  
</p>

Ahora se puede observar el resultado obtenido al guardar una imagen, el orden es el siguiente:
- Imagen original.
- Imagen original con el rectángulo realizado y las máscaras marcadas.
- Imagen segmentada.
- Imagen segmentada con fondo.
- Imagen de fondo.

<p align="center">
<img src="https://github.com/andrearuizg/Proyecto_Final_Grabcut/blob/main/Imagenes/Outputs/output1.png" alt="drawing" width="1000"/>  
</p>

### Referencias

Las [imagenes](https://github.com/andrearuizg/Proyecto_Final_Grabcut/tree/main/Imagenes) fueron tomadas de:
- :bird: [Francisco Calderón](https://www.instagram.com/calderonf/)
- :full_moon: [Camilo Otálora](https://www.instagram.com/camilo_otalora_sanchez)

### Desarrollado por

- :art: [Andrea Juliana Ruiz Gómez](https://github.com/andrearuizg)

- :headphones: [Pablo Eduardo Mosquera Gutierrez](https://github.com/PabloMosG)

- :microphone: [Juan Sebastián Parrado Gutierrez](https://github.com/SebastianParrado) 
