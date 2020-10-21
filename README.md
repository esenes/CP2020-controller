# CP2020-controller
Code to control a Flann microwave CP2020 motion controller

Basic usage:
```
import CP2020

controller = CP2020.CP2020("1.1.1.1", 11)

controller.set_instrument(10, "A")  # set the attenuator on channel A to 10 dB
controller.set_instrument(400, "B") # set the phase shifter on channel B to 400 degrees

controller.close()
```
