import random as rand

def main():
    # Define the probabilities of getting a corner exhumed
    probability_dict = {
        "initial_probability_in_corner": (4*9) / (15 ** 2 - 9) # 4 corners each with a 3x3 (9 tile) grid. First run there's 9 tiles it can't spawn
        ,"probability_in_corner_given_corner": (4*9 - 1) / (15 ** 2 - 10) # Same as above, but now there's 10 tiles it can't spawn and 1 less corner tile for it to be in
        ,"probability_in_corner_given_non_corner": (4*9) / (15 ** 2 - 10) # same as in a corner, but 1 more corner tile it could be in
    }
    
    # Number of simulations
    num_simulations = 100000

    # Store the results of each simulation
    results = []


    for _ in range(num_simulations):
        impossible_exhumed_count = 0
        current_xarp = []
        # 12 exhumeds per xarp
        for i in range(12):
            # initial case
            if i == 0:
                if rand.random() < probability_dict['initial_probability_in_corner']:
                    current_xarp.append(1)
                else:
                    current_xarp.append(0)
            else:
                # if the prior exhumed was a corner, then we check if the next is in a corner
                if current_xarp[i - 1] == 1:
                    # Calculate if it's in a corner again
                    if rand.random() < probability_dict['probability_in_corner_given_corner']:
                        current_xarp.append(1)
                        # if it is in a corner, there's 1 possible tile that causes an impossible exhumed out of (9 * 4 - 1) possible corner tiles. -1 because you're on one of them already
                        if rand.random() < 1 / (9 * 4 - 1):
                            impossible_exhumed_count += 1
                    # if it's not in a corner again
                    else:
                        current_xarp.append(0)
                # if the prior exum was not a corner, then we check if the next is in a corner
                else:
                    if rand.random() < probability_dict['probability_in_corner_given_non_corner']:
                        current_xarp.append(1)
                    else:
                        current_xarp.append(0)
        # append results of sim, did we get an impossible exhumed?
        if impossible_exhumed_count >= 1:
            results.append(1)
        else:
            results.append(0)
        

    # Print the results
    print(f"Total number of runs with at least one impossible exhumed spawn over {num_simulations} simulations: {sum(results)}")
    print(f"Average number of runs with at least one impossible exhumed spawn over {num_simulations} simulations: {sum(results) / num_simulations}")
    print(f"On average you get an impossible exhumed spawn in 1 out of every {round(num_simulations/sum(results), 3)} TOB runs")

if __name__ == "__main__":
    main()
