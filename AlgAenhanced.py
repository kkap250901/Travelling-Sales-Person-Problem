import time

from mysqlx import Result
startTime = time.time()

import random
from math import dist, inf
import read_file


dist_matrix =  read_file.main(535)

iterations = 200
num_ants = 12
num_cities = len(dist_matrix)
alpha = 1  # Phermone Factor
beta = 3 # Visibility Factor
evaporation_rate = 0.5  # Evaporation rate


def nearestNeighbour():
    ant = [random.randint(0,num_cities - 1)]
    current_city = ant[-1]
    next_probable_cities = [x for x in range(0, num_cities) if x not in ant]
    distances= []
    for city in next_probable_cities:
        distances.append((distanceNormal(current_city,city),city))#[20,30,40]#10
        current_city = min(distances, key = lambda t: t[0])[1]
        ant.append(current_city)
    total= calculateDistance(ant)

    return total, ant


# Initialise phermone level
def initalizephermone():
    result = nearestNeighbour()
    initial_phermone = num_cities / result[0]
    phermone_matrix = [[initial_phermone for x in range(len(dist_matrix))] for y in range(len(dist_matrix))]
    return phermone_matrix, result


#Function to calculate distance
def calculateDistance(tour):
    distance = 0
    # [4, 5, 11, 7, 2, 1, 10, 9, 0, 3, 8, 6]


    for i in range(-1,len(tour) - 1):
        distance += dist_matrix[tour[i]][tour[i + 1]]
    return distance


def distanceNormal(city1,city2):
    d = dist_matrix[city1][city2]
    return d


# To get the distance reciprocals   
def distanceReciprocal():
    distance_reciprocal = [[1/dis if dis != 0 else 1/(dis+0.000000000001) for dis in city] for city in dist_matrix]
    return distance_reciprocal


# Now we initalise ants
def initializeants(ants, phermone_matrix,inverse_matrix):
    for i in range(num_ants):
        ant = [random.randint(0, num_cities - 1)]
        for j in range(num_cities):
            current_city = ant[-1]
            next_probable_city = [x for x in range(0, num_cities) if x not in ant]
            # visited =  set(ant)
            # next_probable_city = not_visited - visited
            # next_probable_city = list(next_probable_city) # Just make sure this is right
            # print(type(next_probable_city))
            # print(len(next_probable_city))
            weighting = []
            for city in next_probable_city:
                # print(phermone_matrix[current_city][city])
                # print(inverse_distance[current_city][city])
                probability = (((inverse_matrix[current_city][city]) ** beta ) * (phermone_matrix[current_city][city] ** alpha))
                weighting.append(probability)
                # print(weighting)
                # print(len(weighting))
            if next_probable_city != []: 
                ant.append(random.choices(next_probable_city, weights=weighting)[0])
           
        ants.append(ant)
    return ants


# Phermone Deposit
def pheromoneDeposit(pheromone_matrix, ant, ant_length):
    # print(pheromone_matrix)
    for i in range(-1, num_cities - 1):
        # print(ant[i])
        # print(ant[i + 1])
        pheromone_matrix[ant[i]][ant[i + 1]] += 1 / ant_length
        pheromone_matrix[ant[i + 1]][ant[i]] += 1 / ant_length
    return pheromone_matrix


#pheromone Evaporation
def phermoneEvaporation(phermone):
    for j in range(len(phermone)):
        for i in range(len(phermone)):
            phermone[i][j] *= (1 - evaporation_rate)
    return phermone


# Create a random route for 1st comparison
def randomRoute():
    random_route = random.sample(range(1, num_cities + 1), num_cities)
    return random_route


#Running the Aco algorithm here
def runaco():
    pheromone,result = initalizephermone()
    bestPathTour = result[0]
    bestPathCost = result[1] # Unbounded upper value for comparison
    print(bestPathCost)
    ants = []
    inverse_distance = distanceReciprocal()
    iterations = 0 
    while time.time() - startTime < 1000:
        iterations += 1
        print(bestPathCost)
        ants = initializeants(ants,pheromone,inverse_distance)
        pheromone = phermoneEvaporation(pheromone)
    
        # print(pheromone)
        for ant in ants:
            antTourCost = calculateDistance(ant)

            if antTourCost < bestPathCost:
                bestPathCost = antTourCost
                bestPathTour = ant
            # print(len(pheromone))
            #[1,2,3,4,5,6,7,8,9,0,10,11,1]
            pheromone = pheromoneDeposit(pheromone, ant, antTourCost)
            # print(pheromone)
    print(bestPathTour)
    print(bestPathCost)

runaco()