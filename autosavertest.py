import sys
import pyautogui
import time
import os
from filecmp import dircmp
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

stopstate = False


def safecounter(pattern_name, version):
    pyautogui.write(pattern_name , interval=0.01)
    pyautogui.write(version, interval = 0.01)
    pyautogui.press('Enter')
    var1 = pattern_name + version
        
def autosaver(timestamp, pattern, stopstate):
    version_number = 0
    
    while (stopstate == False):
        if (version_number < 504):
            time.sleep(timestamp)
            pyautogui.keyDown('Ctrl')
            pyautogui.keyDown('Shift')
            pyautogui.press('s')
            pyautogui.keyUp('Ctrl')
            pyautogui.keyUp('Shift')
            safecounter(pattern, str(version_number))
            time.sleep(5)
            version_number = version_number + 1
        else:
            messagebox.showwarning("Full storage", "Please remove backups to continue with autosaver");
            return

    else:
        messagebox.showwarning("Warning", "The autosaver has been stopped");
        return
def stopperwindow():
    window1=tk.Tk()
    window1.title("AUTOSAVER")
    window1.geometry('150x50')
    window1.configure(background = 'grey')

    button3=tk.Button(window1, text = "STOP", fg ="Black", command = cancelstop)
    button3.pack(padx=5,pady=5,ipadx=0,ipady=0)

def cancelstop(stopstate):
    stopstate = True
    
def validation():
    if e1.get() == '':
        messagebox.showwarning("Warning","Please introduce a pattern to start autosave")
    else:
        if (e2.get()== ''):
            messagebox.showwarning("Warning", "Please introduce a timestamp to start autosave");
        else:
            pattern = e1.get()
            timestamp = int(e2.get())
            stopstate = False
            folders(timestamp, pattern, stopstate)
            #stopperwindow()

def folders(timestamp, pattern, stopstate):

    directory = e1.get()
    parent_dir = "C:/Users/blanc/Desktop/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    time.sleep(3)
    directory_1 = e1.get() + "_IncrementalSave"
    parent_dir_1 = "C:/Users/blanc/Desktop/" + e1.get()
    path1 = os.path.join(parent_dir_1, directory_1)
    os.mkdir(path1)
    os.chdir(path)
    autosaver(timestamp, pattern, stopstate);
    
    
window=tk.Tk()
window.title("AUTOSAVER")
window.geometry('380x300')
window.configure(background='grey')

et1=tk.Label(window, text="Pattern",bg="white", fg="black")
et1.pack(side=tk.TOP)
et2=tk.Label(window, text ="Time autosafe (min)",bg="white", fg="black")
et2.pack(padx=5,pady=5,ipadx=0,ipady=0)
e1=tk.Entry(window)
e1.pack(padx=5,pady=5,ipadx=0,ipady=0)
e2=tk.Entry(window)
e2.pack(padx=10,pady=5)

boton1=tk.Button(window, text = "Start Autosave",fg="blue",command = validation)
boton2=tk.Button(window, text = "Cerrar",fg="Black", command = window.destroy)

boton1.pack(padx=5,pady=5,ipadx=0,ipady=0)
boton2.pack(padx=5,pady=5,ipadx=0,ipady=0)
  


    

