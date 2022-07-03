from copy import deepcopy
from itertools import permutations



re
def solution(times, time_limit):
    if len(times) <= 2:
        return []
    
    graph = convert_to_graph(times)
    
    return bellman_ford(times, graph, time_limit, "Start")


def floyd_warshall(matrix):
    l = len(matrix)
    shortest_paths = deepcopy(matrix)
    
    for k in range(l):
        for i in range(l):
            for j in range(l):
                if shortest_paths[i][k] + shortest_paths[k][j] < shortest_paths[i][j]:
                    shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]
                    
    return shortest_paths


def bellman_ford(matrix, graph, time_limit, source):
    dist, prev = bellman_ford_initialize(graph, source)
    
    for number in range(len(graph) - 1):
        for node in graph:
            temp = dict(graph)
            del temp[node]
            
            for neighbor in temp:
                relax_edges(graph, dist, node, neighbor, prev)

    # Check for negative_cycles
    for node in graph:
        for neighbor in graph:
            n_index = neighbor_index(neighbor, len(graph))
            
            if dist[node] + graph[node][n_index] < dist[neighbor]:
                return [number for number in range(0, len(graph) - 2)]

    shortest_paths = floyd_warshall(matrix)
    
    return rescue_max_bunnies(matrix, shortest_paths, time_limit)


def rescue_max_bunnies(matrix, shortest_paths, time_limit):
    n = len(matrix) - 2
    bunny_ids = []

    for number in range(n):
        bunny_ids.append(number)
        
    possible_sets = sorted(subset_generator(bunny_ids))
    best_bunnies = []
    
    for subset in possible_sets:
        for permutation in permutations(subset):
            print(permutation)
            subset_sum = 0
            prev = 0
            next = len(matrix) - 1
            
            for bunny_id in permutation:
                next = bunny_id + 1
                subset_sum += shortest_paths[prev][next]
                prev = next

            subset_sum += shortest_paths[prev][len(matrix) - 1]

            if subset_sum <= time_limit and len(subset) > len(best_bunnies):
                best_bunnies = subset

                if len(best_bunnies) == n:
                    break
            else:
                pass
            
    return best_bunnies


def subset_generator(list):
    l = len(list)
    masks = [1 << i for i in range(l)]
    
    for i in range(1 << l):
        yield [subset for mask, subset in zip(masks, list) if i & mask]


def neighbor_index(neighbor, graph_size):
    if neighbor == "Finish":
        return graph_size - 1
    elif neighbor == "Start":
        return 0
    else:
        return int(neighbor) + 1


def convert_to_graph(matrix):
    keys = ["Start"]
    
    for number in range(1, len(matrix) - 1):
        keys.append(number - 1)
        
    keys.append("Finish")
    graph = dict(zip(keys, matrix))
    
    return graph


def bellman_ford_initialize(graph, source):
    distance = {}
    previous = {}
    
    for node in graph:
        distance[node] = 1000
        previous[node] = None
        
    distance[source] = 0
    
    return distance, previous


def relax_edges(graph, distance, node, neighbor, previous):
    n_index = neighbor_index(neighbor, len(graph))
    
    if distance[node] + graph[node][n_index] < distance[neighbor]:
        distance[neighbor] = distance[node] + graph[node][n_index]
        previous[neighbor] = node


if __name__ == '__main__':
    case1 = [[0, 1, 1, 1, 1],
             [1, 0, 1, 1, 1],
             [1, 1, 0, 1, 1],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 1, 0]]
    print("\n\nCase 1: Provided test case 1.\nTime limit: 3")
    for row in case1:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case1, 3)))

    print("\n\nCase 2: Provided test case 2.\nTime limit: 1")
    case2 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, -1],
             [9, 3, 0, 2, -1],
             [9, 3, 2, 0, -1],
             [9, 3, 2, 2, 0]]
    for row in case2:
        print('', row)
    print("\n  Expected: [1, 2]\nCalculated:", str(solution(case2, 1)))

    print("\n\nCase 3: Infinite negative cycle.\nTime limit: -500")
    case3 = [[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]]
    for row in case3:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case3, -500)))

    print("\n\nCase 4: Max bunnies. None rescuable.\nTime limit: 1")
    case4 = [[1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]]
    for row in case4:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case4, 1)))

    print("\n\nCase 5: One bunny.\nTime limit: 2")
    case5 = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    for row in case5:
        print('', row)
    print("\n  Expected: [0]\nCalculated:", str(solution(case5, 2)))

    print("\n\nCase 6: Multiple revisits.\nTime limit: 10")
    case6 = [[0, 5, 11, 11, 1],
             [10, 0, 1, 5, 1],
             [10, 1, 0, 4, 0],
             [10, 1, 5, 0, 1],
             [10, 10, 10, 10, 0]]
    for row in case6:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case6, 10)))

    print("\n\nCase 7: Multiple Revisits 2.\nTime limit: 5")
    case7 = [[0, 10, 10, 10, 1],
             [0, 0, 10, 10, 10],
             [0, 10, 0, 10, 10],
             [0, 10, 10, 0, 10],
             [1, 1, 1, 1, 0]]
    for row in case7:
        print('', row)
    print("\n  Expected: [0, 1]\nCalculated:", str(solution(case7, 5)))

    print("\n\nCase 8: Time travel.\nTime limit: 1")
    case8 = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    for row in case8:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case8, 1)))

    print("\n\nCase 9: No bunnies.\nTime limit: 1")
    case9 = [[2, 2],
             [2, 2]]
    for row in case9:
        print('', row)
    print("\n  Expected: []\nCalculated:", str(solution(case9, 1)))

    print("\n\nCase 10: Backwards bunny path.\nTime limit: 6")
    case10 = [[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]]
    for row in case10:
        print('', row)
    print("\n  Expected: [0, 1, 2]\nCalculated:", str(solution(case10, 6)))
