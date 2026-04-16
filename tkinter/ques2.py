import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

# ══════════════════════════════════════════════════
#  COLOR PALETTE
# ══════════════════════════════════════════════════
BG_DARK      = "#0D1B2A"
BG_SIDEBAR   = "#111F30"
BG_CARD      = "#1B2E45"
BG_CARD2     = "#162236"
BG_INPUT     = "#0F1E2E"
ACCENT_MINT  = "#2DD4BF"
ACCENT_CORAL = "#FF6B6B"
ACCENT_SKY   = "#38BDF8"
ACCENT_GOLD  = "#FBBF24"
ACCENT_GREEN = "#34D399"
ACCENT_PURPLE= "#A78BFA"
TEXT_WHITE   = "#F0F9FF"
TEXT_MUTED   = "#8BA5C2"
BORDER_CLR   = "#2A4A6B"
SIDEBAR_W    = 200

# ══════════════════════════════════════════════════
#  MATPLOTLIB THEME
# ══════════════════════════════════════════════════
plt.rcParams.update({
    "figure.facecolor": BG_CARD,
    "axes.facecolor":   BG_CARD,
    "axes.labelcolor":  TEXT_MUTED,
    "axes.edgecolor":   BORDER_CLR,
    "xtick.color":      TEXT_MUTED,
    "ytick.color":      TEXT_MUTED,
    "text.color":       TEXT_WHITE,
    "grid.color":       BORDER_CLR,
    "grid.alpha":       0.35,
    "font.family":      "sans-serif",
})

# ══════════════════════════════════════════════════
#  GLOBALS  (track open canvases for cleanup)
# ══════════════════════════════════════════════════
open_figures = []


# ══════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════
def mk_btn(parent, text, command=None, bg=ACCENT_MINT, fg=BG_DARK,
           font_size=11, padx=0, pady=10, width=None, fill=None):
    kw = dict(text=text, command=command, bg=bg, fg=fg,
              activebackground=ACCENT_SKY, activeforeground=BG_DARK,
              font=("Helvetica", font_size, "bold"),
              pady=pady, bd=0, relief="flat", cursor="hand2",
              highlightthickness=0)
    if width:
        kw["width"] = width
    btn = tk.Button(parent, **kw)
    if fill:
        btn.pack(fill=fill, padx=padx, pady=2)
    btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT_SKY, fg=BG_DARK))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg, fg=fg))
    return btn


def stat_card(parent, title, value, unit, color, row, col):
    card = tk.Frame(parent, bg=BG_CARD, highlightthickness=1,
                    highlightbackground=color)
    card.grid(row=row, column=col, padx=8, pady=8, ipadx=10, ipady=10, sticky="nsew")

    tk.Label(card, text=title, bg=BG_CARD, fg=TEXT_MUTED,
             font=("Helvetica", 9, "bold")).pack(anchor="w", padx=10, pady=(8, 0))

    vf = tk.Frame(card, bg=BG_CARD)
    vf.pack(anchor="w", padx=10, pady=(2, 4))
    tk.Label(vf, text=str(value), bg=BG_CARD, fg=color,
             font=("Helvetica", 28, "bold")).pack(side="left")
    tk.Label(vf, text=unit, bg=BG_CARD, fg=TEXT_MUTED,
             font=("Helvetica", 11)).pack(side="left", padx=3, pady=8)

    bg_bar = tk.Frame(card, bg=BORDER_CLR, height=5)
    bg_bar.pack(fill="x", padx=10, pady=(0, 8))
    bg_bar.pack_propagate(False)
    tk.Frame(bg_bar, bg=color, width=int((value / 100) * 180), height=5).pack(side="left")


def section_title(parent, text):
    tk.Label(parent, text=text, bg=BG_DARK, fg=TEXT_WHITE,
             font=("Helvetica", 12, "bold")).pack(anchor="w", padx=4, pady=(10, 4))


