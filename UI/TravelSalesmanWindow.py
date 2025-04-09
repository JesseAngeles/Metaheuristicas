import tkinter as tk
from tkinter import messagebox
from Algorithms.SimulatedAnnealing import SimulatedAnnealing
from Problems.TravelSalesmanProblem import TravelSalesmanProblem
from UI.components import draw_cities, back_to_root

def travel_salesman_problem_window(root):
    problem = TravelSalesmanProblem()
    root.withdraw()

    speed = 1000

    window_a = tk.Toplevel()
    window_a.title("Travel Salesman problem")
    window_a.geometry("1820x1200")
    window_a.protocol("WM_DELETE_WINDOW", root.quit)

    header_frame = tk.Frame(window_a)
    header_frame.pack(pady=20)

    # Label y Entry para "Total Items"
    label_cities = tk.Label(header_frame, text="Cities", font=("Arial", 14), width=15, anchor="w")
    label_cities.grid(row=0, column=0, padx=5, pady=5)

    entry_total_items = tk.Entry(header_frame, width=10)
    entry_total_items.grid(row=0, column=1, padx=5, pady=5)

    frame_items = tk.Frame(window_a)
    frame_items.pack(pady=20)

    boxes, labels_value = [], []
    distance_label, energy_label =[None], [None]  # usando lista para que sean mutables

    frame_footer = tk.Frame(window_a)
    frame_footer.pack(pady=5)
    
    def generate_information():
        total_cities = int(entry_total_items.get())
        problem.generate_information(total_cities)
        
        draw_cities(
            frame_items,
            problem.information['distances'],
            boxes,
            labels_value
        )

    # Footer
    final_row = tk.Frame(frame_footer)
    final_row.pack(pady=5)

    distance = tk.Label(final_row, text="Distance: 0", font=("Arial", 14), width=15, anchor="w")
    distance.pack(side="left", padx=5)

    energy = tk.Label(final_row, text="Energy: 0", font=("Arial", 14), width=15, anchor="w")
    energy.pack(side="left", padx=5)

    distance_label[0] = distance
    energy_label[0] = energy

    def simulated_annealing():
        sa = SimulatedAnnealing(
            information=problem.information,
            energy_function=problem.energy,
            initial_solution_function=problem.generate_initial_solution,
            generate_neighbour_function=problem.random_neighbour
        )

        def update_labels_and_colors(solution, info):
            canvas = frame_items.children["!canvas"]
            # Eliminar todos los textos y líneas anteriores
            canvas.delete("all")

            # Redibujamos las ciudades
            for i in range(len(labels_value)):
                _, x, y = labels_value[i]
                city = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")
                text = canvas.create_text(x, y - 20, text=f"City {i}", font=("Arial", 10))
                boxes[i] = city
                labels_value[i] = (text, x, y)

            # Dibujar líneas entre ciudades según el orden de la solución
            for i in range(len(solution)):
                city_a = solution[i]
                city_b = solution[(i + 1) % len(solution)]  # Conectamos de nuevo al inicio al final

                _, x1, y1 = labels_value[city_a]
                _, x2, y2 = labels_value[city_b]

                canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

            # Dibujar números de orden encima de cada ciudad según el recorrido
            for order, city_index in enumerate(solution):
                _, x, y = labels_value[city_index]
                label_id = canvas.create_text(x, y, text=str(order + 1), font=("Arial", 10), fill="white")
                labels_value[city_index] = (label_id, x, y)

            # Actualizar etiquetas de distancia y energía
            distance_label[0].configure(text=f"Distance: {-sa.energy:.2f}")
            energy_label[0].configure(text=f"Energy: {sa.energy:.2f}")

        # Reset visual
        distance_label[0].configure(text="Distance: 0")
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
    
    tk.Button(window_a, text="Volver", command=lambda: back_to_root(window_a, root)).pack(pady=5)