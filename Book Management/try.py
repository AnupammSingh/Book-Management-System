from tkinter import *
from tkinter import messagebox
import try2
from tkinter import ttk
window = Tk(className = ' Welcome to Login Page')
window.geometry('900x900+100+100')
window.configure(bg = 'Skyblue')
fram = Frame(window, height = 500, width = 600, bd = 2, relief = SOLID, bg = 'Blue')
fram.grid(row = 0, column = 0, padx = 85, pady = 50)
fram.grid_propagate(0)
lbl = Label(fram, text = 'Admin Login', font = ('bold', 15), fg = 'Red')
lbl.grid(row = 0, column = 0, padx = 215, pady = 52)
framt = Frame(window, height = 250, width = 430, bd = 2, relief = SOLID, bg = 'Blue')
framt.grid(row = 0, column = 0)
framt.grid_propagate(0)

txtid_value = StringVar()
txtpass_value = StringVar()

lbl_id = Label(framt, text = 'User ID', font = ('bold', 10), fg = 'Red')
lbl_id.grid(row = 0, column = 0, padx = 10, pady = 20)
lbl_pass = Label(framt, text = 'Password', font = ('bold', 10), fg = 'Red')
lbl_pass.grid(row = 1, column = 0, padx = 10, pady = 20)
txt_id = Entry(framt, font = ('calibri', 10), fg = 'Green', textvariable = txtid_value)
txt_id.grid(row = 0, column = 1, padx = 80)
txt_pass = Entry(framt, font = ('calibri', 10), fg = 'Green', show = '*', textvariable = txtpass_value)
txt_pass.grid(row = 1, column = 1, padx = 80)
def login(event = None):
    result = try2.show_user(txtid_value.get(), txtpass_value.get())
    if not result:
        messagebox.showinfo('Login Error!', 'You are not a valid user')
        txt_id.delete(0, END)
        txt_pass.delete(0, END)
    else:
        messagebox.showinfo('Login Successful!', 'Logged in Successfully')
        txt_id.delete(0, END)
        txt_pass.delete(0, END)
        user_details()

btn = Button(framt, text = 'Login', command = login, cursor = 'hand2')
btn.grid(row = 2, column = 1, pady = 10, columnspan = 2)
btn.bind('<Return>', login)

