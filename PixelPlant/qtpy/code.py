"""
QT Py 2040 design for loading WAV files from SD card and playing them back.
Based on several great Adafruit samples on https://learn.adafruit.com/.
"""

import audiocore  # For audio playback
import board  # For audio playback
import audiobusio  # For audio playback
import sdcardio  # For SD card interactions
import storage  # For SD card interactions
import os  # For eventual dynamic audio file list generation

import busio  # Unneeded with current SD card design?


"""
#Test Audio Payback code - Unused now that list load is working.
wave_file = open("/sd/StarWars60.wav", "rb")
wave = audiocore.WaveFile(wave_file)
"""
"""
Tweaked for use with QTPy2040.
Also added a 100K resistor to the gain <> Vin on audio chip to quiet audio.
Need to find a REAL way to control audio though, as it's still too high even at the low level on the Gain control.
"""
# Audio hardware pin mapping.
audio = audiobusio.I2SOut(board.A2, board.A1, board.A0)

# SD card pin mapping
spi = board.SPI()
cs = board.A3

# SD card storage mounting
sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

# SD card mount. This will fail if the card isn't installed. Should try/except.
storage.mount(vfs, "/sd")


def write_text():
    # Write example from Adafruit - Unused
    with open("/sd/test.txt", "w") as f:
        f.write("Hello world!\r\n")


def read_text():
    # Read example from Adafruit - Unused
    with open("/sd/test.txt", "r") as f:
        print("Read line from file:")
        print(f.readline())


"""
Read .wav files into list.
Need to move from fixed list to dynamically loading .wav files from SD Card
"""
waves = [
    "BabyElephantWalk60.wav",
    "CantinaBand60.wav",
    "Fanfare60.wav",
    "gettysburg.wav",
    "ImperialMarch60.wav",
    "PinkPanther60.wav",
    "preamble.wav",
    "StarWars60.wav",
    "StreetChicken.wav",
    "taunt.wav",
]


def play_files(file_list):
    for file in file_list:
        wave_file = open(f"/sd/{file}", "rb")
        wave = audiocore.WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass
        wave_file.close()


# Play all WAV files once.
play_files(waves)
"""
#Removed Sample loop from Kattni Rembor's example audio playback code.
while True:
    audio.play(wave)
    while audio.playing:
        pass
"""
