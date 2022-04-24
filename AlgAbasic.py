import random
import time
from math import inf



dist_matrix = [[0, 12, 21, 4, 17, 13, 8, 35, 8, 7, 11, 14], [12, 0, 7, 9, 50, 31, 30, 12, 40, 20, 5, 21],
               [21, 7, 0, 15, 31, 14, 40, 5, 32, 30, 13, 9], [4, 9, 15, 0, 8, 9, 6, 30, 3, 10, 9, 15],
               [17, 50, 31, 8, 0, 4, 2, 30, 5, 40, 27, 15], [13, 31, 14, 9, 4, 0, 7, 10, 10, 34, 35, 4],
               [8, 30, 40, 6, 2, 7, 0, 53, 3, 20, 29, 15], [35, 12, 5, 30, 30, 10, 53, 0, 32, 50, 20, 6],
               [8, 40, 32, 3, 5, 10, 3, 32, 0, 25, 21, 16], [7, 20, 30, 10, 40, 34, 20, 50, 25, 0, 6, 32],
               [11, 5, 13, 9, 27, 35, 29, 20, 21, 6, 0, 25], [14, 21, 9, 15, 15, 4, 15, 6, 16, 32, 25, 0]]

iterations = 200
num_ants = 12
num_cities = 12
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

    return total


# Initialise phermone level
def initalizephermone():
    initial_phermone = num_cities / nearestNeighbour()
    phermone_matrix = [[initial_phermone for x in range(len(dist_matrix))] for y in range(len(dist_matrix))]
    return phermone_matrix


#Function to calculate distance
def calculateDistance(tour):
    distance = 0
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
    bestPathTour = []
    bestPathCost = float('inf') # Unbounded upper value for comparison
    startTime = time.time()
    pheromone = initalizephermone()
    ants = []
    inverse_distance = distanceReciprocal()
    while time.time() - startTime < 56:
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



