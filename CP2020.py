import plx_gpib_ethernet

class CP2020:
    '''
    A class that uses the prologix-gpib-ethernet library by nelsond
    to interface a Flann CP2020 controller.

    Check out https://github.com/nelsond/prologix-gpib-ethernet

    Last modified: 19/10/2020 by Eugenio Senes
    '''

    def __init__(self, hostname, gpib_address):
        self = plx_gpib_ethernet.PrologixGPIBEthernetDevice(host=hostname, address=gpib_address)
        self.connect()
        print(self.idn())

    def get_channel(self):
        return self.query('CHAN?')

    def set_channel(self, channel):
        if channel == "A" or channel == "B":
            return self.write('CHAN '+channel)
        else:
            raise ValueError('There are only 2 channels.')

    def get_instrument(self, channel):
        '''
        Returns the name of the instrument connected at that channel.
        '''
        if channel == "A":
            return self.query('INSTDA?')
        elif channel == "B":
            return self.query('INSTDB?')
        else:
            raise ValueError('There are only 2 channels.')

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

    def reset(self):
        self.write('RESET')
        return "Done"

    def get_value(self):
        return self.query('VSET?')

    def set_value(self, value):
        return self.write('VSET '+str(value))



myAtt = CP2020("128.141.161.70", 11)
myAtt.get_channel()
