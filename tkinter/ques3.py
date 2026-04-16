import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# COLORS
BG_DARK = "#0D1B2A"
BG_CARD = "#1B2E45"
BG_SIDEBAR = "#111F30"
TEXT = "white"
ACCENT = "#2DD4BF"

# ================= LOGIN ================= #
class CalmPulseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calm Pulse")
        self.root.geometry("1200x700")
        self.root.configure(bg=BG_DARK)

        self.show_login()

    def show_login(self):
        for w in self.root.winfo_children():
            w.destroy()

        frame = tk.Frame(self.root, bg=BG_DARK)
        frame.pack(expand=True)

        tk.Label(frame, text="◉", font=("Arial", 40), fg=ACCENT, bg=BG_DARK).pack()
        tk.Label(frame, text="Calm Pulse", font=("Arial", 28, "bold"), fg=TEXT, bg=BG_DARK).pack()
        tk.Label(frame, text="Your Personal Stress Management Companion",
                 fg="lightgray", bg=BG_DARK).pack(pady=10)

        self.email = tk.Entry(frame, width=30)
        self.email.pack(pady=5)

        self.password = tk.Entry(frame, show="*", width=30)
        self.password.pack(pady=5)

        # Sign In Button
        tk.Button(frame, text="Sign In", bg=ACCENT, fg="black",
                  command=self.login).pack(pady=10)

        # -------- OR Divider -------- #
        divider = tk.Frame(frame, bg=BG_DARK)
        divider.pack(fill="x", pady=10)

        tk.Frame(divider, bg="gray", height=1, width=100).pack(side="left", padx=10, pady=7)
        tk.Label(divider, text="OR", fg="gray", bg=BG_DARK).pack(side="left")
        tk.Frame(divider, bg="gray", height=1, width=100).pack(side="left", padx=10, pady=7)

        # Google Button
        google_btn = tk.Button(frame, text="🔵 Sign in with Google",
                               bg="#1f2937", fg="white",
                               font=("Arial", 10, "bold"),
                               width=25,
                               command=self.show_main)
        google_btn.pack(pady=5)

        google_btn.bind("<Enter>", lambda e: google_btn.config(bg="#374151"))
        google_btn.bind("<Leave>", lambda e: google_btn.config(bg="#1f2937"))

        # Microsoft Button
        ms_btn = tk.Button(frame, text="🟦 Sign in with Microsoft",
                           bg="#1f2937", fg="white",
                           font=("Arial", 10, "bold"),
                           width=25,
                           command=self.show_main)
        ms_btn.pack(pady=5)

        ms_btn.bind("<Enter>", lambda e: ms_btn.config(bg="#374151"))
        ms_btn.bind("<Leave>", lambda e: ms_btn.config(bg="#1f2937"))

        # Skip Login
        tk.Button(frame, text="Skip Login", command=self.show_main).pack(pady=10)

    def login(self):
        if self.email.get() and self.password.get():
            self.show_main()
        else:
            messagebox.showerror("Error", "Enter details")

    # ================= MAIN ================= #
    def show_main(self):
        for w in self.root.winfo_children():
            w.destroy()

        # Sidebar
        sidebar = tk.Frame(self.root, bg=BG_SIDEBAR, width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="Calm Pulse", fg="white",
                 bg=BG_SIDEBAR, font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(sidebar, text="Dashboard", bg=BG_SIDEBAR, fg="white",
                  command=self.show_dashboard).pack(fill="x")

        tk.Button(sidebar, text="AI Chat", bg=BG_SIDEBAR, fg="white",
                  command=self.toggle_chat).pack(fill="x")

        # Content
        self.content = tk.Frame(self.root, bg=BG_DARK)
        self.content.pack(side="left", fill="both", expand=True)

        # Chat Panel
        self.chat_frame = tk.Frame(self.root, bg="#0f172a", width=300)

        self.chat_box = tk.Text(self.chat_frame, bg="#020617", fg="white")
        self.chat_box.pack(fill="both", expand=True)

        self.chat_entry = tk.Entry(self.chat_frame)
        self.chat_entry.pack(fill="x")

        tk.Button(self.chat_frame, text="Send",
                  command=self.send_msg).pack()

        self.chat_visible = False

    # ================= DASHBOARD ================= #
    def show_dashboard(self):
        for w in self.content.winfo_children():
            w.destroy()

        tk.Label(self.content, text="Dashboard", fg="white",
                 bg=BG_DARK, font=("Arial", 20, "bold")).pack(anchor="w", padx=20)

        # Cards
        card_frame = tk.Frame(self.content, bg=BG_DARK)
        card_frame.pack(pady=10)

        def card(title, value, color):
            f = tk.Frame(card_frame, bg=BG_CARD, width=200, height=100)
            f.pack(side="left", padx=10)
            f.pack_propagate(False)

            tk.Label(f, text=title, fg="gray", bg=BG_CARD).pack()
            tk.Label(f, text=value, fg=color,
                     bg=BG_CARD, font=("Arial", 18, "bold")).pack()

        card("🔥 Stress", "62/100", "red")
        card("😊 Mood", "7/10", "green")
        card("⏱ Focus", "4.5/10", "cyan")
        card("😴 Sleep", "7.2h", "yellow")

        # Weekly Graph
        fig, ax = plt.subplots(figsize=(5, 2))
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        values = [5, 6, 7, 8, 6, 7, 9]
        ax.bar(days, values, color="#38BDF8")

        canvas = FigureCanvasTkAgg(fig, master=self.content)
        canvas.get_tk_widget().pack()

        # Doughnut Chart
        fig2, ax2 = plt.subplots()
        vals = [40, 35, 25]
        ax2.pie(vals, colors=["green", "yellow", "red"],
                wedgeprops=dict(width=0.4))
        ax2.text(0, 0, "62%", ha="center", fontsize=16)

        canvas2 = FigureCanvasTkAgg(fig2, master=self.content)
        canvas2.get_tk_widget().pack()

    # ================= CHAT ================= #
    def toggle_chat(self):
        if not self.chat_visible:
            self.chat_frame.pack(side="right", fill="y")
            self.chat_visible = True
        else:
            self.chat_frame.pack_forget()
            self.chat_visible = False

    def send_msg(self):
        msg = self.chat_entry.get()
        if not msg:
            return

        self.chat_box.insert("end", "You: " + msg + "\n")
        self.chat_box.insert("end", "AI: Tell me more about that.\n\n")
        self.chat_entry.delete(0, "end")


# RUN
root = tk.Tk()
app = CalmPulseApp(root)
root.mainloop()