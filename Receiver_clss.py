import serial



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
            #parcel_str = parcel.decode('utf-8')
            #print(parcel_str)
            elem_list = parcel_str.split("\r\n")

            for elem in elem_list:
                if elem.isdigit():
                    number = int(elem)
                    print(number)
                    self.signal.append(number)
                    self.number_of_elts += 1
        except UnicodeEncodeError as e:
            raise e
            return 1
        except ValueError as e:
            raise e
            return 1
        return 0





str = "laskfaslkf alskfalskfj alkfjaslkfj asfas"
str_list = str.split(" ")
for elem in str_list:
    print(elem)

receiver = Receiver(1)
receiver.init_port_manually("COM3")
while 1:
    receiver.read_data()