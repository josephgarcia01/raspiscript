#!/bin/bash

# Opens an RDP session and checks if the window is still active.
# Author: joseph g.
# Date: 6/24

#The only segment that needs editing is LINE 10:
#Provide valid USER and PASSWORD in respective fields for testing/deployment.
open_session() {
    sleep 10
    rdesktop bedtrackingsrv2 -d DOMAIN -u USER -p PASSWORD -f -T rdp
}

check_window() {
    window_name=$1
    if xdotool search --name "$window_name" >/dev/null; then
        return 0
    else
        return 1
    fi
}

open_session

while true; do

sleep 100

check_window "rdp"

if [ $? -eq 1 ]
then
    sleep 5
    sudo reboot
fi
    
done
