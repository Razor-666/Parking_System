from os import times
import time
import sys
from curses import window
from multiprocessing import active_children
from tkinter import *
import random
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox
import ast
# from barcode import EAN13

class Jam:
    def __init__(self, parent):
        self.parent = parent
        self.komponen()
        self.update()

    def komponen(self):
        self.teksJam = StringVar()
        
        layarJam = Frame(self.parent, bd=10)
        layarJam.pack()

        self.jam = Label(layarJam, textvariable=self.teksJam, font=('Helvetica', 25, 'bold'),bg = "light blue",fg="red")
        self.jam.pack()

    def update(self):
        datJam = time.strftime("%H:%M:%S", time.localtime())
        self.teksJam.set(datJam)
        self.timer = self.parent.after(1000, self.update)

root =Tk()
root.title(string="")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

root.bind('<Escape>',lambda e: root.quit())



def signin():
    username = user.get()
    password = code.get()

    file=open('/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Parking System")
        screen.geometry('925x500+322+200')
        screen.configure(bg="#fff")
        screen.resizable(False, False)
        waktu_masuk = time.strftime("%H:%M", time.localtime())
        noticket_random=random.randint(100000000000, 999999999999)

        def checkin():
            No_plat = Noplat.get()
            jenis_kendaraan = Jeniskendaraan.get()
            Jam_masuk = Jammasuk.get()
            file=open('/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/checkin.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)
            dicts={No_plat:Jam_masuk}
            r.update(dicts)
            file.truncate(0)
            file.close()

            file=open('/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/checkin.txt', 'w')
            w=file.write(str(r))

            ######## TIKET CHECK IN #################
            layar = Toplevel(root)
            layar.title("Check in")
            layar.geometry('445x520')
            layar.configure(bg='#fff')
            bagian_atas=Label(layar, text= 'PARKING TICKET CHECK IN', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 22, 'bold'))
            bagian_atas.place(x=0, y=5)

            Label(layar, text="TRY TICKETING MALL SIMPLE",bg='white',fg='black',font=('Microsoft YaHei UI Light',18,'bold')).place(x=15,y=100)
            
            noticket = Label(layar, text='Ticket No :', fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold'))
            noticket.place(x=15,y=150)
            no_ticket = Label(layar, text=noticket_random, fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold'))
            no_ticket.place(x=165,y=150)
            waktu = Label(layar, text='Tanggal', fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold'))
            waktu.place(x=15,y=200)

            Label(layar, text=':', fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold')).place(x=148,y=200)

            tmpl_waktu = Label(layar, text=time.strftime("%C %b %Y", time.localtime()), fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold'))
            tmpl_waktu.place(x=165,y=200)

            timew = Label(layar, text='Waktu', fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold'))
            timew.place(x=15,y=250)

            Label(layar, text=':', fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold')).place(x=148,y=250)
            tmpl_timew = Label(layar, text=waktu_masuk, fg='black', bg='white', font=('Microsoft YaHei UI Light',18,'bold'))
            tmpl_timew.place(x=165,y=250)

            Label(layar, text='JANGAN MENINGGALKAN TIKET &', fg='black', bg='white', font=('Microsoft YaHei UI Light',16,'bold')).place(x=16,y=410)
            Label(layar, text='BARANG BERHARGA', fg='black', bg='white', font=('Microsoft YaHei UI Light',16,'bold')).place(x=75,y=440)
            Label(layar, text='DI DALAM KENDARAAN ANDA', fg='black', bg='white', font=('Microsoft YaHei UI Light',16,'bold')).place(x=26,y=470)

            layar.mainloop()
            ######## TIKET CHECK IN #################

            ######## TIKET CHECK OUT #################
        def checkout():
            tampil = Toplevel(root)
            tampil.title("Check out")
            tampil.geometry('445x520')
            tampil.configure(bg='#fff')
            nopol = Noplat.get()
            Label(tampil, text='PARKING TICKET CHECK OUT', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 20, 'bold')).place(x=3, y=5)
            keluar_nopol = Label(tampil, text='No Kendaraan', fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold'))
            keluar_nopol.place(x=3,y=60)
            Label(tampil, text=':', fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold')).place(x=218, y=60)
            Label(tampil, text=nopol, fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold')).place(x=230, y=60)

            Label(tampil, text='Masuk', fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold')).place(x=3, y=110)
            Label(tampil, text=':', fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold')).place(x=218, y=110)
            masuk_wkt = Label(tampil, text=waktu_masuk, fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold'))
            masuk_wkt.place(x=230, y=110)

            time_keluar = time.strftime("%H:%M", time.localtime())
            Label(tampil, text='Keluar', fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold')).place(x=3, y=160)
            Label(tampil, text=':', fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold')).place(x=218, y=160)
            keluar_wkt = Label(tampil, text=time_keluar, fg='black', bg='white', font=('Microsoft YaHei UI Light', 17, 'bold'))
            keluar_wkt.place(x=230, y=160)


            #################### SELISIH WAKTU + HARGA #####################
            x = datetime.datetime.strptime(waktu_masuk, "%H:%M")
            y = datetime.datetime.strptime(time_keluar, "%H:%M")
            harga_sejam = 3000
            selisih = y-x
            last_selisih = selisih
            if selisih <= last_selisih:
                harga = harga_sejam

            Label(tampil, text='Rp.', fg='black', bg='white', font=('Microsoft YaHei UI Light', 19, 'bold')).place(x=120, y=210)
            Label(tampil, text=harga, fg='black', bg='white', font=('Microsoft YaHei UI Light', 19, 'bold')).place(x=180, y=210)

            Label(tampil, text='Hati Hati di Jalan', fg='black', bg='white', font=('Microsoft YaHei UI Light', 19, 'bold')).place(x=75, y=260)
            Label(tampil, text='Terima Kasih', fg='black', bg='white', font=('Microsoft YaHei UI Light', 19, 'bold')).place(x=100, y=300)

            tampil.mainloop()
            ######## TIKET CHECK OUT #################

        ##### INTI HALAMAN DUA CHECK IN ##########
        ####################### SIGN UP ##################################
        footer = Frame(screen, bg='blue', height=100)
        footer.pack(side=TOP, fill=X)
        heading=Label(screen, text= 'Parking System', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=350, y=5)

        ############################No Kendaraan
        no_kendaraan=Label(screen, text='No Kendaraan', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',14))
        no_kendaraan.place(x=20, y=120)
        def on_enter(e):
            Noplat.delete(0, 'end')

        def on_leave(e):
            name = Noplat.get()
            if name=='':
                Noplat.insert(0,'No plat')

        Noplat = Entry(screen, width=25, fg='black', border = 3 ,bg="white",font=('Microsoft YaHei UI Light', 11))
        Noplat.place(x=20, y=150)
        Noplat.insert(0,'No plat')
        Noplat.bind('<FocusIn>', on_enter)
        Noplat.bind('<FocusOut>', on_leave)

        ############################Jenis Kendaraan
        jenis_kendaraan=Label(screen, text='Jenis Kendaraan', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',14))
        jenis_kendaraan.place(x=20, y=200)
        def on_enter(e):
            Jeniskendaraan.delete(0, 'end')

        def on_leave(e):
            name = Jeniskendaraan.get()
            if name=='':
                Jeniskendaraan.insert(0,'Jenis kendaraan')

        Jeniskendaraan = Entry(screen, width=25, fg='black', border = 3 ,bg="white",font=('Microsoft YaHei UI Light', 11))
        Jeniskendaraan.place(x=20, y=230)
        Jeniskendaraan.insert(0,'Jenis kendaraan')
        Jeniskendaraan.bind('<FocusIn>', on_enter)
        Jeniskendaraan.bind('<FocusOut>', on_leave)

        ############################Jam Masuk
        Label(screen, text='Jam Masuk', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',14)).place(x=20,y=280)

        def on_enter(e):
            Jammasuk.delete(0, 'end')

        def on_leave(e):
            name = Jammasuk.get()
            if name=='':
                Jammasuk.insert(0,waktu_masuk)
                # Jammasuk.insert(0,time.strftime("%H:%M", time.localtime()))

        Jammasuk = Entry(screen, width=25, fg='black', border = 3 ,bg="white",font=('Microsoft YaHei UI Light', 11))
        Jammasuk.place(x=20, y=310)
        Jammasuk.insert(3, 'Jam Masuk')
        Jammasuk.bind('<FocusIn>', on_enter)
        Jammasuk.bind('<FocusOut>', on_leave)

        check_in = Button(screen, width=39, pady=7, text='Check in', bg= '#57a1f8', fg='white', border=0, command=checkin)
        check_in.place(x=550,y=350)

        check_out = Button(screen, width=39, pady=7, text='Check out', bg= '#57a1f8', fg='white', border=0, command=checkout)
        check_out.place(x=550,y=400)

        ################################### HAL SIGN IN ##################################
        Jam(screen) #Tampilan Jam
        screen.mainloop()
    
    else:
        messagebox.showerror('Invalid', "invalid username or password")

############################@@@@@@@@@@@@@@@@@@@@@@@
def signup_command():
    window=Toplevel(root)
    window.title(string="")
    window.geometry('925x500+300+200')
    window.configure(bg="#fff")
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password:
            try:
                file = open('/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/datasheet.txt', 'w')
                w=file.write(str(r))

                messagebox.showinfo('Signup', 'Sucessfully sign up')

            except:
                file=open('/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/datasheet.txt', 'w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
    
        else:
            messagebox.showerror('Invalid', "Both Password should match")
        
    def sign():
        window.destroy()

    ####################### SIGN UP ##################################
    img = PhotoImage(file='/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/signup.png')
    Label(window, image=img, bg='white').place(x=150,y=150)

    frame = Frame(window, width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame, text= 'Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ############################-----------------------------
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name=='':
            user.insert(0,'Username')

    user = Entry(frame, width=25, fg='black', border = 0 ,bg="white",font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width =295, height=2, bg='black').place(x=25, y=107)

    ############################-----------------------------
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name=='':
            code.insert(0,'Password')

    code = Entry(frame, width=25, fg='black', border = 0 ,bg="white",font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)


    Frame(frame, width =295, height=2, bg='black').place(x=25, y=177)

    ############################-----------------------------
    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        name = confirm_code.get()
        if name=='':
            confirm_code.insert(0,'Confirm Password')

    confirm_code = Entry(frame, width=25, fg='black', border = 0 ,bg="white",font=('Microsoft YaHei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0,'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)

    Frame(frame, width =295, height=2, bg='black').place(x=25, y=247)

    ###########################

    Button(frame, width=39, pady=7, text='Sign up', bg= '#57a1f8', fg='white', border=0, command=signup).place(x=25,y=250)

    label = Label(frame, text="I have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
    label.place(x=90,y=290)

    sign_in = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    sign_in.place(x=200,y=290)

    window.mainloop()

#################@@@@@@@@@@@@@@@@@@@@@@


####################### SIGN IN ##################################
img = PhotoImage(file='/home/fire-x/Documents/Folder_ParkingSystem/Main Login Page/login.png')
Label(root, image=img, bg='white').place(x=50,y=50)

frame = Frame(root, width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame, text= 'Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

############################-----------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border = 0 ,bg="white",font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width =295, height=2, bg='black').place(x=25, y=107)

############################-----------------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame, width=25, fg='black', border = 0 ,bg="white",font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width =295, height=2, bg='black').place(x=25, y=177)

###########################

sign_in = Button(frame, width=39, pady=7, text='Sign in', bg= '#57a1f8', fg='white', border=0, command=signin)
sign_in.place(x=25,y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215,y=270)


root.mainloop()