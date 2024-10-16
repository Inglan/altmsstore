import tkinter as tk
import requests
import json
import urllib.parse
import webbrowser

results = []

def searchstore(query):
    request = requests.get("https://storeedgefd.dsx.mp.microsoft.com/v9.0/pages/searchResults?market=US&locale=en-US&deviceFamily=windows.desktop&query=" + urllib.parse.quote(query))
    response = request.text
    json_response = json.loads(response)
    searchresults = []
    for i in json_response[1]["Payload"]["SearchResults"]:
        searchresults.append({"id": i["ProductId"], "title": i["Title"]})
    return searchresults

def search():
    query = entry.get()
    print(f"Searching for: {query}")
    results = searchstore(query)
    results_listbox.delete(0, tk.END)
    for result in results:
        results_listbox.insert(tk.END, result["title"] + " - ID=" + result["id"])

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

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

def install_selected_item():
    selected_index = results_listbox.curselection()
    if selected_index:
        selected_item = results_listbox.get(selected_index)
        item_id = selected_item.split(" - ID=")[-1]
        print(f"Installing item with ID: {item_id}")

def details_selected():
    selected_index = results_listbox.curselection()
    if selected_index:
        selected_item = results_listbox.get(selected_index)
        item_id = selected_item.split(" - ID=")[-1]
        webbrowser.open("https://apps.microsoft.com/detail/" + item_id)

install_button = tk.Button(button_frame, text="Install", command=install_selected_item)
install_button.pack(side=tk.LEFT, padx=5)

details_button = tk.Button(button_frame, text="Details", command=details_selected)
details_button.pack(side=tk.LEFT, padx=5)

root.mainloop()