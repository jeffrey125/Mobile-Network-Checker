from tkinter import *
import tkinter.messagebox
import os

#changes current working directory
os.chdir(r'C:\Users\ACHIM.ACHIM-PC\Desktop\Automate The Boring Stuff\python to exe\Mobile Network Checker')

#Prefixes Numbers
globe = ('0817', '09173', '09175', '09176', '09178', '09253', '09255', '09256', '09257', '09258',
         '0905', '0906', '0915', '0916', '0917', '0926', '0927', '0935', '0936', '0937', '0945',
         '0955', '0956', '0965', '0966', '0967', '0975', '0977', '0978', '0979', '0995', '0996', '0997')	
smart = ('0908', '0918', '0919', '0920', '0921', '0928', '0929', '0939', '0946', '0947', '0949', '0998', '0999')	
tnt = ('0907', '0909', '0910', '0912', '0930', '0938', '0946', '0948', '0950')
sun = ('0922', '0923', '0924', '0925', '0931', '0932', '0933', '0934', '0940', '0941', '0942', '0943', '0973', '0974')

#Lists
globe_list = list(globe)
smart_list = list(smart)
tnt_list = list(tnt)
sun_list = list(sun)

#Main Code
class Maincode:

    def __init__(self, master):
        self.enter_button = Button(bottomframe, text='Enter', command=self.retrieve_input) 
        self.enter_button.grid(row=0, column=2)
        self.clear_button = Button(bottomframe, text='Clear Text Field', command=self.clear)
        self.clear_button.grid(row=0, column=3)
        
    def retrieve_input(self):
        number = entry_box.get('1.0', 'end-1c')
        while True:
            if number in globe_list:
                tkinter.messagebox.showinfo("Mobile Network Checker", "It's a Globe number!")
                break
            elif number in smart_list:
                tkinter.messagebox.showinfo("Mobile Network Checker", "It's a Smart number!")
                break
            elif number in tnt_list:
                tkinter.messagebox.showinfo("Mobile Network Checker", "It's a TNT number!")
                break
            elif number in sun_list:
                tkinter.messagebox.showinfo("Mobile Network Checker", "It's a Sun number!")
                break
            else:
                print("Sorry, I dont think that number is a PH Mobile Network Carrier, Please Try Again.")
                break

    def clear(self):
        entry_box.delete('1.0', END)

#GUI config
root = Tk()
root.title('Mobile Network Checker')

#Icon
root.iconbitmap('mnc.ico')

#Frames
topframe = Frame(root)
bottomframe = Frame(root)
topframe.grid()
bottomframe.grid()

#Greeting
greeting = Label(topframe, text='Hi There! Please Input the First 4 digits of the mobile phone to determine what mobile network they use.')
greeting.grid(row=0)

#Entry box and Label
entry_label = Label(bottomframe, text='Please input it here:')
entry_box = Text(bottomframe, height=1, width=4)
entry_label.grid(row=0)
entry_box.grid(row=0, column=1)

main = Maincode(root)
root.mainloop()





