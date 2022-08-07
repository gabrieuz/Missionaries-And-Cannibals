class Left:
    def __init__(self, missionaries, cannibals):
        self.missionaries = missionaries
        self.cannibals = cannibals

    def __str__(self):
        return "left"


class Right:
    def __init__(self, missionaries, cannibals):
        self.missionaries = missionaries
        self.cannibals = cannibals

    def __str__(self):
        return "rigth"


class Boat:
    def __init__(self, left, right, location):
        self.left = left
        self.right = right
        self.location = location

    def __str__(self):
        return "\n======================= Current State =======================" \
            f'\n\t{self.left.missionaries} missionaries and {self.left.cannibals} cannibals on the left side.' \
            f'\n\t{self.right.missionaries} missionaries and {self.right.cannibals} cannibals on the right side.' \
            f'\n\tThe boat is on the {self.location} side.' \
            "\n============================================================="

    def move(self, cannibals, missionaries):
        if cannibals == 0 and missionaries == 0:
            print('\n>> You can\'t move 0 people.')
            return False
        elif cannibals + missionaries > 2:
            print('\n>> You can\'t move more than 2 people at a time.')
            return False

        if self.location == 'left':
            if cannibals > self.left.cannibals:
                print(
                    f'\n>> You can\'t move {cannibals} cannibals, there are {self.left.cannibals} cannibals on the left side.')
            elif missionaries > self.left.missionaries:
                print(
                    f'\n>> You can\'t move {missionaries} missionaries, there are {self.left.missionaries} missionaries on the left side.')

            self.left.missionaries -= missionaries
            self.left.cannibals -= cannibals
            self.right.missionaries += missionaries
            self.right.cannibals += cannibals
            self.location = 'right'

            print(
                f'\n>> You moved {missionaries} missionaries and {cannibals} cannibals to the {self.location} side.')

        else:
            if missionaries > self.right.missionaries:
                print(
                    f'\n>> You can\'t move {missionaries} missionaries, there are {self.right.missionaries} missionaries on the right side.')
            elif cannibals > self.right.cannibals:
                print(
                    f'\n>> You can\'t move {cannibals} cannibals, there are {self.right.cannibals} cannibals on the right side.')

            self.left.missionaries += missionaries
            self.left.cannibals += cannibals
            self.right.missionaries -= missionaries
            self.right.cannibals -= cannibals
            self.location = 'left'

            print(
                f'\n>> You moved {missionaries} missionaries and {cannibals} cannibals to the {self.location} side.')

        if self.left.missionaries == 0 and self.left.cannibals == 0:
            print(f'You win!')
            return True
        if (self.left.missionaries < self.left.cannibals and self.left.missionaries > 0) or (self.right.missionaries < self.right.cannibals and self.right.missionaries > 0):
            print('\n>> Cannibals attacked! Game over...')
            return False


initial_state = Boat(Left(3, 3), Right(0, 0), 'left')


def play(initial_state):
    print('>> Welcome to the missionaries and cannibals problem!')
    print('\n>> The goal is to get all the missionaries and cannibals to the other side of the river.')
    print('\n>> Rules:')
    print('>> 1. The boat can only carry 1 >= 2 people at a time.')
    print('>> 2. The number of cannibals cannot be greater than the number of missionaries.')
    print(initial_state)

    while True:
        print("\nChoose an option:")
        print("\t1. Move")
        print("\t2. State")
        print("\t0. Exit")

        option = int(input(">> "))

        if option == 1:
            print("\n>> Choose the number of missionaries and cannibals to move:")
            input_missionaries = int(input(">> Missionaries: "))
            input_cannibals = int(input(">> Cannibals: "))

            if initial_state.move(input_cannibals, input_missionaries):
                print(initial_state)
            else:
                continue
        elif option == 0:
            print("\n>> Thanks for playing!")
            break
        elif option == 2:
            print(initial_state)
        else:
            print("\n>> Invalid option.")
            continue


if __name__ == '__main__':
    play(initial_state)
