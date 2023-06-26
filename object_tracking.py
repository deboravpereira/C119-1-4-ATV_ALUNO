import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Carregue o rastreador
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

# Selecione a caixa delimitadora na imagem
bbox = cv2.selectROI("Tracking", img, False)

# Inicialize o rastreador em img e na caixa delimitadora
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    ##########################
    # ADICIONE O CÓDIGO AQUI #
    ##########################



while True:
    
    check, img = video.read()   

    # Atualize o rastreador em img e na caixa delimitadora
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Errou",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    cv2.imshow("resultado", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyALLwindows()
