from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("Canvas")
root.geometry("400x400")
root.config(bg="lightgreen")

label_1=Label(root,text="Canvas")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)
canvas_1=Canvas(root,width=200,height=200,highlightbackground="lightblue")
canvas_1.place(relx=0.5,rely=0.6,anchor=CENTER)
dropdown1=[100,200,300,400]
d1=ttk.Combobox(root,state="readonly",value=dropdown1,width=5,height=50)
d1.place(relx=0.1,rely=0.9,anchor=CENTER)
dropdown2=[100,200,300,300,400]
d2=ttk.Combobox(root,state="readonly",value=dropdown2,width=5,height=50)
d2.place(relx=0.3,rely=0.9,anchor=CENTER)
dropdown3=[100,200,300,400]
d3=ttk.Combobox(root,state="readonly",value=dropdown3,width=5,height=50)
d3.place(relx=0.5,rely=0.9,anchor=CENTER)
dropdown4=[100,200,300,400]
d4=ttk.Combobox(root,state="readonly",value=dropdown4,width=5,height=50)
d4.place(relx=0.7,rely=0.9,anchor=CENTER)
dropdown5=["red","green","blue","yellow","brown"]
d5=ttk.Combobox(root,state="readonly",value=dropdown5,width=5,height=50)
d5.place(relx=0.9,rely=0.9,anchor=CENTER)
root.mainloop()

