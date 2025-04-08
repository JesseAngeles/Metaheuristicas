import tkinter as tk
from tkinter import messagebox
from Algorithms.SimulatedAnnealing import SimulatedAnnealing
from Problems.KnapsackProblem import KnapsackProblem
from UI.components import draw_items, back_to_root

def knapsack_problem_window(root):
    problem = KnapsackProblem()
    root.withdraw()

    window_a = tk.Toplevel()
    window_a.title("Knapsack problem")
    window_a.geometry("1000x1000")
    window_a.protocol("WM_DELETE_WINDOW", root.quit)

    tk.Label(window_a, text="Knapsack problem", font=("Arial", 14)).pack(pady=20)

    entry_total_items = tk.Entry(window_a, width=10)
    entry_total_items.pack(pady=10)

    entry_capacity = tk.Entry(window_a, width=10)
    entry_capacity.pack(pady=10)

    frame_items = tk.Frame(window_a)
    frame_items.pack(pady=20)

    boxes, labels_weight, labels_value = [], [], []
    box, weight_label, value_label = [None], [None], [None]  # usando lista para que sean mutables

    def generate_information():
        total_items = int(entry_total_items.get())
        capacity = int(entry_capacity.get())
        problem.generate_information(total_items, capacity)

        draw_items(
            frame_items,
            window_a,
            problem.information['values'],
            boxes,
            labels_weight,
            labels_value,
            weight_label,
            value_label,
            box
        )

    def simulated_annealing():
        sa = SimulatedAnnealing(
            information=problem.information,
            energy_function=problem.energy,
            initial_solution_function=problem.generate_initial_solution,
            generate_neighbour_function=problem.random_neighbour
        )

        def update_labels_and_colors(solution, info):
            weight = value = 0
            for i in range(len(solution)):
                if solution[i]:
                    boxes[i].configure(bg="green")
                    weight += info['values'][i][0]
                    value += info['values'][i][1]
                else:
                    boxes[i].configure(bg="gray")
            weight_label[0].configure(text=f"Weight: {weight}")
            value_label[0].configure(text=f"Value: {value}")

        # Reset visual
        for i in range(len(boxes)):
            boxes[i].configure(bg="black")
        weight_label[0].configure(text="Weight: 0")
        value_label[0].configure(text="Value: 0")
        box[0].configure(bg="gray")

        def run_step():
            if sa.stepSimpleSimulatedAnnealing():
                update_labels_and_colors(sa.solution, sa.information)

                if sa.energy < 0:
                    box[0].configure(bg="gray")
                else:
                    box[0].configure(bg="green")

                window_a.after(1000, run_step)
            else:
                print(f"Mejor solución encontrada: {sa.best_solution}")
                print(f"Energía: {sa.best_energy}")
                messagebox.showinfo("Simulated Annealing", "El proceso ha finalizado.")

        run_step()


        
    tk.Button(window_a, text="Generate information", command=generate_information).pack(pady=10)
    tk.Button(window_a, text="Simulated Annealing", command=simulated_annealing).pack(pady=10)
    tk.Button(window_a, text="Volver", command=lambda: back_to_root(window_a, root)).pack(pady=20)
