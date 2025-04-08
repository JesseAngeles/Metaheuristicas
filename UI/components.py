import tkinter as tk

def back_to_root(window, root):
    window.destroy()
    root.deiconify()

def draw_items(frame_items, parent, items, boxes, labels_weight, labels_value, weight_label, value_label, box):
    for widget in frame_items.winfo_children():
        widget.destroy()

    boxes.clear()
    labels_weight.clear()
    labels_value.clear()

    for item in items:
        fila = tk.Frame(frame_items)
        fila.pack(pady=5)

        black_box = tk.Frame(fila, bg="black", width=20, height=20)
        black_box.pack(side="left", padx=10)

        label_w = tk.Label(fila, text=f"{item[0]}", font=("Arial", 14), width=15, anchor="w")
        label_w.pack(side="left", padx=5)

        label_v = tk.Label(fila, text=f"{item[1]}", font=("Arial", 14), width=15, anchor="w")
        label_v.pack(side="left", padx=5)

        boxes.append(black_box)
        labels_weight.append(label_w)
        labels_value.append(label_v)

    # Footer
    final_row = tk.Frame(frame_items)
    final_row.pack(pady=20)

    box[0] = tk.Frame(final_row, bg="green", width=20, height=20)
    box[0].pack(side="left", padx=10)

    weight = tk.Label(final_row, text="Weight: 0", font=("Arial", 14), width=15, anchor="w")
    weight.pack(side="left", padx=5)

    value = tk.Label(final_row, text="Value: 0", font=("Arial", 14), width=15, anchor="w")
    value.pack(side="left", padx=5)

    weight_label[0] = weight
    value_label[0] = value
