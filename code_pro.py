from tkinter import *
from PIL import ImageTk, Image


w1 = Tk()
w1.configure(background="#000000")
w1.title("Powered By KEATS")
w1.geometry("550x350+530+220")
w1.resizable(0, 0) 


#Define the function to change the value in label widget
def choose_yes(label1,label2):
   label1.configure(text= "THANKK YOUUUU SOOOOO MUCHH!\nSEND ME HI ON WHATSAPP ^_^", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
   label2.configure(state=DISABLED)

w1.cnt = 0

#Define the function to change the value in label widget
def choose_no(label1):
	if(w1.cnt == 0):
		label1.configure(text= "PLEASE", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 1):
		label1.configure(text= "PLEASES", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 2):
		label1.configure(text= "PLEASESS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 3):
		label1.configure(text= "PLEASESSS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 4):
		label1.configure(text= "PLEASESSSS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 5):
		label1.configure(text= "PLEASESSSSS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 6):
		label1.configure(text= "PLEASESSSSSS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	elif(w1.cnt == 7):
		label1.configure(text= "PLEASESSSSSSS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	else:
		label1.configure(text= "PLEASESSSSSSSS", height=3,width=35,fg="#FF0000",font='Helvetica 10 bold')
	w1.cnt += 1

propose_lable = Label(w1,text="WILL  YOU  BE  MY  VALENTINE ? PLEASE",height=3,width=35,fg="#FF0000",bg="#FFFFFF",font='Helvetica 10 bold')
propose_lable.pack()
propose_lable.place(x=130,y=25)


frame = Frame(w1, width=110, height=110)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("C:\\Users\\dhamu\\OneDrive\\Desktop\\new_please1.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()



badLuck_btn = Button(w1,text="NO",height=1,width=10,bg="#FFFFFF",fg="#0000ff",command = lambda:choose_no(propose_lable))
badLuck_btn.pack()
badLuck_btn.place(x=175,y=265)

Lucky_btn = Button(w1,text="YES",height=1,width=10,bg="#FFFFFF",fg="#0000ff",command=lambda:choose_yes(propose_lable,badLuck_btn))
Lucky_btn.pack()
Lucky_btn.place(x=285,y=265)



w1.mainloop()