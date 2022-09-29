############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############

import os
import sys
import time
import random

############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES WILL NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############

input_file = "AISearchfile012.txt"

############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

##### begin change 1 #####
the_particular_city_file_folder = "city-files"
path_for_city_files = "../" + the_particular_city_file_folder
##### end change 1   #####
    
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the folder '" + the_particular_city_file_folder + "'.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############

############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME, E.G., 'abcd12'.
############

##### begin change 2 #####
the_particular_alg_codes_and_tariffs = "alg_codes_and_tariffs.txt"
path_for_alg_codes_and_tariffs = "../" + the_particular_alg_codes_and_tariffs
##### end change 2   #####

code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############

my_user_name = "ccbd24"

############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############

my_first_name = "Kush"
my_last_name = "Kapur"

############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############

algorithm_code = "AC"

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############


num_ants = 50
num_cities = len(dist_matrix)
#Pheromone Factor
alpha = 1  
#Visibility Factor
beta = 5
#Evaporation Rate
evaporation_rate = 0.5
#Probability of constructing the current best solution after stagnation
ProbabilityBest = 0.1
AverageCities = num_cities / 2
#Smoothing constant 
smoothingParameter = 0.8
startTime = time.time()
#Adaptive mutation probability max
mutation_probability_max = 0.5
#Adaptive mutation probability min
mutation_probability_min = 0.1  
#Constant multiplier 
constantMultiplier = 100


#Nearest Neighbour algorithm which is essentially basic greedy algorithm to calculate the initial phermone levels
def nearestNeighbour():
    ant = [random.randint(0,num_cities - 1)]
    current_city = ant[-1]
    while len(ant) != num_cities:
        next_probable_cities = [x for x in range(0, num_cities) if x not in ant]
        distances= []
        for city in next_probable_cities:
            distances.append((distanceNormal(current_city,city),city))
        current_city = min(distances, key = lambda t: t[0])[1]
        ant.append(current_city)
    total= calculateDistanceNormal(ant)

    return total,ant


# Initialise phermone level
def initalizephermone():
    total,ant = nearestNeighbour()
    initial_phermone = num_cities / total # Initial Pheromone Levels
    phermone_matrix = [[initial_phermone for x in range(len(dist_matrix))] for y in range(len(dist_matrix))]
    return phermone_matrix ,ant,total


#Function to calculate distance of a tour
def calculateDistanceNormal(tour):
    distance = 0
    for i in range(-1,len(tour) - 1):
        distance += dist_matrix[tour[i]][tour[i + 1]]
    return distance


#Funciton to calculate distance of an array of ants
#returns a distance matrix corresponding to each tour in array
def calculateDistance(ants):
    distances_of_routes = []
    for i in range(len(ants)):
        total_distance = 0
        for j in range(-1, num_cities - 1):
            total_distance = total_distance + distanceNormal(ants[i][j],ants[i][j+1])  # Mayeb
        distances_of_routes.append(total_distance)
    return distances_of_routes


#Just normal distance calculator between 2 cities
def distanceNormal(city1,city2):
    d = dist_matrix[city1][city2]
    return d


# To get the distance reciprocals   
def distanceReciprocal():
    distance_reciprocal = [[1/dis if dis != 0 else 1/(dis+0.000000000001) for dis in city] for city in dist_matrix]
    return distance_reciprocal


#Enhancement Part of Aco with a combination with Genetic

#Enhancement 1 To calculate fitness of a route 
def calculate_fitness(distances_of_routes):
    fitness = []
    for i in range(num_ants):
        g = 1 / distances_of_routes[i]
        fitness.append(g)
    return fitness


def calculate_avg_fitness(fitness):
    avg = sum(fitness)/num_ants
    return avg


