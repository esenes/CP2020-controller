import plx_gpib_ethernet

class CP2020(plx_gpib_ethernet.PrologixGPIBEthernetDevice):
    '''
    A class that uses the prologix-gpib-ethernet library by nelsond
    to interface a Flann CP2020 controller.
    Check out https://github.com/nelsond/prologix-gpib-ethernet
    Last modified: 20/10/2020 by Eugenio Senes
    '''

    def __init__(self, hostname, gpib_address):
        super().__init__(host=hostname, address=gpib_address)
        self.connect()
        print(self.idn())

        print('Channel A:')
        print(self.query('INSTIDA?'))
        print('Channel B:')
        print(self.query('INSTIDB?'))


    # ----- GENERAL INSTRUMENT CONTROL
    def get_gpib_address(self):
        return int(self.query('ADDRSET?'))

    def set_gpib_address(self, new_addr):
        return self.write('ADDRSET '+str(new_addr))

    def reset(self):
        self.write('RESET')

    # ----- CHANNEL CONTROL
    def get_instrument(self, channel):
        '''
        Returns the name of the instrument connected at that channel.
        '''
        if channel == "A":
            return self.query('INSTIDA?')
        elif channel == "B":
            return self.query('INSTIDB?')
        else:
            raise ValueError('Wrong channel name')

    def get_channel(self):
        msg = int(self.query('CHAN?'))
        if msg == 1:
            return "A"
        elif msg == 2:
            return "B"

    def set_channel(self, channel):
        if channel == "A" or channel == "B":
            return self.write('CHAN '+channel)
        else:
            raise ValueError('Wrong channel name')

    # ----- MODE CONTROL
    def get_mode(self, human=False):
        '''
        0 = value mode; 1 = step mode
        '''
        if human:
            answer = self.query('MODE?')
            if answer == '0\n': return "Value mode"
            elif answer == '1\n': return "Step mode"
        else:
            return self.query('MODE?')

    # ----- INCREASE MODE
    def get_increase_step(self):
        return float(self.query('ISET?'))

    def set_increase_step(self, step):
        return self.write('ISET '+str(step))

    def increase(self):
        return self.write('INC')

    def decrease(self):
        return self.write('DEC')

    # ----- VALUE MODE
    def get_value(self): # use this also for read current value
        return float(self.query('VSET?'))

    def set_value(self, value):
        return self.write('VSET '+str(value))

    # ----- STEP MODE
    def get_motor_steps(self):
        return int(self.query('SSET?'))

    def set_motor_steps(self, step):
        return self.write('SSET '+str(step))


    # ----- CUSTOM SET COMMANDS
    def set_instrument(self, value, channel, verbose=False, n_attempts=5):
        '''
        Set the instrument connected on that channel, then checks that the
        command is received
        '''
        if self.get_channel() != channel:
            self.set_channel(channel)

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
