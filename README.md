README

Given a CSV file of soccer teams in the World Cup and their FIFA ratings, tournament.py determines the percent chance that each team will win the tournament.

tournament.py takes one argument and will return an error and exit if that argument is missing or is not a CSV file.

The global variable SimulationCount determines how many times the simulation will run. In theory, the higher the number the more likely it is that the results will reflect reality. Of course, tournament.py does not account for entropy or upsets.

teams is a list of dictionaries, each of which contains 'team' and 'rating' keys and their associated team name and FIFA rating values.

counts is a dictionary that is populated as each tournament simulation is run. It contains a key for each team and the associated value of the total number of times they win the World Cup after all simulations are run.

Each tournament is simulated by pitting two teams against each other and determing the winner by plugging their FIFA scores into a probability function. This function always returns a probabilty ratio between 0 and 1, and this probability ratio is compared to a randomly generated float between 0 and 1. If the random float is less than the probablity then the first team wins. Otherwise, the second team wins.

This functionality is repeated for each pair of two teams until we move through the entire bracket and a tournament winner is chosen. The winner is marked in the counts dictionary, and the entire process is repeated until SimulationCount is exhausted.

Two sample CSV files are included in this directory.

Expected Output:

Germany: 16.0% chance of winning
England: 14.6% chance of winning
United States: 14.4% chance of winning
France: 8.8% chance of winning
Australia: 8.1% chance of winning
Japan: 6.9% chance of winning
Canada: 6.8% chance of winning
Netherlands: 5.3% chance of winning
Sweden: 4.6% chance of winning
Brazil: 3.3% chance of winning
Norway: 3.0% chance of winning
Spain: 2.8% chance of winning
Italy: 2.7% chance of winning
China PR: 2.7% chance of winning
