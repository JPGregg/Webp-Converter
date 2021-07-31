'''
Purpose: To recursively look through folder and child folders to change all contained Webp files to PNG files.
    These will not change the original, but will create a folder titled "PNGs" that contains all of the new images.

Need to provide code to link the webp to png converter.

Pseudocode:
converter = "C\\blah\\blah"         this makes a variable that saves the location of the converter.


'''

import os
import subprocess

#os.chdir("C:\\Users\\gregg\\OneDrive\\Desktop")

#print(os.getcwd())

#print(os.listdir())

#os.makedirs('os_test\\os_test_deeper')
#os.removedirs('os_test2\\os_test_deeper')

converter_location = 'C:\\Users\\gregg\\OneDrive\\Desktop\\VSCode Stuff\\Webp_to_Png\\libwebp-1.2.0-windows-x64\\bin\\dwebp'
start_directory = 'C:\\Users\\gregg\\OneDrive\\Desktop\\testFolder'

for dirpath, dirnames, filenames in os.walk(start_directory):
    #print('Current Path:', dirpath)
    #print('Directories:', dirnames)
    #print('Files:', filenames)
    #print()

    for file in filenames:
        if file.endswith(".webp"):
            print("converting...")
            ##webp_file_location = dirpath + '\\' + file + ' '
            ##png_file = '-o ' + dirpath + '\\' + file.replace(".webp", ".png")
            
            webp_file_location = dirpath + '\\' + file
            png_file = dirpath + '\\' + file.replace(".webp", ".png")
            file = f'{converter_location} {webp_file_location} -o {png_file}'

            ##file = converter_location + webp_file_location + png_file 
            
            
            #file = 'C:\\Users\\gregg\\OneDrive\\Desktop\\VSCode Stuff\\Webp_to_Png\\libwebp-1.2.0-windows-x64\\bin\\dwebp C:\\Users\\gregg\\OneDrive\\Desktop\\testFolder\\level1Folder1\\image1.webp -o C:\\Users\\gregg\\OneDrive\\Desktop\\testFolder\\level1Folder1\\image1.png'
            subprocess.call(file)
            #print(file)

'''
the for loop is now looping through every file and every directory.
in each directory, examine every file.
    for every file that ends in .webp:
        call the converter app on this file and paste result to directory.


dwebp test2.webp -o test2.png

dwebp is the decoding program that takes webp files as input
test2.webp was the name of the webp file
-o specifies the output name, I THINK.
test2.png is output file name.
'''