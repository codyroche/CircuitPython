# Pixel Plant
Beginnings of the hardware to drive a small art piece. Final project may incorporate many more features, but for now the project will cover audio playback and a basic Neopixel light pattern.

Currently making designs using the following:
 - Adafruit Qt Py 2040 (with supporting Amp and SD card reader)
 - Adafruit Feather M4 Express (with supporting PropMaker feather and SD card reader)

Pros and cons to both designs that are fairly obvious. Might break them down further at a later date.

Both designs will require audio to be converted into 16-bit mono WAV files, as documented in the [Adafruit audio conversion guide](https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion).

Other critical references to complete the work include the following:
 - [Adafruit CircuitPython audio playback guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-audio-out)
 - [Adafruit SD card guide](https://learn.adafruit.com/adafruit-microsd-spi-sdio)
 - [Adafruit MAX98357 I2S Class-D Mono Amp guide](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp)
 - [Adafruit QT Py 2040 guide](https://learn.adafruit.com/adafruit-qt-py-2040)
 - [Adafruit Prop-Maker FeatherWing Overview](https://learn.adafruit.com/adafruit-prop-maker-featherwing/overview)

## QT Py 2040 Design Option
This is the in progress design and was the proof of concept for loading and playing SD card WAV files.

### Components
Parts Used:
 - [Adafruit QT Py RP2040](https://www.adafruit.com/product/4900)
 - [Adafruit Micro SD SPI or SDIO Card Breakout Board - 3V ONLY!](https://www.adafruit.com/product/4682)
 - [Adafruit MAX98357 I2S Class-D Mono Amp](https://www.adafruit.com/product/3006)
 - 100K resistor to reduce gain on amp.


### Layout
![Fritzing Diagram](images/Pixel%20Plant%20QT%20Py%202040_bb.png)

## Feather M4 Express Design Option
Initial audio playback testing was completed on this hardware. Battery power options were also tested.

## Open Tasks for version 1.0

Software Todo:
 - Add dynamic inventory from SD card .WAV files
 - Add NEO lighting pattern
 - Add more functions and a main function

Hardware Todo:
 - Add a volume control potentiometer
 - Clean up Fritzing layout
 - Make PCB design for mounting hardware