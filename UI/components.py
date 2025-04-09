import tkinter as tk
import math

def back_to_root(window, root):
    window.destroy()
    root.deiconify()

def draw_items(frame_items, items, boxes, labels_weight, labels_value):
    for widget in frame_items.winfo_children():
        widget.destroy()

    boxes.clear()
    labels_weight.clear()
    labels_value.clear()

    columns = 25
    for index, item in enumerate(items):
        row = index // columns
        col = index % columns

        cell = tk.Frame(frame_items)
        cell.grid(row=row, column=col, padx=10, pady=10)

        black_box = tk.Frame(cell, bg="black", width=20, height=20)
        black_box.pack(pady=2)

        label_w = tk.Label(cell, text=f"W: {item[0]}", font=("Arial", 10))
        label_w.pack()

        label_v = tk.Label(cell, text=f"V: {item[1]}", font=("Arial", 10))
        label_v.pack()

        boxes.append(black_box)
        labels_weight.append(label_w)
        labels_value.append(label_v)
        
def draw_cities(frame_items, items, boxes, labels_value):
    for widget in frame_items.winfo_children():
        widget.destroy()

    boxes.clear()
    labels_value.clear()

    canvas = tk.Canvas(frame_items, width=640, height=640, bg="white")
    canvas.pack()

    num_cities = len(items)
    radius = 300
    center_x = 320
    center_y = 320

    for i in range(num_cities):
        angle = 2 * math.pi * i / num_cities
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        city = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")
        text = canvas.create_text(x, y, text=f"{i}", font=("Arial", 10), fill="white")

        boxes.append(city)  # ID del círculo
        labels_value.append((text, x, y))  # Guardamos también la posición

def draw_bars(frame_items, size, boxes, labels_value):
    for widget in frame_items.winfo_children():
        widget.destroy()
    
    boxes.clear()
    labels_value.clear()
    
    canvas = tk.Canvas(frame_items, width=50 * size, height=500, bg="white")
    canvas.pack()
    
    frame_items.canvas = canvas  # Guardamos el canvas para acceder luego
    
    for i in range(size):
        x = i * 50 + 25
        y_bottom = 270  # espacio para evitar solaparse con los labels
        y_top = y_bottom - 10  # altura inicial mínima

        bar = canvas.create_rectangle(x - 5, y_top, x + 5, y_bottom, fill="black")
        text = canvas.create_text(x, y_top - 10, text="V: 0", font=("Arial", 10))

        boxes.append(bar)
        labels_value.append(text)
