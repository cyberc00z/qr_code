#generate qr code within bulk
import os, qrcode
import cv2 as cv
import numpy as np

FOLDER = 'dataset/training/gaussian'

if not os.path.isdir(FOLDER):
       os.mkdir(FOLDER)

for data in np.random.choice(np.arange(10,100), size=12, replace=False):
       qr = qrcode.QRCode(
          error_correction=qrcode.constants.ERROR_CORRECT_M,
          box_size=10,
          border=4
       )
       qr.add_data(data)
       qr.make(fit=True)
       img = qr.make_image(fill_color='black', back_color='white')
       img = np.float32(np.asarray(img))*255
       img = cv.blur(img, (5, 5))
       img = np.dstack((img, img, img))
       print("Printing QR Codes BLurred ")
       cv.imwrite(os.path.join(FOLDER, f"{data}.jpg"), img)
