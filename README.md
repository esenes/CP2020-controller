# CP2020-controller
Code to control a Flann microwave CP2020 motion controller

Basic usage:
```
import Attenuator_flann_621

attenuator = Attenuator_flann_621.Attenuator_flann_621("128.141.161.239", 11, "A")
attenuator.set_value(16) # dB
```
