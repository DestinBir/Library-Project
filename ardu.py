import pyfirmata
from time import sleep
from playsound import playsound
import tkinter as tk


root = tk.Tk()
root.geometry('1000x200')
root.title('BBC')

rouge = 'Equipe 1'
bleu = 'Equipe 2'

equipe = tk.StringVar()

equipe.set('Neutre')

title_1 = tk.Label(root, textvariable=equipe, font=('Bold', 30))
title_1.grid(columnspan=2, row=0, pady=15, padx=50)

def bluebtn():
    equipe.set(bleu)
    root.configure(bg='blue')

def redbtn():
    equipe.set(rouge)
    root.configure(bg='red')



def timer(t) : 
    while t!=0:
        t=t-1
        sleep(1)
    False 



port = 'COM8'
# try:
arduino = pyfirmata.Arduino(port)
print('Arduino cnnected')
run = True
#except:
#    print('Arduino disconnected')
#    run = False

if run:
    blue = arduino.get_pin('d:2:i')
    red = arduino.get_pin('d:3:i')
    it = pyfirmata.util.Iterator(arduino)
    it.start()

while run:
    try:
        val_b = blue.read()
        val_r = red.read()
        if val_r:
            redbtn()
            print('Rouge')
            playsound('1.wav')
            timer(3)
            
        if val_b:
            bluebtn()
            print('Blue')
            playsound('2.wav')
            timer(3)
    except:
       print('Arduino disconnected')

root.mainloop()