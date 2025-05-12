import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Algorithms.SimulatedAnnealing1 import SimulatedAnnealing
from Problems.SumFunctionProblem1 import SumFunctionProblem
from UI.components import draw_bars, back_to_root

def sum_function_window(root):
    problem = SumFunctionProblem()
    root.withdraw()

    speed = 1000

    window_a = tk.Toplevel()
    window_a.title("Sum function problem")
    window_a.geometry("1820x1200")
    window_a.protocol("WM_DELETE_WINDOW", root.quit)

    tk.Label(window_a, text="Sum function problem", font=("Arial", 14)).pack(pady=20)

    header_frame = tk.Frame(window_a)
    header_frame.pack(pady=20)

    # Label y Entry para "size"
    label_size = tk.Label(header_frame, text="Size", font=("Arial", 14), width=15, anchor="w")
    label_size.grid(row=0, column=0, padx=5, pady=5)

    entry_size = tk.Entry(header_frame, width=10)
    entry_size.insert(END, "10")
    entry_size.grid(row=0, column=1, padx=5, pady=5)

    # Label y Entry para "min"
    label_min = tk.Label(header_frame, text="Min", font=("Arial", 14), width=15, anchor="w")
    label_min.grid(row=1, column=0, padx=5, pady=5)

    entry_min = tk.Entry(header_frame, width=10)
    entry_min.insert(END, "-10")
    entry_min.grid(row=1, column=1, padx=5, pady=5)

    # Label y Entry para "max"
    label_max = tk.Label(header_frame, text="Max", font=("Arial", 14), width=15, anchor="w")
    label_max.grid(row=2, column=0, padx=5, pady=5)

    entry_max = tk.Entry(header_frame, width=10)
    entry_max.insert(END, "10")
    entry_max.grid(row=2, column=1, padx=5, pady=5)



    frame_items = tk.Frame(window_a)
    frame_items.pack(pady=20)

    boxes, labels_value = [], []
    value_label, energy_label = [None], [None]  # usando lista para que sean mutables

    frame_footer = tk.Frame(window_a)
    frame_footer.pack(pady=5)
    
    def generate_information():
        size = int(entry_size.get())
        min = int(entry_min.get())
        max = int(entry_max.get())
        
        problem.generate_information(size, min, max)

        draw_bars(
            frame_items,
            problem.information['size'],
            boxes,
            labels_value
        )

    # Footer
    final_row = tk.Frame(frame_footer)
    final_row.pack(pady=5)

    value = tk.Label(final_row, text="Value: 0", font=("Arial", 14), width=15, anchor="w")
    value.pack(side="left", padx=5)

    energy = tk.Label(final_row, text="Energy: 0", font=("Arial", 14), width=15, anchor="w")
    energy.pack(side="left", padx=5)

    value_label[0] = value
    energy_label[0] = energy

    def simulated_annealing():
        sa = SimulatedAnnealing(
            information=problem.information,
            energy_function=problem.energy,
            initial_solution_function=problem.generate_initial_solution,
            generate_neighbour_function=problem.random_neighbour
        )

        def update_labels_and_colors(solution, info):
            energy = sa.energy

            value_label[0].configure(text=f"Value: {-energy:.2f}")
            energy_label[0].configure(text=f"Energy: {energy:.2f}")

            min_value = info["min"]
            max_value = info["max"]
            value_range = max_value - min_value if max_value != min_value else 1

            canvas = frame_items.canvas
            canvas_height = int(canvas["height"])
            y_bottom = canvas_height - 30
            max_bar_height = canvas_height - 60  # deja espacio arriba

            for idx, val in enumerate(solution):
                # Escalar altura según min y max
                normalized = (val - min_value) / value_range
                bar_height = normalized * max_bar_height
                y_top = y_bottom - bar_height
                x = idx * 50 + 25

                # Actualiza barra
                canvas.coords(boxes[idx], x - 5, y_top, x + 5, y_bottom)

                # Actualiza texto
                canvas.itemconfig(labels_value[idx], text=f"V: {val}")
                canvas.coords(labels_value[idx], x, y_top - 10)


        # Reset visual
        value_label[0].configure(text="Value: 0")
        energy_label[0].configure(text="Energy: 0")
        
        def run_step():
            if sa.stepSimpleSimulatedAnnealing():
                update_labels_and_colors(sa.solution, sa.information)
                window_a.after(int(speed), run_step)
            else:
                messagebox.showinfo("Simulated Annealing", "Process finished")

        run_step()

    def change_speed(fast):
        nonlocal speed
        if fast:
            speed /= 2
        else:
            speed *= 2
        
    button_frame = tk.Frame(window_a)
    button_frame.pack(pady=5) 
        
    tk.Button(button_frame, text="Generate information", command=generate_information).pack(side="left", padx=10)
    tk.Button(button_frame, text="Simulated Annealing", command=simulated_annealing).pack(side="left", padx=10)
    
    speed_frame = tk.Frame(window_a)
    speed_frame.pack(pady=5)
    tk.Button(speed_frame, text="Fast", command=lambda: change_speed(True)).pack(side="left", padx = 10)
    tk.Button(speed_frame, text="Low", command=lambda: change_speed(False)).pack(side="left", padx = 10)
    
    tk.Button(window_a, text="Menu", command=lambda: back_to_root(window_a, root)).pack(pady=5)