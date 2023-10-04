import tkinter as tk
from tkinter import *
from tkinter import messagebox


class MyGui:
   def __init__(self):
        self.root  = tk.Tk()
        self.root["bg"] = "black"
        #this is a custom background I was messing with previously
        #filename = PhotoImage(file = "imagegenshin.png")
        #background_label = Label(self.root, image=filename)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.title("Primogem Calculator (bad)")
        self.root.geometry("400x275")
        self.root.resizable(False, False)
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0, bg="black", fg="white")
        self.filemenu.add_command(label="Close", command=exit)
        #function to change theme.
        def change_theme():
            current_mode = self.root["bg"]
            if current_mode == "black":
                self.root["bg"] = "white"
                self.labelDir_for_primos.config(bg="white", fg="black")
                self.primogems.config(bg="white", fg="black")
                self.labelDir_for_days.config(bg="white", fg="black")
                self.days.config(bg="white", fg="black")
                self.filemenu.config(bg="white", fg="black")
                self.labelDir_for_calc2.config(bg="white", fg="black")
                self.welkin.config(bg="white", fg="black")
                return
            if current_mode == "white":
                self.root["bg"] = "black"
                self.labelDir_for_primos.config(bg="black", fg="white")
                self.primogems.config(bg="black", fg="white")
                self.labelDir_for_days.config(bg="black", fg="white")
                self.days.config(bg="black", fg="white")
                self.filemenu.config(bg="black", fg="white")
                self.labelDir_for_calc2.config(bg="black", fg="white")
                self.welkin.config(bg="black", fg="grey")
                
            return
        self.filemenu.add_command(label="Light/Dark mode", command=change_theme)
        #save file function,  yes this is important to define before the menu button.
        def save_to_file():
            result = messagebox.askyesno(
                title= "Save",
                message = "Would you like to save on-screen data?",
                detail = "This will create a new txt file, or overwrite the one that already exists.")
            if not result: 
                return
            if result:
                days_for_calc = float(self.days.get())
                primos_for_calc = float(self.primogems.get())
                file = open("My_Primos_2.txt", "w")
                file.write(f"Primos with: \nCommissions: {(days_for_calc*60) + primos_for_calc}\nWelkin: {(days_for_calc*150) + primos_for_calc}\nWelkin without commissions: {(days_for_calc*90) + primos_for_calc}")
                file.write(f"\nYou have {int(primos_for_calc/160)} pity in primogems already.")
                file.write(f"\nPotential pity:\nCommissions: {int((days_for_calc*60) + primos_for_calc)/160}\nWelkin: {int((days_for_calc*150) + primos_for_calc)/160}\nWelkin without commissions: {int((days_for_calc*90) + primos_for_calc)/160}")
                file.write(f"\nThe original numbers are:\nDays: {days_for_calc} Primos: {primos_for_calc}\n Please add these numbers with your ingame pity if you wish.")
                file.close
                return
        self.filemenu.add_command(label="Save", command=save_to_file, state="disabled")
        self.menubar.add_cascade(menu=self.filemenu, label="Options")
        self.root.config(menu=self.menubar)
        
        
        
        #making the label and entry box for current primogems
        self.labelText_for_primos=StringVar()
        self.labelText_for_primos.set("Enter current primogems")
        self.labelDir_for_primos=Label(self.root, textvariable=self.labelText_for_primos, height=4, bg="black", fg="white")
        self.labelDir_for_primos.pack()
        def button_command():
            days_for_calc = self.days.get()
            primos_for_calc = self.primogems.get()
            self.root.update_idletasks()
            try:
                days_for_calc = int(days_for_calc)
                primos_for_calc = int(primos_for_calc)
            except ValueError:
                self.days.delete(0, END)
                self.primogems.delete(0, END)
                messagebox.showerror("ValueError", "You are missing a number for at least one text entry.")
                return
            
            self.filemenu.entryconfig("Save", state="normal")
            if (self.var1.get() == 1):
                self.root.update_idletasks()
                calculation = (days_for_calc*150) + primos_for_calc
                print(calculation)
                labelText_for_calc=IntVar()
                labelText_for_calc.set(f"Potentially {float(self.days.get())*150 + float(self.primogems.get())} Primos in {self.days.get()} days\n More potential info in txt file.")
                self.labelDir_for_calc2.config(textvariable=labelText_for_calc)
                return 
            if (self.var1.get() == 0):
                calculation = (float(self.days.get())*60 + float(self.primogems.get()))
                print(calculation)
                labelText_for_calc=IntVar()
                
                labelText_for_calc.set(f"Potentially {float(self.days.get())*60 + float(self.primogems.get())} Primos in {self.days.get()} days\n More potential info in txt file.")
                
                self.labelDir_for_calc2.config(textvariable=labelText_for_calc)
                
            return 
        self.directory_for_primos=StringVar(None)
        #entry for primogems
        self.primogems=Entry(self.root,textvariable=self.directory_for_primos,width=20, bg="black", fg="white")
        self.primogems.insert(0, "0")
        self.primogems.pack()
        #making the label and entry box for days
        self.labelText_for_days=StringVar()
        self.labelText_for_days.set("Enter Days")
        self.labelDir_for_days=Label(self.root, textvariable=self.labelText_for_days, height=4, bg="black", fg="white")
        self.labelDir_for_days.pack()

        self.directory_for_days=StringVar(None)
        #entry for days
        self.days=Entry(self.root,textvariable=self.directory_for_days,width=20, bg="black", fg="white")
        self.days.insert(0, "0")
        self.days.pack()


        #checkbox for welkin. and the button
        self.var1 = tk.IntVar()
        self.welkin = tk.Checkbutton(self.root, text='Welkin', variable= self.var1, onvalue=1, offvalue=0, bg="black", fg="light grey")
        self.welkin.pack()
        Button(self.root, text="Calculate", command=button_command).pack()

        #making the label for the calculation
        self.labelText_for_calc2=IntVar()
        self.days_for_label2 = self.days.get()
        self.labelText_for_calc2.set(f"Potentially {0.0} Primos in {0} days.\n More potential info in txt file.")
        self.labelDir_for_calc2=Label(self.root, textvariable=self.labelText_for_calc2, height=4, bg="black", fg="white")
        self.labelDir_for_calc2.pack()
        
        self.root.mainloop()

        
        
        
  
MyGui()



