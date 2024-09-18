
class Game:
    games_list = []  # Lista de juegos creados

    def __init__(self, code, title, category):
        self.code = code
        self.title = title
        self.category = category

    @classmethod
    def add_game(cls, code, title, category):
        # Validar que el código del juego no esté repetido
        if any(game.code == code for game in cls.games_list):
            raise ValueError("Game code already exists")
        
        game = Game(code, title, category)
        cls.games_list.append(game)

    @classmethod
    def show_games(cls):
        if not cls.games_list:
            print("No games available.")
        else:
            print("Available games:")
            for game in cls.games_list:
                print(f"Code: {game.code}, Title: {game.title}, Category: {game.category}")
