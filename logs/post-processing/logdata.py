import json
import os
import sys

averages = []

if len(sys.argv) != 2:
    print("Usage: python3 logdata.py [filename]")
    sys.exit(1)

filename = sys.argv[1]

print("Reading JSON files")
with open('logs/' + filename + '.json','r') as f:  
    datadict = json.load(f)

listLength = len(datadict[str(0)].split())

for x in range(0, listLength):
    averages.append(0)

for i in range(0, listLength):
    for j in range(0, len(datadict)):
        datavalue = datadict[str(j)].split()
        averages[i] += float(datavalue[i])
    averages[i] /= len(datadict)
    averages[i] = round(averages[i], 3)

#Average
print("Sensor Value Averages: ")
print("Temp Sensor Motor Controller 1: " + str(averages[0]) + "C")
print("Temp Sensor Motor Controller 2: " + str(averages[1]) + "C")
print("Temp Sensor Motor 1: " + str(averages[2]) + "C")
print("Temp Sensor Motor 2: " + str(averages[3]) + "C")
print("Temp Sensor Battery System: " + str(averages[4]) + "C")
print("System Calibration: " + str(averages[5]) + "")
print("Gyrometer Calibration: " + str(averages[6]) + "")
print("Accelerometer Calibration: " + str(averages[7]) + "")
print("Magnometer Calibration: " + str(averages[8]) + "")
print("Orientation X-Axis: " + str(averages[9]) + "°")
print("Orientation Y-Axis: " + str(averages[10]) + "°")
print("Orientation Z-Axis: " + str(averages[11]) + "°")
print("Angular Velocity X-Axis: " + str(averages[12]) + "rad/s")
print("Angular Velocity Y-Axis: " + str(averages[13]) + "rad/s")
print("Angular Velocity Z-Axis: " + str(averages[14]) + "rad/s")
print("Linear Acceleration X-Axis: " + str(averages[15]) + "m/s^2")
print("Linear Acceleration Y-Axis: " + str(averages[16]) + "m/s^2")
print("Linear Acceleration Z-Axis: " + str(averages[17]) + "m/s^2")
print("Magnetic Field X-Axis: " + str(averages[18]) + "uT")
print("Magnetic Field Y-Axis: " + str(averages[19]) + "uT")
print("Magnetic Field Z-Axis: " + str(averages[20]) + "uT")
print("Gravitational Acceleration X-Axis: " + str(averages[21]) + "m/s^2")
print("Gravitational Acceleration Y-Axis: " + str(averages[22]) + "m/s^2")
print("Gravitational Acceleration Z-Axis: " + str(averages[23]) + "m/s^2")
print("Total Acceleration X-Axis: " + str(averages[24]) + "m/s^2")
print("Total Acceleration Y-Axis: " + str(averages[25]) + "m/s^2")
print("Total Acceleration Z-Axis: " + str(averages[26]) + "m/s^2")
print("IMU Board Temperature: " + str(averages[27]) + "C")
print("Pressure: " + str(averages[28]) + "kPa")
print("Low Voltage System [Voltage]: " + str(averages[29]) + "V")
print("Low Voltage System [Current]: " + str(averages[30]) + "mA")
print("BMS Orion [Voltage]: " + str(averages[31]) + "V")
print("BMS Orion [Current]: " + str(averages[32]) + "mA")
print("BMS Orion [Capacity]: " + str(averages[33]) + "%")
print("Brake Actuator: " + str(averages[34]) + "")
print("Motor Controller: " + str(averages[35]) + "")
print("Ping Reading: " + str(averages[36]) + "")

#Orientation

#Graph

#Score