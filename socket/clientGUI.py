import socket
import tkinter as tk
from PIL import Image, ImageTk
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.68.120", 1234))

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
normalUnitArray = []
for i in range(30):
    normalUnitArray.append(0)
    # Initialize / populate the array.


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

hyperloop_background = tk.PhotoImage(file='images\\background\\hyperloop_black_background.png')

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

    message = s.recv(1024)
    nums = message.decode('utf-8').split()
    print(nums)
   
    #transSpeed.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    #motorSpeed_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)

    #motorVoltage_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    #motorCurrent_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)

    motorControllerTemp1_Label.value['text'] = float(nums[0])
    motorControllerTemp2_Label.value['text'] = float(nums[1])
    motorTemp1_Label.value['text'] = float(nums[2])
    motorTemp2_Label.value['text'] = float(nums[3])

    #pressure_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    #rideHeight_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    #distance_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    #velocity_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    #acceleration_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)

    batteryVoltage_Label.value['text'] = float(nums[24])
    batteryCurrent_Label.value['text'] = float(nums[25])
    batteryTemp1_Label.value['text'] = float(nums[4])

    # Recursive function to update values.
    root.after(REFRESH_RATE, updateRandValues)

# totally useful function.
def brakeon():
    print('brakeon')

def brakeoff():
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

transSpeed = tkLabelUnit(master=com_canv, str="Transfer Speed:", val=normalUnitArray[0], unit='kB/s', list=2, offsetX=20)

# MOTOR
# Creates workspace for all motor elements.
# Set bg to 'blue' in motor_canv to see the extent of the workspace.
MOTOR_HEIGHT=280
MOTOR_WIDTH=400
motor_canv = tk.Canvas(main_canv, width=MOTOR_WIDTH, height=MOTOR_HEIGHT, highlightthickness=0, bg='black') 
motor_canv.place(x=COL2, y=35, anchor='nw')

motorTitle = tkTitle(master=motor_canv, iconpos=0.5, icon=motor_icon)

motorVoltage_Label = tkLabelUnit(master=motor_canv, str='Voltage: ', val=normalUnitArray[23], unit='V', list=0)
motorCurrent_Label = tkLabelUnit(master=motor_canv, str='Current: ', val=normalUnitArray[22], unit='A', list=1)

motorControllerTemp1_Label = tkLabelUnit(master=motor_canv, str='Controller 1 Temp: ', val=normalUnitArray[0], unit='°C', list=2)
motorControllerTemp2_Label = tkLabelUnit(master=motor_canv, str='Controller 2 Temp:', val=normalUnitArray[1], unit='°C', list=3)
motorTemp1_Label = tkLabelUnit(master=motor_canv, str='Motor 1 Temp:', val=normalUnitArray[2], unit='°C', list=4)
motorTemp2_Label = tkLabelUnit(master=motor_canv, str='Motor 2 Temp:', val=normalUnitArray[3], unit='°C', list=5)


# POD
# Creates workspace for physical elements of the pod.
# Set bg to 'blue' in pod_canv to see the extent of the workspace.
POD_HEIGHT=160
POD_WIDTH=400
pod_canv = tk.Canvas(main_canv, width=POD_WIDTH, height=POD_HEIGHT, highlightthickness=0, bg='black')   
pod_canv.place(x=COL3, y=35, anchor='nw')

podTitle = tkTitle(master=pod_canv, iconpos=0.5, icon=pod_icon)

pressure_Label = tkLabelUnit(master=pod_canv, str='Pressure:', val=normalUnitArray[21], unit='kPa', list=0)

# KINEMATICS
# Creates workspace for all motion related elements.
# Set bg to 'blue' in kin_canv to see the extent of the workspace.
KIN_HEIGHT=200
KIN_WIDTH=400
kin_canv = tk.Canvas(main_canv, width=KIN_WIDTH, height=KIN_HEIGHT, highlightthickness=0, bg='black')   
kin_canv.place(x=COL1, y=COM_HEIGHT+TIME_HEIGHT+30, anchor='nw')

kinematicTitle = tkTitle(master=kin_canv, iconpos=0.5, icon=kin_icon)

distance_Label = tkLabelUnit(master=kin_canv, str='Distance Traveled:', val=normalUnitArray[10], unit='km', list=0)
velocity_Label = tkLabelUnit(master=kin_canv, str='Pod Speed:', val=normalUnitArray[11], unit='km/h', list=1)
acceleration_Label = tkLabelUnit(master=kin_canv, str='Acceleration:', val=normalUnitArray[12], unit='km/h²', list=2)

# BATTERY
# Creates workspace for elements relating to battery management.
# Set bg to 'blue' in bat_canv to see the extent of the workspace.
BAT_HEIGHT=300
BAT_WIDTH=400
bat_canv = tk.Canvas(main_canv, width=BAT_WIDTH, height=BAT_HEIGHT, highlightthickness=0, bg='black')   
bat_canv.place(x=COL3, y=POD_HEIGHT+50, anchor='nw')

batteryTitle = tkTitle(master=bat_canv, iconpos=0.5, icon=battery_icon)


batteryCurrent_Label = tkLabelUnit(master=bat_canv, str='Current:', val=normalUnitArray[24], unit='A', list=0)
batteryVoltage_Label = tkLabelUnit(master=bat_canv, str='Voltage:', val=normalUnitArray[25], unit='V', list=1)
batteryLife_Label = tkLabelUnit(master=bat_canv, str='Battery Life:', val=normalUnitArray[26], unit='%', list=2)
batteryTemp1_Label = tkLabelUnit(master=bat_canv, str='Pack 1 Temp:', val=normalUnitArray[15], unit='°C', list=3)


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


# UPDATE / REFRESH
# This is start calling the update function which is recursive.
# The recursion is essentially the update / represh.
root.after(REFRESH_RATE, updateRandValues)

# END
root.mainloop()