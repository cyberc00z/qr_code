#!/usr/bin/env python3

import os, sys
import numpy as np
import cv2 as cv
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
from numpy.lib.arraypad import pad
import easygui

top = tk.Tk()
top.geometry('500x500')
top.title('Qr Code Reader ')
top.configure(background='white')
label= Label(top, background="#CDCDCD", font=('calibri', 20,'bold'))

def liveCapture():
     cap = cv.VideoCapture(0)
     cv.namedWindow("Live Capture")
     image_count = 0
     while True:
           ret , frame = cap.read()

           if not ret:
                print("Failed to open source")
                break

           cv.imshow("LIVE DETECTION", frame)

           k = cv.waitKey(1)

           # for exit live capturing window please press esc
           if k%256 == 27:
                print("Exiting")
                break

           #enter
           elif k%256 == 32:
                name = "" 
                cv.imwrite(name, frame)
                print("Image Saved!")
                image_count += 1

     cap.release()

def Close():
     cv.waitKey(0)
     cv.destroyAllWindows()
     cv.waitKey(1)
     

detection = tk.Button(top, text="Live Capture", command=liveCapture,padx=10,pady=5)
detection.configure(background='#364156',foreground='white',font=('calibri',10,'bold'))
detection.pack(side=TOP,pady=50)
close = tk.Button(top, text="Exit/Close",command=Close, padx=10, pady=5 )
close.configure(background='#364156', foreground='white', font=('calibri',10,'bold'))
close.pack(side=BOTTOM,pady=50)
top.mainloop()
