import tkinter as tk

def search():
    query = entry.get()
    print(f"Searching for: {query}")

root = tk.Tk()
root.title("Simple TK App with Search")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(frame, text="Search", command=search)
search_button.pack(side=tk.LEFT)

root.mainloop()