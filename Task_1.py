import os
import tkinter as tk

def expand(s:str):
  if "$HOME" in s:
        s = s.replace("$HOME", os.getcwd())
  for k in os.environ:
    s = s.replace("$" + k, os.environ[k])
  return s

def run_cmd():
    raw = expand(entry.get())  #получаем и расширяем команду
    text.insert(tk.END, f"vfs> {raw}\n")  #выводит vfs как команду в текстовое поле
    cmd, *args = raw.split()  #разделяем команду и аргументы

    if cmd == "exit":
        root.destroy()  #закрываем
    elif cmd == "ls":
        text.insert(tk.END, f"ls {' '.join(args)}\n")  #заглушка для ls
    elif cmd == "cd":
        text.insert(tk.END, f"cd {' '.join(args)}\n")  #заглушка для cd
    else:
        text.insert(tk.END, f"Command not found\n")
    entry.delete(0, tk.END)  #чисти поле ввода

root = tk.Tk()
root.title("Эмулятор - [username@hostname]") #название окна
text = tk.Text(root, height=10, width=50) #текстовое поле для вывода
text.pack()
entry = tk.Entry(root, width=50) #поле для ввода
entry.pack()
entry.bind('<Return>', lambda e: run_cmd()) #привязываем Enter к выполнению команды

tk.Button(root, text="Run", command=run_cmd).pack() #кнопка Run
root.mainloop()