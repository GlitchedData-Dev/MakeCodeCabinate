#!/bin/bash
DIR="/home/pi/RetroPie/roms/makecode"

#monitor the directory for if a new file is created
inotifywait -m -r -e create "$DIR" | while read f

#if a new file is created, execute the python file
do
	python3 /home/pi/files.py
done
