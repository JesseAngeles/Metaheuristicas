import tkinter as tk

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