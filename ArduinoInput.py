#Copyright 2022 Caleb Stupin
#PHSC 480 Advanced Physics Laboratory
#FILE NAME: ArduinoInput.py
#PROJECT NAME: Raspberry Pi Oscilloscope with Fourier Analysis Capability
#DESCRIPTION: Inputs values from the Arduino

import numpy as np
import time
import serial

#Initialize serial port (USB)
ser = serial.Serial('/dev/ttyACM0', 38400, timeout = 1)

#For testing purposes
#t=1
#def oscilloscope_input():
#    return np.sin(20*(t + time.time())) 
#l = []

#FUNCTION: oscilloscope_input()
#DESCRIPTION: returns an analog value from the Arduino ADC
#PARAMETERS: N/A
#RETURNS: output, a string the ADC value reading
#GLOBALS: ser, the serial port information
def oscilloscope_input():
    input = str(ser.read()).strip('b\'')        #strips the string of b and ' characters 
    #print(ser.read(5))
    #str(input).strip('b\'')
    l = []
    if input == '\\n':                          #newline character signals start of the number
        
        newval = str(ser.read()).strip('b\'')
        if newval != '\r':                      #\r character signals end of number
            l.append(newval)
                
        newval = str(ser.read()).strip('b\'')
        if newval != '\r':
            l.append(newval)
        else:
            return ''.join(l)
        
        newval = str(ser.read()).strip('b\'')
        if newval != '\r':
            l.append(newval)
    
    #print(''.join(l))
    
    output = ''.join(l)
    output.strip('\n')
    
    return output.strip(' ')                    #newline characters and spaces will make isdigit() return false, so they must be stripped
    


#For testing purposes: 
#print (oscilloscope_input())
    
#for i in range(100):
    #while True:
    #    a = oscilloscope_input()
    #    if a.isdigit() and  a != '':
    #	    print(a)
    #	    break
