import tkinter as tk # подключаем библиотеку

win = tk.Tk() # создаем окно
win.title("Первый проект!!!!") # именуем окно 
win.geometry("650x500") # устанавливаем размеры окна
win.iconbitmap(default="ico_5966527.png")
win.configure(bg="#B88C8C")


Label = tk.Label(text="Пятница", font=("Arial", 28), fg="#00FF15")
Label.pack(side="top")

Label3 = tk.Label(win, text="Математические основы 8:30-10:00", font=("Arial", 22), fg="#0011FF")
Label3.pack(side="top")

Label4 = tk.Label(win, text="Перерыв 10 мин", font=("Arial", 20), fg="#F00000")
Label4.pack(side="top")

Label5 = tk.Label(win, text="Проектынй менеджмент 10;10-11:40", font=("Arial", 22), fg="#0400FF")
Label5.pack(side="top")

Label2 = tk.Label(win, text="Перерыв 30 мин", font=("Arial", 20), fg="#FF0000")
Label2.pack(side="top")


Label6 = tk.Label(win, text="Проектынй менеджмент 12:10-13:40", font=("Arial", 22), fg="#2500F5")
Label6.pack(side="top")

Label2 = tk.Label(win, text="Перерыв 30 мин", font=("Arial", 20), fg="#FF0000")
Label2.pack(side="top")


Label5 = tk.Label(win, text="Моделирование физический процессов в приложения 14:10-15:40", font=("Arial", 22), fg="#1900FF")
Label5.pack(side="top")


win.mainloop() # запуск окна