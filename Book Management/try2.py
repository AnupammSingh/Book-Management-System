import sqlite3
def connection():
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('create table if not exists book_issues(Book_Id text primary key, Student_id text, book_name text, Student_Name text, Issue_Date, Return_Date )')
    mycursor.execute('create table if not exists book_details(Book_Id text primary key, Book_Name text, Book_Category text, Author text, Book_ISBN text, Price int)')
    mycursor.execute('create table if not exists user_details(id text primary key, name text, password text)')
    mycursor.execute('create table if not exists student_regis(Id text primary key, Name text, Date_of_Birth text, Mobile text, Email text, Address text, Course text, Course_Duration text, Course_Fee int)')
    conn.commit()
    conn.close()
connection()

def insert_book(Book_Id, Book_Name, Book_Category, Author, Book_ISBN, Price, Status):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('insert into book_details values(?, ?, ?, ?, ?, ?, ?)', (Book_Id, Book_Name, Book_Category, Author, Book_ISBN, Price, Status))
    conn.commit()
    conn.close()


def insert_issue_book(Book_Id, Student_Id, book_name, Student_Name, Issue_Date, Return_Date, Status):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('insert into book_issues values(?, ?, ?, ?, ?, ?, ?)', (Book_Id, Student_Id, book_name, Student_Name, Issue_Date, Return_Date, Status))
    conn.commit()
    conn.close()

def insert_user(id, name, password):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('insert into user_details values(?, ?, ?)', (id, name, password))
    conn.commit()
    conn.close()

def insert_student(Id, Name, Date_of_Birth, Mobile, Email, Address, Course, Course_Duration, Course_Fee):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('insert into student_regis values(?, ?, ?, ?, ?, ?, ?, ?, ?)', (Id, Name, Date_of_Birth, Mobile, Email, Address, Course, Course_Duration, Course_Fee))
    conn.commit()
    conn.close()


def update_user(password, Id):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('update user_details set password = ? where Id = ?', (password, Id))
    conn.commit()
    conn.close()

def update_student(Name, Date_of_Birth, Mobile, Email, Address, Course, Course_Duration, Course_Fee, Id):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('update student_regis set Name = ?, Date_of_Birth = ?, Mobile = ?, Email = ?, Address = ?, Course = ?, Course_Duration = ?, Course_Fee = ? where Id = ?', (Name, Date_of_Birth, Mobile, Email, Address, Course, Course_Duration, Course_Fee, Id))
    conn.commit()
    conn.close()

def update_book(Book_Name, Book_Category, Author, Book_ISBN, Price, Status, Book_Id):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('update book_details set Book_Name = ?, Book_Category = ?, Author = ?, Book_ISBN = ?, Price = ?, Status = ? where Book_Id = ?', (Book_Name, Book_Category, Author, Book_ISBN, Price, Status, Book_Id))
    conn.commit()
    conn.close()

def update_status(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('update book_details set  Status = "Issued" where Book_Id = ?', (id,))
    conn.commit()
    conn.close()




def delete_user(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('delete from user_details where id = ?', (id,))
    conn.commit()
    conn.close()

def delete_student(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('delete from student_regis where id=?',(id,))
    conn.commit()
    conn.close()

def delete_book_issue(bookid,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('delete from book_issues where Book_id=?',(bookid,))
    conn.commit()
    conn.close()



def show_user(id, password):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select * from user_details where id = ? and password = ?', (id, password))
    var = mycursor.fetchall()
    return var

def show_student():
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select * from student_regis')
    var = mycursor.fetchall()
    return var

def show_book():
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select * from book_details where Status = "AV"')
    var = mycursor.fetchall()
    return var

def show_bookissue():
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select * from book_issues')
    row = mycursor.fetchall()
    return row

def check_user(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select * from user_details where id = ?', (id,))
    var = mycursor.fetchall()
    return var

def Get_student_name(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select Name from student_regis where Id = ?', (id,))
    var = mycursor.fetchall()
    return var

def Get_book_name(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('Select Book_Name from book_details where Book_Id = ?', (id,))
    var = mycursor.fetchall()
    return var

def return_status(id,):
    conn = sqlite3.connect('student.db')
    mycursor = conn.cursor()
    mycursor.execute('update book_details set  Status = "AV" where Book_Id = ?', (id,))
    conn.commit()
    conn.close()

'''for x in show_user():
    print (x)'''
