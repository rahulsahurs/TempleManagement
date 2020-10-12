import tkinter as tk
import tkinter as tk1
import tkinter as tk2
from tkinter import ttk, messagebox
from tkinter import Menu
import sqlite3
import os
from tabulate import tabulate
from PIL import ImageTk, Image

root1 = tk.Tk()
root1.title(" Management System By Smart_tech ")
root1.geometry("950x600")
root1.minsize(950, 600)
root1.maxsize(950, 600)
root1.configure(bg='LightSkyBlue1')

appLabel = tk.Label(text=" SHREE AADINATH DIGAMBER JAIN MANDIR ",
                    fg="DarkGoldenrod3", width=40, bg='LightSkyBlue1')
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(20, 15))
mLabel = tk.Label(text="Atishay Kshetra Kakaganj,sagar(M.P) mob:7748810808", width=70, font=("Sylfaen", 12),
                  fg='Black', bg='LightSkyBlue1')
mLabel.grid(row=1, column=0, padx=(100, 10), pady=(0, 30))

separator = ttk.Separator(orient='horizontal').grid(
    column=0, row=2, columnspan=2, sticky='ew', pady=(0, 30))


def take_entry1():
    date1 = 0

    root = tk1.Tk()
    root.title("Management")
    root.geometry("1080x700")
    root.minsize(1080, 700)
    root.maxsize(1080, 700)

    image = Image.open("mandirr.jpg")
    image = image.resize((100, 100), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    label_for_image = tk1.Label(root, bg='grey')
    tk1.Label(label_for_image, image=image).grid(row=0, column=4)
    label_for_image.pack()

    app_label = tk1.Label(label_for_image, text=" SHREE AADINATH DIGAMBER JAIN MANDIR ", fg="DarkGoldenrod3",
                          width=40, bg='grey')
    app_label.config(font=("Sylfaen", 30))
    app_label.grid(row=0, columnspan=4, padx=(10, 10), pady=(20, 30))

    app_label1 = tk1.Label(label_for_image, text=" New Entry ",
                           fg="Lawn Green", width=20, bg='grey')
    app_label1.config(font=("Sylfaen", 20))
    app_label1.place(x=400, y=95)

    ttk.Separator(label_for_image, orient='horizontal').grid(column=0, row=1, columnspan=6, sticky='ew',
                                                             pady=(0, 50))

    s_label = tk1.Label(label_for_image, text="S.NO.",
                        width=40, anchor='center', font=("Sylfaen", 12))
    s_label.grid(row=1, column=0, pady=(80, 20))
    name_label = tk1.Label(label_for_image, text="NAME",
                           width=40, anchor='center', font=("Sylfaen", 12))
    name_label.grid(row=2, column=0, padx=(10, 0), pady=20)
    amount_label = tk1.Label(label_for_image, text="AMOUNT",
                             width=40, anchor='center', font=("Sylfaen", 12))
    amount_label.grid(row=3, column=0, padx=(10, 0), pady=20)
    phone_label = tk1.Label(label_for_image, text="PHONE",
                            width=40, anchor='center', font=("Sylfaen", 12))
    phone_label.grid(row=4, column=0, padx=(10, 0), pady=20)
    address_label = tk1.Label(
        label_for_image, text="ADDRESS", width=40, anchor='center', font=("Sylfaen", 12))
    address_label.grid(row=5, column=0, padx=(10, 0), pady=20)
    date_label = tk1.Label(label_for_image, text="DATE",
                           width=15, anchor='center', font=("Sylfaen", 10))
    date_label.place(x=830, y=190)
    d_label = tk1.Label(label_for_image, text="PARTICULAR",
                        width=40, anchor='center', font=("Sylfaen", 12))
    d_label.grid(row=7, column=0, padx=(10, 0), pady=20)

    s_entry = tk1.Entry(label_for_image, width=40)
    name_entry = tk1.Entry(label_for_image, width=40)
    amount_entry = tk1.Entry(label_for_image, width=40)
    phone_entry = tk1.Entry(label_for_image, width=40)
    address_entry = tk1.Entry(label_for_image, width=40)
    date_entry = tk1.Entry(label_for_image, text=date1, width=10)
    tk1.Entry(label_for_image, width=40)

    combo_example = ttk.Combobox(label_for_image,
                                 values=[
                                     "prakshal",
                                     "shri g virajman",
                                     "shanti dhara",
                                     "dravya", 'vrat bhandar', 'mandir vyavastha', 'oshadi dan', 'akhand jyoti',
                                     'yantra shri virajan', 'other'])
    combo_example.grid(column=1, row=7)
    combo_example.bind('<<ComboboxSelected>>')
    combo_example.get()

    s_entry.grid(row=1, column=1, pady=(80, 20))
    name_entry.grid(row=2, column=1, pady=20)
    amount_entry.grid(row=3, column=1, pady=20)
    phone_entry.grid(row=4, column=1, pady=20)
    address_entry.grid(row=5, column=1, pady=20)
    date_entry.place(x=950, y=194)

    connection = sqlite3.connect('management.db')

    table__name = "management_table1"
    student__id = "student_id"
    student__name = "student_name"
    amount_t = "student_college"
    student__address = "student_address"
    student__phone = "student_phone"
    date_t = "student_date"
    particular_r = "student_particular"

    connection.execute(" CREATE TABLE IF NOT EXISTS " + table__name + " ( " + student__id +
                       " INTEGER, " + student__name + " TEXT, " + amount_t + " TEXT, " +
                       student__address + " TEXT, " + date_t + " BLOB, " + particular_r + " BLOB, "
                       + student__phone + " INTEGER);")

    def take_name_input():
        sr_no = s_entry.get()
        s_entry.delete(0, tk1.END)
        username = name_entry.get()
        name_entry.delete(0, tk1.END)
        amount = amount_entry.get()
        amount_entry.delete(0, tk1.END)
        address = address_entry.get()
        address_entry.delete(0, tk1.END)
        date = date_entry.get()
        date_entry.delete(0, tk1.END)
        particular = combo_example.get()
        combo_example.delete(0, tk1.END)
        phone = int(phone_entry.get())
        phone_entry.delete(0, tk1.END)

        connection.execute("INSERT INTO " + table__name + " ( " + student__id + ", " + student__name + ", " +
                           amount_t + ", " + student__address + ", " + date_t + ", " + particular_r + ", "
                           + student__phone +
                           ") VALUES ( '" + sr_no + "', '"
                           + username + "', '" + amount + "', '" +
                           address + "', '" + date + "', '" + particular + "', '" + str(phone) + "');")
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")

    def destroy_root_window():
        root.destroy()
        second_window = tk1.Tk()
        second_window.geometry("1400x700")
        second_window.title("Display results")

        app_label9 = tk1.Label(
            second_window, text="SHREE AADINATH DIGAMBER JAIN MANDIR", fg="red", width=40)
        app_label9.config(font=("Sylfaen", 30))
        app_label9.pack()

        tree = ttk.Treeview(second_window, selectmode='browse')
        tree["columns"] = ("one", "two", "three", "four",
                           "five", "six", "seven")
        tree.column("#0", width=0, minwidth=0, stretch=tk1.NO)

        tree.heading("one", text="SR.NO.")
        tree.heading("two", text="Date")
        tree.heading("three", text="Name")
        tree.heading("four", text="Amount")
        tree.heading("five", text="Address")
        tree.heading("six", text="Particular")
        tree.heading("seven", text="Phone")

        cursor = connection.execute("SELECT * FROM " + table__name + " ;")
        i = 1

        for row in cursor:
            tree.insert('', i,
                        values=(row[0], row[4], row[1],
                                row[2], row[3], row[5], row[6]))
            i = i + 1
        tree.pack(side="left")

        def i_print():
            pri = []
            for line in tree.get_children():
                pr = tree.item(line)['values']
                pri += [pr]
            template = ["SR.NO.", "Date", "Name",
                        "Amount", "Address", "Particular", "Phone"]
            print_t = tabulate(pri, template)
            with open("temp.txt", "w") as f:
                f.write(print_t)
            os.startfile("temp.txt", "print")

        def delete_entry():
            selected_item = tree.selection()[0]
            values = (tree.item(selected_item)['values'])
            j = values[0]
            query = F"DELETE FROM {table__name} WHERE {student__id} = {j};"
            connection.execute(query)
            connection.commit()
            tree.delete(selected_item)

        m = Menu(second_window, tearoff=0)
        m.add_command(label="Delete", command=delete_entry)

        def do_popup(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        tree.bind("<Button-3>", do_popup)

        display_button3 = tk1.Button(
            second_window, text="Print", command=lambda: i_print(), bg="pale goldenrod")
        display_button3.place(x=650, y=650)
        second_window.mainloop()

    ttk.Separator(label_for_image, orient='horizontal').grid(column=0, row=11, columnspan=6, sticky='ew',
                                                             pady=(30, 0))

    tk1.Button(label_for_image, text="Take input", command=lambda: take_name_input(), bg="pale goldenrod").grid(
        row=12, column=0, pady=30)

    tk1.Button(label_for_image, text="Display result", command=lambda: destroy_root_window(),
               bg="pale goldenrod").grid(row=12, column=1, pady=30)

    root.mainloop()


def take_due_entry1():
    date1 = 0

    root = tk2.Tk()
    root.title("Management")
    root.geometry("1080x700")
    root.minsize(1080, 700)
    root.maxsize(1080, 700)

    image = Image.open("mandirr.jpg")
    image = image.resize((100, 100), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    label_for_image = tk2.Label(root, bg='grey')
    tk2.Label(label_for_image, image=image).grid(row=0, column=4)
    label_for_image.pack()

    app_label = tk2.Label(label_for_image, text=" SHREE AADINATH DIGAMBER JAIN MANDIR ", fg="DarkGoldenrod3", width=40,
                          bg='grey')
    app_label.config(font=("Sylfaen", 30))
    app_label.grid(row=0, columnspan=4, padx=(10, 10), pady=(20, 30))

    app_label1 = tk2.Label(
        label_for_image, text=" Due Amount Entry (Boli) ", fg="Lawn Green", width=20, bg='grey')
    app_label1.config(font=("Sylfaen", 15))
    app_label1.place(x=400, y=95)

    ttk.Separator(label_for_image, orient='horizontal').grid(column=0, row=1, columnspan=6, sticky='ew',
                                                             pady=(0, 50))

    s_label = tk2.Label(label_for_image, text="S.NO.",
                        width=40, anchor='center', font=("Sylfaen", 12))
    s_label.grid(row=1, column=0, pady=(80, 20))
    name_label = tk2.Label(label_for_image, text="NAME",
                           width=40, anchor='center', font=("Sylfaen", 12))
    name_label.grid(row=2, column=0, padx=(10, 0), pady=20)
    amount_label = tk2.Label(label_for_image, text="AMOUNT",
                             width=40, anchor='center', font=("Sylfaen", 12))
    amount_label.grid(row=3, column=0, padx=(10, 0), pady=20)
    phone_label = tk2.Label(label_for_image, text="PHONE",
                            width=40, anchor='center', font=("Sylfaen", 12))
    phone_label.grid(row=4, column=0, padx=(10, 0), pady=20)
    address_label = tk2.Label(
        label_for_image, text="ADDRESS", width=40, anchor='center', font=("Sylfaen", 12))
    address_label.grid(row=5, column=0, padx=(10, 0), pady=20)
    date_label = tk2.Label(label_for_image, text="DATE",
                           width=15, anchor='center', font=("Sylfaen", 10))
    date_label.place(x=830, y=190)
    d_label = tk2.Label(label_for_image, text="PARTICULAR",
                        width=40, anchor='center', font=("Sylfaen", 12))
    d_label.grid(row=7, column=0, padx=(10, 0), pady=20)

    s_entry = tk2.Entry(label_for_image, width=40)
    name_entry = tk2.Entry(label_for_image, width=40)
    amount_entry = tk2.Entry(label_for_image, width=40)
    phone_entry = tk2.Entry(label_for_image, width=40)
    address_entry = tk2.Entry(label_for_image, width=40)
    date_entry = tk2.Entry(label_for_image, text=date1, width=10)
    tk2.Entry(label_for_image, width=40)

    combo_example = ttk.Combobox(label_for_image,
                                 values=[
                                     "prakshal",
                                     "shri g virajman",
                                     "shanti dhara",
                                     "dravya", 'vrat bhandar', 'mandir vyavastha', 'oshadi dan', 'akhand jyoti',
                                     'yantra shri virajan', 'other'])
    combo_example.grid(column=1, row=7)
    combo_example.bind('<<ComboboxSelected>>')
    combo_example.get()

    s_entry.grid(row=1, column=1, pady=(80, 20))
    name_entry.grid(row=2, column=1, pady=20)
    amount_entry.grid(row=3, column=1, pady=20)
    phone_entry.grid(row=4, column=1, pady=20)
    address_entry.grid(row=5, column=1, pady=20)
    date_entry.place(x=950, y=194)

    connection = sqlite3.connect('management.db')

    table__name = "management_table2"
    student__id = "student_id"
    student__name = "student_name"
    amount_t = "student_college"
    student__address = "student_address"
    student__phone = "student_phone"
    date_t = "student_date"
    particular_r = "student_particular"

    connection.execute(" CREATE TABLE IF NOT EXISTS " + table__name + " ( " + student__id +
                       " INTEGER, " + student__name + " TEXT, " + amount_t + " TEXT, " +
                       student__address + " TEXT, " + date_t + " BLOB, " + particular_r + " BLOB, "
                       + student__phone + " INTEGER);")

    def take_name_input():
        sr_no = int(s_entry.get())
        s_entry.delete(0, tk2.END)
        username = name_entry.get()
        name_entry.delete(0, tk2.END)
        amount = amount_entry.get()
        amount_entry.delete(0, tk2.END)
        address = address_entry.get()
        address_entry.delete(0, tk2.END)
        date = date_entry.get()
        date_entry.delete(0, tk2.END)
        particular = combo_example.get()
        combo_example.delete(0, tk2.END)
        phone = int(phone_entry.get())
        phone_entry.delete(0, tk2.END)

        connection.execute("INSERT INTO " + table__name + " ( " + student__id + ", " + student__name + ", " +
                           amount_t + ", " + student__address + ", " + date_t + ", " + particular_r + ", "
                           + student__phone +
                           ") VALUES ( '" + str(sr_no) + "', '"
                           + username + "', '" + amount + "', '" +
                           address + "', '" + date + "', '" + particular + "', '" + str(phone) + "');")
        connection.commit()
        messagebox.showinfo("Success", "Data Saved Successfully.")

    def destroy_root_window():
        root.destroy()
        second_window = tk2.Tk()
        second_window.geometry("1400x700")
        second_window.title("Due Amount Entries")

        app_label3 = tk2.Label(
            second_window, text="SHREE AADINATH DIGAMBER JAIN MANDIR", fg="red", width=40)
        app_label3.config(font=("Sylfaen", 30))

        app_label3.pack()

        tree = ttk.Treeview(second_window, selectmode='browse')
        tree["columns"] = ("one", "two", "three", "four",
                           "five", "six", "seven")
        tree.column("#0", width=0, minwidth=0, stretch=tk2.NO)

        tree.heading("one", text="SR.NO.")
        tree.heading("two", text="Date")
        tree.heading("three", text="Name")
        tree.heading("four", text="Amount")
        tree.heading("five", text="Address")
        tree.heading("six", text="Particular")
        tree.heading("seven", text="Phone")

        cursor = connection.execute("SELECT * FROM " + table__name + " ;")
        i = 1

        for row in cursor:
            tree.insert('', i,
                        values=(row[0], row[4], row[1],
                                row[2], row[3], row[5], row[6]))
            i = i + 1
        tree.pack(side="left")

        def i_print():
            pri = []
            for line in tree.get_children():
                pr = tree.item(line)['values']
                pri += [pr]
            template = ["SR.NO.", "Date", "Name",
                        "Amount", "Address", "Particular", "Phone"]
            print_t = tabulate(pri, template)
            with open("temp.txt", "w") as f:
                f.write(print_t)
            os.startfile("temp.txt", "print")

        def delete_entry():
            selected_item = tree.selection()[0]
            values = (tree.item(selected_item)['values'])
            j = values[0]
            query = F"DELETE FROM {table__name} WHERE {student__id} = {j};"
            connection.execute(query)
            connection.commit()
            tree.delete(selected_item)

        m = Menu(second_window, tearoff=0)
        m.add_command(label="Delete", command=delete_entry)

        def do_popup(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        tree.bind("<Button-3>", do_popup)

        display_button3 = tk2.Button(
            second_window, text="Print", command=lambda: i_print(), bg="pale goldenrod")
        display_button3.place(x=650, y=650)
        second_window.mainloop()

    ttk.Separator(label_for_image, orient='horizontal').grid(column=0, row=11, columnspan=6, sticky='ew',
                                                             pady=(30, 0))

    tk2.Button(label_for_image, text="Take input", command=lambda: take_name_input(), bg="pale goldenrod").grid(
        row=12, column=0, pady=30)

    tk2.Button(label_for_image, text="Display result", command=lambda: destroy_root_window(),
               bg="pale goldenrod").grid(row=12, column=1, pady=30)

    root.mainloop()


def take_entry():
    root1.destroy()
    take_entry1()


def take_due_entry():
    root1.destroy()
    take_due_entry1()


button = tk.Button(text="RECIEPT ENTRY", command=lambda: take_entry(), height=7, width=40, bg='LightSteelBlue3',
                   fg='Black', font=10)
button.grid(row=3, column=0, padx=(100, 10))

button = tk.Button(text="DUE AMOUNT ENTRY (BOLI)", command=lambda: take_due_entry(), height=7, width=40,
                   bg='LightSteelBlue3',
                   fg='Black', font=10)
button.grid(row=5, column=0, padx=(100, 10))

root1.mainloop()
