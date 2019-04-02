import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import sys



class imageProcessor:
    def __init__(self):

        #Directory where the two folders for processed and not processed are contained
        #This method grabs the folder where the program is saved
        self.directory = os.path.dirname(os.path.realpath(__file__)) + '/'
        self.pics = dict()
        
        self.k = 0
        self.max = 0

        #We iterate through every file contained in the not processed folder
        for filename in os.listdir(self.directory + 'Not_Processed/'):
            if('.png' in filename):
                self.pics[self.k] = filename
                self.k += 1
        if(self.k == 0):
            print('Error: ','There are no pictures in the Not_Processed folder')
            sys.exit()
            
        self.max = self.k
        self.k = 0
        
        self.window = tk.Tk()
        self.window.bind('<Return>', self.enter)
        self.top_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)

        #Mount picture onto Top Frame
        
        self.img = ImageTk.PhotoImage(Image.open(self.directory + 'Not_Processed/' + self.pics[self.k]))
        
        self.panel = tk.Label(self.top_frame, image = self.img)

        #Mount things in Bottom Frame
 
        self.comment_entry = tk.Entry(self.bottom_frame, width = 50)
        self.note_label = tk.Label(self.bottom_frame, text = 'Notes:')

        #Pack Everything
        self.panel.pack(side = 'top')
        self.note_label.pack(side = 'left')
        self.comment_entry.pack(side = 'left')

        #Pack Frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Start the idle loop waiting for event
        self.window.mainloop()

    #This function handles the enter key
    def enter(self, event):
        comment = self.comment_entry.get()
        comment = comment.lower()
        openF = open(self.directory + '/Processed/My Comments.txt', 'a')
        
        #Handle notes entered
        if comment == 'g':
            openF.write(self.pics[self.k] + '\t Good'  + '\n')
            os.rename(self.directory + 'Not_Processed/' + self.pics[self.k], self.directory + 'Processed/' + self.pics[self.k])
            
        elif comment == 'b':
            openF.write(self.pics[self.k] + '\t Bad' + '\n')
            os.rename(self.directory + 'Not_Processed/' + self.pics[self.k], self.directory + 'Processed/' + self.pics[self.k])
            
            
        elif comment == 'quit':
            self.k = self.max
           
        else:
            openF.write(self.pics[self.k] + '\t' + comment + '\n')
            os.rename(self.directory + 'Not_Processed/' + self.pics[self.k], self.directory + '/Processed/' + self.pics[self.k])
        
        openF.close()
        if(self.k + 1 < self.max):
            self.comment_entry.delete(0, 'end')
            self.k += 1
            self.img = ImageTk.PhotoImage(Image.open(self.directory + 'Not_Processed/' + self.pics[self.k]))
            self.panel.configure(image = self.img)
            self.panel.update()
        else:
            messagebox.showinfo('Image Processor','There are no more pictures')
            self.window.destroy()
        
test = imageProcessor()
