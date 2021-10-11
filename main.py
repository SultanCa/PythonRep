# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:30:13 2021

@author: ssult
"""

import gui
import serial


def SendSerialData():
    inputText=t1.get()
    print(inputText)
    inputText += '\n'
    sericom.write(inputText.encode())
    #readData=sericom.read()
    #print(readData)
    #sericom.write(inputText.encode('utf-8'))
    #sericom.write(.encode())
    
def GetSerialData():
    print(sericom.in_waiting)
    if sericom.inWaiting()>0:
        outputData=sericom.readline().decode()
        print(outputData)
        t2.insert(0, str(outputData))
        
def Connect():
    print(t.get())
    sericom.baudrate=1000000
    sericom.port=str(t.get())    
    try:
        sericom.open()
        print("Connected")
        lbl1.config(text="Connected!")
    except:
        print("Could not connect")
    

sericom=serial.Serial()
    
obj=gui.GUI()

# root = tk.Tk()
# fr1=tk.LabelFrame(root)
# fr1.grid(row=0, column=0, padx=20, pady=20)
# tk.Button(fr1, width=15).grid(row=0, column=0, padx=20, pady=20)
# tk.Entry(fr1).grid(row=1, column=0, padx=0, pady=20)

fr=obj.Frame(obj.window)
fr.grid(row=0, column=0, padx=20, pady=20)

obj.Label(fr, "COM Port Info\nEx:Com5", 15, 10, 0, 0)

t=obj.Text(fr, 15)
t.grid(row=1, column=0, padx=10, pady=10)

b=obj.Button(fr, "Connect", Connect, 15, 2, 0)
b.grid(row=2, column=0, padx=20, pady=10)

lbl1=obj.Label(obj.window, "Connection Status:\nNotConnnected!!!", 15, 15, 1, 0)


frPart1=obj.Frame(obj.window)
frPart1.grid(row=0, column=1, padx=30, pady=30)

fr1=obj.Frame(frPart1)
fr1.grid(row=0, column=1, padx=30, pady=30)

t1=obj.Text(fr1, 15)
t1.grid(row=0, column=1, padx=20, pady=10)

btn1=obj.Button(fr1, "Send", SendSerialData, 15, 0, 0)
btn1.grid(row=1, column=1, padx=10, pady=10)

fr2=obj.Frame(frPart1)
fr2.grid(row=0, column=2, padx=30, pady=30)

t2=obj.Text(fr2, 15)
t2.grid(row=0, column=2, padx=20, pady=10)

btn2=obj.Button(fr2, "Get", GetSerialData, 15, 0, 0)
btn2.grid(row=1, column=2, padx=10, pady=10)

frPart2=obj.Frame(obj.window)
frPart2.grid(row=1, column=1, padx=30, pady=30)

t3=obj.LargeText(frPart2, 15, 15, 0, 1, 30, 30)
t4=obj.LargeText(frPart2, 15, 15, 0, 2, 30, 30)


# obj.Button("Send", SendSerialData, 15, 1, 0, 50, 10)
# # #obj.Label(30, 0, 1)
# t2=obj.Text(15, 0, 1)
# t2.grid(row=0, column=1)
# obj.Button("Get", GetSerialData, 15, 1, 1, 40, 10)

obj.window.mainloop()

#root.mainloop()

sericom.close()