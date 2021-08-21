from resources import *

if __name__ == "__main__":
    n_cities = int(input('Number of cities to generate: '))
    coordinates, x, y = generate_cities(n_cities)




    solution, gens = genetic_alg(coordinates, 2000, 100, 1)

    graph_route(coordinates, solution[0])
    plt.show()

    #graph_generations(gens)
    #plt.show

