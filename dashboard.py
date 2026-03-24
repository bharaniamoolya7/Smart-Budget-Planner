import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- THEME: NEURAL ---
BG_WHITE = "#ffffff"
CARD_WHITE = "#f9fafb"
TEXT_COLOR = "#1e293b"
ACCENT_ANN = "#6366f1"
NEURAL_GLOW = "#f5f3ff"


class SmartBudgetANN:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Smart Budget Planner (ANN Pro)")
        self.root.geometry("1280x950")
        self.root.configure(bg=BG_WHITE)

        self.ranked_features = []
        self.all_features = ["Food", "Transport", "Utilities", "Healthcare", "Entertainment", "Others"]
        self.fig = None
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="🧠 SMART BUDGET PLANNER (ANN)", font=("Segoe UI", 18, "bold"),
                 bg=BG_WHITE, fg=TEXT_COLOR).pack(pady=5)

        self.main = tk.Frame(self.root, bg=BG_WHITE)
        self.main.pack(fill="both", expand=True, padx=20)

        # --- LEFT PANEL ---
        self.left = tk.Frame(self.main, bg=CARD_WHITE, padx=15, pady=10, highlightthickness=1,
                             highlightbackground="#e2e8f0")
        self.left.place(x=0, y=0, width=360, height=820)

        self.salary = self.create_input(self.left, "Monthly Gross Income (X1)")
        self.rent = self.create_input(self.left, "Monthly Rent / Home Loan (X2)")
        self.emi = self.create_input(self.left, "Other EMIs (X3)")
        self.deductions = self.create_input(self.left, "Other Deductions (X4)")
        self.target_save = self.create_input(self.left, "Target Savings Amount (Y_Target)")

        tk.Label(self.left, text="Rank Priority (X_Features):", font=("Segoe UI", 9, "bold"), bg=CARD_WHITE).pack(
            anchor="w", pady=(5, 2))
        self.btn_frame = tk.Frame(self.left, bg=CARD_WHITE)
        self.btn_frame.pack(fill="x")

        self.feature_btns = {}
        for f in self.all_features:
            btn = tk.Button(self.btn_frame, text=f, font=("Segoe UI", 8), bg="#ffffff", relief="groove", pady=1,
                            command=lambda x=f: self.add_to_rank(x))
            btn.pack(side="top", fill="x", pady=1)
            self.feature_btns[f] = btn

        self.rank_label = tk.Label(self.left, text="Neural Pattern: None", font=("Segoe UI", 7, "italic"),
                                   bg=CARD_WHITE, fg=ACCENT_ANN, wraplength=320, justify="left")
        self.rank_label.pack(pady=2)

        tk.Button(self.left, text="🔄 Reset Pattern", font=("Segoe UI", 8), command=self.reset_rank,
                  relief="flat").pack()

        tk.Button(self.left, text="RUN NEURAL ANALYSIS", command=self.run_ann_engine,
                  bg=ACCENT_ANN, fg="white", font=("Segoe UI", 11, "bold"), relief="flat", pady=10).pack(fill="x",
                                                                                                         pady=10)

        self.dl_btn = tk.Button(self.left, text="📥 DOWNLOAD REPORT", command=self.download_report,
                                bg="#10b981", fg="white", font=("Segoe UI", 9, "bold"), relief="flat", pady=8,
                                state="disabled")
        self.dl_btn.pack(fill="x")

        # --- RIGHT PANEL ---
        self.right = tk.Frame(self.main, bg=BG_WHITE)
        self.right.place(x=380, y=0, width=850, height=850)

    def add_to_rank(self, feature):
        if feature not in self.ranked_features:
            self.ranked_features.append(feature)
            self.feature_btns[feature].configure(state="disabled", bg="#f1f5f9")
            self.rank_label.config(text="Pattern: " + " → ".join(self.ranked_features))

    def reset_rank(self):
        self.ranked_features = []
        for btn in self.feature_btns.values():
            btn.configure(state="normal", bg="#ffffff")
        self.rank_label.config(text="Neural Pattern: None")

    def create_input(self, parent, txt):
        tk.Label(parent, text=txt, font=("Segoe UI", 8, "bold"), bg=CARD_WHITE).pack(anchor="w")
        e = tk.Entry(parent, font=("Segoe UI", 9), relief="flat", highlightthickness=1, highlightbackground="#cbd5e1")
        e.pack(fill="x", pady=2)
        return e

    def run_ann_engine(self):
        try:
            if not self.ranked_features:
                return messagebox.showwarning("Rank Missing", "Please rank your priorities first!")

            s, r, e, d = float(self.salary.get()), float(self.rent.get() or 0), float(self.emi.get() or 0), float(
                self.deductions.get() or 0)
            t_save = float(self.target_save.get() or 0)

            net_income = s - r - e - d
            if t_save > net_income: return messagebox.showerror("Error", "Savings exceed income!")

            data = {"Target Savings": t_save, "Rent/Loan": r, "Other EMIs": e}
            spendable = net_income - t_save
            weights = [0.45, 0.25, 0.15, 0.08, 0.05, 0.02]

            temp_data = {}
            for i, feature in enumerate(self.ranked_features):
                if i < len(weights): temp_data[feature] = spendable * weights[i]

            # --- OPTIMIZATION (6k, 12k, 8k limits) ---
            extra_sum = 0
            limits = {"Transport": 6000, "Utilities": 12000, "Food": 8000}

            for field, limit in limits.items():
                if temp_data.get(field, 0) > limit:
                    extra_sum += (temp_data[field] - limit)
                    temp_data[field] = limit

            if extra_sum > 0: data["Safe Wealth Fund"] = extra_sum

            data.update(temp_data)
            self.render_results(data, s, r, e, d, extra_sum)
            self.dl_btn.configure(state="normal")

        except ValueError:
            messagebox.showerror("Error", "Enter numeric values!")

    def render_results(self, data, gross, r, e, d, extra):
        for w in self.right.winfo_children(): w.destroy()

        report_frame = tk.Frame(self.right, bg=BG_WHITE)
        report_frame.pack(fill="x", pady=5)

        report = f"💰 Gross: ₹{gross:,.0f} | 📉 Fixed: ₹{r + e + d:,.0f} | ✅ Net: ₹{gross - r - e - d:,.0f}\n"
        report += f"✅ Savings: ₹{data['Target Savings']:,.0f} | 🛡️ Extra Protected: ₹{extra:,.0f}\n"
        for k in self.ranked_features:
            if k in data: report += f"• Allocated: ₹{data[k]:,.0f} on {k}\n"

        tk.Label(report_frame, text=report, font=("Segoe UI", 9), justify="left", bg=BG_WHITE).pack(anchor="w")

        fig_frame = tk.Frame(self.right, bg=BG_WHITE)
        fig_frame.pack(fill="x")

        self.fig = plt.figure(figsize=(6, 3.5), facecolor=BG_WHITE)
        ax = self.fig.add_subplot(111)
        colors = ["#10b981", "#fb7185", "#f43f5e", "#fbbf24", "#34d399", "#818cf8", "#f472b6", "#a78bfa"]
        ax.pie(data.values(), labels=data.keys(), autopct='%1.0f%%', startangle=140,
               colors=colors[:len(data)], wedgeprops=dict(width=0.4), textprops={'fontsize': 7})

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(self.fig, master=fig_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        if extra > 0:
            msg = f"💡 NEURAL INSIGHT: Found extra ₹{extra:,.0f} from capped spending!\n"
            msg += f"⚠️ STOCKS: While they offer high growth, they carry market risk.\n"
            msg += f"👉 BETTER OPTION: Move this to PRIMARY SAVINGS or invest in GOLD.\n"
            msg += "The ANN suggests these for guaranteed safety and stable wealth."

            box = tk.Label(self.right, text=msg, font=("Segoe UI", 9, "bold italic"),
                           bg="#fff7ed", fg="#c2410c", pady=8, padx=10, relief="solid", borderwidth=1, justify="left")
            box.pack(fill="x", pady=10, padx=20)

    def download_report(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path: self.fig.savefig(file_path, dpi=300); messagebox.showinfo("Saved", "Exported!")


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartBudgetANN(root)
    root.mainloop()  # THIS ENSURES THE WINDOW STAYS OPEN