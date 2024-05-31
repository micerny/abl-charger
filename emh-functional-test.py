import myminimalmodbus
# myminimalmodbus is a modified version of minimalmodbus, where is changed response header from ":", to ">"

# Thic code works with ABL eMH1 1W1108 wallbox and any RS485 to USB converter
# Arguments: no argument = print status
#            number = set current in A (possible values 6-16)
#            enable = enable charging
#            disable = disable charging


import serial
import sys
import math as m

def initialize(ABL):
    ABL.serial.baudrate = 38400
    ABL.serial.parity = serial.PARITY_EVEN
    ABL.serial.bytesize = 8
    ABL.serial.stopbits = 1
    try:
        res = ABL.read_registers(1,2) # Dummy call to wake up RS485
    except Exception as e:
        print('Wallbox is ready to communicate')
    return

def get_status_text(status):
    if status == 161:
        return 'Wait for connection'
    elif status == 177:
        return 'Wait for enablement'
    elif status == 178:
        return 'Charging enabled'
    elif status == 194:
        return 'Charging'
    else:
        return 'Unknown status/Charging dissabled'


def read_data(ABL):
    I_set = 0
    Statustext = "ABL no answer"

    if (ABL.read_registers(15,5)== 65535): 
        Statustext = "ABL no answer"
    else:
        value_list = ABL.read_registers(46,5)
        Status = int(m.fmod(value_list[0],256))
        Statustext = get_status_text(Status)
        print('Status: ', Statustext)
# this code is for wallbox with current sensors (I dont't have it)
#        if (Status == 194):
#            i = 2
#            Current = 0
#            while i <= 4:
#                Current= float(value_list[i])/10 #current read out in A provided by eMH1 current sensors
#                Power = Power + Current * VOLTAGE # VOLTAGE either fixed or read by other device
#                i=i+1
#            print('Current R: ', float(value_list[2])/10)
#            print('Current S: ', float(value_list[3])/10)
#            print('Current T: ', float(value_list[4])/10)
#            print('Actual Power: ', Power)
        I_set = (m.fmod(value_list[1],256))/16.66667
        print('Charging point: ', round(I_set,2))

    return 

def set_current (I_Set):
    print('Setting new Charging point ', I_Set)
    ABL.write_registers(20,[int(float(I_Set)*16.66667)]) #set setpoint for current
    return

def set_enable():
    #print('Hexa A1A1 is ', int('A1A1', 16))
    ABL.write_register(registeraddress=5, value=int('A1A1', 16), number_of_decimals=0, functioncode = 16, signed = False)
    return

def set_disable():
    #print('Hexa E0E0 is ', int('E0E0', 16))
    ABL.write_register(registeraddress=5, value=int('E0E0', 16), number_of_decimals=0, functioncode = 16, signed = False)
    return

def is_valid_number(number_str):
    try:
        number = float(number_str)
        if 0 <= number <= 16:
            return True
        else:
            print(f"Number {number_str} is not within the range 0-16.")
            return False
    except ValueError:
        #print(f"Number {number_str} is not a valid number.")
        return False

# Initialize Modbus communication
#ABL = myminimalmodbus.Instrument('/dev/ttyACM0', 1, myminimalmodbus.MODE_ASCII, False, debug=False)
ABL = myminimalmodbus.Instrument('/dev/ttyUSB0', 1, myminimalmodbus.MODE_ASCII, False, debug=False)
initialize(ABL)

read_data(ABL)


args = sys.argv
if len(args) > 1:
    if is_valid_number(args[1]):
        set_current(args[1])
    if args[1] == 'enable':
        set_enable()
    if args[1] == 'disable':
        set_disable()

ABL.serial.close()
