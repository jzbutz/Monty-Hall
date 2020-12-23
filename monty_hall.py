import random
import sys

class Simulation:
    """A class for creating an instance of a Monty Hall problem which simulates the problem.
    
    Attributes:
        doors: contains the numbers of doors to be used for the problem.
    """
    def __init__ (self, doors2):
        """
        Initializes a Simulation Object.
        
        Attributes:
            doors: stores the number of doors to be used for the problem.
            
        Parameters:
            doors: passes in the number of doors from visualization.py
        """
        self.doors = doors2
        
        
    def set_doors(self, switch2):
        """A method to simulate a monty hall problem.
        
        Attributes:
            switch: stores the switch value as true or false where true representing a switch in door selection and false representing staying with the same door.
            counter: a counter to populate a list.
            zonkList: a list to store any number of zonk's and a single car.
            number: stores the number of the door the player has selected originally.
            number2: stores the number of the door that has been opened after the selection.
            number3: stores the number of the door that could be alternatively opened if switch is true.
        
        Parameters:
            switch2: stores the switch value given in visualization.py
        """
        switch = switch2
        counter = 0
        zonkList = []
    
        while (counter < self.doors):
            zonkList.append("zonk")
            counter += 1
        
        zonkList[(random.randrange(self.doors))] = "car"
    
        number = random.randrange(self.doors)
        number2 = random.randrange(self.doors)
    
        while (number == number2 or zonkList[number2] == "car"):
            number2 = random.randrange(self.doors)
    
        number3 = random.randrange(self.doors)
    
        while (number == number3 or number3 == number2):
            number3 = random.randrange(self.doors)
        
        if(switch == True):
            
            if(zonkList[number3] == "car"):
                return True
        
            else:
                return False
            
        if(switch == False):
            
            if(zonkList[number] == "car"):
                return True
            
            else:
                return False
        
    def play_game(self, switch, iterations):
        """A method to call upon multiple instances of set_doors.
        
        Attributes:
            switch2: stores the switch value as true or false where true representing a switch in door selection and false representing staying with the same door.
            gamePlayed: a counter that stores the total number of games played.
            gamesWon: a counter that stores the total number of games won.
            winPercentage: divides number of games won by games played and holds the win percentage.
        
        Parameters:
            switch: stores the switch value given in visualization.py
            iterations: stores the number of iterations given in visualizations.py
        """
        
        switch2 = switch
        gamesPlayed = 0.00
        gamesWon = 0.00
        
        while (iterations > 0):
            winner = self.set_doors(switch2)
            iterations -= 1
            gamesPlayed += 1
            if(winner == True):
                gamesWon += 1
                
        winPercentage = gamesWon / gamesPlayed
        return winPercentage
        
if __name__ == '__main__':
    simulate = Simulation(3)
    simulate.play_game(False, 100)