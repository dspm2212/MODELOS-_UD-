"""
This module defines the Game class, which handles the creation and management of video games for the arcade machine.

Author: Daniel Santiago Perez Madera <dsperezm@udistrital.edu.co>

This file is part of workshop_1.

workshop_1 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

workshop_1 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with workshop_1. If not, see <https://www.gnu.org/licenses/>.
"""

class Game:
    """
    This class represents a video game that can be added to the arcade machine.
    """
    games_list = []  # in this list conteinet games created 

    def __init__(self, code, title, category):
        self.code = code
        self.title = title
        self.category = category

    @classmethod
    def add_game(cls:list , code:str, title:str, category:str)->None:

        """
        Adds a new game to the games_list if the game code is unique.

        Args:
            code (str): The unique code of the game.
            title (str): The title of the game.
            category (str): The category of the game.

        Raises:
            ValueError: If the game code already exists.
        """
        
        if any(game.code == code for game in cls.games_list):
            raise ValueError("Game code already exists")
        
        game = Game(code, title, category)
        cls.games_list.append(game)

    @classmethod
    def show_games(cls:list)-> None:
        """
        Displays the list of available games.

        Returns:
            None: Prints the list of games if any are available.
        """

        if not cls.games_list:
            print("No games available.")
        else:
            print("Available games:")
            for game in cls.games_list:
                print(f"Code: {game.code}, Title: {game.title}, Category: {game.category}")
