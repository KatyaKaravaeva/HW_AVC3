import random
import animal
import includes
import enum


# -----------------------------------------------
class Kind(enum.Enum):
    PREDATORS = 1
    HERBIVORES = 2
    INSECTIVORES = 3


# ----------------------------------------------
class Beast(animal.Animals):
    def __init__(self):
        """
         Initializing
        :argument self.name: beast name
        :argument self.weight: weight
        :argument self.type: beast type
        """
        self.name = ""
        self.weight = 0
        self.type = Kind

    def info_read(self, line_arr, ind):
        """
        Reading the string
        :param line_arr: string array
        :param ind: number of possible values
        :return: int ind
        """
        if ind >= len(line_arr) - 2:
            return 0
        self.name = line_arr[ind]
        self.weight = int(line_arr[ind + 1])
        self.type = Kind(int(line_arr[ind + 2]))
        ind += 3
        return ind

    def random_read(self):
        """
        Random initialization
        """
        self.name = includes.rnd_string(10)
        self.weight = random.randrange(10, 100)
        self.type = Kind(random.randrange(1, 4))

    def print(self):
        """
        Information output
        """
        print("Beast: name = ", self.name, " weight = ", self.weight,
              " type = ", self.type.name, "ratio = ", round(self.ratio(), 2))
        pass

    def write(self, stream):
        """
        Recording to the stream
        :param stream: stream
        """
        stream.write("Beast: name = {}  weight = {}  type = {}, ratio = {}".format \
                         (self.name, self.weight, self.type.name, round(self.ratio(), 2)))
        pass

    def ratio(self):
        """
        Calculation of the additional function
        :return: double result
        """
        count = 0
        length = len(self.name)
        for i in range(length):
            count += ord(self.name[i])
        return float(count) / float(self.weight)
