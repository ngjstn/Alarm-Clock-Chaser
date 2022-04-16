# SPDX-FileCopyrightText: 2018 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
import os
import board
import vlc

player = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/RPI_testing/Belle.mp3') 

while True:
    
    player.play()
    time.sleep(10)
    player.stop()
