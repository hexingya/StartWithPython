import sport


class Movie:
    def __init__(self, name):
        self.name = name

    def watch(self):
        # print('...watching {0}'.format(self.name))
        print(f'...watching {self.name}')

    def play(self):

        choice = input("Choose of [Cricket, Tennis or Soccer] : ").lower()

        if choice == "cricket":
            sport.playcricket()
        elif choice == "tennis":
            sport.playtennis()
        elif choice == "soccer":
            sport.playsoccer()
        else:
            print("Invalid Option!")
