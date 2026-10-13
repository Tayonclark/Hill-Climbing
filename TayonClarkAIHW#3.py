Heuristic = {
    "A": 7,
    "B": 5,
    "C": 3,
    "U": 4,
    "E": 2,
    "G": 3,
    "I": 6,
    "J": 2,
    "K": 1,
    "Y": 2,
    "M": 0
}

State_space_graph = {
    "A": ["B", "C", "U"],
    "B": ["E", "G"],
    "C": ["G", "I", "J"],
    "U": ["K", "Y"],
    "E": ["G", "M"],
    "G": ["M"],
    "I": ["M"],
    "J": ["K"],
    "K": ["J"],
    "Y": ["M"],
    "M": []

}

def Hill_Climbing(start_state, goal_state):
    current = start_state
    path = [current]

    while current != goal_state:
        print(f"Current node: {current}, Heauristic  = {Heuristic[current]}")
        neighbor_nodes = State_space_graph[current]

        if not neighbor_nodes:
            print("No Neighboring Nodes.")
            return  path, False

        Lowest_heuristic_neighbor = min(neighbor_nodes, key=lambda node: Heuristic[node])

        if Heuristic[Lowest_heuristic_neighbor] >= Heuristic[current]:
            print("No appropriate neighbor found. Hill Climbing terminates.")
            return path, False

        current = Lowest_heuristic_neighbor
        path.append(current)
    print(f"Goal-State reached:{goal_state}")
    return path, True

path, Correct = Hill_Climbing("A", "M")
print(" -> ".join(path))
print("Correct =", Correct)

