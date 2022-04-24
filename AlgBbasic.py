# Genetic algorithm

# Cretaing the initial population
# selecting the best genes
# crossing over
# mutation to introdce variations

# Chromosome
# Start with randomly selected k chromosomes which is the population
# Each chromosome is a solution
# Crossover

# Creating the

import random

distances = [[0, 12, 21, 4, 17, 13, 8, 35, 8, 7, 11, 14], [12, 0, 7, 9, 50, 31, 30, 12, 40, 20, 5, 21],
             [21, 7, 0, 15, 31, 14, 40, 5, 32, 30, 13, 9], [4, 9, 15, 0, 8, 9, 6, 30, 3, 10, 9, 15],
             [17, 50, 31, 8, 0, 4, 2, 30, 5, 40, 27, 15], [13, 31, 14, 9, 4, 0, 7, 10, 10, 34, 35, 4],
             [8, 30, 40, 6, 2, 7, 0, 53, 3, 20, 29, 15], [35, 12, 5, 30, 30, 10, 53, 0, 32, 50, 20, 6],
             [8, 40, 32, 3, 5, 10, 3, 32, 0, 25, 21, 16], [7, 20, 30, 10, 40, 34, 20, 50, 25, 0, 6, 32],
             [11, 5, 13, 9, 27, 35, 29, 20, 21, 6, 0, 25], [14, 21, 9, 15, 15, 4, 15, 6, 16, 32, 25, 0]]

num_cities = len(distances)
populations = []
population_size = 100
mutation_probability = 0.1
iteration = 40000


# This creates a random route
def createRoute():
    random_route = random.sample(range(1, num_cities+1), num_cities)
    return random_route


# Creating the initial population
def createPopulation():
    population = []
    for i in range(population_size):
        population.append(createRoute())
    return population


# To calculate the distance between cities
def distance(city1, city2):
    length = distances[city1 - 1][city2 - 1]
    return length


# Calculating Distance of the path
def calculateDistance(local_population):
    distances_of_routes = []
    for i in range(len(local_population)):
        total_distance = 0
        for j in range(-1, num_cities - 1):
            total_distance = total_distance + distance(local_population[i][j], local_population[i][j + 1])  # Mayeb
        distances_of_routes.append(total_distance)
    return distances_of_routes


def calculate_fitness(distances_of_routes):
    fitness = []
    for i in range(population_size):
        g = 1 / distances_of_routes[i]
        fitness.append(g)

    return fitness


def mutation(cities):
    # Here mutation could still mean that 1st and 2nd index are same
    # so imp. could be 1st != 2nd ind
    probability = random.random()  # Make sure this is ok
    if probability < mutation_probability:
        first_index = random.randint(0, num_cities - 1)
        second_index = random.randint(0, num_cities - 1)
        cities[first_index], cities[second_index] = cities[second_index], cities[first_index]
    return cities


# change it to tour
def crossover(fitness, local_population):
    parent1_index = local_population.index(random.choices(local_population, weights=fitness)[0])
    # print(parent1_index)
    # Another improvement could be only selecting the best
    # parents writing another function for the best selection
    parent2_index = local_population.index(random.choices(local_population, weights=fitness)[0])  # Maybe that p1=p2
    # so imp could be p1!=p2

    parent1 = local_population[parent1_index]
    parent2 = local_population[parent2_index]

    random_index = random.randint(0, len(parent1) + 1)

    child1 = parent1
    child2 = parent2

    child1 = parent1[:random_index] + parent2[random_index:]
    child2 = parent2[:random_index] + parent2[random_index:]

    # if calculateDistance_for_one_tour(child2,1,)
    def remove_duplicates(array1, array2):
        seen = set()
        for i in range(len(array1)):
            if array1[i] not in seen:
                seen.add(array1[i])
            else:
                array1[i] = [elem for elem in array2 if elem not in array1][0]
        return array1

    child1_no_dup = remove_duplicates(child1, child2)
    child2_no_dup = remove_duplicates(child2, child1)
    distance1 = calculateDistance([child1_no_dup, child2_no_dup])
    if distance1[0] > distance1[1]:
        return child1_no_dup
    else:
        return child2_no_dup


def geneticAlgorithm():
    local_population = createPopulation()  # A random population is being generated
    distance_of_routes = calculateDistance(local_population)
    fitness = calculate_fitness(distance_of_routes)
    for i in range(iteration):
        New_Pop = []
        for j in range(len(local_population)):
            z = crossover(fitness, local_population)
            z = mutation(z)
            New_Pop.append(z)
        local_population = New_Pop
    distance1 = calculateDistance(local_population)
    min_dis = min(distance1)
    route = local_population[distance1.index(min_dis)]
    print(route)
    print(min_dis)


geneticAlgorithm()
