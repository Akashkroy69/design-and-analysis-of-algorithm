import tkinter as tk
from tkinter import messagebox, ttk

def LCS(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Fill DP Table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to find LCS string
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs = X[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return dp, lcs


def compute():
    X = entry1.get()
    Y = entry2.get()

    if not X or not Y:
        messagebox.showwarning("Warning", "Please enter both strings!")
        return

    dp, lcs = LCS(X, Y)
    result_label.config(text=f"LCS: {lcs}\nLength: {len(lcs)}")

    # Show DP Table
    for widget in frame_dp.winfo_children():
        widget.destroy()

    m, n = len(X), len(Y)
    ttk.Label(frame_dp, text="DP Table", font=('Arial', 12, 'bold')).grid(row=0, column=0)
    
    for i in range(m+1):
        for j in range(n+1):
            ttk.Label(frame_dp, text=str(dp[i][j]), width=3, borderwidth=1,
                      relief="solid").grid(row=i+1, column=j)


# UI Window
root = tk.Tk()
root.title("Longest Common Subsequence Tool - By Ritika Bhaumik")
root.geometry("650x500")

tk.Label(root, text="Longest Common Subsequence (LCS) Solver",
         font=('Arial', 16, 'bold'), fg="blue").pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack()

tk.Label(frame_input, text="Enter String 1:", font=('Arial', 12)).grid(row=0, column=0)
entry1 = tk.Entry(frame_input, width=25)
entry1.grid(row=0, column=1)

tk.Label(frame_input, text="Enter String 2:", font=('Arial', 12)).grid(row=1, column=0)
entry2 = tk.Entry(frame_input, width=25)
entry2.grid(row=1, column=1)

tk.Button(root, text="Compute LCS", command=compute,
          font=('Arial', 12), bg="green", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 14), fg="darkred")
result_label.pack(pady=5)

frame_dp = tk.Frame(root)
frame_dp.pack(pady=10)

# Branding (Your Signature 😎)
tk.Label(root, text="© Ritika Bhaumik", font=('Arial', 10, "italic"), fg="gray").pack(side=tk.BOTTOM, pady=8)

root.mainloop()
