import tkinter as tk
from tkinter import simpledialog, messagebox

# Настройки полотна
WINDOW_SIZE = 900
CENTER_X = WINDOW_SIZE // 2
CENTER_Y = WINDOW_SIZE // 2
COLOR = "black"
LINE_WIDTH = 2

# Класс полотна
class DrawCirclesApp:
    # Инициализация полотна
    def __init__(self, root):
        self.root = root
        self.root.title("Вложенные окружности (Enter - добавить, D - удалить, Esc - выход)")

        self.is_initialized = False

        self.start_radius = self.ask_radius()
        if self.start_radius is None:
            return
        
        self.step = self.ask_step()
        if self.step is None:
            return

        self.canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg="white")
        self.canvas.pack()

        self.is_initialized = True

        self.circles = []

        self.current_radius = self.start_radius

        # Назначение клавиш
        self.root.bind('<Return>', self.draw_next_circle)
        self.root.bind('<KeyPress-d>', self.remove_last_circle)
        self.root.bind('<KeyPress-D>', self.remove_last_circle)
        self.root.bind('<Escape>', self.quit)

        print(f"Начальный радиус: {self.start_radius}, шаг: {self.step}")
        print("Enter — добавить окружность, D — удалить последнюю, Esc — выход")

    # Задание радиуса
    def get_radius(self):
        max_radius = WINDOW_SIZE // 2 - 10
        while True:
            r = simpledialog.askinteger(
                "Начальный радиус",
                f"Введите начальный радиус окружности\n(от 1 до {max_radius}):",
                minvalue=1, maxvalue=max_radius, parent=self.root
            )
            if r is None:
                return None
            return r

    # Задание шага (уменьшения радиуса)
    def get_step(self):
        while True:
            s = simpledialog.askinteger(
                "Шаг уменьшения",
                f"Введите шаг уменьшения радиуса r\n(целое положительное число, от 1 до {self.start_radius}):",
                minvalue=1, maxvalue=self.start_radius, parent=self.root
            )
            if s is None:
                return None
            return s

    # Отрисовка следующей окружности кнопкой "Enter"
    def draw_next_circle(self, event):
        if self.current_radius > 0:
            x1 = CENTER_X - self.current_radius
            y1 = CENTER_Y - self.current_radius
            x2 = CENTER_X + self.current_radius
            y2 = CENTER_Y + self.current_radius

            circle_id = self.canvas.create_oval(
                x1, y1, x2, y2,
                outline=COLOR,
                width=LINE_WIDTH
            )

            self.circles.append(circle_id)
            self.current_radius -= self.step
        else:
            messagebox.showinfo("Готово", "Достигнута последняя возможная окружность!")

    # Удаление последней окружности кнопкой "D"
    def remove_last_circle(self, event):
        if self.circles:
            last_circle_id = self.circles.pop()
            self.canvas.delete(last_circle_id)
            self.current_radius += self.step
    
    # Закрытие приложения кнопкой "Esc"
    def quit(self, event):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = DrawCirclesApp(root)

    if app.is_initialized:
        root.deiconify()
        root.mainloop()
    else:
        root.destroy()