def user_details():
    nwin = Toplevel(window)
    nwin.title('Student Registration')
    '''nwin.geometry('900x900+100+100')'''
    nwin.state('zoomed')
    nwin.configure(bg = 'Salmon')

    def book_regis():
        nwins = Toplevel(window)
        nwins.title('Book Registration')
        '''nwins.geometry('900x900+100+100')'''
        nwins.state('zoomed')
        nwins.configure(bg='Salmon')

        frmi = Frame(nwins, height=60, width=500, bd=2, relief=SOLID, bg='Purple')
        frmi.grid(row=0, column=0, padx=150, pady=10)
        frmi.grid_propagate(0)
        lbl = Label(frmi, text='Book Registration Form', font=('bold', 15), fg='Green')
        lbl.grid(row=0, column=0, padx=120, pady=10)
        framsd = Frame(nwins, height=270, width=540, bd=2, relief=SOLID, bg='salmon')
        framsd.grid(row=1, column=0, padx=10, pady=50)
        framsd.grid_propagate(0)
        txtidss_value = StringVar()
        txtnames_value = StringVar()
        txtbooca_value = StringVar()
        txtauth_value = StringVar()
        txtbookisbn_value = StringVar()
        txtprice_value = StringVar()

        lbl_idss = Label(framsd, text='Book Id', font=('bold', 10), fg='Purple')
        lbl_idss.grid(row=0, column=0, padx=5, pady=10)
        txt_idss = Entry(framsd, font=('calibri', 10), fg='Green', textvariable=txtidss_value)
        txt_idss.grid(row=0, column=1, padx=10, pady=15)

        lbl_names = Label(framsd, text='Book Name', font=('bold', 10), fg='Purple')
        lbl_names.grid(row=0, column=2, padx=5, pady=10)
        txt_names = Entry(framsd, font=('calibri', 10), fg='Green', textvariable=txtnames_value)
        txt_names.grid(row=0, column=3, padx=5, pady=10)

        lbl_booca = Label(framsd, text='Book Category', font=('bold', 10), fg='Purple')
        lbl_booca.grid(row=1, column=0, padx=5, pady=10)
        txt_booca = Entry(framsd, font=('calibri', 10), fg='Green', textvariable=txtbooca_value)
        txt_booca=ttk.Combobox(framsd,width=10,font=('bold',10),textvariable=txtbooca_value)
        txt_booca['values']=('Select','Language','Management', 'Biography', 'Fiction', 'Novel')
        txt_booca.current(0)
        txt_booca.grid(row=1, column=1, padx=5, pady=10)

        lbl_auth = Label(framsd, text='Author', font=('bold', 10), fg='Purple')
        lbl_auth.grid(row=1, column=2, padx=5, pady=10)
        txt_auth = Entry(framsd, font=('calibri', 10), fg='Green', textvariable=txtauth_value)
        txt_auth.grid(row=1, column=3, padx=5, pady=10)

        lbl_bookisbn = Label(framsd, text='Book ISBN', font=('bold', 10), fg='Purple')
        lbl_bookisbn.grid(row=2, column=0, padx=5, pady=10)
        txt_bookisbn = Entry(framsd, font=('calibri', 10), fg='Green', textvariable=txtbookisbn_value)
        txt_bookisbn.grid(row=2, column=1, padx=5, pady=10)

        lbl_price = Label(framsd, text='Price', font=('bold', 10), fg='Purple')
        lbl_price.grid(row=2, column=2, padx=5, pady=10)
        txt_price = Entry(framsd, font=('calibri', 10), fg='Green', textvariable=txtprice_value)
        txt_price.grid(row=2, column=3, padx=5, pady=10)

        frmend = Frame(nwins, height=200, width=700, bd=2, relief=SOLID, bg='Darkslateblue')
        frmend.grid_propagate(0)
        frmend.grid(row=2, column=0, pady=30, padx=20)

        def clearbookData():
            txt_idss.delete(0, END)
            txt_names.delete(0, END)
            txt_booca.delete(0, END)
            txt_auth.delete(0, END)
            txt_bookisbn.delete(0, END)
            txt_price.delete(0, END)

        def get_value(event):
            index = display.focus()
            asd = display.item(index, 'value')
            clearbookData()
            txt_idss.insert(END, asd[0])
            txt_names.insert(END, asd[1])
            txt_booca.insert(END, asd[2])
            txt_auth.insert(END, asd[3])
            txt_bookisbn.insert(END, asd[4])
            txt_price.insert(END, asd[5])

        def showbook(event):
            for item in display.get_children():
                display.delete(item)
            for x in try2.show_book():
                display.insert('', END, values=x)

        display = ttk.Treeview(frmend, column = ('bookid', 'bookname', 'bookcategory', 'author', 'bookisbn', 'price'))
        display.column('#0', minwidth=0, width=0)
        display.column('bookid', anchor='center', width=100)
        display.column('bookname', anchor='center', width=100)
        display.column('bookcategory', anchor='center', width=100)
        display.column('author', anchor='center', width=100)
        display.column('bookisbn', anchor='center', width=100)
        display.column('price', anchor='center', width=100)
        display.heading('#0', text="")
        display.heading('bookid', text="Book_ID")
        display.heading('bookname', text="Book Name")
        display.heading('bookcategory', text="Book Category")
        display.heading('author', text='Author')
        display.heading('bookisbn', text="Book_Isbn")
        display.heading('price', text="Book Price")
        display.grid(row=0, column=0, columnspan=4)
        display.bind('<Enter>', showbook)
        display.bind('<<TreeviewSelect>>', get_value)



        def submitbook(event=None):
            try2.insert_book(txtidss_value.get(), txtnames_value.get(), txtbooca_value.get(), txtauth_value.get(),
                             txtbookisbn_value.get(), txtprice_value.get(), 'AV')
            messagebox.showinfo('Submission Successful!', 'Submission Done')
            clearbookData()
        submit = Button(framsd, text='Submit', font=('bold', 10), command=lambda:[submitbook()], cursor='hand2')
        submit.grid(row=5, column=0, pady=10)
        submit.bind('<Return>', submitbook)

        def updatebook(event=None):
            try2.update_book(txtnames_value.get(), txtbooca_value.get(), txtauth_value.get(),
                             txtbookisbn_value.get(), txtprice_value.get(), 'AV', txtidss_value.get())
            messagebox.showinfo('Update Successful!', 'Updated Successfully')
            clearbookData()

        btn = Button(framsd, text='Update', font=('bold', 10), command=lambda:[updatebook()], cursor = 'hand2')
        btn.grid(row=5, column=1, pady=10)
        btn.bind('<Return>', updatebook)

        def deletebook(event=None):
            try2.delete_book(txtids_value.get())
            messagebox.showinfo('Deleted Success', 'You have Deleted succesfully')
            clearbookData()

        delete = Button(framsd, text='Delete', font=('bold', 10), command=lambda: [deletebook()], cursor='hand2')
        delete.grid(row=5, column=2, pady=10)
        delete.bind('<Return>', deletebook)

        def closebook(event=None):
            messagebox.showinfo('Closed!!', 'Do you want to quit')
            nwins.destroy()

        close = Button(framsd, text='Close', font=('bold', 10), command=lambda: [closebook()], cursor='hand2')
        close.grid(row=5, column=3, pady=10)
        close.bind('<Return>', closebook)

    def change_password():
        chpd = Toplevel(nwin)
        chpd.title('Change Password')
        '''chpd.geometry('800x800+100+100')'''
        chpd.state('zoomed')
        chpd.configure(bg='Purple')
        fra = Frame(chpd, height=500, width=600, bd=2, relief=SOLID, bg='Blue')
        fra.grid(row=0, column=0, padx=85, pady=50)
        fra.grid_propagate(0)
        lbl = Label(fra, text='Change Password', font=('bold', 15), fg='Red')
        lbl.grid(row=0, column=0, padx=215, pady=52)
        fraa = Frame(chpd, height=250, width=430, bd=2, relief=SOLID, bg='Blue')
        fraa.grid(row=0, column=0)
        fraa.grid_propagate(0)

        txtida_value = StringVar()
        txtnpass_value = StringVar()

        lbl_ida = Label(fraa, text='User ID', font=('bold', 10), fg='Red')
        lbl_ida.grid(row=0, column=0, padx=10, pady=20)
        lbl_npass = Label(fraa, text='New Password', font=('bold', 10), fg='Red')
        lbl_npass.grid(row=1, column=0, padx=10, pady=20)
        txt_ida = Entry(fraa, font=('calibri', 10), fg='Green', textvariable=txtida_value)
        txt_ida.grid(row=0, column=1, padx=40)
        txt_npass = Entry(fraa, font=('calibri', 10), fg='Green', show='*', textvariable=txtnpass_value)
        txt_npass.grid(row=1, column=1, padx=40)

        def change(event=None):
            result = try2.check_user(txtida_value.get())
            if not result:
                messagebox.showinfo('Not valid user', 'The User Id does not exists')
                txt_ida.delete(0, END)
                txt_npass.delete(0, END)
            else:
                messagebox.showinfo('Password changed successfully')
                try2.update_user(txtnpass_value.get(), txtida_value.get())
                txt_ida.delete(0, END)
                txt_npass.delete(0, END)

        btn = Button(fraa, text='Confirm', command=lambda: [change()], cursor='hand2')
        btn.grid(row=2, column=0, pady=10, columnspan=2)
        btn.bind('<Return>', change)

    def book_issue():
        book = Toplevel(window)
        book.title('Book Issue')
        book.state('zoomed')
        book.configure(bg='Skyblue')

        frmbok = Frame(book, height=60, width=500, bd=2, relief=SOLID, bg='Yellow')
        frmbok.grid_propagate(0)
        frmbok.grid(row=0, column=0, padx=150, pady=20)

        lbl = Label(frmbok, text='Book Issue', font=('bold', 15), fg='Red')
        lbl.grid(row=0, column=0, padx=150, pady=10)

        frmmid = Frame(book, height=300, width=500, bd=2, relief=SOLID, bg="Pink")
        frmmid.grid_propagate(0)
        frmmid.grid(row=1, column=0)

        txtbid_value = StringVar()
        txtsid_value = StringVar()
        txtbname_value = StringVar()
        txtsname_value = StringVar()
        txtissd_value = StringVar()
        txtrd_value = StringVar()

        lblbid = Label(frmmid, text='Book_ID', font=('bold', 10), fg='Red')
        lblbid.grid(row=0, column=0, padx=5, pady=10)
        txtbid = Entry(frmmid, font=('bold', 10), fg='Red', textvariable=txtbid_value)
        txtbid.grid(row=0, column=1)

        lblsid = Label(frmmid, text="Student_ID", font=('bold', 10), fg='Red')
        lblsid.grid(row=0, column=2, padx=5, pady=10)
        txtsid = Entry(frmmid, font=('bold', 10), fg='Red', textvariable=txtsid_value)
        txtsid.grid(row=0, column=3)

        lblbname = Label(frmmid, text='Book Name', font=('bold', 10), fg='Red')
        lblbname.grid(row=1, column=0, padx=5, pady=10)
        txtbname = Entry(frmmid, font=('bold', 10), fg='Red', textvariable=txtbname_value)
        txtbname.grid(row=1, column=1)

        lblsname = Label(frmmid, text='Student Name', font=('bold', 10), fg='Red')
        lblsname.grid(row=1, column=2, padx=5, pady=10)
        txtsname = Entry(frmmid, font=('bold', 10), fg='Red', textvariable=txtsname_value)
        txtsname.grid(row=1, column=3)

        lbleissd = Label(frmmid, text='Issue Date', font=('bold', 10), fg='Red')
        lbleissd.grid(row=2, column=0, padx=5, pady=10)
        txteissd = Entry(frmmid, font=('bold', 10), fg='Red', textvariable=txtissd_value)
        txteissd.grid(row=2, column=1)

        lblrd = Label(frmmid, text="Return Date", font=('bold', 10), fg='Red')
        lblrd.grid(row=2, column=2, padx=5, pady=10)
        txtrd = Entry(frmmid, font=('bold', 10), fg='Red', textvariable=txtrd_value)
        txtrd.grid(row=2, column=3)

        frmend = Frame(book, height=250, width=500, bd=2, relief=SOLID, bg='Darkslateblue')
        frmend.grid_propagate(0)
        frmend.grid(row=2, column=0)

        def bookname(event):
            for n in try2.Get_book_name(txtbid_value.get()):
                if n or '':
                    txtbname.delete(0,END)
                    txtbname.insert(END, n[0])
                else:
                    messagebox.showinfo('Not Valid', 'Not a valid book', parent=book)
                    txtbname.delete(0,END)
                    txtbid.delete(0, END)

        txtbid.bind('<KeyRelease>', bookname)

        def stuname(event):
            for n in try2.Get_student_name(txtsid_value.get()):
                if not n:
                    messagebox.showinfo('Not Valid', 'Not a valid student id', parent=book)
                    txtsname.delete(0,END)
                    txtsid.delete(0, END)
                else:
                    txtsname.delete(0, END)
                    txtsname.insert(END, n[0])

        txtsid.bind('<KeyRelease>', stuname)

        def clearbookData():
            txtbid.delete(0, END)
            txtsid.delete(0, END)
            txtbname.delete(0, END)
            txtsname.delete(0, END)
            txteissd.delete(0, END)
            txtrd.delete(0, END)

        def show_bookissue(event):
            for x in bvr.get_children():
                bvr.delete(x)
            for x in try2.show_bookissue():
                bvr.insert('',END,values = x)

        def get_value(event):
            index = bvr.focus()
            asdee = bvr.item(index, 'value')
            clearbookData()
            txtbid.insert(END, asdee[0])
            txtsid.insert(END, asdee[1])
            txtbname.insert(END, asdee[2])
            txtsname.insert(END, asdee[3])
            txteissd.insert(END, asdee[4])
            txtrd.insert(END, asdee[5])



        def issue(event=None):
            try2.insert_issue_book(txtbid_value.get(), txtsid_value.get(), txtbname_value.get(), txtsname_value.get(),
                             txtissd_value.get(), txtrd_value.get(), 'Issued')
            try2.update_status(txtbid_value.get())
            messagebox.showinfo('Book Issued', 'The book has been issued')
            

        btn = Button(frmmid, text='Book Issue', command=lambda: [issue()], cursor='hand2')
        btn.grid(row=3, column=1, padx=30,pady=10, columnspan=2)
        btn.bind('<Return>', issue)

        bifrmend = Frame(book, height=300, width=1000, bd=2, relief=SOLID, bg='Pink')
        bifrmend.propagate(0)
        bifrmend.grid(row=2, column=0)

        bvr = ttk.Treeview(bifrmend,columns=('bookid', 'bookname', 'studentname', 'studentid', 'issuedate', 'returndate'))
        bvr.column('#0', minwidth=0, width=0)
        bvr.column('bookid', anchor='center', width=105)
        bvr.column('bookname', anchor='center', width=110)
        bvr.column('studentname', anchor='center', width=110)
        bvr.column('studentid', anchor='center', width=110)
        bvr.column('issuedate', anchor='center', width=110)
        bvr.column('returndate', anchor='center', width=110)

        bvr.heading('#0', text='')
        bvr.heading('bookid', text='Book ID')
        bvr.heading('bookname', text='Book Name')
        bvr.heading('studentname', text='Student Name')
        bvr.heading('studentid', text='Student Id')
        bvr.heading('issuedate', text='Issue Date')
        bvr.heading('returndate', text='Return Date')
        bvr.grid(row=0, column=0, padx=5)
        bvr.bind('<Enter>', show_bookissue)
        bvr.bind('<<TreeviewSelect>>', get_value)

    def book_return():
        bookr = Toplevel(window)
        bookr.title('Book Return')
        bookr.state('zoomed')
        bookr.configure(bg = 'Cyan')

        frmr = Frame(bookr, height=70, width=520, bd=2, relief=SOLID, bg='Orange')
        frmr.grid(row=0, column=0, padx=150, pady = 10)
        frmr.grid_propagate(0)

        lbl = Label(frmr, text='Book Return', font=('bold', 15), fg='Green')
        lbl.grid(row=0, column=0, padx=120, pady=10)

        frmmir = Frame(bookr, height=300, width=500, bd=2, relief=SOLID, bg="Pink")
        frmmir.grid_propagate(0)
        frmmir.grid(row=1, column=0)

        txtbid_value = StringVar()
        txtsid_value = StringVar()
        txtbname_value = StringVar()
        txtsname_value = StringVar()

        lblbrid = Label(frmmir, text='Book_ID', font=('bold', 10), fg='Red')
        lblbrid.grid(row=0, column=0, padx=5, pady=10)
        txtbrid = Entry(frmmir, font=('bold', 10), fg='Red', textvariable=txtbid_value)
        txtbrid.grid(row=0, column=1)

        lblsrid = Label(frmmir, text="Student_ID", font=('bold', 10), fg='Red')
        lblsrid.grid(row=0, column=2, padx=5, pady=10)
        txtsrid = Entry(frmmir, font=('bold', 10), fg='Red', textvariable=txtsid_value)
        txtsrid.grid(row=0, column=3)

        lblbrname = Label(frmmir, text='Book Name', font=('bold', 10), fg='Red')
        lblbrname.grid(row=1, column=0, padx=5, pady=10)
        txtbrname = Entry(frmmir, font=('bold', 10), fg='Red', textvariable=txtbname_value)
        txtbrname.grid(row=1, column=1)

        lblsrname = Label(frmmir, text='Student Name', font=('bold', 10), fg='Red')
        lblsrname.grid(row=1, column=2, padx=5, pady=10)
        txtsrname = Entry(frmmir, font=('bold', 10), fg='Red', textvariable=txtsname_value)
        txtsrname.grid(row=1, column=3)

        def clearbookissue():
            txtbrid.delete(0, END)
            txtsrid.delete(0, END)
            txtbrname.delete(0, END)
            txtsrname.delete(0, END)
            

        def show_bookissue(event):
            for x in bvr.get_children():
                bvr.delete(x)
            for x in try2.show_bookissue():
                bvr.insert('',END,values = x)

        def get_value(event):
            index = bvr.focus()
            asdee = bvr.item(index, 'value')
            clearbookissue()
            txtbrid.insert(END, asdee[0])
            txtsrid.insert(END, asdee[1])
            txtbrname.insert(END, asdee[2])
            txtsrname.insert(END, asdee[3])
            
        bifrmende = Frame(bookr, height=300, width=1000, bd=2, relief=SOLID, bg='Pink')
        bifrmende.propagate(0)
        bifrmende.grid(row=2, column=0)

        bvr = ttk.Treeview(bifrmende,columns=('bookid', 'bookname', 'studentname', 'studentid', 'issuedate', 'returndate'))
        bvr.column('#0', minwidth=0, width=0)
        bvr.column('bookid', anchor='center', width=105)
        bvr.column('bookname', anchor='center', width=110)
        bvr.column('studentname', anchor='center', width=110)
        bvr.column('studentid', anchor='center', width=110)
        bvr.column('issuedate', anchor='center', width=110)
        bvr.column('returndate', anchor='center', width=110)

        bvr.heading('#0', text='')
        bvr.heading('bookid', text='Book ID')
        bvr.heading('bookname', text='Book Name')
        bvr.heading('studentname', text='Student Name')
        bvr.heading('studentid', text='Student Id')
        bvr.heading('issuedate', text='Issue Date')
        bvr.heading('returndate', text='Return Date')
        bvr.grid(row=0, column=0, padx=5)
        bvr.bind('<Enter>', show_bookissue)
        bvr.bind('<<TreeviewSelect>>', get_value)

        def returns(event=None):
            try2.delete_book_issue(txtbid_value.get())
            try2.return_status(txtbid_value.get())
            messagebox.showinfo('Book Return', 'The book has been returned', parent = bookr)
            clearbookissue()
        btn = Button(frmmir, text='Book Return', command=lambda: [returns()], cursor='hand2')
        btn.grid(row=3, column=1, padx=30,pady=10, columnspan=2)
        btn.bind('<Return>', returns)
        

    menubar = Menu(nwin)
    nwin.configure(menu = menubar)
    m1 = Menu(menubar)
    m2 = Menu(menubar)
    menubar.add_cascade(label = 'Registration', menu = m1)
    menubar.add_cascade(label = 'Issue & Return', menu = m2)
    m1.add_command(label = 'Member Registration', command = ' ')
    m1.add_command(label = 'Student Registration', command = user_details)
    m1.add_command(label = 'Book Registration', command = book_regis)
    m1.add_separator()
    m1.add_command(label = 'Exit', command = nwin.destroy)
    m2.add_command(label = 'Book Issue', command = book_issue)
    m2.add_command(label = 'Book Return', command = book_return)
    menubar.add_command(label = 'Change Password', command = change_password)

    frm = Frame(nwin, height=70, width=520, bd=2, relief=SOLID, bg='Orange')
    frm.grid(row=0, column=0, padx=150, pady = 10)
    frm.grid_propagate(0)

    lbl = Label(frm, text='Student Registration Form', font=('bold', 15), fg='Green')
    lbl.grid(row=0, column=0, padx=120, pady=10)

    frams = Frame(nwin, height=300, width=520, bd=2, relief=SOLID, bg='salmon')
    frams.grid(row=1, column=0, padx=50, pady=10)
    frams.grid_propagate(0)
    txtids_value = StringVar()
    txtname_value = StringVar()
    txtdob_value = StringVar()
    txtmob_value = StringVar()
    txtema_value = StringVar()
    txtadd_value = StringVar()
    txtcour_value = StringVar()
    txtcourdu_value = StringVar()
    txtcourf_value = StringVar()

    lbl_ids = Label(frams, text='Id', font=('bold', 10), fg='Purple')
    lbl_ids.grid(row=0, column=0, padx=5, pady=10)
    txt_ids = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtids_value)
    txt_ids.grid(row=0, column=1, padx=5, pady=10)

    lbl_name = Label(frams, text='Name', font=('bold', 10), fg='Purple')
    lbl_name.grid(row=0, column=2, padx=5, pady=10)
    txt_name = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtname_value)
    txt_name.grid(row=0, column=3, padx=5, pady=10)

    lbl_dob = Label(frams, text='Date of Birth', font=('bold', 10), fg='Purple')
    lbl_dob.grid(row=1, column=0, padx=5, pady=10)
    txt_dob = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtdob_value)
    txt_dob.grid(row=1, column=1, padx=5, pady=10)

    lbl_mobile = Label(frams, text='Mobile', font=('bold', 10), fg='Purple')
    lbl_mobile.grid(row=1, column=2, padx=5, pady=10)
    txt_mobile = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtmob_value)
    txt_mobile.grid(row=1, column=3, padx=5, pady=10)

    lbl_email = Label(frams, text='Email', font=('bold', 10), fg='Purple')
    lbl_email.grid(row=2, column=0, padx=5, pady=10)
    txt_email = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtema_value)
    txt_email.grid(row=2, column=1, padx=5, pady=10)

    lbl_address = Label(frams, text='Address', font=('bold', 10), fg='Purple')
    lbl_address.grid(row=2, column=2, padx=5, pady=10)
    txt_address = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtadd_value)
    txt_address.grid(row=2, column=3, padx=5, pady=10)

    lbl_course = Label(frams, text='Course', font=('bold', 10), fg='Purple')
    lbl_course.grid(row=3, column=0, padx=5, pady=10)
    txt_course = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtcour_value)
    txt_course.grid(row=3, column=1, padx=5, pady=10)

    lbl_courdu = Label(frams, text='Course Duration', font=('bold', 10), fg='Purple')
    lbl_courdu.grid(row=3, column=2, padx=5, pady=10)
    txt_courdu = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtcourdu_value)
    txt_courdu.grid(row=3, column=3, padx=5, pady=10)

    lbl_courf = Label(frams, text='Course Fee', font=('bold', 10), fg='Purple')
    lbl_courf.grid(row=4, column=0, padx=5, pady=10)
    txt_courf = Entry(frams, font=('calibri', 10), fg='Green', textvariable = txtcourf_value)
    txt_courf.grid(row=4, column=1, padx=5, pady=10)

    frmend = Frame(nwin, height=250, width=1000, bd=2, relief=SOLID, bg='Darkslateblue')
    frmend.grid_propagate(0)
    frmend.grid(row=2, column=0, padx=5, pady=30)

    def clearstuvalue():
        txt_ids.delete(0, END)
        txt_name.delete(0, END)
        txt_dob.delete(0, END)
        txt_mobile.delete(0, END)
        txt_email.delete(0, END)
        txt_address.delete(0, END)
        txt_course.delete(0, END)
        txt_courdu.delete(0, END)
        txt_courf.delete(0, END)

    def stuname(event):
        n = try2.Get_student_name(txtids_value.get())

        if n or '':
            txt_name.delete(0, END)
            txt_name.insert(END, n[0])
        else:
            messagebox.showinfo('Not Valid', 'Not a valid student')
            txt_name.delete(0, END)

    txt_ids.bind('<KeyRelease>', stuname)

    def show_studata(event):
        for item in tvr.get_children():
            tvr.delete(item)
        for x in try2.show_student():
            tvr.insert('', END, values=x)

    def get_value(event):
        clearstuvalue()
        inde = tvr.focus()
        asde = tvr.item(inde, 'value')
        txt_ids.insert(END, asde[0])
        txt_name.insert(END, asde[1])
        txt_dob.insert(END, asde[2])
        txt_mobile.insert(END, asde[3])
        txt_email.insert(END, asde[4])
        txt_address.insert(END, asde[5])
        txt_course.insert(END, asde[6])
        txt_courdu.insert(END, asde[7])
        txt_courf.insert(END, asde[8])

    tvr = ttk.Treeview(frmend,columns=('id', 'name', 'dob', 'mobile', 'email', 'address', 'course', 'course_duration', 'fee'))
    tvr.column('#0', minwidth=0, width=0)
    tvr.column('id', anchor=CENTER, width=100)
    tvr.column('name', anchor=CENTER, width=100)
    tvr.column('dob', anchor=CENTER, width=100)
    tvr.column('mobile', anchor=CENTER, width=100)
    tvr.column('address', anchor=CENTER, width=100)
    tvr.column('course', anchor=CENTER, width=100)
    tvr.column('course_duration', anchor=CENTER, width=100)
    tvr.column('fee', anchor=CENTER, width=100)
    tvr.heading('#0', text='')
    tvr.heading('id', text='Student ID')
    tvr.heading('name', text='name')
    tvr.heading('dob', text='DOB')
    tvr.heading('mobile', text='Mobile')
    tvr.heading('email', text='Email')
    tvr.heading('address', text='Address')
    tvr.heading('course', text='Course')
    tvr.heading('course_duration', text='Duration')
    tvr.heading('fee', text='Fee')
    tvr.grid(row=0, column=0, columnspan=4)
    tvr.bind('<Enter>', show_studata)
    tvr.bind('<<TreeviewSelect>>', get_value)

    def submits(event=None):
        try2.insert_student(txtids_value.get(), txtname_value.get(), txtdob_value.get(), txtmob_value.get(), txtema_value.get(), txtadd_value.get(), txtcour_value.get(), txtcourdu_value.get(), txtcourf_value.get())
        messagebox.showinfo('Submission Successful!', 'Submission Done')
        clearstuvalue()
    submit = Button(frams, text='Submit', font=('bold', 10), command=lambda:[submits()], cursor='hand2')
    submit.grid(row=5, column=0, pady=10)
    submit.bind('<Return>', submits)

    def updates(event=None):
        try2.update_student(txtname_value.get(), txtdob_value.get(), txtmob_value.get(), txtema_value.get(), txtadd_value.get(), txtcour_value.get(), txtcourdu_value.get(), txtcourf_value.get(), txtids_value.get())
        messagebox.showinfo('Update Successful!', 'Updated Successfully')
        clearstuvalue()
    update = Button(frams, text='Update', font=('bold', 10), command=lambda:[updates()], cursor='hand2')
    update.grid(row=5, column=1, pady=10)
    update.bind('<Return>', updates)

    def deletes(event=None):
        try2.delete_student(txtids_value.get())
        messagebox.showinfo('Deletion Successful!', 'Deleted Successfully')
        clearstuvalue()
    delete = Button(frams, text='Delete', font=('bold', 10), command=lambda:[deletes()], cursor='hand2')
    delete.grid(row=5, column=2, pady=10)
    delete.bind('<Return>', deletes)

    def closes(event=None):
        messagebox.showinfo('Close!', 'Closed')
        nwin.destroy()
    close = Button(frams, text='Close', font=('bold', 10), command=lambda:[closes()], cursor='hand2')
    close.grid(row=5, column=3, pady=10, columnspan=4)
    close.bind('<Return>', closes)






window.mainloop()