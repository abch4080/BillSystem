from tkinter import *
from PIL import ImageTk,Image

secondFrame = Tk()
secondFrame.geometry('725x400')
secondFrame.title('Gaurav S')
secondFrame.iconbitmap('login.ico')
# secondFrame.resizable('false','false')

# Frame and main data
frame = Frame(secondFrame,width=725,height=400,bg='white')
frame.place(x=0,y=0)

userName = Label(secondFrame,text='Gaurav Sorate',fg='#57a1f8',bg='white',font=(('Microsoft Yahei UI Light',19,'bold')))
userName.place(x=0,y=12)

#frame for list box
frame1 = Frame(secondFrame,width=500,height=200,bg='green')
frame1.place(x=35,y=70)


# costomer list
listBox = Listbox(frame1,font=('arial',11),width=40,height=16,bg="#32405b",fg='white',cursor='hand2',selectbackground="#5a95ff")
listBox.pack(side=LEFT,fill=BOTH,padx=1,ipadx=0,ipady=0)

scrollerBar = Scrollbar(frame1)
scrollerBar.pack(side=LEFT,fill=BOTH)

listBox.config(yscrollcommand=scrollerBar.set)
scrollerBar.config(command=listBox.yview())
# Entery for new consumer
task = StringVar()
task_entery = Entry(secondFrame,width=18,font='arial 20',bd=0,bg='gray').place(x=40,y=364)

#button for creating the new consumer
Button(secondFrame,text='Create New',pady=2,border=0.5,fg='black',bg='white',font=(('Microsoft Yahei UI Light',10,'bold'))).place(x=320,y=365)

secondFrame.mainloop()