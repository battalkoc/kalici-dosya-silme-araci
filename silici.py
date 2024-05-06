import os
import random
import string
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_random_data(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def overwrite_file_randomly(file_path, num_iterations):
    try:
        for i in range(num_iterations):
            with open(file_path, 'w') as file:
                file.write(generate_random_data(1024))  # 1024 bytes random data
        messagebox.showinfo("Başarılı", f"{num_iterations} kez dosya başarıyla üzerine yazıldı.")
    except Exception as e:
        messagebox.showerror("Hata", f"İşlem sırasında bir hata oluştu:\n{e}")

def delete_file(file_path):
    try:
        file_size = os.path.getsize(file_path)
        with open(file_path, 'w') as file:
            file.write(generate_random_data(file_size))
        os.remove(file_path)
        messagebox.showinfo("Başarılı", "Dosya başarıyla silindi ve boş alan temizlendi.")
    except Exception as e:
        messagebox.showerror("Hata", f"İşlem sırasında bir hata oluştu:\n{e}")

def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def execute_overwrite_and_delete():
    file_path = file_entry.get()
    if not os.path.exists(file_path):
        messagebox.showerror("Hata", "Seçilen dosya mevcut değil.")
        return

    num_iterations = int(iteration_var.get())
    overwrite_file_randomly(file_path, num_iterations)
    delete_file(file_path)


root = tk.Tk()
root.title("Kalıcı Dosya Silme Aracı")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()


file_label = tk.Label(frame, text="Dosya Yolu:")
file_label.grid(row=0, column=0, sticky="w")

file_entry = tk.Entry(frame, width=50)
file_entry.grid(row=0, column=1, columnspan=2)

browse_button = tk.Button(frame, text="Gözat", command=select_file)
browse_button.grid(row=0, column=3)

iteration_label = tk.Label(frame, text="Tekrar Sayısı:")
iteration_label.grid(row=1, column=0, sticky="w")

iteration_var = tk.StringVar(value="1")
iteration_entry = tk.Entry(frame, textvariable=iteration_var)
iteration_entry.grid(row=1, column=1)

execute_button = tk.Button(frame, text="İşlemi Başlat", command=execute_overwrite_and_delete)
execute_button.grid(row=2, column=0, columnspan=4, pady=10)

root.mainloop()
