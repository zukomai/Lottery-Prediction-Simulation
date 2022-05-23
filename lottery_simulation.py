"""
LOTTERY TICKET SIMULATION SCRIPT
Import modules in to script.
"""
import random
from collections import Counter

"""
Function that generates six sets of numbers based on 
the range set in available numbers to choose from 
"""


def pick_six():
    available_numbers = list(range(1, 45))
    ticket = []
    for ticket_number in range(6):
        picked_number = random.choice(available_numbers)
        ticket.append(picked_number)
        available_numbers.remove(picked_number)
    return sorted(ticket)


"""
User will input the selected numbers they want for the lottery.
The list of numbers is default as a string, so needs to be converted into an integer.
Each number is appended to a new list as an integer.
"""

my_ticket_org = [17, 21, 31, 32, 35, 42]
my_ticket = []
for i in my_ticket_org:
    my_ticket.append(int(i))
print("Your lottery ticket numbers are: {}".format(my_ticket))

"""
Set the win condition to False to continue while loop until True.
To count the number of games, set a variable that tracks with integer.
The winning_num_archive is used to track each iteration of lottery numbers generated - 
which can be used to see what duplicates were found. 
"""

win_condition = False
game_count = 0
winning_num_archive = []

"""
The while loop will run while False, adding 1 to each iteration of game count,
setting the winning numbers to calling the function of pick_six, generating a new set of,
numbers each time. 
Next, we append the winning numbers into the archive list.
If, the winning number matches the ticket, we calculate the total cost of the games,
the total amount of weeks, and the number of years it took to win.
Finally, we set the win_condition to True to break the loop and print the total amount of games,
being added in the console.
"""

while win_condition is False:
    game_count += 1
    winning_numbers = pick_six()
    winning_num_archive.append(winning_numbers)

    if winning_numbers == my_ticket:
        total_cost = game_count * 1
        total_weeks = game_count / 2
        total_years = round(total_weeks / 52, 1)

        print("\n You won! and it only took {:,}".format(game_count))
        print("total cost: ${:,}".format(total_cost))
        print("total weeks: {:,} weeks".format(total_weeks))
        print("total years: {:,} years".format(total_years))

        win_condition = True

    if game_count % 10000 == 0:
        print("\r", "Game Count : {:,}".format(game_count), end="")

"""
The counter variable is used to find each sublist in the list of winning numbers
and for each sublist, it will count how many times that winning lottery number was 
generated. Can set the amount that needs to be duplicated in order to be displayed to the console.
"""

counter = Counter(str(e) for e in winning_num_archive)
for key, c in counter.most_common():
    if c > 8:
        print("the winning number {} occurred {}".format(key, c))

"""
END OF SCRIPT
"""