# ══════════════════════════════════════════════════
#  CLEAR MAIN CONTENT AREA
# ══════════════════════════════════════════════════
def clear_content(content_frame):
    global open_figures
    for fig in open_figures:
        plt.close(fig)
    open_figures.clear()
    for w in content_frame.winfo_children():
        w.destroy()


# ══════════════════════════════════════════════════
#  PAGE: DASHBOARD
# ══════════════════════════════════════════════════
def show_dashboard(content_frame, active_btn_ref):
    clear_content(content_frame)
    set_active(active_btn_ref[0], active_btn_ref)

    # ── Header ──────────────────────────────────
    hdr = tk.Frame(content_frame, bg=BG_DARK)
    hdr.pack(fill="x", padx=20, pady=(18, 0))
    tk.Label(hdr, text="Dashboard", bg=BG_DARK, fg=TEXT_WHITE,
             font=("Helvetica", 18, "bold")).pack(side="left")
    tk.Label(hdr, text="Today's wellness overview", bg=BG_DARK,
             fg=TEXT_MUTED, font=("Helvetica", 10)).pack(side="right", pady=4)

    ttk.Separator(content_frame).pack(fill="x", padx=20, pady=10)

    # ── Stat Cards ──────────────────────────────
    cf = tk.Frame(content_frame, bg=BG_DARK)
    cf.pack(fill="x", padx=20)
    for c in range(4):
        cf.columnconfigure(c, weight=1)

    stats = [
        ("Stress Score",  72, "/100", ACCENT_CORAL),
        ("Focus Time",    80, "/100", ACCENT_MINT),
        ("Sleep Quality", 65, "/100", ACCENT_SKY),
        ("Mood Today",    85, "/100", ACCENT_GOLD),
    ]
    for i, (title, val, unit, color) in enumerate(stats):
        stat_card(cf, title, val, unit, color, row=0, col=i)

    # ── ROW 1 charts: Happiness + Emotional ─────
    row1 = tk.Frame(content_frame, bg=BG_DARK)
    row1.pack(fill="x", padx=20, pady=(10, 0))

    # Chart 1 – Weekly Happiness
    lc = tk.Frame(row1, bg=BG_CARD, highlightthickness=1,
                  highlightbackground=BORDER_CLR)
    lc.pack(side="left", fill="both", expand=True, padx=(0, 6))

    fig1, ax1 = plt.subplots(figsize=(5.5, 2.8))
    open_figures.append(fig1)
    days      = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    happiness = [6, 7, 5, 8, 7, 9, 8]
    bclrs     = [ACCENT_MINT if h >= 8 else ACCENT_SKY if h >= 6 else ACCENT_CORAL
                 for h in happiness]
    bars1 = ax1.bar(days, happiness, color=bclrs, width=0.55, zorder=3)
    for bar, h in zip(bars1, happiness):
        ax1.text(bar.get_x() + bar.get_width() / 2, h + 0.15,
                 str(h), ha="center", va="bottom", fontsize=9,
                 color=TEXT_WHITE, fontweight="bold")
    ax1.set_ylim(0, 11)
    ax1.set_title("Weekly Happiness", color=TEXT_WHITE, fontsize=11,
                  fontweight="bold", pad=8)
    ax1.yaxis.set_visible(False)
    ax1.spines[:].set_visible(False)
    ax1.grid(axis="y", zorder=0)
    fig1.tight_layout(pad=1.2)
    FigureCanvasTkAgg(fig1, master=lc).get_tk_widget().pack(
        fill="both", expand=True, padx=4, pady=4)

    # Chart 2 – Emotional Breakdown
    rc = tk.Frame(row1, bg=BG_CARD, highlightthickness=1,
                  highlightbackground=BORDER_CLR)
    rc.pack(side="left", fill="both", expand=True, padx=(6, 0))

    fig2, ax2 = plt.subplots(figsize=(5.2, 2.8))
    open_figures.append(fig2)
    emotions = ["Motivation", "Calm", "Focus", "Mood", "Energy"]
    evals    = [85, 65, 80, 75, 70]
    eclrs    = [ACCENT_GREEN, ACCENT_MINT, ACCENT_SKY, ACCENT_GOLD, ACCENT_CORAL]
    bars2 = ax2.barh(emotions, evals, color=eclrs, height=0.55, zorder=3)
    for bar, v in zip(bars2, evals):
        ax2.text(v + 1, bar.get_y() + bar.get_height() / 2,
                 f"{v}%", va="center", fontsize=8,
                 color=TEXT_WHITE, fontweight="bold")
    ax2.set_xlim(0, 112)
    ax2.set_title("Emotional Breakdown", color=TEXT_WHITE, fontsize=11,
                  fontweight="bold", pad=8)
    ax2.xaxis.set_visible(False)
    ax2.spines[:].set_visible(False)
    ax2.grid(axis="x", zorder=0)
    fig2.tight_layout(pad=1.2)
    FigureCanvasTkAgg(fig2, master=rc).get_tk_widget().pack(
        fill="both", expand=True, padx=4, pady=4)

    # ── ROW 2: Stress Doughnut (prominent) ──────
    row2 = tk.Frame(content_frame, bg=BG_DARK)
    row2.pack(fill="x", padx=20, pady=(10, 10))

    dough_card = tk.Frame(row2, bg=BG_CARD, highlightthickness=1,
                          highlightbackground=BORDER_CLR)
    dough_card.pack(side="left", fill="both", ipadx=10)

    fig3, ax3 = plt.subplots(figsize=(4.2, 3.0))
    open_figures.append(fig3)
    labels3 = ["Low", "Medium", "High"]
    vals3   = [40, 35, 25]
    clrs3   = [ACCENT_GREEN, ACCENT_GOLD, ACCENT_CORAL]
    wedges, texts, autotexts = ax3.pie(
        vals3, labels=labels3, colors=clrs3, autopct="%1.0f%%",
        pctdistance=0.76, startangle=90,
        wedgeprops=dict(width=0.55, edgecolor=BG_CARD, linewidth=3)
    )
    for at in autotexts:
        at.set_fontsize(9); at.set_color(BG_DARK); at.set_fontweight("bold")
    for t in texts:
        t.set_color(TEXT_MUTED); t.set_fontsize(9)
    ax3.text(0, 0.05, "72", ha="center", va="center",
             fontsize=22, color=ACCENT_CORAL, fontweight="bold")
    ax3.text(0, -0.25, "Stress\nIndex", ha="center", va="center",
             fontsize=9, color=TEXT_MUTED)
    ax3.set_title("Stress Level Distribution", color=TEXT_WHITE,
                  fontsize=11, fontweight="bold", pad=10)
    fig3.tight_layout(pad=1.0)
    FigureCanvasTkAgg(fig3, master=dough_card).get_tk_widget().pack(
        fill="both", expand=True, padx=6, pady=6)

    # Legend beside doughnut
    legend_card = tk.Frame(row2, bg=BG_CARD2, highlightthickness=1,
                           highlightbackground=BORDER_CLR)
    legend_card.pack(side="left", fill="both", expand=True, padx=(8, 0))

    tk.Label(legend_card, text="Stress Breakdown",
             bg=BG_CARD2, fg=TEXT_WHITE,
             font=("Helvetica", 11, "bold")).pack(anchor="w", padx=16, pady=(16, 8))

    legend_items = [
        ("Low Stress",    "40%", ACCENT_GREEN,
         "Calm and relaxed. Great state!"),
        ("Medium Stress", "35%", ACCENT_GOLD,
         "Moderate tension. Keep balanced."),
        ("High Stress",   "25%", ACCENT_CORAL,
         "Elevated stress. Try breathing exercises."),
    ]
    for name, pct, color, desc in legend_items:
        row = tk.Frame(legend_card, bg=BG_CARD2)
        row.pack(fill="x", padx=16, pady=6)
        tk.Frame(row, bg=color, width=12, height=12).pack(side="left", pady=3)
        info = tk.Frame(row, bg=BG_CARD2)
        info.pack(side="left", padx=10)
        tk.Label(info, text=f"{name}  {pct}", bg=BG_CARD2, fg=color,
                 font=("Helvetica", 10, "bold")).pack(anchor="w")
        tk.Label(info, text=desc, bg=BG_CARD2, fg=TEXT_MUTED,
                 font=("Helvetica", 8)).pack(anchor="w")

    # Weekly insight
    insight = tk.Frame(legend_card, bg=BORDER_CLR)
    insight.pack(fill="x", padx=16, pady=(16, 12), ipady=10)
    tk.Label(insight, text="💡  Insight", bg=BORDER_CLR, fg=ACCENT_MINT,
             font=("Helvetica", 9, "bold")).pack(anchor="w", padx=10, pady=(6, 2))
    tk.Label(insight,
             text="Your stress peaks mid-week.\nSchedule breaks on Wed & Thu.",
             bg=BORDER_CLR, fg=TEXT_MUTED,
             font=("Helvetica", 9), justify="left").pack(anchor="w", padx=10, pady=(0, 6))

    # ── Footer tip ───────────────────────────────
    tk.Label(content_frame,
             text="✦  Tip: Your mood peaks on weekends. Carry that energy into Monday!",
             bg=BG_DARK, fg=TEXT_MUTED, font=("Helvetica", 9)).pack(pady=(0, 10))


