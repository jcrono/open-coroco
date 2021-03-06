#!/usr/bin/env python

#importing libraries
import yarp as y
import serial  as s
from serial import SerialException
from numpy  import pi
from time   import sleep
from motor_tools  import *
#from motor_position import *


#--------------Yarp ports definition---------------------

#starting yarp network
y.Network.init()


#creting an output port for stm32_1_position
out_1       =y.BufferedPortBottle()
out_1_name  ="/stm32_2/position/out1"
out_1.open(out_1_name)


#creating an input port from stm32_2
in_1        =y.BufferedPortBottle()
in_1_name   ="/stm32_2/position/in1"
in_1.open(in_1_name)


#creating an input port from PS3 controller
in_speed        =y.BufferedPortBottle()
in_speed_name   ="/stm32_2/speed/in_1"
in_speed.open(in_speed_name)



#connecting with remote port STM32_1
style=y.ContactStyle()
style.persistent=1
stm32_1_input_port_1_name="/stm32_1/position/in1"
stm32_3_input_port_1_name="/stm32_3/position/in2"
stm32_4_input_port_1_name="/stm32_4/position/in2"
y.Network.connect(out_1_name,stm32_1_input_port_1_name,style)
y.Network.connect(out_1_name,stm32_3_input_port_1_name,style)
y.Network.connect(out_1_name,stm32_4_input_port_1_name,style)



#------------------Initial values -----------------

#for speeds and postition calculations
max_speed=12*2*pi
last_raw_angle=0.
raw_angle=0.
angle=0.
rads=0.

value=33
cmd_speed=0.0

#for serial port
stm32_1=motor_position()
stm32_2=motor_position()
serial_device_counter=0
connected=False

serial_1=0



motor=motor_tools()


while True:

    #-------------------Confirming stm32_1_position from yarp bottles-----------

    #stm32_1=motor.checking_motor_position('1',stm32_1,stm32_2_input_port_1,stm32_2_input_port_1_name)
    stm32_1=motor.checking_motor_position('1',stm32_1,in_1,in_1_name)

    #print "motor 1=> serial: ",stm32_1.serial,"position: ",stm32_1.position
    #raw_input("raw input")
    #------------Connecting to the serial port---------------------

    #initial connection
    motor.connecting_to_stm32(2,stm32_1.serial,0,0,0)
   

    #-----------------------------
    try:
   
        while motor.connected==True:

  
            motor.serial_port_communication(motor,cmd_speed,value)


            #-----------Connected to STM32-------------------------------

            if motor.position=='2':            
            
                #-------------------Communication though yarp bottles-----------
                sleep(0.01)

                #sending a bottle through the output_port_1
                motor.send_a_bottle(out_1,motor.position,motor.serial_device_counter)

                #receaving a bottle from the input port 1
                motor.receive_a_motor_bottle(in_1,in_1_name)
                
                #receiving a bottle from PS3 controller
                cmd_speed=motor.receive_a_joystick_bottle(in_speed,in_speed_name)

            #------not connected to STM32 2----------------
            else:
                motor.retry_serial_connection()

    except SerialException:
        motor.serial_exception_handling()
 
