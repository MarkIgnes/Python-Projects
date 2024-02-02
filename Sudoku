from tkinter import *
import tkinter as tk
import random
from numpy import loadtxt

window = Tk()
window.geometry("720x650")
window.resizable(0, 0)
#window.resizable(0,0)
canvas = Canvas(window, width = 720, height = 650)
canvas.pack()
#Vertical Lines
line = canvas.create_line(235, 70, 235, 630, width=(15), fill="gray")
line = canvas.create_line(458, 70, 458, 630, width=(15), fill="gray")
#Horizontal lines
line = canvas.create_line(10, 256, 690, 256, width=(15), fill="gray")
line = canvas.create_line(10, 441, 690, 441, width=(15), fill="gray")

clear_val = 0
seed_val = 0
def clear():
    #print("Botton works")
    global clear_val
    clear_val = 1
    for y in range(9):
        for x in range(9):
            if y == 8 and x == 8:
                clear_val = 0
            entry_text[(y*9)+x].set('')
def seed():
    
    ran_num = random.randrange(0,10)
    seed = loadtxt("seeds.txt",dtype = int, comments = "#", delimiter=",",skiprows = ran_num, unpack = False, max_rows = 1)
    global seed_val
    seed_val = 1
    for y in range(9):
        for x in range(9):
            if y == 8 and x == 8:
                seed_val = 0
            entry_text[(y*9)+x].set(seed[(y*9)+x])
     
def Inst_Bttns():
    clear_btn = tk.Button(window, text='Clear', command = clear, width= 10)
    clear_btn.place( x = 600,y=10)

    seed_btn = tk.Button(window, text='Seed', command = seed, width= 10)
    seed_btn.place( x = 600,y=40)

entry_text = [StringVar() for i in range(81)]

FixedCell = [Entry(window, width=2, textvariable=entry_text[i], font=("Ariel", 30), justify = CENTER) for i in range(81)]

