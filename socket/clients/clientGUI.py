import sys
import socket
import tkinter as tk
from PIL import Image, ImageTk
import random

if len(sys.argv) != 2:
        print("Usage: python3 clientThread.py <hostID>")
        sys.exit(1)

serverIP = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverIP, 1234))

# PIXEL FORMATTING
# Used to adjust pixel coordinates of frames and labels.
HEIGHT=750
WIDTH=1200
OFFSET=25
VALUE_OFFSET = 60
UNIT_OFFSET = 60
LABEL_BEGIN_X = 190
LABEL_BEGIN_Y = 70
COL1 = 0
COL2 = 410
COL3 = 820

# IMAGE PIXEL SIZE REFERENCE
LOGO_HEIGHT=166
LOGO_WIDTH=373
ICON_HEIGHT=60
ICON_WIDTH=60

# UPDATE RANDOM NUMBER TEST
# Tests to see if label values can change without issues.
REFRESH_RATE = 50   # Measured in milliseconds
MIN_FLOAT = 0.0
MAX_FLOAT = 300.0
DIGITS = 2

# normal unit array = replace with error 

# INITIALIZATION
# Creation of the program(root) and its workspace(main_canv).
root = tk.Tk()
root.resizable(False, False)
main_canv = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black',highlightthickness=0)
main_canv.pack()


# IMAGE / ICON FILE PATHS
# Hyperloop Logo courtesy of Cal Poly Pomona Hyperloop Club.
# Icons courtesy of FreePik.com.
#hyperloop_logo = tk.PhotoImage(file='images\\hyperloop\\hyperloop_logo_scale25.png')
battery_icon = tk.PhotoImage(file='images\\icons\\battery.png')
com_icon = tk.PhotoImage(file='images\\icons\\com.png')
kin_icon = tk.PhotoImage(file='images\\icons\\kin.png')
pod_icon = tk.PhotoImage(file='images\\icons\\pod.png')
time_icon = tk.PhotoImage(file='images\\icons\\time.png')
motor_icon = tk.PhotoImage(file='images\\icons\\motor.png')
progress_icon = ImageTk.PhotoImage(file='images\\icons\\progress.png')
calib_icon = tk.PhotoImage(file='images\\icons\\calib.png')

hyperloop_background = tk.PhotoImage(file='images\\background\\2020_2021_background.png')

# HYPERLOOP LOGO
# Creates and adds Hyperloop Logo to the workspace.
#title_logo_canv = tk.Canvas(main_canv, width=LOGO_WIDTH, height=LOGO_HEIGHT, highlightthickness=0)
#title_logo_canv.place(relx=0, rely=0, anchor='nw')
#title_logo_canv.create_image(0,0,anchor='nw',image=hyperloop_logo)

background_canv = tk.Canvas(main_canv, width=WIDTH, height=HEIGHT, highlightthickness=0)
background_canv.place(relx=0, rely=0, anchor='nw')
background_canv.create_image(0,0,anchor='nw',image=hyperloop_background)

# TITLES WITH ICON
# Simplifies positioning of title and icon.

class tkTitle:
    def __init__(self, master=root, title='', iconpos=0.4, titlepos=0.6, icon=battery_icon):
        self.title = tk.Label(master, text=title, bg="black", fg='mistyrose2', font=('Helvetica',20,'bold'), pady=5)
        self.title.place(relx=titlepos, rely=0, anchor='n')

        self.icon = tk.Canvas(master, width=ICON_WIDTH, height=ICON_HEIGHT, highlightthickness=0)
        self.icon.place(relx=iconpos, rely=0, anchor='n')
        self.icon.create_image(0,0,anchor='nw', image=icon)

# LABELS WITH UNITS
# Simplifies positioning of labels, values, and units.
class tkLabelUnit:
    def __init__(self, master=root, str='text', val=0.01, unit='m', list=0, offsetX=0):
        self.label = tk.Label(master, text=str, bg='black', fg='mint cream', font=('garamond',11,), justify='right')
        self.label.place(x=LABEL_BEGIN_X+offsetX, y=LABEL_BEGIN_Y+list*OFFSET, anchor='ne')

        self.value = tk.Label(master, text=val, bg='black', fg='mint cream', font=('garamond',11,), justify='right')
        self.value.place(x=LABEL_BEGIN_X+VALUE_OFFSET+offsetX,y=LABEL_BEGIN_Y+list*OFFSET, anchor='ne')

        self.unit = tk.Label(master, text=unit, bg='black', fg='mint cream', font=('garamond',11,),justify='left')
        self.unit.place(x=LABEL_BEGIN_X+UNIT_OFFSET+offsetX,y=LABEL_BEGIN_Y+list*OFFSET, anchor='nw')

