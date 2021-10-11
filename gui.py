# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:51:29 2021

@author: ssult
"""

import tkinter as tk

class GUI:
    
    
    def __init__(self):
        self.window=tk.Tk()
           
    def Button(self, root, buttonName, commandName, width, x=0, y=0):
        button=tk.Button(root, text=buttonName, width=width, command=commandName)
        return button

    def Text(self, root, width):
        text=tk.Entry(root, width=width)
        return text
    
    def LargeText(self, root, height, width, x, y, padx, pady):
        tk.Text(root, height=height, width=width).grid(row=x, column=y, padx=padx, pady=pady)
     
    def Label(self, root, text, width, font, x=0, y=0):
        label=tk.Label(root, text=text, width=width, font=("Helvetica", font))
        label.grid(row=x, column=y)
        return label
        
    def Frame(self, root):
        frame=tk.LabelFrame(root)
        return frame