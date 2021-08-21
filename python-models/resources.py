from matplotlib import pyplot as plt
import numpy as np
import math
import time
import itertools


# Foundational functions for defining and visualizing the problem

def connectpoints(ax,x1,y1,x2,y2):
    ax.plot([x1,x2],[y1,y2],'r-')

# Used as the core of the fitness function in the genetic algorithm
def get_distance(x1,y1,x2,y2):
    d = round(math.hypot(x2-x1, y2-y1),2)
    return d

def generate_cities(n_cities):
    coordinates = []
    for i in range(n_cities):
        coordinates.append((np.random.randint(0,100), np.random.randint(0,100)))

    x = [coordinate[0] for coordinate in coordinates]
    y = [coordinate[1] for coordinate in coordinates]
    
    return coordinates, x, y


# Used to find an exact 100% Optimized solution for a given set of cities. Problem scales in exponential time as
# the number of cities being calculated increases. One test of 11 cities required around 16 minutes to process and 
# the resulting object containing all possible solutions was about 6GB. Clearly if we want to determine reasonably
# efficient solutions we will need to make use of heuristics.

# clean this up to only take a set of coordinates? a little redundant to require x and y considering they are derivatices of coordinates
def exact_solution(coordinates, x, y):
    
    
    start = time.process_time()

    # Generate a list of all possible combinations or routes from point to point
    combs = itertools.permutations(coordinates, len(coordinates))

    #Iterate through the permutation generator and append each uniquie route to 'routes'. Routes that are identical forward and backwards are removed since they are equal in distance.
    routes = []
    for p in combs:
        if p[0] <= p[-1]:
            routes.append(list(p))

    #For each route, calculate the total distance
    for route in routes:
        distance = 0
        for i in range(len(route)):
            try:
                d = get_distance(route[i][0], route[i][1],route[i+1][0], route[i+1][1])
                distance = distance + d
            except:
                route.append(round(distance,2))
                continue


    end = time.process_time()
    path_count = len(routes)
    process_time = str(end-start)
    print(process_time)
    print('Number of paths generated: ' + str(len(routes)))
    
    #Identify the path of shortest and longest distance
    optimum = min(routes, key = lambda t: t[(len(routes[0])-1)])
    worst = max(routes, key = lambda t: t[(len(routes[0])-1)])
    
    return optimum, worst, x, y, path_count


# Given variables returned by the above function, create a matlab plot
def graph_solution(optimum, worst, x, y, path_count, n_cities): 
    #graph the cities without solution:
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.plot(x, y, 'o', color='black');
    ax1.axis('equal')
    ax1.set_title(str(n_cities) + ' Cities, ' + str(path_count) + ' Paths' )
    ax2.plot(x, y, 'o', color='black');

    for i in range(len(optimum)-1):
        try:
            connectpoints(ax2, optimum[i][0],optimum[i][1],optimum[i+1][0],optimum[i+1][1])
        except:
            continue
    ax2.axis('equal')
    ax2.set_title(str(n_cities) + ' Cities, Total Distance: ' + str(optimum[-1]))


    ax1.axes.xaxis.set_visible(False)
    ax1.axes.yaxis.set_visible(False)
    ax2.axes.xaxis.set_visible(False)
    ax2.axes.yaxis.set_visible(False)

    fig.show()
    

def graph_cities(coordinates):

    x = [coordinate[0] for coordinate in coordinates]
    y = [coordinate[1] for coordinate in coordinates]
    
    fig, ax = plt.subplots(1, 1, figsize=(7.5,6))

    ax.plot(x, y, 'o', color='black');
    ax.axis('equal')
    

    #ax1.axes.xaxis.set_visible(False)
    #ax1.axes.yaxis.set_visible(False)


    fig.show()

    #image = fig.savefig('coordinates.jpg')

    return fig, ax


# Given a set of coordinates and a given route through said coordinates, graph the
# problem and solution
def graph_route(coordinates, route):

    x = [coordinate[0] for coordinate in coordinates]
    y = [coordinate[1] for coordinate in coordinates]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,10))

    fig.suptitle('Generated Cities vs Solution', fontsize=16)

    ax1.plot(x, y, 'o', color='black');
    ax1.axis('equal')
    
    ax2.plot(x, y, 'o', color='black');

    for i in range(len(route)-1):
        try:
            connectpoints(ax2, route[i][0],route[i][1],route[i+1][0],route[i+1][1])
        except:
            continue
    ax2.axis('equal')
    


    ax1.axes.xaxis.set_visible(False)
    ax1.axes.yaxis.set_visible(False)
    ax2.axes.xaxis.set_visible(False)
    ax2.axes.yaxis.set_visible(False)

    fig.show()

    #image = plt.savefig(fig)

    return fig, ax1, ax2

# Genetic Algorithm Functions:

# Given a set of coordinates, generate an "individual" in the sense that it is a 
# Single member of a population, a single potenial solution for the given problem.
# Since any given set of coordinates cannot apear twice we must eliminate any repeats.
# TODO: Eliminate the usage of random numbers to increase performance
def generate_individual(coordinates):
    ind = []
    i = 0
    while i < len(coordinates):
        gene = np.random.randint(0, len(coordinates))
        if coordinates[gene] not in ind:
            ind.append(coordinates[gene])
            i += 1
    return ind

#A given solution or "individual" will be a list of tuple coordinates:
# [(1,34),(34,55),(75,11),(78,57)]  A four bit individual
# A population will be a list of individuals of n size given by:
def generate_population(coordinates, inital_population_size):
    
    population = []
    
    for i in range(inital_population_size):
        ind = generate_individual(coordinates)
        population.append(ind)
            
    return population


