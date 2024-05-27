import cv2
import numpy as np
from PIL import Image
import pytesseract

# Pytesseract yolunu belirtiyoruz
pytesseract.pytesseract.tesseract_cmd = r"C:\alican\teserract\tesseract.exe"
while True:
    secenek =int(input("görüntü taramak için 1 çıkmak için 2 yi tuşlayınız.."))
    if secenek==1 :
        def metinOku(resim_yolu):
            image = cv2.imread(resim_yolu)  # Okuyacağımız resmin yolunu alıyoruz
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Resmimimizi gri tona çeviriyoruz

            # Resimdeki kirlilik varsa onları temizliyoruz
            kernel = np.ones((1, 1), np.uint8)
            image = cv2.erode(image, kernel, iterations=1)
            image = cv2.dilate(image, kernel, iterations=1)

            # Resmimizdeki gri tonları siyah yapıyoruz
            image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
            cv2.imwrite('temizlenmisResim.png', image)

            sonuc = pytesseract.image_to_string(Image.open('temizlenmisResim.png'), lang='tur')
            #sonuc2 = pytesseract.image_to_data(Image.open('temizlenmisResim.png'), lang='tur')
            return sonuc#,sonuc2

        print('Okuma Başladı')
        print(' ')
        # Metin olarak görmek istediğimiz resmin yolunu belirtiyoruz
        print(metinOku(r'C:\fatura.png'))
        print(' ')
        print('Okuma Bitti')
    else:
        break
        quit()