# ══════════════════════════════════════════════════
#  PAGE: RESET / SETTINGS
# ══════════════════════════════════════════════════
def show_reset(content_frame, active_btn_ref):
    clear_content(content_frame)
    set_active(active_btn_ref[1], active_btn_ref)

    hdr = tk.Frame(content_frame, bg=BG_DARK)
    hdr.pack(fill="x", padx=20, pady=(18, 0))
    tk.Label(hdr, text="Reset & Settings", bg=BG_DARK, fg=TEXT_WHITE,
             font=("Helvetica", 18, "bold")).pack(side="left")
    ttk.Separator(content_frame).pack(fill="x", padx=20, pady=10)

    # ── Reset card ──────────────────────────────
    rcard = tk.Frame(content_frame, bg=BG_CARD, highlightthickness=1,
                     highlightbackground=BORDER_CLR)
    rcard.pack(padx=20, pady=10, fill="x")

    tk.Label(rcard, text="⚠  Reset All Data",
             bg=BG_CARD, fg=ACCENT_CORAL,
             font=("Helvetica", 12, "bold")).pack(anchor="w", padx=20, pady=(16, 4))
    tk.Label(rcard,
             text="This will clear all your wellness data, scores, and history.\n"
                  "This action cannot be undone.",
             bg=BG_CARD, fg=TEXT_MUTED,
             font=("Helvetica", 10), justify="left").pack(anchor="w", padx=20, pady=(0, 12))

    def do_reset():
        if messagebox.askyesno("Confirm Reset",
                               "Are you sure you want to reset all data?\nThis cannot be undone."):
            messagebox.showinfo("Reset Complete", "✓  All data has been reset successfully.")

    btn = mk_btn(rcard, "🗑   Reset All Data", command=do_reset,
                 bg=ACCENT_CORAL, fg=TEXT_WHITE, font_size=11, pady=10)
    btn.pack(anchor="w", padx=20, pady=(0, 16))
    btn.bind("<Enter>", lambda e: btn.config(bg="#ff4444"))
    btn.bind("<Leave>", lambda e: btn.config(bg=ACCENT_CORAL))

    # ── Preferences card ────────────────────────
    pcard = tk.Frame(content_frame, bg=BG_CARD, highlightthickness=1,
                     highlightbackground=BORDER_CLR)
    pcard.pack(padx=20, pady=10, fill="x")

    tk.Label(pcard, text="⚙  Preferences",
             bg=BG_CARD, fg=TEXT_WHITE,
             font=("Helvetica", 12, "bold")).pack(anchor="w", padx=20, pady=(16, 8))

    prefs = [
        ("Daily Reminder Notifications", True),
        ("Weekly Summary Email",         False),
        ("Dark Mode",                    True),
        ("Show Stress Alerts",           True),
    ]
    toggle_vars = []
    for label, default in prefs:
        row = tk.Frame(pcard, bg=BG_CARD)
        row.pack(fill="x", padx=20, pady=6)
        tk.Label(row, text=label, bg=BG_CARD, fg=TEXT_WHITE,
                 font=("Helvetica", 10)).pack(side="left")
        var = tk.BooleanVar(value=default)
        toggle_vars.append(var)
        cb = tk.Checkbutton(row, variable=var, bg=BG_CARD,
                            activebackground=BG_CARD,
                            selectcolor=BG_CARD2,
                            fg=ACCENT_MINT, activeforeground=ACCENT_MINT)
        cb.pack(side="right")

    def save_prefs():
        messagebox.showinfo("Saved", "✓  Preferences saved successfully.")

    mk_btn(pcard, "💾  Save Preferences", command=save_prefs,
           bg=ACCENT_MINT, fg=BG_DARK, font_size=11, pady=10,
           fill="x", padx=20).pack(anchor="w", padx=20, pady=(8, 16))