#Enhancement 2
#Mutation function with adapative probabiliry
def mutation(cities,fitness):
    probability = random.random()
    avg_fitness = calculate_avg_fitness(fitness)
    for i in range(num_ants):
        #Threshold being average fitness
        #Here solutions with fitness greater than threshold have lower mutation probability
        if fitness[i] > avg_fitness:
            adaptive_probability = (mutation_probability_max * (mutation_probability_max - mutation_probability_min)) / (max(fitness)-avg_fitness)
        else:
            adaptive_probability = mutation_probability_max

    #Just when probability being a random number
    if probability < adaptive_probability:
        first_index = random.randint(0, num_cities - 1)
        second_index = random.randint(0, num_cities - 1)
        cities[first_index], cities[second_index] = cities[second_index], cities[first_index]
    return cities


#Enhancement 3
#Written specifically for Crossover function to ensure parents are different
def normalMutation(cities):
    first_index = random.randint(0, num_cities - 1)
    second_index = random.randint(0, num_cities - 1)
    cities[first_index], cities[second_index] = cities[second_index], cities[first_index]
    return cities


#Enhancement 4
#Crossover of 2 best ants to find the best possible route
def greedy_crossover(fitness,local_population):
    #This is the first ant from the population
    parent1_index = local_population.index(random.choices(local_population, weights=fitness)[0])
    #This is the second ant from the population to crossover
    parent2_index = local_population.index(random.choices(local_population, weights=fitness)[0])

    parent1 = [x for x in local_population[parent1_index]]
    parent2 = [x for x in local_population[parent2_index]]

    #Random starting city
    start_city = random.randint(0,num_cities - 1)
    #Initialising the child
    child = [start_city]

    #Enhancement 5
    if parent1 == parent2:
        #To ensure both parents are differnt mutation for certain is performed
        #Ensures diversity in chromosomes and improves local search ability 
        parent2 = normalMutation(parent2)
    for i in range(num_cities-1):
        current_city = child[-1]#Current city as the last element 
        left_option_1 = parent1[(parent1.index(current_city) - 1) % len(parent1)] #Doubly linked list 
        right_option_1 = parent1[(parent1.index(current_city) + 1) % len(parent1)] #Two pointers for edges
        left_option_2 = parent2[(parent2.index(current_city) - 1) % len(parent2)] # Checking which edges we can traverse
        right_option_2 = parent2[(parent2.index(current_city) + 1) % len(parent2)]
        probable_city = [left_option_1,right_option_1,left_option_2,right_option_2]
        next_city = min(probable_city,key = lambda x : dist_matrix[current_city][x])# List of cities that can be visited
        child.append(next_city)
        parent1.remove(current_city) # Removal ensuring no need possibility of gene repetion 
        parent2.remove(current_city)
    return child


