import tkinter as tk
from tkinter import messagebox
from utils import gen_shortcode
from database import save_url
short_code=""

def generate():## it creates short code
    global short_code
    long_url = url_entry.get()
    if long_url == "":
        messagebox.showerror("Error", "Please enter a URL!")
        return
    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        messagebox.showerror("Invalid URL", "Please enter a valid URL!")
        return
    short_code = gen_shortcode()
    save_url(long_url, short_code)
    result_label.config(text=f"Short Code: {short_code}")
def copy_code():
    if short_code == "":
        messagebox.showerror("Error", "Please generate a short code first!")
        return
    window.clipboard_clear()
    window.clipboard_append(short_code)
    window.update()
def clear_all():
    url_entry.delete(0, tk.END)
    result_label.config(text="")
window = tk.Tk()
window.title("Smart URL Shortener")
window.geometry("500x300")
window.configure(bg="lightblue")
title_label = tk.Label(
    window,
    text="Smart URL Shortener",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=15)
url_label = tk.Label(
    window,
    text="Enter URL:",
    font=("Arial", 12),
    bg="lightblue"
)
url_label.pack(pady=5)
url_entry = tk.Entry(
    window,
    width=45,
    font=("Arial", 11)
)
url_entry = tk.Entry(
    window,
    width=45,
    font=("Arial", 11)
)
url_entry.pack(pady=5)

shorten_button = tk.Button(
    window,
    text="Shorten URL",
    command=generate,
    font=("Arial", 11, "bold")
)
shorten_button.pack(pady=5)
copy_button = tk.Button(
    window,
    text="Copy Code",
    command=copy_code,
    font=("Arial", 11, "bold")
)
copy_button.pack(pady=5)
clear_button = tk.Button(
    window,
    text="Clear",
    command=clear_all,
    font=("Arial", 11, "bold")
)
clear_button.pack(pady=5)
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    padx=10,
    pady=10

)
result_label.pack()
window.mainloop()



