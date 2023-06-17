
import tkinter as tk
import random

# Создание главного окна и его конфигурация
window = tk.Tk()
window.title("Ты ГЕЙ?")
window.geometry("300x200")
window_message = tk.Label(window, text="Ты ГЕЙ?")
window_message.pack()

# Функция для печати сообщения по нажатию на первую кнопку
def show_message():
    message_window = tk.Toplevel()
    message_window.title("Ты ГЕЙ?")
    message_window.geometry("200x100")
    
    message_label = tk.Label(message_window, text="Я так и знал!")
    message_label.pack()

# Функция для перемещения кнопки в пределах главного окна
def move_button():
    x = random.randint(10, 170)
    y = random.randint(10, 10)
    move_button.place(x=x, y=y)

# Создание кнопок и их конфигурация
message_button = tk.Button(window, text="Да", command=show_message)
message_button.pack(side=tk.LEFT, padx=60)

move_button = tk.Button(window, text="Нет", command=move_button)
move_button.pack(side=tk.RIGHT, padx=60)

# Запуск цикла для отображения главного окна
window.mainloop()