# UPDATE FUNCTION
# Will assign random numbers to values whenever called.
def updateRandValues():

    message = s.recv(2048)
    nums = message.decode('utf-8').split()
    print(nums)
    """
    motorControllerTemp1_Label.value['text'] = float(nums[0])
    motorControllerTemp2_Label.value['text'] = float(nums[1])
    motorTemp1_Label.value['text'] = float(nums[2])
    motorTemp2_Label.value['text'] = float(nums[3])

    batteryVoltage_Label.value['text'] = float(nums[10])
    batteryCurrent_Label.value['text'] = float(nums[10])
    batteryTemp1_Label.value['text'] = float(nums[4])
    """
    motorControllerTemp1.value['text'] = nums[0]
    motorControllerTemp2.value['text'] = nums[1]
    motorTemp1.value['text'] = nums[2]
    motorTemp2.value['text'] = nums[3]
    batterySystemTemp.value['text'] = nums[4]
    # IMU Readings
    calib_system.value['text'] = nums[5]
    calib_gyrometer.value['text'] = nums[6]
    calib_accelerometer.value['text'] = nums[7]
    calib_magnometer.value['text'] = nums[8]

    x_absOrientation.value['text'] = float(nums[9])
    y_absOrientation.value['text'] = float(nums[10])
    z_absOrientation.value['text'] = float(nums[11])

    """
    x_angVelocity.value['text'] = float(nums[8])
    y_angVelocity.value['text'] = float(nums[9])
    z_angVelocity.value['text'] = float(nums[10])
    x_acceleration.value['text'] = float(nums[11])
    y_acceleration.value['text'] = float(nums[12])
    z_acceleration.value['text'] = float(nums[13])
    x_linearAcceleration.value['text'] = float(nums[14])
    y_linearAcceleration.value['text'] = float(nums[15])
    z_linearAcceleration.value['text'] = float(nums[16])
    x_gravity.value['text'] = float(nums[17])
    y_gravity.value['text'] = float(nums[18])
    z_gravity.value['text'] = float(nums[19])
    ambient_temp.value['text'] = float(nums[20])
    """
    # Pressure Sensor 
    kPa_Pressure.value['text'] = nums[21]
    # Current + Voltage Sensor
    motorVoltage.value['text'] = nums[22]
    motorCurrent.value['text'] = nums[23]
    batteryVoltage.value['text'] = nums[24]
    batteryCurrent.value['text'] = nums[25]
    batteryCapacity.value['text'] = nums[26]

    # Recursive function to update values.
    root.after(REFRESH_RATE, updateRandValues)

# totally useful function.
def brakeon():
    s.send(bytes('brakeon', 'utf-8'))
    print('brakeon')

def brakeoff():
    s.send(bytes('brakeoff', 'utf-8'))
    print('brakeoff')

# TIME
# Creates workspace for all time elements.
# Set bg to 'blue' in time_canv to see the extent of the workspace.
TIME_HEIGHT=150
TIME_WIDTH=400
time_canv = tk.Canvas(main_canv, width=TIME_WIDTH, height=TIME_HEIGHT, highlightthickness=0, bg='black')    
time_canv.place(x=COL1, y=35, anchor='nw')

timeTitle = tkTitle(master=time_canv,iconpos=0.5, icon=time_icon)

elapse_label = tk.Label(time_canv, text='Time Elapsed:', bg='black', fg='white', font=('garamond',11,),justify='right')
elapse_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y, anchor='ne')
elapse_value = tk.Label(time_canv, text='00:00:00', bg='black', fg='white', font=('garamond',11,), justify='left')
elapse_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y)

estimate_label = tk.Label(time_canv, text='Expected Run Time:', bg='black', fg='white', font=('garamond',11,),justify='right')
estimate_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y + OFFSET, anchor='ne')
estimate_value = tk.Label(time_canv, text='00:00:00', bg='black', fg='white', font=('garamond',11), justify='left')
estimate_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y + OFFSET)