# ══════════════════════════════════════════════════
#  PAGE: PROFILE (placeholder)
# ══════════════════════════════════════════════════
def show_profile(content_frame, active_btn_ref):
    clear_content(content_frame)
    set_active(active_btn_ref[2], active_btn_ref)

    hdr = tk.Frame(content_frame, bg=BG_DARK)
    hdr.pack(fill="x", padx=20, pady=(18, 0))
    tk.Label(hdr, text="My Profile", bg=BG_DARK, fg=TEXT_WHITE,
             font=("Helvetica", 18, "bold")).pack(side="left")
    ttk.Separator(content_frame).pack(fill="x", padx=20, pady=10)

    pcard = tk.Frame(content_frame, bg=BG_CARD, highlightthickness=1,
                     highlightbackground=BORDER_CLR)
    pcard.pack(padx=20, pady=10, fill="x")

    avatar = tk.Label(pcard, text="👤", bg=BG_CARD, font=("Helvetica", 48))
    avatar.pack(pady=(20, 4))
    tk.Label(pcard, text="Demo User", bg=BG_CARD, fg=TEXT_WHITE,
             font=("Helvetica", 14, "bold")).pack()
    tk.Label(pcard, text="demo@calmpulse.io", bg=BG_CARD, fg=TEXT_MUTED,
             font=("Helvetica", 10)).pack(pady=(2, 16))

    fields = [("Name", "Demo User"), ("Email", "demo@calmpulse.io"),
              ("Age", "25"), ("Goal", "Reduce Stress")]
    for lbl, val in fields:
        row = tk.Frame(pcard, bg=BG_CARD)
        row.pack(fill="x", padx=24, pady=4)
        tk.Label(row, text=lbl + ":", bg=BG_CARD, fg=TEXT_MUTED,
                 font=("Helvetica", 9, "bold"), width=10, anchor="w").pack(side="left")
        tk.Label(row, text=val, bg=BG_CARD, fg=TEXT_WHITE,
                 font=("Helvetica", 10)).pack(side="left")

    tk.Label(pcard, bg=BG_CARD, height=1).pack()


