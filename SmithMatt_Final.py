from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("YardStick")
root.geometry("800x500")
img1= PhotoImage(file = r"C:\Users\smity\OneDrive\Pictures\landscape.png")

myCanvas = Canvas(root, width=800, height=500)
myCanvas.pack(fill="both", expand=True)

myCanvas.create_image(0,0, image= img1, anchor="nw")

myTitle = Label(root, text="YardStick!", width=40, height=5, font=('Times New Roman', 15, 'bold')).grid(row=0, columnspan=3)
myDescription = Label(root, text="Enter your yards measurements for a free estimate!").grid(row=1, columnspan=3)
widthLabel= Label(root, text="Enter the width of your yard: ").grid(row=2, column=0)
lengthLabel= Label(root, text="Enter the length of your yard: ").grid(row=3, column=0)



def button_click():
    global img2
    top= Toplevel()
    top.title("Your Free Estimate")
    img2= ImageTk.PhotoImage(Image.open(r"C:\Users\smity\OneDrive\Pictures\landscape.png"))



e1 = Entry(root, width=30).grid(row=2, column=1)
e2 = Entry(root, width=30).grid(row=3, column=1)

button_next = Button(root, text="Next", padx=20, pady=10, command= button_click)
button_exit= Button(root, text= "Exit Program", command=root.quit)

button_next.grid(row=4, column=2, columnspan=1)
button_exit.grid(row=4, column=1, columnspan=1)

root.mainloop()