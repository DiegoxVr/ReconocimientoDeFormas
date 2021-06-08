import cv2 #Importar OpenCV2
import numpy as np #Manejo de arrays.

cap = cv2.VideoCapture(0) 

azulBajo = np.array([100,100,20],np.uint8) 
azulAlto = np.array([125,255,255],np.uint8) 

while True:

  ret,frame = cap.read()

  if ret==True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,azulBajo,azulAlto)
    contornos, hierarchy = cv2.findContours(mask,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 3000:
        epsilon = 0.01*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)
        x,y,w,h = cv2.boundingRect(approx)
        #---------------------TRIANGULO---------------------------------------
        if len(approx)==3:
          cv2.putText(frame,'Pieza aceptada', (x,y-5),1,1.5,(0,255,0),2)
        else:
          cv2.putText(frame,'Pieza no aceptada', (x,y-5),1,1.5,(0,0,255),2)
        #---------------------CUADRADO----------------------------------------
        #if len(approx)==4:
        #  aspect_ratio = float(w)/h #ancho/alto
        #  if aspect_ratio == 1: #Si es 1, sus lados son iguales.
        #    cv2.putText(image,'Pieza aceptada', (x,y-5),1,1.5,(0,255,0),2)
        #  else:
        #    cv2.putText(image,'Pieza no aceptada', (x,y-5),1,1.5,(0,0,255),2)
        #--------------------RECTANGULO---------------------------------------
        #if len(approx)==4:
        #  aspect_ratio = float(w)/h
        #  if aspect_ratio != 1:
        #    cv2.putText(image,'Pieza aceptada', (x,y-5),1,1.5,(0,255,0),2)
        #  else:
        #    cv2.putText(image,'Pieza no aceptada', (x,y-5),1,1.5,(0,0,255),2)
        #--------------------PENTAGONO----------------------------------------
        #if len(approx)==5:
        #  cv2.putText(frame,'Pieza aceptada', (x,y-5),1,1.5,(0,255,0),2)
        #else:
        #  cv2.putText(frame,'Pieza no aceptada', (x,y-5),1,1.5,(0,0,255),2)
        #--------------------HEXAGONO-----------------------------------------
        #if len(approx)==6:
        #  cv2.putText(frame,'Pieza aceptada', (x,y-5),1,1.5,(0,255,0),2)
        #else:
        #  cv2.putText(frame,'Pieza no aceptada', (x,y-5),1,1.5,(0,0,255),2)
        #--------------------CIRCULO------------------------------------------
        #if len(approx)>10:
        #  cv2.putText(frame,'Pieza aceptada', (x,y-5),1,1.5,(0,255,0),2)
        #else:
        #  cv2.putText(frame,'Pieza no aceptada', (x,y-5),1,1.5,(0,0,255),2)
        nuevoContorno = cv2.convexHull(c)
        cv2.drawContours(frame, [nuevoContorno], 0, (0,0,0), 3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()