# ══════════════════════════════════════════════════
#  SIDEBAR ACTIVE STATE
# ══════════════════════════════════════════════════
def set_active(active_widget, all_btns):
    for btn in all_btns:
        if btn and btn.winfo_exists():
            btn.config(bg=BG_SIDEBAR, fg=TEXT_MUTED)
    if active_widget and active_widget.winfo_exists():
        active_widget.config(bg=ACCENT_MINT, fg=BG_DARK)


# ══════════════════════════════════════════════════
#  BUILD MAIN APP WINDOW (post login)
# ══════════════════════════════════════════════════
def open_main_app():
    root.withdraw()
    app = tk.Toplevel()
    app.title("Calm Pulse")
    app.geometry("1200x780")
    app.configure(bg=BG_DARK)
    app.resizable(True, True)
    app.protocol("WM_DELETE_WINDOW", lambda: (app.destroy(), root.destroy()))

    # ── SIDEBAR ─────────────────────────────────
    sidebar = tk.Frame(app, bg=BG_SIDEBAR, width=SIDEBAR_W)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    # Brand
    brand = tk.Frame(sidebar, bg=BG_SIDEBAR)
    brand.pack(fill="x", pady=(24, 8))
    tk.Label(brand, text="◉", bg=BG_SIDEBAR, fg=ACCENT_MINT,
             font=("Helvetica", 22)).pack()
    tk.Label(brand, text="Calm Pulse", bg=BG_SIDEBAR, fg=TEXT_WHITE,
             font=("Helvetica", 13, "bold")).pack()

    ttk.Separator(sidebar, orient="horizontal").pack(fill="x", padx=12, pady=8)

    # ── CONTENT AREA ────────────────────────────
    content_frame = tk.Frame(app, bg=BG_DARK)
    content_frame.pack(side="left", fill="both", expand=True)

    # Nav buttons (built first so we can pass refs)
    btn_refs = [None, None, None, None]   # [dash, reset, profile, logout]

    nav_items = [
        ("📊  Dashboard",   0),
        ("🔄  Reset",       1),
        ("👤  Profile",     2),
    ]

    def make_nav(text, idx, cmd):
        btn = tk.Button(sidebar, text=text, command=cmd,
                        bg=BG_SIDEBAR, fg=TEXT_MUTED,
                        activebackground=ACCENT_MINT, activeforeground=BG_DARK,
                        font=("Helvetica", 10, "bold"),
                        bd=0, relief="flat", cursor="hand2",
                        anchor="w", padx=18, pady=12,
                        highlightthickness=0)
        btn.pack(fill="x", pady=2)
        btn.bind("<Enter>", lambda e, b=btn, i=idx: b.config(
            bg=ACCENT_MINT if btn_refs[i] == b else BORDER_CLR,
            fg=BG_DARK if btn_refs[i] == b else TEXT_WHITE))
        btn.bind("<Leave>", lambda e, b=btn, i=idx: b.config(
            bg=ACCENT_MINT if btn_refs[i] == b else BG_SIDEBAR,
            fg=BG_DARK if btn_refs[i] == b else TEXT_MUTED))
        return btn

    b0 = make_nav("📊  Dashboard", 0,
                  lambda: show_dashboard(content_frame, btn_refs))
    btn_refs[0] = b0

    b1 = make_nav("🔄  Reset", 1,
                  lambda: show_reset(content_frame, btn_refs))
    btn_refs[1] = b1

    b2 = make_nav("👤  Profile", 2,
                  lambda: show_profile(content_frame, btn_refs))
    btn_refs[2] = b2

    # Spacer + Logout at bottom
    tk.Frame(sidebar, bg=BG_SIDEBAR).pack(fill="y", expand=True)
    ttk.Separator(sidebar).pack(fill="x", padx=12, pady=4)

    # User info strip
    user_strip = tk.Frame(sidebar, bg=BG_SIDEBAR)
    user_strip.pack(fill="x", padx=10, pady=8)
    tk.Label(user_strip, text="👤", bg=BG_SIDEBAR, fg=TEXT_MUTED,
             font=("Helvetica", 16)).pack(side="left")
    info = tk.Frame(user_strip, bg=BG_SIDEBAR)
    info.pack(side="left", padx=6)
    tk.Label(info, text="Demo User", bg=BG_SIDEBAR, fg=TEXT_WHITE,
             font=("Helvetica", 9, "bold")).pack(anchor="w")
    tk.Label(info, text="demo@calmpulse.io", bg=BG_SIDEBAR, fg=TEXT_MUTED,
             font=("Helvetica", 7)).pack(anchor="w")

    def logout():
        app.destroy()
        root.deiconify()

    logout_btn = tk.Button(sidebar, text="⏻  Log Out", command=logout,
                           bg=BG_SIDEBAR, fg=ACCENT_CORAL,
                           activebackground=ACCENT_CORAL, activeforeground=BG_DARK,
                           font=("Helvetica", 10, "bold"),
                           bd=0, relief="flat", cursor="hand2",
                           anchor="w", padx=18, pady=10,
                           highlightthickness=0)
    logout_btn.pack(fill="x", pady=(0, 12))

    # Load dashboard by default
    show_dashboard(content_frame, btn_refs)


