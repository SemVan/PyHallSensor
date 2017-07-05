import serial
import Spectrum_amalyzer
import numpy as np


class Receiver:

    def __init__(self, dev_id):
        self.device_is = dev_id
        self.ser = serial.Serial()
        self.signal = []
        self.number_of_elts = 0
        return

    def init_port(self):
        self.ser.baudrate = 115200
        self.ser.timeout = 1
        self.ser.parity = serial.PARITY_NONE
        self.ser.rtscts = 0
        return

    def init_port_manually(self,port_name):
        self.ser.baudrate = 115200
        self.ser.timeout = 1
        self.ser.parity = serial.PARITY_NONE
        self.ser.rtscts = 0
        self.ser.port = port_name
        try:
            self.ser.open()
        except serial.SerialException as e:
            raise e


    def read_data(self):
        full_buff = ""
        while not(full_buff.__contains__('\r\n')):
            s = self.ser.read()
            s = s.decode('utf-8')
            full_buff += s
        self.parse_data(full_buff)
        return


    def parse_data(self, parcel_str):
        #if type(parcel) != type (b'as'):
          #  return 1

        try:

            elem_list = parcel_str.split("\r\n")

            for elem in elem_list:
                if elem.isdigit():
                    number = int(elem)
                    self.signal.append(number)
                    self.number_of_elts += 1
        except UnicodeEncodeError as e:
            raise e
            return 1
        except ValueError as e:
            raise e
            return 1
        return 0


def write_file(signal_array):
    file = open("signal.txt",'w')
    for elem in signal_array:
        file.write(str(elem))
        file.write('\n')
    file.close()

def filter_signal(signal, window_size):
    filtered_signal = np.convolve(signal, np.ones(window_size,),'valid')
    np.divide(filtered_signal, window_size, filtered_signal)
    return filtered_signal


receiver = Receiver(1)
receiver.init_port_manually("COM3")

filter_size = 91
receiver.ser.reset_input_buffer()
while receiver.number_of_elts < 1024 + filter_size:
    receiver.read_data()

receiver.ser.close()
clear_signal = filter_signal(receiver.signal, filter_size)
write_file(clear_signal)
f1 = open('signal.txt', 'r')


Spectrum_amalyzer.process_signal(f1, 'old', 1)
Spectrum_amalyzer.plt.show()