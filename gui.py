from tkinter import *
from data import data_pull, cleanup
import time
from error_handler import Error_Handler
from error_handler import check_hr, check_bo, check_bp
from datastore import insertData, getData
from encryption import encrypt, generate_key
from alert_system import page_doctor
from pathlib import Path
import os
import random

# Time intervals for retrieving data
hr_interval = 5
bp_interval = 5
bo_interval = 5

min_int = 5

# current p_id
p_id = random.randint(0,10000)

##Generate private/public key
key_file = str(p_id)+".key"
if not os.path.isfile(key_file):
    private_key = generate_key(p_id)
# Run the UI
def runUI():

    window = Tk()
    
    hr = IntVar()
    bp = IntVar()
    bp2 = IntVar()
    bo = IntVar()

    window.title("Patient : " + str(p_id))
    
    label1 = Label(window, text='Heart Rate')
    label1.grid(row=0, column=0)

    textBox1 = Label(window, height=2, width=10, textvariable = hr)
    textBox1.grid(row=1, column=0)
    
    label2 = Label(window, text='Systolic Blood Pressure')
    label2.grid(row=0, column=1)

    textBox2 = Label(window, height=2, width=10, textvariable = bp)
    textBox2.grid(row=1, column=1)

    label2 = Label(window, text='Diastolic Blood Pressure')
    label2.grid(row=0, column=2)

    textBox2 = Label(window, height=2, width=10, textvariable = bp2)
    textBox2.grid(row=1, column=2)

    label3 = Label(window, text='Blood Oxygen')
    label3.grid(row=0, column=3)

    textBox3 = Label(window, height=2, width=10, textvariable = bo)
    textBox3.grid(row=1, column=3)
    
    def dataLoop():
        mainLoop(hr, bp, bp2, bo)
        window.after(10, dataLoop)
    
    window.after(10, dataLoop)
    
    def on_closing():
        cleanup()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()

# Grab data
# Send to UI
# Attempt to encrypt data
# Store (theoretically encrypted) data
# Handle errors
def mainLoop(hr, bp, bp2, bo):
    min_int = min(hr_interval, bp_interval, bo_interval)
    data_obj = data_pull()
    insertData(p_id,data_obj)

    hr.set(data_obj.get("heart_rate"))
    bp.set(data_obj.get("blood_pressure1"))
    bp2.set(data_obj.get("blood_pressure2"))
    bo.set(data_obj.get("blood_oxygen"))

    ##data encryption
    # encrypted_message = encrypt(data_obj, private_key)
    # print(encrypted_message)
    ##data storage
    #insertData(1, encrypted_message)

    #workaround to store unencrypted data
    if(Error_Handler(data_obj)):
        page_doctor(data_obj,0x01,check_hr(data_obj))
        page_doctor(data_obj,0x02,check_bp(data_obj))
        page_doctor(data_obj,0x03,check_bo(data_obj))
