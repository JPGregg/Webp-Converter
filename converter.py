#!/usr/bin/env python
'''
Copies every .webp file to .png from "start_directory" on down.
**This requires libwebp converter from URL: https://developers.google.com/speed/webp/download
'''

import os
import subprocess

converter_location = 'C:\\Users\\gregg\\OneDrive\\Desktop\\VSCode Stuff\\Webp_to_Png\\libwebp-1.2.0-windows-x64\\bin\\dwebp'
start_directory = 'C:\\Users\\gregg\\OneDrive\\Desktop\\testFolder'

for dirpath, dirnames, filenames in os.walk(start_directory):
    for file in filenames:
        if file.endswith(".webp"):           
            webp_file_location = dirpath + '\\' + file
            png_file = dirpath + '\\' + file.replace(".webp", ".png")
            
            file = f'{converter_location} {webp_file_location} -o {png_file}'
            subprocess.call(file)