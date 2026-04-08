import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

# ---------------- TERMS WINDOW ----------------
def open_terms():
    terms_win = tk.Toplevel(root)
    terms_win.title("Terms & Conditions")
    terms_win.geometry("600x400")
    terms_win.configure(bg="white")

    tk.Label(terms_win, text="Terms & Conditions",
             font=("Arial", 18, "bold"), bg="white").pack(pady=10)

    terms_text = """
• This system is for educational use only
• Do not misuse or manipulate data
• Accuracy depends on dataset
• Unauthorized sharing is prohibited
• Prototype system only

Click Accept to continue.
"""
    tk.Label(terms_win, text=terms_text, bg="white",
             justify="left").pack(padx=20)

    def accept():
        terms_win.destroy()

    def reject():
        root.destroy()

    tk.Button(terms_win, text="Accept", bg="green", fg="white",
              width=15, command=accept).pack(pady=10)

    tk.Button(terms_win, text="Reject", bg="red", fg="white",
              width=15, command=reject).pack()

# ---------------- LOAD DATA ----------------
def load_data():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if file_path:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        df = df.fillna(0)
        messagebox.showinfo("Success", "Dataset Loaded Successfully")

# ---------------- CLEAR ----------------
def clear():
    for widget in content_frame.winfo_children():
        widget.destroy()

# ---------------- DASHBOARD ----------------
def dashboard():
    clear()

    tk.Label(content_frame, text="📊 Government Death Records Dashboard",
             font=("Arial", 20, "bold"), bg="#ffffff").pack(pady=20)

    if df.empty:
        tk.Label(content_frame, text="Load dataset to view analysis",
                 bg="#ffffff").pack()
        return

    total = df["DeathRegCount"].sum()
    male = df["DeathRegMale"].sum()
    female = df["DeathRegFemale"].sum()

    tk.Label(content_frame, text=f"Total Deaths: {int(total)}", bg="#ffffff").pack()
    tk.Label(content_frame, text=f"Male Deaths: {int(male)}", bg="#ffffff").pack()
    tk.Label(content_frame, text=f"Female Deaths: {int(female)}", bg="#ffffff").pack()

# ---------------- VIEW DATA WITH FILTER ----------------
def view_data():
    if df.empty:
        messagebox.showerror("Error", "Load dataset first")
        return

    clear()

    tk.Label(content_frame, text="📋 Filtered Death Records",
             font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)

    year_col = None
    zone_col = None

    for col in df.columns:
        if "year" in col.lower():
            year_col = col
        if "zone" in col.lower():
            zone_col = col

    filter_frame = tk.Frame(content_frame, bg="#ffffff")
    filter_frame.pack(pady=10)

    # Year dropdown
    tk.Label(filter_frame, text="Year:", bg="#ffffff").grid(row=0, column=0, padx=5)
    years = ["All"] + (sorted(df[year_col].astype(str).unique()) if year_col else [])
    year_var = tk.StringVar(value="All")
    year_menu = ttk.Combobox(filter_frame, textvariable=year_var, values=years, state="readonly")
    year_menu.grid(row=0, column=1, padx=5)

    # Zone dropdown
    tk.Label(filter_frame, text="Zone:", bg="#ffffff").grid(row=0, column=2, padx=5)
    zones = ["All"] + (sorted(df[zone_col].astype(str).unique()) if zone_col else [])
    zone_var = tk.StringVar(value="All")
    zone_menu = ttk.Combobox(filter_frame, textvariable=zone_var, values=zones, state="readonly")
    zone_menu.grid(row=0, column=3, padx=5)

    table_frame = tk.Frame(content_frame)
    table_frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(table_frame)
    tree.pack(side="left", fill="both", expand=True)

    ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview).pack(side="right", fill="y")

    def update_table():
        for row in tree.get_children():
            tree.delete(row)

        filtered_df = df.copy()

        if year_var.get() != "All" and year_col:
            filtered_df = filtered_df[filtered_df[year_col].astype(str) == year_var.get()]

        if zone_var.get() != "All" and zone_col:
            filtered_df = filtered_df[filtered_df[zone_col].astype(str) == zone_var.get()]

        tree["columns"] = list(filtered_df.columns)
        tree["show"] = "headings"

        for col in filtered_df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=90, anchor="center")

        for i in filtered_df.index:
            tree.insert("", "end", values=list(filtered_df.loc[i]))

    tk.Button(filter_frame, text="Apply", bg="#3498db", fg="white",
              command=update_table).grid(row=0, column=4, padx=10)

    update_table()

