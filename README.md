# 5 EVENT MOUSE
1. [Importamos las librerías necesarias](#schema1)
2. [Ponemos nombre a la ventana donde va a estar la imagen](#schema2)
3. [Necesitamos la función setMouseCallBack.](#schema3)
4. [Creamos la función dibujando](#schema4)

<hr>

<a name="schema1"></a>

# 1. Importamos las librerías necesarias
~~~python
import cv2 as cv
import numpy as np 
~~~
<hr>

<a name="schema2"></a>

# 2.Ponemos nombre a la ventana donde va a estar la imagen
~~~python
cv.namedWindow('Event Mouse')
~~~
<hr>

<a name="schema3"></a>

# 3.Necesitamos la función setMouseCallBack.
Argumentos el nombre de la ventana y el nombre de la función que se va ejecutar cuando usemos la función setMouseCallBack
~~~python
 cv.setMouseCallback('Event Mouse',dibujando)
~~~



<hr>

<a name="schema4"></a>

# 4. Creamos la función dibujando

Argumentos: Event = evento del raton

EVENT_MOUSEMOVE = 0

EVENT_LBUTTONDOWN

EVENT_RBUTTONDOWN

EVENT_MBUTTONDOWN

EVENT_LBUTTONUP

EVENT_RBUTTONUP

EVENT_MBUTTONUP

EVENT_LBUTTONDBLCLK

EVENT_RBUTTONDBLCLK

EVENT_MBUTTONDBLCLK


x,y = coordenada de donde esta el raton

flags 

EVENT_FLAG_LBUTTON

EVENT_FLAG_RBUTTON

EVENT_FLAG_MBUTTON

EVENT_FLAG_CTRLKEY

EVENT_FLAG_SHIFTKEY

EVENT_FLAG_ALTKEY
~~~python
def dibujando(event,x,y,flags,param):
	# Imprimimos la información sobre los eventos que se estén realizando
	print('-----------------------------')
	print('event=',event)
	print('x=',x)
	print('y=',y)
	print('flags=',flags)
~~~

<hr>

<a name="schema5"></a>

# 5.  Ejemplos de acciones con algunos eventos del mouse

~~~python
    # Ejemplos de acciones con algunos eventos del mouse
    #Click boton izquierdo del raton
	if event == cv.EVENT_LBUTTONDOWN:
		cv.circle(imagen,(x,y),20,(255,255,255),2)
    #Click boton derecho del raton
	if event == cv.EVENT_RBUTTONDOWN:
		cv.circle(imagen,(x,y),20,(0,0,255),2)
    #Doble Click boton izquierdo del raton
	if event == cv.EVENT_LBUTTONDBLCLK:
		cv.circle(imagen,(x,y),10,(255,0,0),-1)
    #Doble Click boton derecho del raton
	if event == cv.EVENT_RBUTTONDBLCLK:
		cv.circle(imagen,(x,y),10,(0,255,0),-1)
    #Mensaje cuando se deja de pulsar algun boton
	if event == cv.EVENT_LBUTTONUP:
		cv.putText(imagen,'Ha dejado de presionar (Izquierdo)',(x,y),2,0.4,(255,255,0),1,cv.LINE_AA)

	if event == cv.EVENT_RBUTTONUP:
		cv.putText(imagen,'Ha dejado de presionar (Derecho)',(x,y),2,0.4,(0,255,255),1,cv.LINE_AA)
~~~

<hr>

<a name="schema6"></a>

# 6. Vamos a visualizar la imagen y el click del raton
~~~python
while True:
	cv.imshow('Event Mouse',imagen)
	
	k = cv.waitKey(1) & 0xFF
	if k == ord('l'): # Limpiar el contenido de la imagen
		imagen = np.zeros((480,640,3),np.uint8)
	elif k == 27:
		break

cv.destroyAllWindows()
~~~




Tutorial seguido https://omes-va.com/eventos-del-mouse-opencv-python/