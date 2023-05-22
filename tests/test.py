from controller import cp2020

controller = cp2020.CP2020("1.1.1.1", 11)

controller.set_instrument(10, "A")  # set the attenuator on channel A to 10 dB
controller.set_instrument(400, "B") # set the phase shifter on channel B to 400 degrees

controller.close()