#placing the entry boxes
for y in range(9):
    for x in range(9):
        FixedCell[(y*9)+x].place(x=(38 + (x * 71) + (10*(x//3))), y=(80+(y*60)+(5*(y//3))) )


# the label for game centered
Title = Label(window, text="SuDoKu!!!").place(x=330, y=40)

#defines the values to '' and 1-9, also does all the comparision logic for sudoku
def character_limit(entry_txt):
    #character value checker
    try:
        num_temp = int(entry_txt.get())
        if len(entry_txt.get()) > 1:
            if '0' in entry_txt.get():
                entry_txt.set(entry_txt.get()[:1])
            else:
                entry_txt.set(entry_txt.get()[-1:])
        else:
            if num_temp == 0:
                entry_txt.set('')
    except ValueError:
        if len(entry_txt.get()) > 1:
            entry_txt.set(entry_txt.get()[:1])
        else:
            entry_txt.set('')
                 
    #sudoku comparison logic
    Completion_Checker = 0
    if clear_val != 1 and seed_val != 1:
        for y in range(9):
            for z in range(9):
                if entry_text[z+(9*y)].get() == '':
                    FixedCell[z+(9*y)].config(background= "white" )
                else:
                    h_count=0
                    v_count=0
                    b_count=0
                    for a in range(9):
                        part1 = a*3
                        part2 = ((a%3)*2)
                        part3 = ((z//3)*3)
                        part4 = ((y//3)*27)
                        B_cell = ((part1-part2)+part3+part4)
                            
                        if entry_text[z+(9*y)].get() == entry_text[a+(9*y)].get():
                            if z+(9*y) != a+(9*y):
                                FixedCell[z+(9*y)].config(background= "red" )
                        else:
                            h_count+=1

                        if entry_text[z+(9*y)].get() == entry_text[((a*9)+z)].get():
                            if z+(9*y) != (a*9)+z:
                                FixedCell[z+(9*y)].config(background= "red" )
                        else:
                            v_count+=1

                        if entry_text[z+(9*y)].get() == entry_text[B_cell].get():
                            if z+(9*y) != B_cell:
                                FixedCell[z+(9*y)].config(background= "red" )
                        else:
                            b_count+=1
                                 
                        if h_count == 8 and v_count == 8 and b_count == 8:
                            FixedCell[z+(9*y)].config(background= "white" )
                            Completion_Checker+=1
                       
    if Completion_Checker == 82:
        for y in range(9):
            for z in range(9):
                FixedCell[z+(9*y)].config(background= "green" )
        
                

def Define_Traces():

    entry_text[0].trace("w", lambda *args: character_limit(entry_text[0]))
    entry_text[1].trace("w", lambda *args: character_limit(entry_text[1]))
    entry_text[2].trace("w", lambda *args: character_limit(entry_text[2]))
    entry_text[3].trace("w", lambda *args: character_limit(entry_text[3]))
    entry_text[4].trace("w", lambda *args: character_limit(entry_text[4]))
    entry_text[5].trace("w", lambda *args: character_limit(entry_text[5]))
    entry_text[6].trace("w", lambda *args: character_limit(entry_text[6]))
    entry_text[7].trace("w", lambda *args: character_limit(entry_text[7]))
    entry_text[8].trace("w", lambda *args: character_limit(entry_text[8]))
    entry_text[9].trace("w", lambda *args: character_limit(entry_text[9]))
    entry_text[10].trace("w", lambda *args: character_limit(entry_text[10]))
    entry_text[11].trace("w", lambda *args: character_limit(entry_text[11]))
    entry_text[12].trace("w", lambda *args: character_limit(entry_text[12]))
    entry_text[13].trace("w", lambda *args: character_limit(entry_text[13]))
    entry_text[14].trace("w", lambda *args: character_limit(entry_text[14]))
    entry_text[15].trace("w", lambda *args: character_limit(entry_text[15]))
    entry_text[16].trace("w", lambda *args: character_limit(entry_text[16]))
    entry_text[17].trace("w", lambda *args: character_limit(entry_text[17]))
    entry_text[18].trace("w", lambda *args: character_limit(entry_text[18]))
    entry_text[19].trace("w", lambda *args: character_limit(entry_text[19]))
    entry_text[20].trace("w", lambda *args: character_limit(entry_text[20]))
    entry_text[21].trace("w", lambda *args: character_limit(entry_text[21]))
    entry_text[22].trace("w", lambda *args: character_limit(entry_text[22]))
    entry_text[23].trace("w", lambda *args: character_limit(entry_text[23]))
    entry_text[24].trace("w", lambda *args: character_limit(entry_text[24]))
    entry_text[25].trace("w", lambda *args: character_limit(entry_text[25]))
    entry_text[26].trace("w", lambda *args: character_limit(entry_text[26]))
    entry_text[27].trace("w", lambda *args: character_limit(entry_text[27]))
    entry_text[28].trace("w", lambda *args: character_limit(entry_text[28]))
    entry_text[29].trace("w", lambda *args: character_limit(entry_text[29]))
    entry_text[30].trace("w", lambda *args: character_limit(entry_text[30]))
    entry_text[31].trace("w", lambda *args: character_limit(entry_text[31]))
    entry_text[32].trace("w", lambda *args: character_limit(entry_text[32]))
    entry_text[33].trace("w", lambda *args: character_limit(entry_text[33]))
    entry_text[34].trace("w", lambda *args: character_limit(entry_text[34]))
    entry_text[35].trace("w", lambda *args: character_limit(entry_text[35]))
    entry_text[36].trace("w", lambda *args: character_limit(entry_text[36]))
    entry_text[37].trace("w", lambda *args: character_limit(entry_text[37]))
    entry_text[38].trace("w", lambda *args: character_limit(entry_text[38]))
    entry_text[39].trace("w", lambda *args: character_limit(entry_text[39]))
    entry_text[40].trace("w", lambda *args: character_limit(entry_text[40]))
    entry_text[41].trace("w", lambda *args: character_limit(entry_text[41]))
    entry_text[42].trace("w", lambda *args: character_limit(entry_text[42]))
    entry_text[43].trace("w", lambda *args: character_limit(entry_text[43]))
    entry_text[44].trace("w", lambda *args: character_limit(entry_text[44]))
    entry_text[45].trace("w", lambda *args: character_limit(entry_text[45]))
    entry_text[46].trace("w", lambda *args: character_limit(entry_text[46]))
    entry_text[47].trace("w", lambda *args: character_limit(entry_text[47]))
    entry_text[48].trace("w", lambda *args: character_limit(entry_text[48]))
    entry_text[49].trace("w", lambda *args: character_limit(entry_text[49]))
    entry_text[50].trace("w", lambda *args: character_limit(entry_text[50]))
    entry_text[51].trace("w", lambda *args: character_limit(entry_text[51]))
    entry_text[52].trace("w", lambda *args: character_limit(entry_text[52]))
    entry_text[53].trace("w", lambda *args: character_limit(entry_text[53]))
    entry_text[54].trace("w", lambda *args: character_limit(entry_text[54]))
    entry_text[55].trace("w", lambda *args: character_limit(entry_text[55]))
    entry_text[56].trace("w", lambda *args: character_limit(entry_text[56]))
    entry_text[57].trace("w", lambda *args: character_limit(entry_text[57]))
    entry_text[58].trace("w", lambda *args: character_limit(entry_text[58]))
    entry_text[59].trace("w", lambda *args: character_limit(entry_text[59]))
    entry_text[60].trace("w", lambda *args: character_limit(entry_text[60]))
    entry_text[61].trace("w", lambda *args: character_limit(entry_text[61]))
    entry_text[62].trace("w", lambda *args: character_limit(entry_text[62]))
    entry_text[63].trace("w", lambda *args: character_limit(entry_text[63]))
    entry_text[64].trace("w", lambda *args: character_limit(entry_text[64]))
    entry_text[65].trace("w", lambda *args: character_limit(entry_text[65]))
    entry_text[66].trace("w", lambda *args: character_limit(entry_text[66]))
    entry_text[67].trace("w", lambda *args: character_limit(entry_text[67]))
    entry_text[68].trace("w", lambda *args: character_limit(entry_text[68]))
    entry_text[69].trace("w", lambda *args: character_limit(entry_text[69]))
    entry_text[70].trace("w", lambda *args: character_limit(entry_text[70]))
    entry_text[71].trace("w", lambda *args: character_limit(entry_text[71]))
    entry_text[72].trace("w", lambda *args: character_limit(entry_text[72]))
    entry_text[73].trace("w", lambda *args: character_limit(entry_text[73]))
    entry_text[74].trace("w", lambda *args: character_limit(entry_text[74]))
    entry_text[75].trace("w", lambda *args: character_limit(entry_text[75]))
    entry_text[76].trace("w", lambda *args: character_limit(entry_text[76]))
    entry_text[77].trace("w", lambda *args: character_limit(entry_text[77]))
    entry_text[78].trace("w", lambda *args: character_limit(entry_text[78]))
    entry_text[79].trace("w", lambda *args: character_limit(entry_text[79]))
    entry_text[80].trace("w", lambda *args: character_limit(entry_text[80]))

Inst_Bttns()
Define_Traces()
window.mainloop()
