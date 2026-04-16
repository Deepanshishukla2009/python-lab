import tkinter as tk
from tkinter import messagebox

class CalmPulseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calm Pulse")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f5f7fa")

        self.show_login()

    # ---------------- LOGIN ---------------- #
    def show_login(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg="#f5f7fa")
        frame.pack(expand=True)

        tk.Label(frame, text="Calm Pulse", font=("Arial", 28, "bold"), bg="#f5f7fa").pack(pady=10)
        tk.Label(frame, text="Your Personal Stress Management Companion", font=("Arial", 14), bg="#f5f7fa").pack(pady=5)

        tk.Label(frame, text="Email", bg="#f5f7fa").pack()
        self.email_entry = tk.Entry(frame)
        self.email_entry.pack()

        tk.Label(frame, text="Password", bg="#f5f7fa").pack()
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.pack()

        tk.Button(frame, text="Sign In", bg="#28a745", fg="white", command=self.login).pack(pady=10)
        tk.Button(frame, text="Sign in with Google", width=25, command=self.show_dashboard).pack(pady=10)
        tk.Button(frame, text="Sign in with Microsoft", width=25, command=self.show_dashboard).pack(pady=10)
        tk.Button(frame, text="Skip Login", command=self.show_dashboard).pack()

    def login(self):
        if self.email_entry.get() and self.password_entry.get():
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Enter details")

    # ---------------- DASHBOARD ---------------- #
    def show_dashboard(self):
        self.clear_window()

        top = tk.Frame(self.root, bg="#4a90e2")
        top.pack(fill="x")

        tk.Label(top, text="Calm Pulse", fg="white", bg="#4a90e2",
                 font=("Arial", 16, "bold")).pack(side="left", padx=10)

        nav = tk.Frame(top, bg="#4a90e2")
        nav.pack(side="left", padx=20)

        tk.Button(nav, text="Dashboard", command=self.show_dashboard_content).pack(side="left", padx=5)
        tk.Button(nav, text="Games").pack(side="left", padx=5)
        tk.Button(nav, text="Camera").pack(side="left", padx=5)
        tk.Button(nav, text="Stress Check").pack(side="left", padx=5)
        tk.Button(nav, text="explore").pack(side="left", padx=5)

        tk.Button(top, text="AI Chat", command=self.toggle_chat).pack(side="right", padx=10)

        main = tk.Frame(self.root, bg="white")
        main.pack(expand=True, fill="both")

        self.left_frame = tk.Frame(main, bg="white")
        self.left_frame.pack(side="left", fill="both", expand=True)

        # ❌ NO AUTO LOAD HERE (IMPORTANT FIX)

        # Chat Panel
        self.chat_frame = tk.Frame(main, bg="#eef2f7", width=300)
        self.chat_display = tk.Text(self.chat_frame, state="disabled")
        self.chat_display.pack(expand=True, fill="both")

        self.chat_entry = tk.Entry(self.chat_frame)
        self.chat_entry.pack(fill="x")

        tk.Button(self.chat_frame, text="Send", command=self.send_message).pack()

        self.chat_visible = False

    # ---------------- DASHBOARD CONTENT ---------------- #
    def show_dashboard_content(self):
        for w in self.left_frame.winfo_children():
            w.destroy()

        tk.Label(self.left_frame, text="Dashboard",
                 font=("Arial", 20, "bold"), bg="white").pack(anchor="w", padx=20, pady=10)

        # -------- TOP CARDS -------- #
        cards = tk.Frame(self.left_frame, bg="white")
        cards.pack(pady=10)

        def card(text, val):
            f = tk.Frame(cards, bg="#f0f4f8", width=200, height=100)
            f.pack_propagate(False)
            tk.Label(f, text=text, font=("Arial", 12, "bold"), bg="#f0f4f8").pack()
            tk.Label(f, text=val, font=("Arial", 14), bg="#f0f4f8").pack()
            return f

        card("🔥 Stress", "62/100").pack(side="left", padx=10)
        card("😊 Mood", "7/10").pack(side="left", padx=10)
        card("⏱ Focus", "4.5/10").pack(side="left", padx=10)
        card("😴 Sleep", "7.2 hrs").pack(side="left", padx=10)

        # -------- GRAPH -------- #
        tk.Label(self.left_frame, text="😊 Weekly Happiness",
                 font=("Arial", 14, "bold"), bg="white").pack(anchor="w", padx=20)

        canvas = tk.Canvas(self.left_frame, width=600, height=200, bg="white")
        canvas.pack(pady=10)

        values = [5, 6, 7, 8, 6, 7, 9]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for i, v in enumerate(values):
            x = i * 70 + 40
            canvas.create_line(x, 180, x, 180 - v * 15, width=10)
            canvas.create_text(x, 190, text=days[i])

        # -------- EMOTIONAL BARS -------- #
        tk.Label(self.left_frame, text="Emotional Breakdown",
                 font=("Arial", 14, "bold"), bg="white").pack(anchor="w", padx=20)

        moods = [("😊 Happy", 40), ("😢 Sad", 20), ("🔥 Stress", 25), ("😌 Calm", 10), ("😡 Angry", 5)]

        for m, v in moods:
            f = tk.Frame(self.left_frame, bg="white")
            f.pack(anchor="w", padx=20, pady=3)

            tk.Label(f, text=m, width=12, anchor="w", bg="white").pack(side="left")

            c = tk.Canvas(f, width=200, height=20, bg="#ddd", highlightthickness=0)
            c.pack(side="left")

            fill = v * 2
            c.create_rectangle(0, 0, fill, 20, fill="blue")
            c.create_polygon(fill, 0, fill+10, 10, fill, 20, fill="blue")

            tk.Label(f, text=f"{v}%", bg="white").pack(side="left")

        # -------- STRESS CIRCLE -------- #
        stress_frame = tk.Frame(self.left_frame, bg="white")
        stress_frame.pack(pady=20)

        tk.Label(stress_frame, text="Stress Level",
         font=("Arial", 14, "bold"), bg="white").pack()

        circle = tk.Canvas(stress_frame, width=150, height=150, bg="white", highlightthickness=0)
        circle.pack()

       # Outer circle
        circle.create_oval(10, 10, 140, 140, outline="#ddd", width=10)

       # Filled arc (62%)
        circle.create_arc(10, 10, 140, 140, start=90, extent=-223, fill="#ff4d4d", outline="")

       # Center text
        circle.create_text(75, 75, text="62%", font=("Arial", 14, "bold"))            

    # ---------------- CHAT ---------------- #
    def toggle_chat(self):
        if not self.chat_visible:
            self.chat_frame.pack(side="right", fill="y")
            self.chat_visible = True
        else:
            self.chat_frame.pack_forget()
            self.chat_visible = False

    def send_message(self):
        msg = self.chat_entry.get()
        if not msg:
            return
        self.chat_display.config(state="normal")
        self.chat_display.insert("end", "You: " + msg + "\n")
        self.chat_display.insert("end", "AI: Tell me more...\n\n")
        self.chat_display.config(state="disabled")
        self.chat_entry.delete(0, "end")

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()


# RUN
root = tk.Tk()
app = CalmPulseApp(root)
root.mainloop()