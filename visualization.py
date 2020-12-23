import sys
import os
from monty_hall import Simulation
import pandas as pd
import seaborn as sns

class Plot:
    """A class for creating an many instances of a Monty Hall problem which simulates the problem, then graphically represents the result.
    
    Attributes:
        doors: contains the numbers of doors to be used for the problem.
        simulations: contains the number of simulations that will run.
    """
    def __init__ (self, doors, simulations):
        """
        Initializes a Plot Object. Creates and populates a dictionary used to hold the results of simulations created by calling the simulation class.
        
        Attributes:
            doors: stores the number of doors to be used for the problem.
            simulations: contains the number of simulations that will run.
            sequence: a dictionary that will hold the iteration number, win percentage, door number, and switch values.
            simulation: an instance of the Simulation class is created.
            
        Parameters:
            doors: passes in the number of doors from class creation.
            simulations: passes in the number of simulations from class creation.
        """
        self.doors = doors
        self.simulations = simulations
        self.sequence = {"Iteration":[], "Win Percentage":[], "Doors":[], "Switched":[]}
        self.simulation = Simulation(doors)
        
        while (self.simulations > 0):
            if (self.simulations % 2 == 0):
                self.sequence["Iteration"].append(self.simulations)
                self.sequence["Win Percentage"].append(self.simulation.play_game(True,self.simulations))
                self.sequence["Doors"].append(self.doors)
                self.sequence["Switched"].append(True)
                self.simulations -= 1
            else:
                self.sequence["Iteration"].append(self.simulations)
                self.sequence["Win Percentage"].append(self.simulation.play_game(False,self.simulations))
                self.sequence["Doors"].append(self.doors)
                self.sequence["Switched"].append(False)
                self.simulations -= 1
        
        self.make_plot(self.sequence)
        
    def make_plot(self, sequence):
        """
        A method that creates a dataframe from the dictionary populated in Plot, then creates a graphical representation of the results.
        
        Attributes:
            df: stores dataframe created from the sequence dictionary.
            
        Parameters:
            sequence: a dictionary that holds the values associated with each iteration, win percentage, iteration number, and switched.
        """
        df = pd.DataFrame(self.sequence)
        print(df)
        sns.lmplot(data = df, x="Iteration", y="Win Percentage", hue="Switched").savefig('visualization.png', dpi=600, format='png')
        
    
if __name__ == '__main__':
    plot = Plot(5, 100)