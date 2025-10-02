import getpass
import os
import socket
import tkinter as tk
import sys

def expand(s: str):
    if "$HOME" in s:
        s = s.replace("$HOME", os.getcwd())
    for k in os.environ:
        s = s.replace("$" + k, os.environ[k])
    return s

def run_cmd():
    raw = expand(entry.get())
    text.insert(tk.END, f"vfs> {raw}\n")
    cmd, *args = raw.split()

    if cmd == "exit":
        root.destroy()
    elif cmd == "ls":
        text.insert(tk.END, f"ls {' '.join(args)}\n")
    elif cmd == "cd":
        text.insert(tk.END, f"cd {' '.join(args)}\n")
    elif cmd == "echo":
        text.insert(tk.END, f"{' '.join(args)}\n")
    else:
        text.insert(tk.END, f"Command not found\n")
    entry.delete(0, tk.END)


def run_script(path):
    try:
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line[0] == '#':
                    continue
                text.insert(tk.END, f"vfs> {line}\n")
                cmd, *args = line.split()

                if cmd == "exit":
                    root.after(10000, root.destroy)
                    return
                elif cmd == "ls":
                    text.insert(tk.END, f"ls {' '.join(args)}\n")
                elif cmd == "cd":
                    text.insert(tk.END, f"cd {' '.join(args)}\n")
                elif cmd == "echo":
                    text.insert(tk.END, f"{' '.join(args)}\n")
                else:
                    text.insert(tk.END, f"Command not found\n")
    except Exception as e:
        text.insert(tk.END, f"Error: {e}\n")

#для командной строки
vfs_path = None
script_path = None

if len(sys.argv) >= 2: #sys.argv - список строк, который используется для получения аргументов, переданных скрипту из командной строки
    vfs_path = sys.argv[1]

if len(sys.argv) >= 3:
    script_path = sys.argv[2]

print(f"VFS: {vfs_path}")
print(f"Script: {script_path}")

root = tk.Tk()
root.title("Эмулятор " + getpass.getuser() + "@" + socket.gethostname())
text = tk.Text(root, height=10, width=50)
text.pack()
entry = tk.Entry(root, width=50)
entry.pack()
entry.bind('<Return>', lambda e: run_cmd())
tk.Button(root, text="Run", command=run_cmd).pack()

if script_path:
    run_script(script_path)

root.mainloop()