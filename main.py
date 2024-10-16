import tkinter as tk
import requests
import json
import urllib.parse


def search(query):
    request = requests.get("https://storeedgefd.dsx.mp.microsoft.com/v9.0/pages/searchResults?market=US&locale=en-US&deviceFamily=windows.desktop&query=" + urllib.parse.quote(query))
    response = request.text
    json_response = json.loads(response)
    results = []
    for i in json_response[1]["Payload"]["SearchResults"]:
        print(str(i["ProductId"]))
        print(str(i["Title"]))


def search():
    query = entry.get()
    print(f"Searching for: {query}")
    search(query)

root = tk.Tk()
root.title("SchoolStore")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(frame, text="Search", command=search)
search_button.pack(side=tk.LEFT)

# results
results_frame = tk.Frame(root)
results_frame.pack(pady=10)

results_listbox = tk.Listbox(results_frame, width=100, height=20)
results_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(results_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=results_listbox.yview)

root.mainloop()