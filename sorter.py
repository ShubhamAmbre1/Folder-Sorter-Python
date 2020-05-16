import os
import shutil
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
folder_name = filedialog.askdirectory()

os.chdir(folder_name)

for dirpath,dirnames,filenames in os.walk(folder_name):
    for file in filenames:
        name, ext = file.split('.')
        print(name, ext)
        if not os.path.exists(os.path.join(os.getcwd(), ext)):
            os.makedirs(ext)
            shutil.move(file, os.path.join(os.getcwd(), ext))
        else:
            shutil.move(file, os.path.join(os.getcwd(), ext))