# ══════════════════════════════════════════════════
#  SIGN IN LOGIC
# ══════════════════════════════════════════════════
SAMPLE_EMAIL    = "demo@calmpulse.io"
SAMPLE_PASSWORD = "calm123"


def sign_in():
    email    = email_entry.get().strip()
    password = password_entry.get().strip()

    for e in (email_entry, password_entry):
        e.config(highlightbackground=BORDER_CLR, highlightthickness=1)

    if not email or not password:
        if not email:
            email_entry.config(highlightbackground=ACCENT_CORAL, highlightthickness=2)
        if not password:
            password_entry.config(highlightbackground=ACCENT_CORAL, highlightthickness=2)
        messagebox.showwarning("Missing Fields", "Please enter email and password.")
        return

    if email == SAMPLE_EMAIL and password == SAMPLE_PASSWORD:
        open_main_app()
    else:
        messagebox.showerror("Login Failed",
                             "Invalid credentials.\n\n"
                             f"Use sample login:\n"
                             f"  Email:    {SAMPLE_EMAIL}\n"
                             f"  Password: {SAMPLE_PASSWORD}")


def fill_sample():
    email_entry.delete(0, tk.END)
    email_entry.insert(0, SAMPLE_EMAIL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, SAMPLE_PASSWORD)


