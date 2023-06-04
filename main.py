from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from abc import ABC, abstractmethod

calculations = []
infologin = 0
class useraccount(ABC):
    username = None
    email = None
    password = None
    status = None
    @abstractmethod
    def setpassword(self, password):
        pass
    @abstractmethod
    def getpassword(self):
        pass
    @abstractmethod
    def signin(self):
        pass

class newaccount(useraccount):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.data = {
            "username" : "",
            "email" : "",
            "password" : "",
            "status" : "pengguna baru"
            }
        self.status = self.data['status']
    def setpassword(self, password):
        self.password = password
    def getpassword(self):
        return self.password
    def signin(self):
        if self.username == self.data['username']:
            if self.email == self.data['email']:
                if self.password == self.data['password']:
                    messagebox.showerror('Sign up Gagal!', 'Pastikan Username, Email dan Password tidak kosong!')
        else:
            frame1.pack(fill=BOTH, expand=True)
            frame01.pack_forget()
            messagebox.showinfo('Sign up Berhasil!', 'Hello ' + self.username + '!')

class savedaccount(useraccount):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {
            "username" : "vyoharyadi",
            "email" : "vyoharyadi@gmail.com",
            "password" : "070803",
            "status" : "pengguna lama"
            }
        self.email = self.data['email']
        self.status = self.data['status']
    def setpassword(self, password):
        self.password = password
    def getpassword(self):
        return self.password
    def signin(self):
        if self.username == self.data['username']:
            if self.password == self.data['password']:
                frame1.pack(fill=BOTH, expand=True)
                frame02.pack_forget()
                messagebox.showinfo('Sign in Berhasil!', 'Hello ' + self.username + '!')
        else:
            messagebox.showerror('Sign in Gagal!', 'Username atau Password yang Anda masukkan salah!')

def sign_up():
    global infologin
    infologin = 1
    username = user_val.get()
    email = email_val.get()
    password = pass_val.get()
    signupinfo = newaccount(username, email, password)
    signupinfo.signin()

def log_in():
    frame02.pack(fill=BOTH, expand=True)
    frame01.pack_forget()
        
def sign_in():
    global infologin
    infologin = 2
    username = loguser_val.get()
    password = logpass_val.get()
    signininfo = savedaccount(username, password)
    signininfo.signin()

def menu_konversi():
    frame1.pack(fill=BOTH, expand=True)
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

def menu_riwayat():
    frame2.pack(fill=BOTH, expand=True)
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    global calculations
    textboxr.config(state=NORMAL)
    textboxr.delete(1.0, END)
    textboxr.config(state=DISABLED)
    for i in range(len(calculations)):
        textresult = str(calculations[i]) + '\n'
        textboxr.config(state=NORMAL)
        textboxr.insert(END, textresult)
        textboxr.config(state=DISABLED)
        
def menu_bantuan():
    frame3.pack(fill=BOTH, expand=True)
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    texthelp = "1. Bilangan Desimal\nSistem angka yang terdiri dari sepuluh digit dari angka 0 hingga 9.\n2. Bilangan Biner\nSistem angka dengan menggunakan dua lambang angka yakni 0 dan 1.\n3. Bilangan Oktal\nsistem bilangan berbasis delapan angka yakni 0,1,2,3,4,5,6,7.\n4. Bilangan Heksadesimal\nSistem angka yang memiliki 16 basis. Simbol-simbol itu mulai dari 0 sampai 9 kemudian dilanjutkan dengan A sampai F."
    textboxb.insert(END, texthelp)
    textboxb.config(state=DISABLED)

