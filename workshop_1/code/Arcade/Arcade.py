"""
This module has class definition of the created and show the Video Game Arcade Machine.

Author: Daniel Santiago Perez Madera <dsperezm@udistrital.edu.co>

This file is part of workshop_1.

workshop_1 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

workshop_1 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with workshop_1. If not, see <https://www.gnu.org/licenses/>. 
"""


from game import Game

class ArcadeMachine:

    """
    This class represents the Arcade Machine, with methods to select its material and add games.
    """

    def __init__(self):
        self.material = None
        self.games = []
        self.price = 0

    def choose_material(self)-> None:

        """
        This method allows the user to choose a material for the arcade machine and set its price accordingly.

        Returns:
            None: Updates the material and price of the arcade machine.
        """

        materials = {'1': 'Wood', '2': 'Aluminum', '3': 'Carbon Fiber'}
        print("Choose the material for your Arcade Machine:")
        print("1. Wood\n2. Aluminum\n3. Carbon Fiber")
        choice = input("Enter your choice: ")

        if choice in materials:
            self.material = materials[choice]
            self.price = 1000 if self.material == 'Wood' else 1500 if self.material == 'Aluminum' else 2000
            print(f"Material selected: {self.material} - Price: ${self.price}")
        else:
            raise ValueError("Invalid material choice")

    def add_game(self)-> None:
        """
        This method allows the user to add a game to the arcade machine from the existing game list.

        Raises:
            ValueError: If the game code does not exist in the game list.
        """

        Game.show_games()
        code = input("Enter the game code to add it to the Arcade Machine: ")
        for game in Game.games_list:
            if game.code == code:
                self.games.append(game)
                print(f"Game '{game.title}' added to the Arcade Machine.")
                return
        raise ValueError("Game not found")

    def show_machine_details(self):
        print(f"Material: {self.material}, Price: ${self.price}")
        if self.games:
            print("Games in this machine:")
            for game in self.games:
                print(f" - {game.title}")
        else:
            print("No games added yet.")
