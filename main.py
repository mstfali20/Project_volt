import serial
from serial import Serial
import tkinter as tk 
import time
import xlsxwriter
import keyboard

volt3 = []
volt2 = []
volt1 = []


def main():
    planWorkbook = xlsxwriter.Workbook('not.xlsx')
    planSheet = planWorkbook.add_worksheet('calculus')



    planSheet.write('A1',1)
    planSheet.write('B1',2)
    planSheet.write('C1',3)


    form =tk.Tk() 
    form.resizable(False,False)
    form.title('Gui')
    form.geometry('300x45') 
    port=tk.Label(text='PORT',fg='black',bg='white',font='Times 10 bold') 
    port.place(x=0,y=0) 
    baudrate=tk.Label(text='Baundrate',fg='black',bg='white',font='Times 10 bold') 
    baudrate.place(x=0,y=20) 
    port_entr=tk.Entry() 
    port_entr.place(x=50,y=0) 
    baudrate_entr=tk.Entry() 
    baudrate_entr.place(x=70,y=20) 
    def kayitog(): 
        

        global x
        x = 2

        global y
        y = 2

        global z
        z = 2

        ser = serial.Serial(port_entr.get(),baudrate_entr.get())
        while True:

            data = ser.readline().decode('utf').strip('\n')
 
            if ' volt3' in data:
                volt3.append(data)
                planSheet.write('C'+ str(z), data.strip('\n'))
                z += 1
            if ' volt2' in data:
                volt2.append(data)
                planSheet.write('B'+ str(x), data.strip('\n'))
                x += 1
            if ' volt' in data:
                volt1.append(data)
                planSheet.write('A'+ str(y), data.strip('\n'))
                y += 1            

            if keyboard.is_pressed('q'):
                close()
    def close():


        planWorkbook.close()
        exit()

    btn=tk.Button(form,text='Enter',fg='bLack',bg='white',command=kayitog)
    btn.place(x=200,y=20) 


    form.mainloop()     
    

main()