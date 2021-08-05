#!/usr/bin/env python
'''
Copies every .webp file to .png from "start_directory" on down.
**This requires libwebp converter from URL: https://developers.google.com/speed/webp/download
'''

import os
import subprocess
from tkinter import Tk, filedialog, messagebox

root = Tk()
root.withdraw()

converter_location = filedialog.askopenfile(title = "Select dwebp.exe file")
converter_location = converter_location.name
start_directory = str(filedialog.askdirectory(title = "Select starting directory for picture conversion"))
print(converter_location)

#converter_location = 'C:\\Users\\gregg\\OneDrive\\Desktop\\VSCode Stuff\\Webp_to_Png\\libwebp-1.2.0-windows-x64\\bin\\dwebp'
#start_directory = 'C:\\Users\\gregg\\OneDrive\\Desktop\\testFolder'

if converter_location.endswith("dwebp.exe"):
    for dirpath, dirnames, filenames in os.walk(start_directory):
        for file in filenames:
            if file.endswith(".webp"):           
                webp_file_location = dirpath + '\\' + file
                png_file = dirpath + '\\' + file.replace(".webp", ".png")
                
                file = f'{converter_location} {webp_file_location} -o {png_file}'
                subprocess.call(file)