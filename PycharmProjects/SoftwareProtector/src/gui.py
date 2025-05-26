import tkinter as tk
from tkinter import messagebox
from license_checker import check_license
from integrity_checker import verify_integrity
import json

with open('config.json') as f:
    config = json.load(f)

EXPECTED_HASH = config['expected_hash']

def on_submit():
    key = entry.get()
    if not check_license(key):
        messagebox.showerror("Помилка", "Невалідний ліцензійний ключ.")
        return
    if not verify_integrity('main.py', EXPECTED_HASH):
        messagebox.showerror("Помилка", "Порушено цілісність файлу.")
        return
    messagebox.showinfo("Успіх", "Захист пройдено. Запуск програми...")

root = tk.Tk()
root.title("Захист ПЗ")
root.geometry("400x150")

label = tk.Label(root, text="Введіть ліцензійний ключ:")
label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack()
tk.Button(root, text="Перевірити", command=on_submit).pack(pady=10)

root.mainloop()