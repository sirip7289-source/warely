from ortools.linear_solver import pywraplp

def calculate_rebalancing(warehouses, demands, costs):
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Variables: x[i, j] = amount to move from warehouse i to j
    transfers = {}
    for i in warehouses:
        for j in warehouses:
            if i != j:
                transfers[(i, j)] = solver.NumVar(0, solver.infinity(), f'tr_{i}_{j}')

    # Constraint: Capacity and Demand (Simplified)
    # Minimize Cost
    objective = solver.Objective()
    for (i, j), var in transfers.items():
        cost = costs.get((i, j), 1.0)
        objective.SetCoefficient(var, cost)
    
    objective.SetMinimization()
    status = solver.Solve()
    
    results = []
    if status == pywraplp.Solver.OPTIMAL:
        for (i, j), var in transfers.items():
            if var.solution_value() > 0:
                results.append({"from": i, "to": j, "amount": var.solution_value()})
    
    return results