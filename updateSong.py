import vlc

def updateSong(songName):
    if songName == "Love": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/LoveStory.mp3')

    elif songName == "japan": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/NeverGiveUp.mp3')

    elif songName == "DoIt": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/JustDoIt.mp3')

    elif songName == "knowledge": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/HereInMyGarage.mp3')

    elif songName == "iphone": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/iphone.mp3')

    elif songName == "Belle": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/Belle.mp3')

    elif songName == "jojo": 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/jojo.mp3')

    else: 
        song = vlc.MediaPlayer('/home/pi/Desktop/P2_A_G27/songs/NeverGiveUp.mp3')

    song.audio_set_volume(100)
    return song
