import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

# ---------------- LOAD DATA ----------------
def load_data():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        messagebox.showinfo("Success", "Dataset Loaded Successfully")

# ---------------- CLEAR FRAME ----------------
def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

# ---------------- VIEW DATA ----------------
def view_data():
    if df.empty:
        messagebox.showerror("Error", "Load dataset first")
        return

    clear_frame()

    title = tk.Label(content_frame, text="📊 Death Records Table", font=("Arial", 18, "bold"), bg="#ecf0f1")
    title.pack(pady=10)

    tree = ttk.Treeview(content_frame)
    tree.pack(fill="both", expand=True)

    tree["column"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    for i in df.index:
        tree.insert("", "end", values=list(df.loc[i]))

# ---------------- ADD RECORD ----------------
def add_record():
    if df.empty:
        messagebox.showerror("Error", "Load dataset first")
        return

    clear_frame()

    tk.Label(content_frame, text="➕ Add New Record", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

    form_frame = tk.Frame(content_frame, bg="#ecf0f1")
    form_frame.pack()

    entries = []

    for i, col in enumerate(df.columns):
        tk.Label(form_frame, text=col, bg="#ecf0f1").grid(row=i, column=0, padx=10, pady=5)
        e = tk.Entry(form_frame)
        e.grid(row=i, column=1, padx=10, pady=5)
        entries.append(e)

    def save():
        global df
        data = [e.get() for e in entries]
        df.loc[len(df)] = data
        messagebox.showinfo("Success", "Record Added")

    tk.Button(content_frame, text="Save", bg="#27ae60", fg="white", width=15, command=save).pack(pady=10)

# ---------------- DELETE ----------------
def delete_record():
    if df.empty:
        messagebox.showerror("Error", "Load dataset first")
        return

    clear_frame()

    tk.Label(content_frame, text="❌ Delete Record", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

    tk.Label(content_frame, text="Enter Row Index:", bg="#ecf0f1").pack()
    entry = tk.Entry(content_frame)
    entry.pack()

    def delete():
        global df
        try:
            idx = int(entry.get())
            df.drop(idx, inplace=True)
            messagebox.showinfo("Deleted", "Record Deleted")
        except:
            messagebox.showerror("Error", "Invalid Index")

    tk.Button(content_frame, text="Delete", bg="#e74c3c", fg="white", command=delete).pack(pady=10)

# ---------------- GRAPH ----------------
def show_graphs():
    if df.empty:
        messagebox.showerror("Error", "Load dataset first")
        return

    clear_frame()

    tk.Label(content_frame, text="📈 Data Visualization", font=("Arial", 18, "bold"), bg="#ecf0f1").pack(pady=10)

    def year_graph():
        if "Year" in df.columns:
            df["Year"].value_counts().sort_index().plot(kind="line", marker='o', title="Year-wise Death Trend")
            plt.xlabel("Year")
            plt.ylabel("Deaths")
            plt.show()

    def gender_graph():
        if "Gender" in df.columns:
            counts = df["Gender"].value_counts()

            # Bar Graph
            counts.plot(kind="bar", title="Male vs Female Deaths")
            plt.xlabel("Gender")
            plt.ylabel("Count")
            plt.show()

            # Pie Chart
            counts.plot(kind="pie", autopct='%1.1f%%', title="Gender Ratio")
            plt.show()

    tk.Button(content_frame, text="📊 Year-wise Graph", width=20, bg="#3498db", fg="white", command=year_graph).pack(pady=5)
    tk.Button(content_frame, text="👨‍🦱 Male vs Female Graph", width=20, bg="#9b59b6", fg="white", command=gender_graph).pack(pady=5)

# ---------------- DASHBOARD ----------------
def show_dashboard():
    clear_frame()

    tk.Label(content_frame, text="🏠 Dashboard", font=("Arial", 20, "bold"), bg="#ecf0f1").pack(pady=20)

    tk.Label(content_frame, text="Welcome to Death Data Management System", font=("Arial", 14), bg="#ecf0f1").pack(pady=10)

    tk.Label(content_frame, text="Use the menu to analyze and manage data", bg="#ecf0f1").pack()

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Death Data System")
root.geometry("1000x550")
root.configure(bg="#ecf0f1")

# Sidebar
sidebar = tk.Frame(root, bg="#2c3e50", width=220)
sidebar.pack(side="left", fill="y")

# Content
content_frame = tk.Frame(root, bg="#ecf0f1")
content_frame.pack(side="right", expand=True, fill="both")

# Header
header = tk.Frame(root, bg="#1abc9c", height=50)
header.place(x=220, y=0, relwidth=1)

tk.Label(header, text="Death Data Analysis System", bg="#1abc9c", fg="white",
         font=("Arial", 16, "bold")).pack(pady=10)

# Sidebar Title
tk.Label(sidebar, text="MENU", bg="#2c3e50", fg="white", font=("Arial", 18)).pack(pady=20)

# Button Style
def create_btn(text, cmd):
    return tk.Button(sidebar, text=text, command=cmd,
                     bg="#34495e", fg="white", width=22, height=2,
                     bd=0, activebackground="#1abc9c")

create_btn("🏠 Dashboard", show_dashboard).pack(pady=5)
create_btn("📂 Load Dataset", load_data).pack(pady=5)
create_btn("📊 View Data", view_data).pack(pady=5)
create_btn("➕ Add Record", add_record).pack(pady=5)
create_btn("❌ Delete Record", delete_record).pack(pady=5)
create_btn("📈 Graphs", show_graphs).pack(pady=5)
create_btn("🚪 Exit", root.quit).pack(pady=20)

show_dashboard()

root.mainloop()