def menu_tentang():
    global infologin
    if infologin == 1:
        username = user_val.get()
        email = email_val.get()
        password = pass_val.get()
        tentang = newaccount(username, email, password)
        frame4.pack(fill=BOTH, expand=True)
        frame1.pack_forget()
        frame2.pack_forget()
        frame3.pack_forget()
        textabout = "Data Pengguna:\nUsername: " + tentang.username + "\nEmail : " + tentang.email + "\nPassword: " + tentang.getpassword() + "\nStatus: " + tentang.status
        textboxt.insert(END, textabout)
        textboxt.config(state=DISABLED)
    elif infologin == 2:
        username = loguser_val.get()
        password = logpass_val.get()
        tentang = savedaccount(username, password)
        frame4.pack(fill=BOTH, expand=True)
        frame1.pack_forget()
        frame2.pack_forget()
        frame3.pack_forget()
        textabout = "Data Pengguna:\nUsername: " + tentang.username + "\nEmail : " + tentang.email + "\nPassword: " + tentang.getpassword() + "\nStatus: " + tentang.status
        textboxt.insert(END, textabout)
        textboxt.config(state=DISABLED)

def menu_keluar():
    frame01.pack(fill=BOTH, expand=True)
    frame02.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    user_val.set('')
    email_val.set('')
    pass_val.set('')
    loguser_val.set('')
    logpass_val.set('')

def record_history(args):
    global calculations
    calculations.append(args)

def clearhistory():
    textboxr.config(state=NORMAL)
    textboxr.delete(1.0, END)
    textboxr.config(state=DISABLED)
    global calculations
    while len(calculations) > 0:
        calculations.pop()

def submit():
    opsi1 = cbb1_val.get()
    opsi2 = cbb2_val.get()
    n = input_val.get()
    if opsi1 == 'Desimal':
        n = int(n)
        if opsi2 == 'Desimal':
            r = n
        elif opsi2 == 'Biner':
            b = 0
            i = 1
            while n > 0:
                rem = n % 2
                b = b + (rem * i)
                i = i * 10
                n = n // 2
            r = b
        elif opsi2 == 'Oktal':
            i = 1
            o = 0
            while n > 0:
                o = o + (n % 8) * i
                n = n // 8
                i = int(i * 10)
            r = o
        elif opsi2 == 'Heksadesimal':
            conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            h = '' 
            while n > 0 :
                rem = n % 16
                h = conversion_table[rem] + h
                n = n // 16
            r = h

    elif opsi1 == 'Biner':
        n = int(n)
        if opsi2 == 'Desimal':
            d = 0
            i = 0
            while n > 0:
                rem = n % 10
                d = d + (rem * pow(2, i))
                n = n // 10
                i += 1
            r = d
        elif opsi2 == 'Biner':
            r = n
        elif opsi2 == 'Oktal':
            d = 0
            i = c = 1
            o = ""
            while n > 0:
                rem = n % 10
                d = d + (rem * i)
                if c%3 == 0:
                    o = o + str(d)
                    i = c = 1
                    d = 0
                else:
                    i = i*2
                    c = c+1
                n = int(n / 10)
            if c != 1:
                o = o + str(d)
            r = o[::-1]
        elif opsi2 == 'Heksadesimal':
            d = int(str(n), 2)
            r = hex(d).replace("0x", "")

    elif opsi1 == 'Oktal':
        if opsi2 == 'Desimal':
            r = int(n,8)
        elif opsi2 == 'Biner':
            n = int(n)
            i = 0
            c = 0
            while n > 0:
                d = n % 10
                c += d * pow(8, i)
                n //= 10
                i += 1
            b = 0
            rem = 0
            i = 1
            while c > 0:
                rem = c % 2
                c //= 2
                b += rem * i
                i *= 10
            r = b
        elif opsi2 == 'Oktal':
            r = n
        elif opsi2 == 'Heksadesimal':
            d = int(str(n), 8)
            r = hex(d).replace("0x", "")

    elif opsi1 == 'Heksadesimal':
        if opsi2 == 'Desimal':
            r = int(n,16)
        elif opsi2 == 'Biner':
            conversion_table = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
            b = ''
            for i in n:
                b += conversion_table[i]
            r = b
        elif opsi2 == 'Oktal':
            conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            c = 0
            for i in n:
                c = c * 16 + conversion_table[i]
            o = ''
            while c > 0:
                d = c % 8
                o = str(d) + o
                c //= 8
            r = o 
        elif opsi2 == 'Heksadesimal':
            r = n
    record_history(r)
    lbl_output.config(text = r)

