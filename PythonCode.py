# constants
WELCOME_MESSAGE = "WELCOME TO <THE ESPORT TOURNAMENT>!"
QUIT_MESSAGE = "\tPress 'Q' at any point to QUIT and repeat registration process"
INVALID_INPUT_MESSAGE = "Invalid input! Please enter LETTERS ONLY WITHOUT SPACES."
MAX_REGISTRATIONS = 3

# class
class Player:
    def __init__(self, name, gamertag):
        self.name = name
        self.gamertag = gamertag

class Tournament:
    def __init__(self):
        self.registrations = []

    def welcome(self):
        print(WELCOME_MESSAGE)
        print(QUIT_MESSAGE)
        input("\t\t\tPress ENTER to continue. . .")

    def get_name(self):
        while True:
            name = input("Enter your NAME: ").upper()

            if name.lower() == 'q':
                print("Returning to the beginning of the registration process...")
                continue

            if not name.isalpha():
                print(INVALID_INPUT_MESSAGE)
                continue

            return name

    def get_gamertag(self):
        while True:
            gamertag = input("Enter your GAMER TAG: ")

            if gamertag.lower() == 'q':
                print("Returning to the beginning of the registration process...")
                continue

            return gamertag

    def register_players(self):
        while len(self.registrations) < MAX_REGISTRATIONS:
            name = self.get_name()
            gamertag = self.get_gamertag()
            player = Player(name, gamertag)
            self.registrations.append(player)

    def display_registration(self):
        print("Registration Process Completed!")
        print("Registered Names and Gamer Tags:")

        for player in self.registrations:
            print(f"Name: {player.name}")
            print(f"Gamer Tag: {player.gamertag}\n")

def main():
    tournament = Tournament()
    tournament.welcome()
    tournament.register_players()
    tournament.display_registration()

if __name__ == "__main__":
    main()
