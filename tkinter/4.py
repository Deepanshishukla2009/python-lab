import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

# ---------- LOGIN FUNCTION ----------
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# ---------- DASHBOARD ----------
def open_dashboard():
    dash = tk.Tk()
    dash.title("Student Management System")
    dash.geometry("700x500")

    # Date & Time
    time_label = tk.Label(dash, font=("Arial", 12))
    time_label.place(x=10, y=10)

    def update_time():
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        time_label.config(text=now)
        time_label.after(1000, update_time)

    update_time()

    tk.Label(
        dash,
        text="Student Management System",
        font=("Arial", 20, "bold")
    ).pack(pady=50)

    dash.mainloop()


# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Login Page")
root.geometry("500x400")
root.configure(bg="white")

tk.Label(root, text="Login Page", font=("Arial", 16, "bold"),
         bg="white").place(x=10, y=10)

# ---------- FRAME ----------
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------- TOP IMAGE ----------
try:
    img = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\WhatsApp Image 2026-03-28 at 2.45.11 PM.jpeg")
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(img)

    tk.Label(frame, image=photo, bg="white").grid(row=0, column=0, columnspan=3, pady=10)
except:
    pass

# ---------- USER ICON ----------
try:
    user_icon = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\Screenshot 2026-03-28 145645.png")
    user_icon = user_icon.resize((20, 20))
    user_img = ImageTk.PhotoImage(user_icon)
except:
    user_img = None

# ---------- PASSWORD ICON ----------
try:
    pass_icon = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\Screenshot 2026-03-28 145802.png")
    pass_icon = pass_icon.resize((20, 20))
    pass_img = ImageTk.PhotoImage(pass_icon)
except:
    pass_img = None

# ---------- USERNAME ----------
if user_img:
    tk.Label(frame, image=user_img, bg="white").grid(row=1, column=0, padx=5)

tk.Label(frame, text="Username", bg="white").grid(row=1, column=1, padx=5, pady=5)
username_entry = tk.Entry(frame)
username_entry.grid(row=1, column=2, padx=5, pady=5)

# ---------- PASSWORD ----------
if pass_img:
    tk.Label(frame, image=pass_img, bg="white").grid(row=2, column=0, padx=5)

tk.Label(frame, text="Password", bg="white").grid(row=2, column=1, padx=5, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=2, column=2, padx=5, pady=5)

# ---------- BUTTON ----------
tk.Button(frame, text="Login", command=login, bg="green", fg="white").grid(
    row=3, column=0, columnspan=3, pady=10
)

# ---------- RUN ----------
root.mainloop()