from Algorithms.HillClimbing import HillClimbing
from Algorithms.SimulatedAnnealing import SimulatedAnnealing

from Problems.KnapsackProblem import KnapsackProblem
from Problems.TravelSalesmanProblem import TravelSalesManProblem
from Problems.SumFunctionProblem import SumFunctionProblem
from Problems.Cec2017 import Cec2017
import Problems.cec2017.cec2017.functions as functions

ksp = KnapsackProblem(10, 10)
tsm = TravelSalesManProblem(7)
sfp = SumFunctionProblem(10, -5, 5)
cec = Cec2017(function=functions.f1)

################################################################
s = HillClimbing(cec,max_random=30)
s.method = s.randomMutation

s.problem.printInformation()
s.printSolution()

for _ in range(10):
    s.optimize(epochs=10)
    print(s.evaluate(s.solution))
    if s.is_best:
        s.resetProblem()


# ################################################################
# s = SimulatedAnnealing(ksp,max_temperature=10,max_iter=20)

# s.problem.printInformation()
# s.printSolution()

# for _ in range(10):
#     s.optimize(epochs=100)
#     s.printSolution()
#     if s.is_best:
#         s.resetProblem()

# ################################################################
# s = SimulatedAnnealing(tsm,max_temperature=10,max_iter=20)

# s.problem.printInformation()
# s.printSolution()

# for _ in range(10):
#     s.optimize(epochs=100)
#     s.printSolution()
#     if s.is_best:
#         s.resetProblem()

# ################################################################
# s = SimulatedAnnealing(sfp,max_temperature=10,max_iter=20)

# s.problem.printInformation()
# s.printSolution()

# for _ in range(10):
#     s.optimize(epochs=100)
#     s.printSolution()
#     if s.is_best:
#         s.resetProblem()


# ################################################################
# h = HillClimbing(ksp)
# h.method = h.randomMutation

# h.problem.printInformation()
# h.printSolution()

# for _ in range(10):
#     h.optimize(10)
#     h.printSolution()
#     if h.is_best:
#         h.resetProblem()

# ################################################################
# h = HillClimbing(TravelSalesManProblem(7))
# h.method = h.randomMutation

# h.problem.printInformation()
# h.printSolution()

# for _ in range(20):
#     h.optimize()
#     h.printSolution()
#     if h.is_best:
#         h.resetProblem()

# ################################################################
# h = HillClimbing(SumFunctionProblem(10,-5,5))
# h.method = h.randomMutation

# h.problem.printInformation()
# h.printSolution()

# for _ in range(20):
#     h.optimize()
#     h.printSolution()
#     if h.is_best:
#         h.resetProblem()
