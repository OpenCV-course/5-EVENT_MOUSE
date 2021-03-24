import cv2 as cv
import numpy as np 

#Creamos la función dibujando
#Argumentos: Event = evento del raton
#x,y = coordenada de donde esta el raton
def dibujando(event,x,y,flags,param):
	# Imprimimos la información sobre los eventos que se estén realizando
	print('-----------------------------')
	print('event=',event)
	print('x=',x)
	print('y=',y)
	print('flags=',flags)

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




#Creamos una imagen
imagen = np.zeros((480,640,3),np.uint8)
#Ponemos nombre a la ventana donde va a estar la imagen
cv.namedWindow('Event Mouse')

#Necesitamos la función setMouseCallBack. Argumentos el nombre de la ventana 
# y el nombre de la función que se va ejecutar cuando usemos la función setMouseCallBack
cv.setMouseCallback('Event Mouse',dibujando)

#Vamos a visualizar la imagen y el click del raton
while True:
	cv.imshow('Event Mouse',imagen)
	
	k = cv.waitKey(1) & 0xFF
	if k == ord('l'): # Limpiar el contenido de la imagen
		imagen = np.zeros((480,640,3),np.uint8)
	elif k == 27:
		break

cv.destroyAllWindows()