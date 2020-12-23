# Monty Hall
 Data Analysis using the Monty Hall Problem

This program is simulates the monty hall problem and creates a visualization for data analysis.

If you are not familiar with the monty hall problem, here is the question.

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

vos Savant, Marilyn (9 September 1990a). "Ask Marilyn". Parade: 16. Archived from the original on 21 January 2013. Retrieved 23 December 2020.

This program simulates opening the doors and making a selection and provides a visualization of the
outcome over many different iterations.

To change the number of doors, edit plot = Plot(5, 100) where 5 is the number of doors.
To change the number of simulations, edit plot = Plot(5, 100) where 100 is the number of simulations.

To run the program, ensure that monty_hall.py and visualization.py are in the same directory and run
visualization from the terminal using python3 visualization.py. The visualization will appear as 
visualization.png in the directory you are running the program from.

You must have pandas, NumPy, seaborn installed for the program to work.
