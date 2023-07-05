import socket
from threading import Thread
from tkinter import *

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

'''def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))'''

"""receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()"""


class gui:
    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occured!")
                client.close()
                break


    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.recieve)


    def _init_(self):
        self.Window=Tk()
        self.Window.withdraw()
        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)
        self.pls=Label(self.login,text="Please Login to continue.",justify=CENTER,font=("Cambria",14),bd=2)
        self.pls.place(relheight=0.15,relx=0.2,rely=0.07)
        self.labelName=Label(self.login,text="Name:",font=("Cambria",14),bd=1)
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)
        self.entryName=Entry(self.login,font=("Cambria",14),bd=1)
        self.entryName.place(relheight=0.12,relwidth=0.4,relx=0.35,rely=0.2)
        self.entryName.focus()
        self.goButton=Button(self.login,text="Continue",command=lambda:self.goAheah(self.entryName.get()))
        self.goButton.place(relx=0.4,rely=0.55)
        self.Window.mainloop()


g=gui()

