## Simulate a FIFA World Cup tournament ##
import csv, sys, random

SimulationCount = 1000

def main():
  if len(sys.argv) != 2:
    sys.exit("Must include a team rankings file")

  if (sys.argv[1].endswith('.csv') is False):
    sys.exit("Team rankings file must be of type CSV")

  teams = []
  with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for team in reader:
      team["rating"] = int(team["rating"])
      teams.append(team)
  print(teams)

  counts = {}
  for i in range(SimulationCount):
    winner = simulate_tournament(teams)
    if winner in counts:
      counts[winner] += 1
    else:
      counts[winner] = 1
  print(counts)

  for team in sorted(counts, key=lambda team: counts[team], reverse=True):
    print(f"{team}: {counts[team] * 100 / SimulationCount:.1f}% chance of winning")

# Return True if team1 wins, else False
def simulate_game(team1, team2):
  rating1 = team1["rating"]
  rating2 = team2["rating"]
  probability = 1 / (1 + 10**((rating2 - rating1) / 600))
  return random.random() < probability

# Return a list of winning teams for one round
def simulate_round(teams):
  winners = []
  for i in range(0, len(teams), 2):
    if simulate_game(teams[i], teams[i + 1]):
        winners.append(teams[i])
    else:
        winners.append(teams[i + 1])
  return winners

# Return name of winning team
def simulate_tournament(teams):
  while len(teams) > 1:
    teams = simulate_round(teams)
  return teams[0]["team"]

if __name__ == "__main__":
  main()