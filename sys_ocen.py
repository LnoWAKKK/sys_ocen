import tkinter as tk

grades = {}
class Grade_manager:
    def __init__(self):
        pass



def teacher_login_UI():
    new_window = tk.Toplevel(root)
    new_window.title("Login nauczyciela")
    new_window.geometry("100x50")
    PS_ent = tk.Entry(new_window, width=30).pack(pady=5, padx=2)
    PS_en = tk.Label(new_window, text="login").pack(pady=5, padx=1)





#window
root = tk.Tk()
root.title("SUPER system oceniania")
root.geometry("150x200")
root.resizable(False, False)

#UI
WRU = tk.Label(root, text="Kim jesteś?").pack(pady=4)
TB = tk.Button(root, text="nauczyciel", command=lambda: teacher_login_UI()).pack(pady=5)
TS = tk.Button(root, text="uczeń", command=None).pack(pady=5)

root.mainloop()