# COMMUNICATIONS
# Creates workspace for all communication elements.
# Set bg to 'blue' in com_canv to see the extent of the workspace.
COM_HEIGHT=225
COM_WIDTH=400
com_canv = tk.Canvas(main_canv, width=COM_WIDTH, height=COM_HEIGHT, highlightthickness=0, bg='black')   
com_canv.place(x=COL1, y=TIME_HEIGHT+50, anchor='nw')

comLabel = tkTitle(master=com_canv, iconpos=0.5, icon=com_icon)

pod_com_label = tk.Label(com_canv, text='Pod Connection:', bg='black', fg='white', font=('garamond',11,),justify='right')
pod_com_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y, anchor='ne')
pod_com_value = tk.Label(com_canv, text='ESTABLISHED', bg='black', fg='lime green', font=('garamond',11,'bold'), justify='left')
pod_com_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y)

spacex_com_label = tk.Label(com_canv, text='SpaceX Connection:', bg='black', fg='white', font=('garamond',11,),justify='right')
spacex_com_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y + OFFSET, anchor='ne')
spacex_com_value = tk.Label(com_canv, text='NOT ESTABLISHED', bg='black', fg='brown3', font=('garamond',11,'bold'), justify='left')
spacex_com_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y + OFFSET)

""" transSpeed = tkLabelUnit(master=com_canv, str="Transfer Speed:", val=normalUnitArray[0], unit='kB/s', list=2, offsetX=20) """




# MOTOR
# Creates workspace for all motor elements.
# Set bg to 'blue' in motor_canv to see the extent of the workspace.
MOTOR_HEIGHT=280
MOTOR_WIDTH=400
motor_canv = tk.Canvas(main_canv, width=MOTOR_WIDTH, height=MOTOR_HEIGHT, highlightthickness=0, bg='black') 
motor_canv.place(x=COL2, y=35, anchor='nw')

motorTitle = tkTitle(master=motor_canv, iconpos=0.5, icon=motor_icon)

motorControllerTemp1 = tkLabelUnit(master=motor_canv, str='Motor Controller 1 Temp: ', val='Error', unit='°C', list=0)
motorControllerTemp2 = tkLabelUnit(master=motor_canv, str='Motor Controller 2 Temp:', val='Error', unit='°C', list=1)
motorTemp1 = tkLabelUnit(master=motor_canv, str='Motor 1 Temp:', val='Error', unit='°C', list=2)
motorTemp2 = tkLabelUnit(master=motor_canv, str='Motor 2 Temp:', val='Error', unit='°C', list=3)
motorVoltage = tkLabelUnit(master=motor_canv, str='Motor Voltage IN:', val='Error', unit='V', list=4)
motorCurrent = tkLabelUnit(master=motor_canv, str='Motor Current:', val='Error', unit='A', list=5)

# POD
# Creates workspace for physical elements of the pod.
# Set bg to 'blue' in pod_canv to see the extent of the workspace.
POD_HEIGHT=120
POD_WIDTH=400
pod_canv = tk.Canvas(main_canv, width=POD_WIDTH, height=POD_HEIGHT, highlightthickness=0, bg='black')   
pod_canv.place(x=COL3, y=35, anchor='nw')

podTitle = tkTitle(master=pod_canv, iconpos=0.5, icon=pod_icon)

kPa_Pressure = tkLabelUnit(master=pod_canv, str='Pressure:', val='Error', unit='kPa', list=0)
""" pressure_Label = tkLabelUnit(master=pod_canv, str='Pressure:', val='Error', unit='kPa', list=0) """

# KINEMATICS
# Creates workspace for all motion related elements.
# Set bg to 'blue' in kin_canv to see the extent of the workspace.
KIN_HEIGHT=200
KIN_WIDTH=400
kin_canv = tk.Canvas(main_canv, width=KIN_WIDTH, height=KIN_HEIGHT, highlightthickness=0, bg='black')   
kin_canv.place(x=COL1, y=COM_HEIGHT+TIME_HEIGHT+30, anchor='nw')

kinematicTitle = tkTitle(master=kin_canv, iconpos=0.5, icon=kin_icon)

"""
distance_Label = tkLabelUnit(master=kin_canv, str='Distance Traveled:', val=normalUnitArray[10], unit='km', list=0)
velocity_Label = tkLabelUnit(master=kin_canv, str='Pod Speed:', val=normalUnitArray[11], unit='km/h', list=1)
acceleration_Label = tkLabelUnit(master=kin_canv, str='Acceleration:', val=normalUnitArray[12], unit='km/h²', list=2)
"""

