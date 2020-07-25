from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter.font import Font
a,count=[],[1]
for i in range(10):
    a.append(None)
def insert(word):
    if word==1:
        o1.insert(INSERT,a[word])
    if word==2:
        o2.insert(INSERT,a[word])
    if word==3:
        o3.insert(INSERT,a[word])
    if word==4:
        o4.insert(INSERT,a[word])
    if word==5:
        o5.insert(INSERT,a[word])
    if word==6:
        o6.insert(INSERT,a[word])
    if word==7:
        o7.insert(INSERT,a[word])
    if word==8:
        o8.insert(INSERT,a[word])
    if word==9:
        o9.insert(INSERT,a[word])
def lookup():
    s=0
    if count[0]%2!=0:
        word=entry.get()
        word=int(word)
        a[word]=' O'
        count[0]=count[0]+1
        insert(word)
    if a[1]==a[2]==a[3]:
        if a[1]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[1]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[4]==a[5]==a[6]:
        if a[4]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[4]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[7]==a[8]==a[9]:
        if a[7]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[7]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[1]==a[4]==a[7]:
        if a[1]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[1]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[5]==a[2]==a[8]:
        if a[2]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[2]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[6]==a[9]==a[3]:
        if a[3]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[3]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[1]==a[5]==a[9]:
        if a[1]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[1]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if a[5]==a[7]==a[3]:
        if a[3]==' O':
            messagebox.showinfo("Game Over","you wins!")
        elif a[3]==' X':
            messagebox.showinfo("Game Over","you loss!")
    if count[0]%2==0:
        word=random.randint(1,9)
        while a[word]!=None:
            word=random.randint(1,9)
        a[word]=' X'
        insert(word)
        count[0]=count[0]+1

root= Tk()
root.title("tictoc")
mainframe=Frame(root)

my_font = Font(size=36,weight='bold')
text_font=Font(size=56,weight='bold')
one=Label(root,text='tictoc',font=my_font,bg='yellow')
one.pack(fill=X)

mainframe.pack(side=TOP)

topframe= LabelFrame(root,text='Input',padx=5,pady=5,bg='yellow')

entry=Entry(topframe,width=36)
entry.pack(side=LEFT)
button=Button(topframe,text="Enter",command=lookup)
button.pack()

topframe.pack(side=TOP)

bottomframe=Frame(root,bg='skyblue')

o1=Text(bottomframe,width=2,height=1,font=text_font)
o1.grid(row=0,column=0)
o2=Text(bottomframe,width=2,height=1,font=text_font)
o2.grid(row=0,column=1)
o3=Text(bottomframe,width=2,height=1,font=text_font)
o3.grid(row=0,column=2)
o4=Text(bottomframe,width=2,height=1,font=text_font)
o4.grid(row=1,column=0)
o5=Text(bottomframe,width=2,height=1,font=text_font)
o5.grid(row=1,column=1)
o6=Text(bottomframe,width=2,height=1,font=text_font)
o6.grid(row=1,column=2)
o7=Text(bottomframe,width=2,height=1,font=text_font)
o7.grid(row=2,column=0)
o8=Text(bottomframe,width=2,height=1,font=text_font)
o8.grid(row=2,column=1)
o9=Text(bottomframe,width=2,height=1,font=text_font)
o9.grid(row=2,column=2)



bottomframe.pack()
root.mainloop()