# ---------------- GRAPHS ----------------
def graphs():
    if df.empty:
        messagebox.showerror("Error", "Load dataset first")
        return

    # Convert Year
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors='coerce')

    # -------- Year-wise Gender --------
    if all(col in df.columns for col in ["Year", "DeathRegMale", "DeathRegFemale"]):
        data = df.groupby("Year")[["DeathRegMale", "DeathRegFemale"]].sum()

        plt.figure()
        data.plot(marker='o', linewidth=2, color=["#00b894", "#d63031"])
        plt.title("Year-wise Male vs Female Death Registration")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    # -------- Registration vs Certificate --------
    if all(col in df.columns for col in ["Year", "DeathRegCount", "CertiIssueCount"]):
        data = df.groupby("Year")[["DeathRegCount", "CertiIssueCount"]].sum()

        plt.figure()
        data.plot(marker='o', linewidth=2, color=["#0984e3", "#e17055"])
        plt.title("Registration vs Certificate")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    # -------- HEATMAP (ZONE-WISE MAPPING) --------
    zone_col = None
    for col in df.columns:
        if "zone" in col.lower():
            zone_col = col
            break

    if zone_col and "Year" in df.columns and "DeathRegCount" in df.columns:
        pivot = df.pivot_table(values="DeathRegCount",
                               index="Year",
                               columns=zone_col,
                               aggfunc="sum",
                               fill_value=0)

        plt.figure(figsize=(10, 6))
        plt.imshow(pivot, aspect='auto')

        plt.colorbar(label="Deaths")
        plt.title("Zone-wise Heatmap (Year vs Zone)")
        plt.xlabel("Zone")
        plt.ylabel("Year")

        plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=45)
        plt.yticks(range(len(pivot.index)), pivot.index)

        plt.tight_layout()
        plt.show()

# ---------------- HELP ----------------
def help_section():
    clear()

    tk.Label(content_frame, text="Help & Support",
             font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=20)

    help_text = """
1. Load CSV dataset
2. View records
3. Analyze graphs
4. Dashboard shows summary

Support:
Email: support@smc.gov.in
"""
    tk.Label(content_frame, text=help_text, bg="#ffffff",
             justify="left").pack()


# ---------------- MAIN ----------------
root = tk.Tk()
root.title("Government Death Registration System")
root.geometry("1100x600")

# Background
bg_image = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\surat-municipal-corporation.jpg")
bg_image = bg_image.resize((1100, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo
bg_label.lower()

# Header
header = tk.Frame(root, bg="#003366", height=100)
header.pack(fill="x")
header.pack_propagate(False)

inner = tk.Frame(header, bg="#003366")
inner.pack(expand=True)

try:
    logo = Image.open(r"C:\Users\Deepa\OneDrive\Desktop\python lab\tkinter\R.png")
    logo = logo.resize((70, 70))
    logo_photo = ImageTk.PhotoImage(logo)

    tk.Label(inner, image=logo_photo, bg="#003366").pack(side="left", padx=15)
except:
    pass

text_frame = tk.Frame(inner, bg="#003366")
text_frame.pack(side="left")

tk.Label(text_frame, text="SURAT MUNICIPAL CORPORATION",
         bg="#003366", fg="white", font=("Arial", 20, "bold")).pack(anchor="w")

tk.Label(text_frame, text="Death Registration System",
         bg="#003366", fg="white").pack(anchor="w")

# Sidebar
sidebar = tk.Frame(root, bg="#f0f0f0", width=200)
sidebar.pack(side="left", fill="y")

content_frame = tk.Frame(root, bg="#ffffff")
content_frame.pack(side="right", expand=True, fill="both")

def btn(text, cmd):
    return tk.Button(sidebar, text=text, command=cmd,
                     width=25, height=2, bg="#e6e6e6")

tk.Label(sidebar, text="MENU", bg="#f0f0f0",
         font=("Arial", 16)).pack(pady=10)

btn("Dashboard", dashboard).pack(pady=5)
btn("Load Data", load_data).pack(pady=5)
btn("View Data", view_data).pack(pady=5)
btn("Graphs", graphs).pack(pady=5)
btn("Help", help_section).pack(pady=5)
btn("Exit", root.quit).pack(pady=20)

# Show terms first
root.after(200, open_terms)

root.mainloop()