# ══════════════════════════════════════════════════
#  LOGIN WINDOW
# ══════════════════════════════════════════════════
root = tk.Tk()
root.title("Calm Pulse — Sign In")
root.geometry("460x640")
root.configure(bg=BG_DARK)
root.resizable(False, False)

# Brand
bf = tk.Frame(root, bg=BG_DARK)
bf.pack(pady=(36, 4))
tk.Label(bf, text="◉", bg=BG_DARK, fg=ACCENT_MINT,
         font=("Helvetica", 32)).pack()
tk.Label(bf, text="Calm Pulse", bg=BG_DARK, fg=TEXT_WHITE,
         font=("Helvetica", 24, "bold")).pack()
tk.Label(root, text="Your Personal Stress Management System",
         bg=BG_DARK, fg=TEXT_MUTED,
         font=("Helvetica", 10)).pack(pady=(2, 20))

# ── Sample login hint ────────────────────────────
hint = tk.Frame(root, bg="#1a3020", highlightthickness=1,
                highlightbackground=ACCENT_GREEN)
hint.pack(padx=36, fill="x", pady=(0, 8))
tk.Label(hint,
         text=f"🔑  Sample Login:  {SAMPLE_EMAIL}  /  {SAMPLE_PASSWORD}",
         bg="#1a3020", fg=ACCENT_GREEN,
         font=("Helvetica", 9)).pack(pady=7, padx=10)

# ── Login card ───────────────────────────────────
card = tk.Frame(root, bg=BG_CARD, highlightthickness=1,
                highlightbackground=BORDER_CLR)
card.pack(padx=36, fill="x")


