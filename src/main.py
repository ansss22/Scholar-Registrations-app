from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mysql.connector



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword',
    database='nameofDB'
)


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x1200+1+1')
        self.root.title('Management of scholar registrations')
        self.root.configure(background="#edeced")
        self.root.resizable(True, True)

        #-------------- variables --------------------------------
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.address_var = StringVar()
        self.moahel_var = StringVar()
        self.gender_var = StringVar()
        self.search_var = StringVar()  
        self.search_criteria_var = StringVar()
        self.dell_var = StringVar()

        #-------------- Title --------------------------------
        title = Label(self.root, text="Management of scholar registrations", bg='#2A629A', font=('Arial', 14), fg='white')
        title.grid(row=0, column=0, columnspan=3, sticky='ew')

        #------------------- search manage -----------------
        search_Frame = Frame(self.root, bg="#edeced")
        search_Frame.grid(row=1, column=0, columnspan=3, sticky='ew', padx=5, pady=5)

        lbl_search = Label(search_Frame, text='Search student', bg="#edeced")
        lbl_search.pack(side=LEFT, padx=5)

        combo_search = ttk.Combobox(search_Frame, values=('id', 'name', 'email', 'phone'), textvariable=self.search_criteria_var)
        combo_search.pack(side=LEFT, padx=5)

        search_Entry = Entry(search_Frame, textvariable=self.search_var)
        search_Entry.pack(side=LEFT, padx=5)

        se_btn = Button(search_Frame, text='Search', bg='#132742', fg="white",width=8,height=1 ,border=0,font=('Arial',12) ,command=self.search)
        se_btn.pack(side=LEFT, padx=5)

        #---------- details ------------------------
        Details_Frame = Frame(self.root, bg="#edeced")
        Details_Frame.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        #------ scroll ------------------------
        scroll_x = Scrollbar(Details_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Details_Frame, orient=VERTICAL)

        #------ treeview ------------
        self.student_table = ttk.Treeview(Details_Frame,
                                          columns=('id', 'name', 'email', 'phone', 'address', 'gender', 'certi'),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set
                                          )
        self.student_table.grid(row=0, column=0, sticky='nsew')

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        scroll_x.grid(row=1, column=0, sticky='ew')
        scroll_y.grid(row=0, column=1, sticky='ns')

        self.student_table['show'] = 'headings'
        self.student_table.heading('id', text="ID")
        self.student_table.heading('name', text="Name")
        self.student_table.heading('email', text="Email")
        self.student_table.heading('phone', text="Phone")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('gender', text="Gender")
        self.student_table.heading('certi', text="Certi")

        self.student_table.column('id', width=50)
        self.student_table.column('name', width=150)
        self.student_table.column('email', width=200)
        self.student_table.column('phone', width=100)
        self.student_table.column('address', width=200)
        self.student_table.column('gender', width=100)
        self.student_table.column('certi', width=100)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        #-------------- tools --------------------------------
        Manage_Frame = Frame(self.root, bg="#edeced")
        Manage_Frame.grid(row=2, column=2, rowspan=2, sticky='nsew', padx=5, pady=5)

        lbl_ID = Label(Manage_Frame, text="ID", bg="#edeced",font=('Arial',10 ),padx=5, pady=15)
        lbl_ID.pack()
        ID_Entry = Entry(Manage_Frame, textvariable=self.id_var)
        ID_Entry.pack()

        lbl_name = Label(Manage_Frame,bg="#edeced", text="Name",font=('Arial',10 ),padx=5, pady=15)
        lbl_name.pack()
        Name_Entry = Entry(Manage_Frame, textvariable=self.name_var)
        Name_Entry.pack()

        lbl_email = Label(Manage_Frame, bg="#edeced", text="Email",font=('Arial',10 ),padx=5, pady=15)
        lbl_email.pack()
        email_Entry = Entry(Manage_Frame, textvariable=self.email_var)
        email_Entry.pack()

        lbl_phone = Label(Manage_Frame, bg="#edeced", text="Phone",font=('Arial',10 ),padx=5, pady=15)
        lbl_phone.pack()
        phone_Entry = Entry(Manage_Frame, textvariable=self.phone_var)
        phone_Entry.pack()

        lbl_certi = Label(Manage_Frame, bg="#edeced", text="certification",font=('Arial',10),padx=5, pady=15)
        lbl_certi.pack()
        certi_Entry = Entry(Manage_Frame, textvariable=self.moahel_var)
        certi_Entry.pack()

        lbl_gender = Label(Manage_Frame, bg="#edeced", text="Gender",font=('Arial',10 ),padx=5, pady=15)
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, values=('masculin', 'feminine'))
        combo_gender.pack()

        lbl_address = Label(Manage_Frame, bg="#edeced", text="Address",font=('Arial',10 ),padx=5, pady=15)
        lbl_address.pack()
        address_Entry = Entry(Manage_Frame, textvariable=self.address_var)
        address_Entry.pack()

        lbl_delete = Label(Manage_Frame, fg="black", bg="#edeced", text="Delete student by name",font=('Arial', 10 ),padx=5, pady=15)
        lbl_delete.pack()
        delete_Entry = Entry(Manage_Frame, textvariable=self.dell_var)
        delete_Entry.pack()

        # ------------ buttons ------------------
        btn_Frame = Frame(self.root, bg="#edeced")
        btn_Frame.grid(row=3, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

        title1 = Label(btn_Frame, text="Dashboard", font=("Arial", 14), fg='white', bg='#2A629A')
        title1.pack(fill=X)

        add_btn = Button(btn_Frame, text="Add Student",bg='#132742', fg="white",width=16,height=1 ,border=0,font=('Arial',12 , 'bold') , command=self.add)
        add_btn.pack(side=LEFT, padx=5, pady=5)

        del_btn = Button(btn_Frame, text="Delete Student", bg='#132742', fg="white",width=16,height=1 ,border=0,font=('Arial',12 , 'bold') , command=self.delete)
        del_btn.pack(side=LEFT, padx=5, pady=5)

        update_btn = Button(btn_Frame, text="Update Info", bg='#132742', fg="white",width=16,height=1 ,border=0,font=('Arial',12 , 'bold') , command=self.update)
        update_btn.pack(side=LEFT, padx=5, pady=5)

        clear_btn = Button(btn_Frame, text="Clear Labels", bg='#132742', fg="white",width=16,height=1 ,border=0,font=('Arial',12 , 'bold') , command=self.clear)
        clear_btn.pack(side=LEFT, padx=5, pady=5)

        about_btn = Button(btn_Frame, text="About Us", bg='#132742', fg="white",width=16,height=1 ,border=0,font=('Arial',12 , 'bold') , command=self.about)
        about_btn.pack(side=LEFT, padx=5, pady=5)

        exit_btn = Button(btn_Frame, text="Quit",bg='#132742', fg="white",width=16,height=1 ,border=0,font=('Arial',12 , 'bold') , command=root.quit)
        exit_btn.pack(side=LEFT, padx=5, pady=5)

        # Configure grid weights
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        Details_Frame.grid_rowconfigure(0, weight=1)
        Details_Frame.grid_columnconfigure(0, weight=1)

        self.fetch_all()

    def add(self):
        if self.id_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password='Ana22@flipo#', database="stud")
            cur = con.cursor()
            cur.execute("INSERT INTO student (id, name, email, phone, address, gender, certi) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                self.id_var.get(),
                self.name_var.get(),
                self.email_var.get(),
                self.phone_var.get(),
                self.address_var.get(),
                self.gender_var.get(),
                self.moahel_var.get()
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()

    def fetch_all(self):
        con = mysql.connector.connect(host="localhost", user="root", password='Ana22@flipo#', database="stud")
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.address_var.set("")
        self.gender_var.set("")
        self.moahel_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        if row:
            self.id_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.phone_var.set(row[3])
            self.address_var.set(row[4])
            self.gender_var.set(row[5])
            self.moahel_var.set(row[6])

    def update(self):
        if self.id_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password='Ana22@flipo#', database="stud")
            cur = con.cursor()
            cur.execute("UPDATE student SET name = %s, email = %s, phone = %s, address = %s, gender = %s, certi = %s WHERE id = %s", (
                self.name_var.get(),
                self.email_var.get(),
                self.phone_var.get(),
                self.address_var.get(),
                self.gender_var.get(),
                self.moahel_var.get(),
                self.id_var.get()
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()

    def delete(self):
        if self.dell_var.get() == "":
            messagebox.showerror("Error", "Please enter the name of the student to delete")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password='Ana22@flipo#', database="stud")
            cur = con.cursor()
            cur.execute("DELETE FROM student WHERE name = %s", (self.dell_var.get(),))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()

    def search(self):
        if self.search_criteria_var.get() == "" or self.search_var.get() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter a search value")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password='Ana22@flipo#', database="stud")
            cur = con.cursor()
            query = f"SELECT * FROM student WHERE {self.search_criteria_var.get()} LIKE '%{self.search_var.get()}%'"
            cur.execute(query)
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No matching records found")
            con.commit()
            con.close()

    def about(self):
        messagebox.showinfo("", "Ali, Safouane et Anas Etudiants EST filiere IDAA")

root = Tk()
ob = Student(root)
root.mainloop() 