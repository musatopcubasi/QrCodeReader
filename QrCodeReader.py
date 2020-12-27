import cv2
from pyzbar import pyzbar
from selenium import webdriver

browser=webdriver.Firefox()


cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        x, y, w, h = barcode.rect
        #
        barcode_info = barcode.data.decode('utf-8')
        if browser.current_url != barcode_info:
            browser.get(barcode_info)
        print(barcode_info)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    cv2.imshow("frame",frame)

    if cv2.waitKey(25) and 0xFF==ord('q'):
        break

browser.close()
cap.release()
cv2.destroyAllWindows()