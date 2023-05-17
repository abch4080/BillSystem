from tkinter import *
from PIL import ImageTk,Image #  for frame image

# the programming of tkinter is written by Jhon Grayson.

root = Tk()

root.title('Jhon Grayson')  # for title of the frame.

root.iconbitmap('login.ico')    # icon file

root.minsize(300,200)  # ya peksha lahan nahi houshakat
root.geometry('725x400')# by default size he rahanar
root.resizable('false','false')

img = Image.open('2103417.jpg')
resize_img = img.resize((400,400))

img_1 = ImageTk.PhotoImage(resize_img) #file given to frame
img_image = Label(root,image=img_1,border=0,bg='white').place(x=0,y=0) # setting the image to frame

# img_image.pack() # geometory maneger.
# size is big so we need to resize the image.

# Creating the new frame for login form.
frame = Frame(root,width=350,height=400,bg='#fff')
frame.place(x=400,y=0)

heading = Label(frame,text='Log in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',19,'bold'))
heading.place(x=125,y=20)

# Fuction for focues 1
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

# Input Boxses
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=60,y=70)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

# frame Css
Frame(frame,width=230,height=1,bg='black').place(x=40,y=100)


# Fuction for focues 2
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

# Input Boxses
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=60,y=120)
code.insert(0,'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

# frame Css
Frame(frame,width=230,height=1,bg='black').place(x=40,y=150)

# sing in button
Button(frame,width=39,pady=5,text='Sign in',bg='#57a1f8',fg='black',border=0).place(x=20,y=204)
label =Label(frame,text="Don't have account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',11)).place(x=50,y=250)

sing_up = Button(frame,width=7,text='sing-up',border=0,bg='white',cursor='hand2',fg='blue',font=('Microsoft Yahei UI Light',12)).place(x=190,y=247)

root.mainloop()