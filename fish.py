class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def swim(self):
        pass


class Salmon(Fish):
    def __init__(self, name):
        super().__init__(name, species="Salmon")

    def swim(self):
        return "I am swimming like a salmon!"


class Trout(Fish):
    def __init__(self, name):
        super().__init__(name, species="Trout")

    def swim(self):
        return "I am swimming like a trout!"


class Shark(Fish):
    def __init__(self, name):
        super().__init__(name, species="Shark")

    def swim(self):
        return "I am swimming like a shark!"
