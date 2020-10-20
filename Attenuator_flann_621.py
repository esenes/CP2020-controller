import CP2020
from time import sleep

class Attenuator_flann_621(CP2020.CP2020):
    '''
    Child class of Flann CP2020 controller for Flann attenuators series 621.
    Basically the same of using the controller directly, but it queries after setting.

    Last modified: 20/10/2020 by Eugenio Senes
    '''

    def __init__(self, hostname, gpib_address, channel):
        # super().__init__(host=hostname, address=gpib_address)
        CP2020.CP2020.__init__(self, hostname, gpib_address)
        self.set_channel(channel)

    # ----- VALUE MODE, OVERRIDE SET TO CHECK THE SETTING
    def get_value(self): # use this also for read current value
        return float(self.query('VSET?'))

    def set_value(self, value, verbose=False, n_attempts=5):
        self.write('VSET '+str(value))
        # check that it set
        iteration = 0
        while iteration < n_attempts and self.get_value() != value:
            iteration += 1
            self.write('VSET '+str(value))
            sleep(1)
            if verbose: print('Failed to set value. Retry '+str(iteration)+'/'+str(n_attempts))
        else:
            current_val = self.get_value()
            if current_val != value:
                raise IOError("Impossible to set value, check the connection.")
            if current_val == value:
                if verbose: print('Succedeed.')
