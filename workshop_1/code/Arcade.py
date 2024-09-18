from game import Game

class ArcadeMachine:
    def __init__(self):
        self.material = None
        self.games = []
        self.price = 0

    def choose_material(self):
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

    def add_game(self):
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
