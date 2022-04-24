from random import random

import numpy as np
random.seed(40)

d = np.array([[0, 12, 21, 4, 17, 13, 8, 35, 8, 7, 11, 14], [12, 0, 7, 9, 50, 31, 30, 12, 40, 20, 5, 21],
              [21, 7, 0, 15, 31, 14, 40, 5, 32, 30, 13, 9], [4, 9, 15, 0, 8, 9, 6, 30, 3, 10, 9, 15],
              [17, 50, 31, 8, 0, 4, 2, 30, 5, 40, 27, 15], [13, 31, 14, 9, 4, 0, 7, 10, 10, 34, 35, 4],
              [8, 30, 40, 6, 2, 7, 0, 53, 3, 20, 29, 15], [35, 12, 5, 30, 30, 10, 53, 0, 32, 50, 20, 6],
              [8, 40, 32, 3, 5, 10, 3, 32, 0, 25, 21, 16], [7, 20, 30, 10, 40, 34, 20, 50, 25, 0, 6, 32],
              [11, 5, 13, 9, 27, 35, 29, 20, 21, 6, 0, 25], [14, 21, 9, 15, 15, 4, 15, 6, 16, 32, 25, 0]])
n_ants = 12
number_cities = 12


def initalizephermone(number_ants, num_cities):
    phermone = [[0.1] * number_ants] * number_ants
    #Just need to make the diagnols = 0 
    return phermone


def get_inv_distance(distance_matrix):
    distance_reciprocal = 1 / distance_matrix
    distance_reciprocal[distance_reciprocal == np.inf] = 0
    return distance_reciprocal


def initialisepath(num_ants, num_cities):
    path = np.ones((num_ants, num_cities + 1))  # For a last return city
    return path


def initaliseants_into_path(path, iteration, num_cities):
    for ite in range(iteration):
        start_city = random.randint(1, num_cities + 1)
        path[:, 0] = start_city
        path[:, num_cities] = start_city
    return path


def phermone_evaporation(phermone, evapopration_rate):
    phermone = phermone * (1 - evapopration_rate)
    return phermone


def phermoneDeposit(phermone,):
    pass

def ant_movement(num_cities, inv_distances, path, phermone, alpha, beta, number_ants):
    for ant in range(number_ants):
        inverse_distances_copy = np.array(inv_distances)

        for cities in range(num_cities - 1):
            probability = [0] * num_cities
            total = [0] * num_cities
            current_location = int(path[ant, cities] - 1)

            inverse_distances_copy[:, current_location] = 0
            phermone_matrix = np.power(phermone[current_location, :], beta)
            inverse_distances_matrix = np.power(inverse_distances_copy[current_location, :], alpha)
            phermone_matrix = phermone_matrix.reshape(num_cities, 1)
            inverse_distances_matrix = inverse_distances_matrix.reshape(num_cities, 1)

            all_varaibles = np.multiply(phermone_matrix, inverse_distances_matrix)
            total = np.sum(all_varaibles)
            probability = all_varaibles / total
            probability_of_next = np.cumsum(probability)

            r = np.random.random_sample()  # randon no in [0,1)
            # print(r)
            next_city = np.nonzero(probability_of_next > r)[0][0] + 1

            path[ant, cities + 1] = next_city  # adding city to route

        left_cities = list(set([i for i in range(1, num_cities + 1)]) - set(path[ant, :-2]))[0]  # finding the last
        # untraversed city to route
        path[ant, -2] = left_cities  # adding untraversed city to route

    return path


def depositPhermone(pheromne, dist_cost, optimal_path, num_ants, num_cities):
    for i in range(num_ants):
        for j in range(num_cities - 1):
            dt = 1 / dist_cost[i]
            pheromne[int(optimal_path[i, j]) - 1, int(optimal_path[i, j + 1]) - 1] = pheromne[int(optimal_path[i, j]) - 1, int(optimal_path[i, j + 1]) - 1] + dt  # make this into another funct
    return pheromne


def runaco(dist_matrix, num_ants, num_cities, evaporation, alpha, beta, iteration):
    # Finding the inverse distances
    inv_distance = get_inv_distance(dist_matrix)

    # Initalising Phermone
    Phermone = initalizephermone(num_ants, num_cities)

    # Initialising route
    path = initialisepath(num_ants, num_cities)
    path = initaliseants_into_path(path, iteration, num_cities)  # Initalise positions of ants

    path = ant_movement(num_cities, inv_distance, path, Phermone, alpha, beta, num_ants)

    optimal_path = np.array(path)  # intializing optimal route

    dist_cost = np.zeros((num_ants, 1))  # intializing total_distance_of_tour with zero

    for i in range(num_ants):
        s = 0
        for j in range(num_cities - 1):
            s = s + dist_matrix[int(optimal_path[i, j]) - 1, int(optimal_path[i, j + 1]) - 1]  # calcualting total
            # tour distance
        dist_cost[i] = s  # storing distance of tour for 'i'th ant at location 'i'

    dist_min_loc = np.argmin(dist_cost)  # finding location of minimum of dist_cost
    dist_min_cost = dist_cost[dist_min_loc]  # finging min of dist_cost

    best_route = path[dist_min_loc, :]  # intializing current traversed as best route
    Phermone = phermone_evaporation(Phermone, evaporation)  # evaporation of pheromne with (1-e)

    Phermone = depositPhermone(Phermone, dist_cost, optimal_path, num_ants, num_cities)

    print('route of all the ants at the end :')
    print(optimal_path)
    print()
    print('best path :', best_route)
    print('cost of the best path', int(dist_min_cost[0]) + d[int(best_route[-2]) - 1, 0])
    return optimal_path


iterations = 200
n_ants = 12
n_citys = 12

# intialization part

m = n_ants
n = n_citys
e = .5  # evaporation rate
a = 1  # pheromone factor
b = 3

runaco(d, m, n, e, a, b, iterations)
