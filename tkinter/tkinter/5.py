import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from datetime import datetime

# ================= LOGIN FUNCTION =================
def login():
    if username_entry.get() == "admin" and password_entry.get() == "1234":
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# ================= DASHBOARD =================
def open_dashboard():
    dash = tk.Tk()
    dash.title("Student Management System")
    dash.geometry("900x600")

    # ---------- TOP FRAME (FIX GAP ISSUE) ----------
    top_frame = tk.Frame(dash, bg="white", height=80)
    top_frame.pack(fill="x")
    top_frame.pack_propagate(False)

    # ---------- DATE & TIME ----------
    dt_frame = tk.Frame(top_frame, bg="white")
    dt_frame.pack(anchor="nw", padx=10, pady=2)

    tk.Label(dt_frame, text="Date:", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0)
    date_value = tk.Label(dt_frame, bg="white")
    date_value.grid(row=0, column=1)

    tk.Label(dt_frame, text="Time:", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0)
    time_value = tk.Label(dt_frame, bg="white")
    time_value.grid(row=1, column=1)

    def update_time():
        now = datetime.now()
        date_value.config(text=now.strftime("%d-%m-%Y"))
        time_value.config(text=now.strftime("%H:%M:%S"))
        dash.after(1000, update_time)

    update_time()

    # ---------- BOY IMAGE ----------
    try:
        img = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\Screenshot 2026-03-28 150520.png")
        img = img.resize((60, 60))
        photo = ImageTk.PhotoImage(img)

        lbl = tk.Label(top_frame, image=photo, bg="white")
        lbl.image = photo
        lbl.pack(anchor="nw", padx=10)
    except:
        pass

    # ---------- LEFT MENU ----------
    menu_frame = tk.Frame(dash, bg="lightgray", width=200)
    menu_frame.pack(side="left", fill="y")

    # ---------- MAIN AREA ----------
    main_frame = tk.Frame(dash, bg="white")
    main_frame.pack(side="right", fill="both", expand=True)

    # ---------- HEADING (NO GAP) ----------
    tk.Label(main_frame, text="Student Management System",
             font=("Arial", 18, "bold"), bg="white").pack(pady=0)

    # ---------- TABLE ----------
    columns = ("ID", "Name", "Level", "Number")
    tree = ttk.Treeview(main_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    tree.pack(fill="both", expand=True, padx=20, pady=20)

    # ---------- ADD STUDENT WINDOW ----------
    def add_student():
        win = tk.Toplevel(dash)
        win.title("Add Student")
        win.geometry("400x400")

        tk.Label(win, text="Add Student", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=2, pady=10
        )

        labels = ["ID", "Name", "Level", "Number", "Address", "Gender", "Email", "GPA"]
        entries = {}

        for i, text in enumerate(labels):
            tk.Label(win, text=text).grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            if text == "Gender":
                entry = ttk.Combobox(win, values=["Male", "Female", "Other"])
            else:
                entry = tk.Entry(win)

            entry.grid(row=i+1, column=1, padx=10, pady=5)
            entries[text] = entry

        def save():
            data = {k: v.get() for k, v in entries.items()}
            messagebox.showinfo("Saved", "Student Added!")
            print(data)
            win.destroy()

        tk.Button(win, text="Submit", command=save, bg="green", fg="white").grid(
            row=len(labels)+1, column=0, columnspan=2, pady=10
        )

    # ---------- MENU BUTTONS ----------
    def dummy():
        messagebox.showinfo("Info", "Not implemented")

    buttons = [
        ("Add Student", add_student),
        ("Search Student", dummy),
        ("Delete Student", dummy),
        ("Update Student", dummy),
        ("Show Student", dummy),
        ("Export Student", dummy),
        ("Exit", dash.destroy)
    ]

    for text, cmd in buttons:
        tk.Button(menu_frame, text=text, width=20, command=cmd).pack(pady=5)

    dash.mainloop()


# ================= LOGIN WINDOW =================
root = tk.Tk()
root.title("Login Page")
root.geometry("500x400")
root.configure(bg="white")

tk.Label(root, text="Login Page", font=("Arial", 16, "bold"),
         bg="white").place(x=10, y=10)

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------- IMAGE ----------
try:
    img = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\WhatsApp Image 2026-03-28 at 2.45.11 PM.jpeg")
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(img)

    lbl = tk.Label(frame, image=photo, bg="white")
    lbl.image = photo
    lbl.grid(row=0, column=0, columnspan=3, pady=10)
except:
    pass

# ---------- USER ICON ----------
try:
    u = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\Screenshot 2026-03-28 145645.png").resize((20, 20))
    user_img = ImageTk.PhotoImage(u)
    tk.Label(frame, image=user_img, bg="white").grid(row=1, column=0)
except:
    pass

tk.Label(frame, text="Username", bg="white").grid(row=1, column=1)
username_entry = tk.Entry(frame)
username_entry.grid(row=1, column=2)

# ---------- PASS ICON ----------
try:
    p = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\Screenshot 2026-03-28 145802.png").resize((20, 20))
    pass_img = ImageTk.PhotoImage(p)
    tk.Label(frame, image=pass_img, bg="white").grid(row=2, column=0)
except:
    pass

tk.Label(frame, text="Password", bg="white").grid(row=2, column=1)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=2, column=2)

tk.Button(frame, text="Login", command=login, bg="green", fg="white").grid(
    row=3, column=0, columnspan=3, pady=10
)

root.mainloop()