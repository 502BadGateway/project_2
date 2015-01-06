from Tkinter import*
import random
window = Tk()
arena = Canvas(window, width = 500, height = 500, bg = 'white')
arena.pack()
key = Canvas(window, width = 500, height = 170, bg = 'grey')
key.pack()

gif1 = PhotoImage(file = 'red.gif')
key.create_image(40, 90, image = gif1)
window.mainloop()