# A fitness function is what will be used to determine any given solutions
# performance in the context of the problem. We accomplish this by cacluclating the
# total distance of the path taken by the route and apply selective pressure towards
# minimizing this value:
def evaluate(route):
    distance = 0
    for i in range(len(route)):
        try:
            d = get_distance(route[i][0], route[i][1],route[i+1][0], route[i+1][1])
            distance = distance + d
        except:
            continue
    return distance


# An expanded evaluation function to determine fitness across all individuals in a population
def evaluate_population(population):
    evals = []
    for i in range(len(population)):
        ev = (evaluate(population[i]), i)
        evals.append(ev)
    
    avg = 0
    for entry in evals:
        avg += entry[0]
        
    avg = avg/(len(evals))
    #print('Population size: ' + str(len(population)) + "\nAverage Fitness: " + str(avg))
    
    return evals


# Given a list of individuals (a population) along with their coordesponding 
# evaluations, return the individual with the shortest distance route

#Identify the best individual in a given population
def select_best(evals, population):
    
    best_to_worst = sorted(evals)
    best = best_to_worst[0]
    
    return population[best[1]], best[0]

# Return the best performing solution from a random group of 10% of the population
def select_parent(population, evals):
    
    #grab a list of random parents
    random_parents = []
    for i in range(int(len(population)*0.1)):
        ind = np.random.randint(0, len(population))
        random_parents.append([population[ind], evals[ind]])
        
    best_to_worst = sorted(random_parents, key=takeDist)
    
    return best_to_worst[0]

# Used to return specific index as key in sorting 
def takeDist(elem):
    return elem[1][0]


#Main reproduction function, given two parents, return two children.
# Since each gene in a chromosome is unique (we can only visit each city once so no repeats), we can't do
# simple point wise recombination because some children would double back on themselves. Instead,
# we use a specific recombination operator called the OX1 Operator, which allows for recombination
# of unique data that cannot be reapeated in the bitstring (chromosome). 
# More information found athttps://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/Order1CrossoverOperator.aspx

def reproduce(parent1, parent2):
    
    # Choose a random crossover stretch 
    crossover_section = (np.random.randint(0, len(parent1[0])/2), np.random.randint(len(parent1[0])/2, len(parent1[0])))

    #create a blank bitstring for each child
    child1 = [None] * len(parent1[0])
    child2 = [None] * len(parent1[0])

    #Fill in the children with their cooresponding crossover ranges
    for i in range(crossover_section[0], crossover_section[1]):
        child1[i] = parent1[0][i]
        child2[i] = parent2[0][i]
    
    #Iterate over each child and add bits from the second parent that dont already exist in the crossover section 
    i=0
    for entry in child1:
        if entry == None:
            for gene in parent2[0]:
                if gene not in child1:
                    child1[i] = gene
                    i+=1
                    break
                else:
                    continue
        else:
            i+=1
            continue
    i=0
    for entry in child2:
        if entry == None:
            for gene in parent1[0]:
                if gene not in child2:
                    child2[i] = gene
                    i+=1
                    break
                else:
                    continue
        else:
            i+=1
            continue
    
    #Maintain a small chance for cloning to occur, resulting in the child existing as an identical copy of the parent.
    #Modification of rate has not yet been tested. 
    if np.random.randint(0,100) > 92:
        child1 = parent1[0]
    if np.random.randint(0,100) > 92:
        child2 = parent2[0]
    

    return child1, child2

# given a mutation rate, create random bit swaps in the childs bit string and return the mutated child. 
def mutate(child, mutation_rate):
    mutate_chance = (mutation_rate)/(len(child))
    
    for entry in child:
        if np.random.uniform(0,1) < mutate_chance:
            #Mutate
            index1 = np.random.randint(0, len(child))
            gene1 = child[index1]

            index2 = np.random.randint(0, len(child))
            gene2 = child[index2]

            child[index1] = gene2
            child[index2] = gene1

            #print('Mutation')
        else:
            continue
        
    return child

def genetic_alg(coordinates, pop_size, generations, mutation_rate):

    population = generate_population(coordinates, pop_size)
    evals = evaluate_population(population)

    best = select_best(evals, population)
    print('Best solution from inital population: ' + (str(best[1])))
    
    best_by_gen = []

    best_by_gen.append(best)
    
    for i in range(generations):

        next_gen = []
        for x in range(int(pop_size*0.01)):

            parent1 = select_parent(population, evals)
            parent2 = select_parent(population, evals)

            for y in range(int((pop_size*.005))):

                child1, child2 = reproduce(parent1, parent2)
                child1 = mutate(child1, mutation_rate)
                child2 = mutate(child2, mutation_rate)

                next_gen.append(child1)
                next_gen.append(child2)
        population = next_gen
        evals = evaluate_population(population)

        best = select_best(evals, population)
        best_by_gen.append(best)
        #print('Best solution from generation ' + str(i+1) + ": " + (str(best[1])))
    print('Best solution from final ' + '('+ str(i+1) +')' + ' generation: ' + (str(best[1])))
    return best, best_by_gen

# Graph the best performing memeber of each of each generation (returned by the genetic alg function)
def graph_generations(best_by_gen):
    x_gen = [i for i in range(len(best_by_gen))]
    y_gen = [entry[1] for entry in best_by_gen]

    fig = plt.scatter(x_gen, y_gen)
    plt.xlabel('Generation')
    plt.ylabel('Shortest Route Distance')
    plt.ylim(0,1000)
    return fig


