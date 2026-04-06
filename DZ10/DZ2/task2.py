class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species_info(cls):
        return "This is a species of 'Homosapiens'."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message from a static method."

if __name__ == "__main__":
    person = Human("Ivan")
    person.welcome()
    print(Human.species_info())
    print(Human.arbitrary_message())
