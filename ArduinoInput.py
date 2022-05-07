import numpy as np
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 38400, timeout = 1)
t=1

#def oscilloscope_input():
#    return np.sin(20*(t + time.time())) 
#l = []

old_L = ''

lastVal = 0

def oscilloscope_input():
    input = str(ser.read()).strip('b\'')   #strips the string of b and ' characters 
    #print(ser.read(5))
    #str(input).strip('b\'')
    l = []
    if input == '\\n':
        
        newval = str(ser.read()).strip('b\'')
        if newval != '\r':
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
    
    return output.strip(' ')
    


#For testing purposes: 
#print (oscilloscope_input())
    
#for i in range(100):
    #while True:
    #    a = oscilloscope_input()
    #    if a.isdigit() and  a != '':
    #	    print(a)
    #	    break
