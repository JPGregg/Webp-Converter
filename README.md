# Webp-Converter

## Starting from given file, moves through every file and folder within and converts Webp images to PNG.

### Another program is required to run this code. It requires a [libwebp converter](https://developers.google.com/speed/webp/download). E.g. 'libwebp-1.2.0-windows-x64.zip' which was the latest version at the start of this project.
### Starting the program will prompt the user to enter the location of the dwebp.exe file from within the downloaded libwebp folder. Second, the user will be prompted for the starting file location from which the program will begin creating png copies of webp images. Every webp image within the folder - and its subfolders - will undergo this process.
### This process will not delete the original images, simply create an additional image in the png format.
### Currently breaks if any file or folder contains a space. Will attempt fix in the future.
