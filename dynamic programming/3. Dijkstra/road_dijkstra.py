import tkinter as tk
from tkinter import messagebox, ttk

INF = 10**9

def dijkstra(graph, src, V):
    dist = [INF] * V
    dist[src] = 0
    visited = [False] * V

    for _ in range(V):
        u = min(range(V), key=lambda x: INF if visited[x] else dist[x])
        visited[u] = True

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

def compute():
    try:
        V = int(entry_V.get())
        graph = [[] for _ in range(V)]

        for i in range(int(entry_E.get())):
            u = int(edges[i][0].get())
            v = int(edges[i][1].get())
            w = int(edges[i][2].get())
            graph[u].append((v, w))

        src = int(entry_src.get())
        result = dijkstra(graph, src, V)

        result_label.config(text="\n".join(
            [f"To node {i} → {result[i]}" for i in range(V)]
        ))
    except:
        messagebox.showerror("Error", "Invalid input!")

def setup_edges():
    try:
        E = int(entry_E.get())
        for widget in frame_edges.winfo_children():
            widget.destroy()

        global edges
        edges = []

        for i in range(E):
            row = []
            for j, text in enumerate(["u", "v", "w"]):
                tk.Label(frame_edges, text=text).grid(row=i, column=j*2)
                e = tk.Entry(frame_edges, width=5)
                e.grid(row=i, column=j*2 + 1)
                row.append(e)
            edges.append(row)
    except:
        messagebox.showerror("Error", "Enter valid numbers!")

root = tk.Tk()
root.title("Road Network Shortest Path - Dijkstra")
root.geometry("600x500")

tk.Label(root, text="Road Network Using Dijkstra", font=("Arial",16,"bold"), fg="blue").pack()

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Junctions (V): ").grid(row=0, column=0)
entry_V = tk.Entry(frame_input, width=5)
entry_V.grid(row=0, column=1)

tk.Label(frame_input, text="Roads (E): ").grid(row=1, column=0)
entry_E = tk.Entry(frame_input, width=5)
entry_E.grid(row=1, column=1)

tk.Button(frame_input, text="Set Roads", command=setup_edges).grid(row=1, column=3, padx=10)

frame_edges = tk.Frame(root)
frame_edges.pack()

tk.Label(root, text="Source Junction: ").pack()
entry_src = tk.Entry(root, width=5)
entry_src.pack()

tk.Button(root, text="Compute Shortest Paths", command=compute,
         font=("Arial",12), bg="green", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial",12), fg="darkred")
result_label.pack(pady=10)

tk.Label(root, text="© Akash Kumar Roy",
         font=("Arial",10,"italic"), fg="gray").pack(side=tk.BOTTOM, pady=8)

root.mainloop()