def clearform():
    cbbval = "Pilih di sini"
    cbb1.set(cbbval)
    cbb2.set(cbbval)
    input_val.set('')
    lbl_output.config(text = '')

#GUI
window = Tk()
window.title("Konversi Basis Bilangan")
window.resizable(False, False)
width = 370
height = 485
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

frame01 = Frame(window, relief=GROOVE, borderwidth=5, bg="#00539C")
frame01.pack(fill=BOTH, expand=True)
frame02 = Frame(window, relief=GROOVE, borderwidth=5, bg="#00539C")
frame1 = Frame(window, relief=GROOVE, borderwidth=5, bg="#00539C")
frame2 = Frame(window, relief=GROOVE, borderwidth=5, bg="#00539C")
frame3 = Frame(window, relief=GROOVE, borderwidth=5, bg="#00539C")
frame4 = Frame(window, relief=GROOVE, borderwidth=5, bg="#00539C")

barmenu = Menu(window)
barmenu.add_cascade(label='Konversi', command= menu_konversi)
barmenu.add_cascade(label='Riwayat', command= menu_riwayat)
barmenu.add_cascade(label='Bantuan', command=menu_bantuan)
barmenu.add_cascade(label='Tentang', command= menu_tentang)
barmenu.add_cascade(label='Keluar', command= menu_keluar)
window.config(menu=barmenu)

#Sign up
canvas = Canvas(frame01, bg="#00539C",height=465, width=350).place(x = 4, y = 4)
lbl_title1 = Label(frame01, bg="#00539C", fg="#FFD662", font=("Courier",28), text="KONVERTER").place(x = 45, y = 20)
lbl_title2 = Label(frame01, bg="#00539C", fg="#FFD662", font=("Courier",28), text="BASIS").place(x = 135, y = 60)
lbl_title3 = Label(frame01, bg="#00539C", fg="#FFD662", font=("Courier",28), text="BILANGAN").place(x = 135, y = 100)