# BATTERY
# Creates workspace for elements relating to battery management.
# Set bg to 'blue' in bat_canv to see the extent of the workspace.
BAT_HEIGHT=200
BAT_WIDTH=400
bat_canv = tk.Canvas(main_canv, width=BAT_WIDTH, height=BAT_HEIGHT, highlightthickness=0, bg='black')   
bat_canv.place(x=COL3, y=POD_HEIGHT+35, anchor='nw')

batteryTitle = tkTitle(master=bat_canv, iconpos=0.5, icon=battery_icon)

batterySystemTemp = tkLabelUnit(master=bat_canv, str='Battery System Temp:', val='Error', unit='°C', list=0)
batteryVoltage = tkLabelUnit(master=bat_canv, str='Battery Voltage:', val='Error', unit='V', list=1)
batteryCurrent = tkLabelUnit(master=bat_canv, str='Battery Current:', val='Error', unit='mA', list=2)
batteryCapacity = tkLabelUnit(master=bat_canv, str='Battery Capacity:', val='Error', unit='%', list=3)

"""
batteryCurrent_Label = tkLabelUnit(master=bat_canv, str='Current:', val=normalUnitArray[24], unit='A', list=0)
batteryVoltage_Label = tkLabelUnit(master=bat_canv, str='Voltage:', val=normalUnitArray[25], unit='V', list=1)
batteryLife_Label = tkLabelUnit(master=bat_canv, str='Battery Life:', val=normalUnitArray[26], unit='%', list=2)
batteryTemp1_Label = tkLabelUnit(master=bat_canv, str='Pack 1 Temp:', val=normalUnitArray[15], unit='°C', list=3)
"""

# POD PROGRESS
# Creates workspace for the progress bar of the pod.
# Set bg to 'blue' in prog_canv to see the extent of the workspace.
PROG_HEIGHT=100
PROG_WIDTH=1200
PROG_OFFSET = 25
LINE_HEIGHT = PROG_HEIGHT/2
LINE_START_X = 100
LINE_END_X = PROG_WIDTH-100

# Progress position is dependent on distance.
PERCENTAGE = 0.2641354
PROGRESS_X = int(round(PERCENTAGE * (LINE_END_X - LINE_START_X)))

prog_canv = tk.Canvas(main_canv, width=PROG_WIDTH, height=PROG_HEIGHT, highlightthickness=0, bg='black')    
prog_canv.place(x=0, y=LOGO_HEIGHT+TIME_HEIGHT+COM_HEIGHT+60, anchor='nw')

progTitle = tk.Label(prog_canv, text='Pod Progress', bg='black', fg='white', font=('garamond',16,), pady=5)
progTitle.place(relx=0.05,rely=0.05, anchor='nw')
prog_canv.create_line(LINE_START_X,LINE_HEIGHT,LINE_END_X,LINE_HEIGHT,fill='white', width=5)

startLabel = tk.Label(prog_canv, text='START', bg='black', fg='white', font=('garamond',11,), pady=5)
startLabel.place(x=LINE_START_X, y=LINE_HEIGHT + PROG_OFFSET, anchor='n')
endLabel = tk.Label(prog_canv, text='END', bg='black', fg='white', font=('garamond',11,), pady=5)
endLabel.place(x=LINE_END_X, y=LINE_HEIGHT + PROG_OFFSET, anchor='n')

progressIcon = tk.Canvas(prog_canv, width=40, height=40, highlightthickness=0,bg="black")
progressIcon.place(x=LINE_START_X+PROGRESS_X,y=LINE_HEIGHT,anchor='center')
progressIcon.create_image(0,0,anchor='nw', image=progress_icon)


# BUTTONS / CONTROL
# Creates workspace for buttons.
# Set bg to 'blue' in control_canv to see the extent of the workspace.
# Buttons will send commands to the pod.
CONTROL_HEIGHT = 180
CONTROL_WIDTH = 450
control_canv = tk.Canvas(main_canv, width=CONTROL_WIDTH, height=CONTROL_HEIGHT, highlightthickness=0, bg='black')   
control_canv.place(x=COL2-40, y=TIME_HEIGHT+COM_HEIGHT+50, anchor='nw')

