from tkinter import *
from tkinter import messagebox
import os.path
import pytube

root=Tk()
root.geometry("500x250")
root.resizable(False,False)
root.title("Code")
root.config(bg='#D3D3D3')

# download button
def download():
    try:
        ytlink=link1.get()
        if link2 == '':
            vidpt=os.path.expanduser('~\Desktop')
        else:
            vidpt=link2.get()
        youtubelink=pytube.YouTube(ytlink)
        video=youtubelink.streams.get_highest_resolution()
        video.download(vidpt,)
        Result="Loading is complete"
        messagebox.showinfo("Ready",Result)
    except:
        Result="Link does not work"
        messagebox.showerror("Error",Result)

def reset():
    link1.set("")

def Exit():
    root.destroy()


lb=Label(root,text="Download video from YouTube",font=('Arial,15,bold'),bg='#D3D3D3')
lb.pack(pady=15)

lb1=Label(root,text="Video link :",font=('Arial,15,bold'),bg='#D3D3D3')
lb1.place(x=10,y=60)

lb2=Label(root,text="Filepath :",font=('Arial,15,bold'),bg='#D3D3D3')
lb2.place(x=10,y=100)


link1=StringVar()
En1=Entry(root,textvariable=link1,font=('Arial,15,bold'))
En1.place(x=230,y=60)

link2=StringVar()
En2=Entry(root,textvariable=link2,font=('Arial,15,bold'))
En2.place(x=230,y=100)


btn1=Button(root,text="Download",font=('Arial,10,bold'),bd=4,command=download)
btn1.place(x=330,y=130)


btn2=Button(root,text="Clear",font=('Arial,10,bold'),bd=4,command=reset)
btn2.place(x=160,y=190)
btn3=Button(root,text=" Exit ",font=('Arial,10,bold'),bd=4,command=Exit)
btn3.place(x=250,y=190)


root.mainloop()
