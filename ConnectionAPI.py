import requests
import tkinter as tk
from tkinter import ttk

url = "http://137.184.108.252:5000/api/login"

login = {
    "email": "guilhermerondam2@hotmail.com",
    "password": "cDXrPdiWc67u"
}

token = requests.post(url, json=login).json().get("token")

urlCidades = "http://137.184.108.252:5000/api/cidades"

headers = {
    "x-access-token": token
}

cidades = requests.get(urlCidades, headers=headers).json()

root = tk.Tk()
root.title("Lista de Cidades")

root.geometry("900x200")

label_token = tk.Label(root, text=f"Token: {token}")
label_token.pack(pady=10)

tree = ttk.Treeview(root, columns=("ID", "Nome"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome das cidades")

tree.column("ID", width=100)
tree.column("Nome", width=250)

tree.pack(fill="both", expand=True)

for cidade in cidades:
    tree.insert("", "end", values=(cidade["id"], cidade["nome"]))

root.mainloop()