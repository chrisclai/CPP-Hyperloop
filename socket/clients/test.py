from tkinter import *

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def toggleText():  
	if(button['text']=='Submit'):
		button['text']='Submitted'
	else:
		button['text']='Submit'

button = Button(tkWindow,
	text = 'Submit',
	command = toggleText)  
button.pack()  
  
tkWindow.mainloop()

button_swtich = True

def click():
    global button_swtich
    if button_swtich:
        button_switch = False
    else:
        button_swtich = True

brakeButton = tk.Button(control_canv, text="BRAKES", font=('garamond',18,'bold'), command=brake_status, justify='center', padx=40, pady=10, bg='black', fg='red')
brakeButton.place(relx=0.25,rely=0.40,anchor='center')
brakeLabel = tk.Label(control_canv, text='Brake Status:', bg='black', fg='white', font=('garamond',11,),justify='center')
brakeLabel.place(relx=0.25,rely=0.65, anchor='center')
brakeStatus = tk.Label(control_canv, text='DISENGAGED', bg='black', fg='lime green', font=('garamond',11,'bold'),justify='center')
brakeStatus.place(relx=0.25,rely=0.8, anchor='center')

motorButton = tk.Button(control_canv, text="MOTOR", font=('garamond',18,'bold'), command=motor_status, justify='center', padx=40, pady=10, bg='black', fg='red')
motorButton.place(relx=0.75,rely=0.40,anchor='center')
motorLabel = tk.Label(control_canv, text='Motor Status:', bg='black', fg='white', font=('garamond',11,),justify='center')
motorLabel.place(relx=0.75,rely=0.65, anchor='center')
motorStatus = tk.Label(control_canv, text='MOTOR ON', bg='black', fg='lime green', font=('garamond',11,'bold'),justify='center')
motorStatus.place(relx=0.75,rely=0.8, anchor='center')

    # 
    brakeButton.command = int(nums[31]) # status of brakes
    motorButton.command = int(nums[32]) # status of motors

    # Recursive function to update values.
    root.after(REFRESH_RATE, updateRandValues)

    message = s.recv(2048)
    nums = message.decode('utf-8').split()
    print(nums)

# totally useful function.
def brake_status(): # element 31 = brakes; element 32 = motors
    if brakes == 0: 
        s.send(bytes('brakeon', 'utf-8')) 
        print('brake on')
    elif brakes == 1: 
        s.send(bytes('brakeoff', 'utf-8')) 
        print('brake off')
    else:
        pass

def motor_status():
    if motors == 0: 
        s.send(bytes('motoron', 'utf-8')) 
        print('motor on')
    elif motors == 1: 
        s.send(bytes('motoroff', 'utf-8')) 
        print('motor off')
    else:
        pass