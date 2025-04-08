import tkinter as tk
from tkinter import messagebox
from Algorithms.SimulatedAnnealing import SimulatedAnnealing
from Problems.KnapsackProblem import KnapsackProblem
from UI.components import draw_items, back_to_root

def knapsack_problem_window(root):
    problem = KnapsackProblem()
    root.withdraw()

    speed = 1000

    window_a = tk.Toplevel()
    window_a.title("Knapsack problem")
    window_a.geometry("1820x1200")
    window_a.protocol("WM_DELETE_WINDOW", root.quit)

    tk.Label(window_a, text="Knapsack problem", font=("Arial", 14)).pack(pady=20)

    header_frame = tk.Frame(window_a)
    header_frame.pack(pady=20)

    # Label y Entry para "Total Items"
    label_items = tk.Label(header_frame, text="Items", font=("Arial", 14), width=15, anchor="w")
    label_items.grid(row=0, column=0, padx=5, pady=5)

    entry_total_items = tk.Entry(header_frame, width=10)
    entry_total_items.grid(row=0, column=1, padx=5, pady=5)

    # Label y Entry para "Capacity"
    label_capacity = tk.Label(header_frame, text="Capacity", font=("Arial", 14), width=15, anchor="w")
    label_capacity.grid(row=1, column=0, padx=5, pady=5)

    entry_capacity = tk.Entry(header_frame, width=10)
    entry_capacity.grid(row=1, column=1, padx=5, pady=5)

    frame_items = tk.Frame(window_a)
    frame_items.pack(pady=20)

    boxes, labels_weight, labels_value = [], [], []
    box, weight_label, value_label, energy_label = [None], [None], [None], [None]  # usando lista para que sean mutables

    frame_footer = tk.Frame(window_a)
    frame_footer.pack(pady=5)
    
    def generate_information():
        total_items = int(entry_total_items.get())
        capacity = int(entry_capacity.get())
        problem.generate_information(total_items, capacity)

        draw_items(
            frame_items,
            problem.information['values'],
            boxes,
            labels_weight,
            labels_value
        )

    # Footer
    final_row = tk.Frame(frame_footer)
    final_row.pack(pady=5)

    box[0] = tk.Frame(final_row, bg="green", width=20, height=20)
    box[0].pack(side="left", padx=10)

    weight = tk.Label(final_row, text="Weight: 0", font=("Arial", 14), width=15, anchor="w")
    weight.pack(side="left", padx=5)

    value = tk.Label(final_row, text="Value: 0", font=("Arial", 14), width=15, anchor="w")
    value.pack(side="left", padx=5)

    energy = tk.Label(final_row, text="Energy: 0", font=("Arial", 14), width=15, anchor="w")
    energy.pack(side="left", padx=5)

    weight_label[0] = weight
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
            energy = weight = value = 0
            for i in range(len(solution)):
                if solution[i]:
                    boxes[i].configure(bg="green")
                    weight += info['values'][i][0]
                    value += info['values'][i][1]
                else:
                    boxes[i].configure(bg="gray")
            
            energy = sa.energy
            
            weight_label[0].configure(text=f"Weight: {weight}")
            value_label[0].configure(text=f"Value: {value}")
            energy_label[0].configure(text=f"Energy: {energy}")

        # Reset visual
        for i in range(len(boxes)):
            boxes[i].configure(bg="black")
        weight_label[0].configure(text="Weight: 0")
        value_label[0].configure(text="Value: 0")
        energy_label[0].configure(text="Energy: 0")
        
        box[0].configure(bg="gray")

        def run_step():
            if sa.stepSimpleSimulatedAnnealing():
                update_labels_and_colors(sa.solution, sa.information)

                if sa.energy < 0:
                    box[0].configure(bg="gray")
                else:
                    box[0].configure(bg="green")
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
    
    tk.Button(window_a, text="Volver", command=lambda: back_to_root(window_a, root)).pack(pady=5)