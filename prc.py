from tkinter import *
import smtplib
import webbrowser
import d as dd


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='your Gmail')
        self.lbl2=Label(win, text='Gmail password')
        self.lbl3=Label(win, text='Reciever')
        self.lbl4=Label(win, text='subject')
        self.lbl5=Label(win, text='Text')
        self.lbl6=Label(win, text='** make sure you are signed-in to your gmail + and you inputs are corrects and fill all fields  ')
        self.lbl7=Label(win, text='** make sure to enable Acess to low-security apps , go to : https://myaccount.google.com/lesssecureapps ')
        self.lbl9=Label(win, text='** Exit from the App to stop the Attack ')


        self.lbl8=Label(win, text='© Developed By Ahmad HAFE ' , background='gray')







        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.t5=Entry()
        self.t6=Entry()




        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)

        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200 )

        self.lbl5.place(x=100, y=250)
        self.t5.place(x=200, y=250 , width=300 , height=300)







        self.b1=Button(win, text='send one time ', command=self.add)
        self.b4=Button(win, text='loop of Bots', command=self.addLoop)

        self.b2=Button(win, text='Sending Email processing ...',background='green')
        self.b3=Button(win, text='Faild to send ', background='red')
        self.b1.place(x=300, y=600)
        self.b4.place(x=300, y=650)



        self.lbl6.place(x=100, y=700)
        self.lbl7.place(x=100, y=720)
        self.lbl9.place(x=100, y=740)
        self.lbl8.place(x=0, y=780)

        link1 = Label(text=" go to : https://myaccount.google.com/lesssecureapps to enable it ", fg="blue", cursor="hand2")
        link1.place(x=400, y=750)


    def callback(self,url):
        webbrowser.open_new(url)



    def add(self):


        sender=str(self.t1.get())
        password=str(self.t2.get())
        From=str(self.t1.get())
        to=[str(self.t3.get())]
        sub=str(self.t4.get())
        txt=str(self.t5.get())
        result=dd.sendEmail(sender,password,From,to,sub,txt)
        if (result==True):
            self.b2.place(x=450, y=620)
        else:
            self.b3.place(x=450, y=620)


    def addLoop(self):

        while True:
            sender=str(self.t1.get())
            password=str(self.t2.get())
            From=str(self.t1.get())
            to=[str(self.t3.get())]
            sub=str(self.t4.get())
            txt=str(self.t5.get())
            result=dd.sendEmail(sender,password,From,to,sub,txt)
            if (result==True):
                self.b2.place(x=450, y=620)
            else:
                self.b3.place(x=450, y=620)
                break







        #self.t3.insert(END, str(result))
    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.b2.place(x=250, y=650)
        self.b2.place(x=250, y=650)

window=Tk()
mywin=MyWindow(window)
window.title('BOT Gmail Loop ')
window.geometry("800x800+10+10")
window.mainloop()