def field_label(text):
    tk.Label(card, text=text, bg=BG_CARD, fg=TEXT_MUTED,
             font=("Helvetica", 9, "bold"), anchor="w").pack(
                 fill="x", padx=24, pady=(14, 2))


def styled_entry(show=None):
    e = tk.Entry(card, bg=BG_INPUT, fg=TEXT_WHITE,
                 insertbackground=ACCENT_MINT,
                 font=("Helvetica", 11), bd=0,
                 highlightthickness=1, highlightbackground=BORDER_CLR,
                 show=show)
    e.pack(fill="x", padx=24, ipady=9)
    e.bind("<FocusIn>",  lambda ev: e.config(highlightbackground=ACCENT_MINT))
    e.bind("<FocusOut>", lambda ev: e.config(highlightbackground=BORDER_CLR))
    return e


field_label("Email Address")
email_entry = styled_entry()

field_label("Password")
password_entry = styled_entry(show="•")
password_entry.bind("<Return>", lambda e: sign_in())

# row: forgot + fill sample
frow = tk.Frame(card, bg=BG_CARD)
frow.pack(fill="x", padx=24, pady=(6, 0))
tk.Label(frow, text="Forgot password?", bg=BG_CARD, fg=ACCENT_MINT,
         font=("Helvetica", 9), cursor="hand2").pack(side="left")
sample_lbl = tk.Label(frow, text="Use sample ↓", bg=BG_CARD, fg=ACCENT_GREEN,
                      font=("Helvetica", 9, "underline"), cursor="hand2")
sample_lbl.pack(side="right")
sample_lbl.bind("<Button-1>", lambda e: fill_sample())

# Sign In button
btn_f = tk.Frame(card, bg=BG_CARD)
btn_f.pack(fill="x", padx=24, pady=(16, 6))
si_btn = tk.Button(btn_f, text="Sign In  →", command=sign_in,
                   bg=ACCENT_MINT, fg=BG_DARK,
                   activebackground=ACCENT_SKY, activeforeground=BG_DARK,
                   font=("Helvetica", 12, "bold"),
                   pady=12, bd=0, relief="flat", cursor="hand2",
                   highlightthickness=0)
si_btn.pack(fill="x")
si_btn.bind("<Enter>", lambda e: si_btn.config(bg=ACCENT_SKY))
si_btn.bind("<Leave>", lambda e: si_btn.config(bg=ACCENT_MINT))

# Divider
dv = tk.Frame(card, bg=BG_CARD)
dv.pack(fill="x", padx=24, pady=(6, 6))
tk.Frame(dv, bg=BORDER_CLR, height=1).pack(side="left", fill="x", expand=True, pady=7)
tk.Label(dv, text="  or  ", bg=BG_CARD, fg=TEXT_MUTED,
         font=("Helvetica", 9)).pack(side="left")
tk.Frame(dv, bg=BORDER_CLR, height=1).pack(side="left", fill="x", expand=True, pady=7)

# Social buttons
for label in ("🔵  Continue with Google", "🟦  Continue with Microsoft"):
    sb = tk.Button(card, text=label, bg=BG_INPUT, fg=TEXT_WHITE,
                   activebackground=BORDER_CLR, activeforeground=TEXT_WHITE,
                   font=("Helvetica", 10, "bold"),
                   pady=10, bd=0, relief="flat", cursor="hand2",
                   highlightthickness=0)
    sb.pack(fill="x", padx=24, pady=3)
    sb.bind("<Enter>", lambda e, b=sb: b.config(bg=BORDER_CLR))
    sb.bind("<Leave>", lambda e, b=sb: b.config(bg=BG_INPUT))

tk.Label(card, bg=BG_CARD, height=1).pack()

# Footer
tk.Label(root, text="New here?  Create a free account →",
         bg=BG_DARK, fg=TEXT_MUTED,
         font=("Helvetica", 9), cursor="hand2").pack(pady=14)

root.mainloop()