#Enhancement 6
#A changed Initialise function compared to normal below
def initializeants2(ants, phermone_matrix,inverse_matrix,dis_matix_current_pop,newPopuation): # Enhancements 
    #First initilaise empty ants array
    ants = []
    #But now only go through the top 80% performers
    for i in range(num_ants // 5,num_ants):
        #Random Starting city
        ant = [random.randint(0, num_cities - 1)]
        for j in range(num_cities):
            current_city = ant[-1]
            next_probable_city = [x for x in range(0, num_cities) if x not in ant]

            #For Probability
            weighting = []

            for city in next_probable_city:
                probability = (((inverse_matrix[current_city][city]) ** beta ) * (phermone_matrix[current_city][city] ** alpha))
                weighting.append(probability)

            if next_probable_city != []: 
                ant.append(random.choices(next_probable_city, weights=weighting)[0])
        #This is done for 80% of the routes  
        ants.append(ant)
    #The rest 20% comes from genetic part of the algorithm 
    #This is from the population created by the genetic algo and we use the top 20% of those
    sorted_indices_current_pop = [i[0] for i in sorted(enumerate(dis_matix_current_pop),key = lambda x :x[1])]
    for i in range(num_ants // 5):
        ants.append(newPopuation[sorted_indices_current_pop[i]])

    #Just returning a multi dimensional array of routes 
    return ants


# This funciton is only used at start when there is no population created by GA 
def initializeants(ants, phermone_matrix,inverse_matrix):
    ##Initialising empty ants 
    ants = []
    for i in range(num_ants):
        ant = [random.randint(0, num_cities - 1)]
        for j in range(num_cities):
            #Keeping track of the current city that ant is on 
            current_city = ant[-1]
            next_probable_city = [x for x in range(0, num_cities) if x not in ant]

            weighting = []

            #Adding the probabilities into the array
            for city in next_probable_city:
                probability = (((inverse_matrix[current_city][city]) ** beta ) * (phermone_matrix[current_city][city] ** alpha))
                weighting.append(probability)

            if next_probable_city != []: 
                ant.append(random.choices(next_probable_city, weights=weighting)[0])
        ants.append(ant)
    return ants


# This stagnation funciton calculates if one or more path is closing the max value
# Also calculating when all other paths are nearing min value 
#Enhancement 7
def calculateStagnation(phermone,MaxPhermoneLevel,MinPhermoneLevel):
    sum = 0
    for i in range(num_cities):
        for j in range(num_cities):
            #Stagnation function here
            sum += min(MaxPhermoneLevel - phermone[i][j], phermone[i][j] - MinPhermoneLevel)
    stagnation = sum / pow(num_cities,2) #Just here change

    return stagnation


#Calculating Max Pheromone Levels
#Enhancement 8
def MaxPhermone(bestGlobalDis):
    MaxPhermone = (1/(1-evaporation_rate))*(constantMultiplier/bestGlobalDis)
    return MaxPhermone


# Calculating the Min Pheromone Levels
# Enhancement 9 
def MinPhermone(MaxPhermone):
    MinPhermone = (MaxPhermone * (1 - pow(ProbabilityBest,1/num_cities)))/((AverageCities - 1) * pow(ProbabilityBest,1/num_cities))
    return MinPhermone


# Phermone Deposit
# Enhancement 10
def pheromoneDeposit(pheromone_matrix, ant, localBestLength,localbestTour,Globalbestlength,globalBestTour,iteration):

    #Every 10th iteration the global max is used to ensure moving in the right direction
    if iteration % 10 == 0 :
        for i in range(-1, num_cities - 1):
            #Finding out if the edge is present inside the global best tour
            coresspondingIndex = globalBestTour.index(ant[i])
            #Then we test if it is present inside the global best tour and we deposit pheromone
            if ant[i+1] == globalBestTour[(coresspondingIndex + 1) % num_cities] or ant[i+1] == globalBestTour[coresspondingIndex - 1]:
                pheromone_matrix[ant[i+1]][ant[i]] += constantMultiplier/Globalbestlength
                pheromone_matrix[ant[i]][ant[i+1]] += constantMultiplier/Globalbestlength 
            elif ant[i-1] == globalBestTour[(coresspondingIndex + 1) % num_cities] or ant[i-1] == globalBestTour[coresspondingIndex - 1]:
                pheromone_matrix[ant[i-1]][ant[i]] += constantMultiplier/Globalbestlength
                pheromone_matrix[ant[i]][ant[i-1]] += constantMultiplier/Globalbestlength

    #Local best length 
    else:
        #Finding out if the edge is inside the best local tour
        #Then we deposit on those edges 
        for i in range(-1, num_cities - 1): 
            coresspondingIndex = localbestTour.index(ant[i])
            if ant[i+1] == localbestTour[(coresspondingIndex + 1)% num_cities] or ant[i+1] == localbestTour[coresspondingIndex - 1]:
                pheromone_matrix[ant[i+1]][ant[i]] += constantMultiplier/localBestLength
                pheromone_matrix[ant[i]][ant[i+1]] += constantMultiplier/localBestLength 
            elif ant[i-1] == localbestTour[(coresspondingIndex + 1)% num_cities] or ant[i-1] == localbestTour[coresspondingIndex - 1]:
                pheromone_matrix[ant[i-1]][ant[i]] += constantMultiplier/localBestLength
                pheromone_matrix[ant[i]][ant[i-1]] += constantMultiplier/localBestLength
    return pheromone_matrix


#pheromone Evaporation
def phermoneEvaporation(phermone,min,max):
    for j in range(len(phermone)):
        for i in range(len(phermone)):
            phermone[i][j] *= (1 - evaporation_rate)
            if phermone[i][j] < min:
                phermone[i][j] = min
            elif phermone[i][j] > max:
                phermone[i][j] = max
    return phermone


#This is when stagnation occurs then we deposit the pheromones
def phermoneSmoothing(phermone,Maxphermone,stagnation):
    if stagnation < 0.1:
        for i in range(num_cities):
            for j in range(num_cities):
                phermone[i][j] += smoothingParameter * (Maxphermone - phermone[i][j])
    return phermone


#Running the Aco algorithm here
def runaco():
    #Enhancement 11 : decreases number of comparisons 
    #First tours here are from the nearest neighbour algo
    pheromone,bestPathTour,bestPathCost = initalizephermone()
    #Initialising the max pheromone level
    MaxPhermoneLevel = MaxPhermone(bestPathCost)
    #Initialising the min pheromone level
    MinPhermoneLevel = MinPhermone(MaxPhermoneLevel)
    ants = []
    #Finding inverse distances from distance matrix
    inverse_distance = distanceReciprocal()
    #Initilising the iterations for some conditions ahead
    iterations = 0 
    #Initalise the ants only use funciton here not used agaian
    ants = initializeants(ants,pheromone,inverse_distance)
    while time.time() - startTime < 55:
        iterations += 1
        #This here is distance array for routes of ants
        antDisMatrix = calculateDistance(ants)
        #Find the local best length
        LocalBestLength = min(antDisMatrix)
        #best ant found 
        bestAnt = antDisMatrix.index(LocalBestLength)
        #Now using index of best ant we find the local max tour
        LocalBestTour = ants[bestAnt]
        #Now calculate fitness of those distances of tours
        fitness = calculate_fitness(antDisMatrix)

        #This is the new populaiton created by GA
        NewPop =[]
        for m in range(num_ants):
            newants = greedy_crossover(fitness,ants)
            newants = mutation(newants,fitness)
            NewPop.append(newants)
            #Find the best distance 
            dis2 = calculateDistance(NewPop)

        if min(dis2) < LocalBestLength: #Here local best length is updated 
            LocalBestLength = min(dis2) # We have the new local best length here
            LocalBestTour = NewPop[dis2.index(min(dis2))] #Here the local best tour is updated 

        #Here Global path cost is updated 
        if LocalBestLength < bestPathCost:
                #If global updated the max and min pheromone levels recalculated
                bestPathCost = LocalBestLength
                bestPathTour = LocalBestTour
                MaxPhermoneLevel = MaxPhermone(bestPathCost)
                MinPhermoneLevel = MinPhermone(MaxPhermoneLevel)

        #For each route inside the ants matrix we deposit the pheromones
        for ant in ants:
            pheromone = pheromoneDeposit(pheromone,ant,LocalBestLength,LocalBestTour,bestPathCost,bestPathTour,iterations) 

        #Only calculate stagnation at every 8th iteration to save time
        if iterations % 8 == 0:
            stagnation = calculateStagnation(pheromone,MaxPhermoneLevel,MinPhermoneLevel)
            pheromone = phermoneSmoothing(pheromone,MaxPhermoneLevel,stagnation)
        

        #Pheromones are evaporated but also looked for any values lower than min or max levels
        pheromone = phermoneEvaporation(pheromone,MinPhermoneLevel,MaxPhermoneLevel)

        #Here we call the new function which uses the New pop made and 
        #The top 20 percent of new pop is appended with 
        #80% of ants initalised by phermone probability calculation 
        ants = initializeants2(ants,pheromone,inverse_distance,dis2,NewPop)

    print(bestPathTour)
    print(bestPathCost)
    return bestPathTour,bestPathCost

tour,tour_length = runaco()


############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############

############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S,
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATA AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")
    
    











    


