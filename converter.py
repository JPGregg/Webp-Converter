#!/usr/bin/env python
'''
Copies every .webp file to .png from "start_directory" on down.
**This requires libwebp converter from URL: https://developers.google.com/speed/webp/download
'''

import os
import subprocess
from tkinter import Tk, filedialog

class Converter:
    def file_folder_search(self) -> tuple:
        root = Tk()
        root.withdraw() #This keeps the automatic tk window from opening.

        converter_location = filedialog.askopenfile(title = "Select dwebp.exe file").name
        start_directory = str(filedialog.askdirectory(title = "Select starting directory for picture conversion"))
        #opens file & folder selection windows.
        return converter_location, start_directory


    def webp_to_png(self,converter_location,start_directory):
        if converter_location.endswith("dwebp.exe"):
            for dirpath, dirnames, filenames in os.walk(start_directory):
                for file in filenames: #prime candidate for optimization later on. O(n**2) is garbage...but works.
                    if file.endswith(".webp"):           
                        webp_file_location = dirpath + '\\' + file
                        png_file = dirpath + '\\' + file.replace(".webp", ".png")
                        
                        file = f'{converter_location} {webp_file_location} -o {png_file}'
                        subprocess.call(file)

converter = Converter()
converter.webp_to_png(*converter.file_folder_search())