brakeButton = tk.Button(control_canv, text="BRAKES", font=('garamond',18,'bold'), command=brakeon, justify='center', padx=40, pady=10, bg='black', fg='red')
brakeButton.place(relx=0.25,rely=0.40,anchor='center')
brakeLabel = tk.Label(control_canv, text='Brake Status:', bg='black', fg='white', font=('garamond',11,),justify='center')
brakeLabel.place(relx=0.25,rely=0.65, anchor='center')
brakeStatus = tk.Label(control_canv, text='DISENGAGED', bg='black', fg='lime green', font=('garamond',11,'bold'),justify='center')
brakeStatus.place(relx=0.25,rely=0.8, anchor='center')

powerButton = tk.Button(control_canv, text="POWER", font=('garamond',18,'bold'), command=brakeoff, justify='center', padx=40, pady=10, bg='black', fg='red')
powerButton.place(relx=0.75,rely=0.40,anchor='center')
powerLabel = tk.Label(control_canv, text='Power Status:', bg='black', fg='white', font=('garamond',11,),justify='center')
powerLabel.place(relx=0.75,rely=0.65, anchor='center')
powerStatus = tk.Label(control_canv, text='POWER ON', bg='black', fg='lime green', font=('garamond',11,'bold'),justify='center')
powerStatus.place(relx=0.75,rely=0.8, anchor='center')

# CALIBRATION 
# Creates workspace for all calibration elements
# Set bg to 'blue' in motor_canv to see the extent of the workspace.
CALIB_HEIGHT= 280
CALIB_WIDTH= 400
calib_canv = tk.Canvas(main_canv, width=CALIB_WIDTH, height=CALIB_HEIGHT, highlightthickness=0, bg='black') 
calib_canv.place(x=COL3 , y=POD_HEIGHT+BAT_HEIGHT+35 , anchor='nw')

calibTitle = tkTitle(master=calib_canv, iconpos= 0.5, icon=calib_icon) # NEED TO IMPLEMENT CALIB ICON

x_absOrientation = tkLabelUnit(master=calib_canv, str='X Orientation: ', val='Error', unit='°', list=0)
y_absOrientation = tkLabelUnit(master=calib_canv, str='Y Orientation: ', val='Error', unit='°', list=1)
z_absOrientation = tkLabelUnit(master=calib_canv, str='Z Orientation: ', val='Error', unit='°', list=2)
calib_system = tkLabelUnit(master=calib_canv, str='System: ', val='Error', unit='', list=3)
calib_gyrometer = tkLabelUnit(master=calib_canv, str='Gyrometer: ', val='Error', unit='', list=4)
calib_accelerometer = tkLabelUnit(master=calib_canv, str='Accelerometer: ', val='Error', unit='', list=5)
calib_magnometer = tkLabelUnit(master=calib_canv, str='Magnometer: ', val='Error', unit='', list=6)

"""
# Calibration
# Creates workspace for all calib elements.
CALIB_HEIGHT=280
CALIB_WIDTH=400
calib_canv = tk.Canvas(main_canv, width=CALIB_WIDTH, height=CALIB_HEIGHT, highlightthickness=0, bg='black') 
calib_canv.place(x=COL3, y=POD_HEIGHT+BAT_HEIGHT+35, anchor='nw')

calibTitle = tkTitle(master=calib_canv, iconpos=0.5, icon=calib_icon)

calibSystem_Label = tkLabelUnit(master=calib_canv, str='System: ', val="error", unit=' ', list=0)
calibGyro_Label = tkLabelUnit(master=calib_canv, str='Gyro: ', val="error", unit=' ', list=1)

calibAccel_Label = tkLabelUnit(master=calib_canv, str='Accel: ', val="error", unit=' ', list=2)
calibMagno_Label = tkLabelUnit(master=calib_canv, str='Magno:', val="error", unit=' ', list=3)

calibX_Label = tkLabelUnit(master=calib_canv, str='x: ', val="error", unit=' ', list=4)
calibY_Label = tkLabelUnit(master=calib_canv, str='y: ', val="error", unit=' ', list=5)
calibZ_Label = tkLabelUnit(master=calib_canv, str='z: ', val="error", unit=' ', list=6)
"""



# UPDATE / REFRESH
# This is start calling the update function which is recursive.
# The recursion is essentially the update / represh.
root.after(REFRESH_RATE, updateRandValues)

# END
root.mainloop()