canvas = Canvas(frame01, bg="#FFD662",height=180, width=330).place(x = 14, y = 150)
lbl_signup = Label(frame01, bg="#FFD662", fg="#00539C", font=("Courier",11), text="Silahkan daftar untuk memulai!").place(x = 46, y = 158)
lbl_user = Label(frame01, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Masukkan Username:").place(x = 47, y = 178)
user_val = StringVar()
entry_user = Entry(frame01, relief=SOLID, width=43, bd=2, textvariable=user_val).place(x = 50, y = 200)

lbl_email = Label(frame01, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Masukkan Email:").place(x = 47, y = 228)
email_val = StringVar()
entry_email = Entry(frame01, relief=SOLID, width=43, bd=2, textvariable=email_val).place(x = 50, y = 250)

lbl_pass = Label(frame01, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Masukkan Password:").place(x = 47, y = 278)
pass_val = StringVar()
entry_pass = Entry(frame01, relief=SOLID, width=43, bd=2, textvariable=pass_val, show='*').place(x = 50, y = 300)

btn_signup = Button(frame01, relief=FLAT, bg="#FFD662", fg="#00539C", activebackground="#FCF6F5", height=1, width=32, text="Sign up", justify=CENTER, font=("Courier",11), command=sign_up).place(x = 33, y = 360)

lbl_login = Label(frame01, bg="#00539C", fg="#FCF6F5", font=("Courier",11), text="Sudah memiliki akun?").place(x = 30, y = 400)
btn_login = Button(frame01, relief=FLAT, bg="#FFD662", fg="#00539C", activebackground="#FCF6F5", height=1, width=32, text="Log in", justify=CENTER, font=("Courier",11), command=log_in).place(x = 33, y = 420)

#Sign in
canvas = Canvas(frame02, bg="#00539C",height=465, width=350).place(x = 4, y = 4)
lbl_title1 = Label(frame02, bg="#00539C", fg="#FFD662", font=("Courier",28), text="KONVERTER").place(x = 45, y = 20)
lbl_title2 = Label(frame02, bg="#00539C", fg="#FFD662", font=("Courier",28), text="BASIS").place(x = 135, y = 60)
lbl_title3 = Label(frame02, bg="#00539C", fg="#FFD662", font=("Courier",28), text="BILANGAN").place(x = 135, y = 100)

lbl_loguser = Label(frame02, bg="#00539C", fg="#FCF6F5", font=("Courier",13), text="Masukkan Username:").place(x = 47, y = 178)
loguser_val = StringVar()
entry_loguser = Entry(frame02, relief=SOLID, width=43, bd=2, textvariable=loguser_val).place(x = 50, y = 200)

lbl_logpass = Label(frame02, bg="#00539C", fg="#FCF6F5", font=("Courier",13), text="Masukkan Password:").place(x = 47, y = 228)
logpass_val = StringVar()
entry_logpass = Entry(frame02, relief=SOLID, width=43, bd=2, textvariable=logpass_val, show='*').place(x = 50, y = 250)

btn_signin = Button(frame02, relief=FLAT, bg="#FFD662", fg="#00539C", activebackground="#FCF6F5", height=1, width=32, text="Sign in", justify=CENTER, font=("Courier",11), command=sign_in).place(x = 33, y = 360)

#Konversi
canvas = Canvas(frame1, bg="#FFD662",height=335, width=338).place(x = 10, y = 10)

lbl_cbb1 = Label(frame1, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Bentuk Awal:").place(x = 47, y = 48)
cbb1_val = StringVar(value='Pilih di sini')
cbb1 = ttk.Combobox(frame1, width=40, textvariable=cbb1_val) 
cbb1['values'] = ('Desimal','Biner','Oktal','Heksadesimal')
cbb1['state'] = 'readonly'
cbb1.place(x = 51, y = 70)

lbl_input = Label(frame1, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Masukkan Angka Awal:").place(x = 47, y = 118)
input_val = StringVar()
entry_input = Entry(frame1, relief=GROOVE, width=43, bd=2, textvariable=input_val).place(x = 50, y = 140)

lbl_cbb2 = Label(frame1, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Ubah Ke Dalam Bentuk:").place(x = 47, y = 188)
cbb2_val = StringVar(value='Pilih di sini')
cbb2 = ttk.Combobox(frame1, width=40, textvariable=cbb2_val) 
cbb2['values'] = ('Desimal','Biner','Oktal','Heksadesimal')
cbb2['state'] = 'readonly'
cbb2.place(x = 51, y = 210)

lbl_result = Label(frame1, bg="#FFD662", fg="#00539C", font=("Courier",13), text="Hasil Konversi:").place(x = 47, y = 258)

lbl_output = Label(frame1, text = "", bg = "#FFD662", fg="#00539C", font=("Courier",13))
lbl_output.place(x = 47, y = 280)

btn_submit = Button(frame1, relief=FLAT, bg="#FFD662", fg="#00539C", activebackground="#FCF6F5", height=2, width=40, text="Submit", justify=CENTER, command=submit).place(x = 36, y = 368)

btn_clear = Button(frame1, relief=FLAT, bg="#FFD662", fg="#00539C", activebackground="#E94B3C", height=2, width=40, text="Clear", justify=CENTER, command=clearform).place(x = 36, y = 418)

#Riwayat
sb = Scrollbar(frame2)
sb.pack(side=RIGHT, fill=BOTH)

textboxr = Text(frame2, relief=GROOVE, bg="#FFD662", fg="#00539C", bd=5, height = 17, width = 28, font=("Courier"), wrap='word')
textboxr.pack()

textboxr.config(yscrollcommand=sb.set)
sb.config(command=textboxr.yview)

btn_clear = Button(frame2, relief=FLAT, bg="#FFD662", fg="#00539C", activebackground="#E94B3C", height=2, width=40, text="Clear", justify=CENTER, command=clearhistory).place(x = 27, y = 411)

#Bantuan
textboxb = Text(frame3, relief=GROOVE, bg="#FFD662", fg="#00539C", bd=5, height = 21, width = 30, font=("Courier"), wrap='word')
textboxb.pack()

#Tentang
textboxt = Text(frame4, relief=GROOVE, bg="#FFD662", fg="#00539C", bd=5, height = 21, width = 30, font=("Courier"), wrap='word')
textboxt.pack()

window.mainloop()