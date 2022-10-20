import glob
import sys
import os
from os import system as ss

#get a list of all the files currently in the rom directory
list_of_files =  glob.glob('/home/pi/RetroPie/roms/makecode/*')
gamelistFilepath = '/home/pi/.emulationstation/gamelists/MakeCode'

#find the file with the newest creation date/time (gets full path)
latest_file = max(list_of_files, key=os.path.getctime)

#separate file name from full path
filename = latest_file.rsplit('/',1)[1]

print(filename, file=sys.stdout)

#add execute permissions to the file
ss(f'chmod +x {latest_file}')

#open the gamelist file in read mode
file = open('{gamelistFilepath}/gamelist.xml', 'r')

#store all the lines to an array
lines = file.readlines()

#delete the last line
del lines[-1]

#close the file
file.close()

#append the details for the newest file to the array of lines
lines.append('\t<game>\n')
lines.append(f'\t\t<path>{latest_file}</path>\n')
lines.append(f'\t\t<name>{filename}</name>\n')
lines.append('\t</game>\n')
lines.append('</gameList>')

#create a temporary file that stores all the lines
ss('touch {gamelistFilepath}/gamelist_temp.xml')

#open that file in append mode and write all the lines to it
file = open('{gamelistFilepath}/gamelist_temp.xml', 'a')
for line in lines:
	file.write(line)

#remove the original gamelist file and create a new one with the content of the temporary file
#(this deletes the temporary file in the process
ss(f'rm {gamelistFilepath}/gamelist.xml')
ss(f'mv {gamelistFilepath}/gamelist_temp.xml {gamelistFilepath}/gamelist.xml')

