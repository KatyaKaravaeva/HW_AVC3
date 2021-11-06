import includes
import random
import animal
import enum


# -----------------------------------------------
class Kind(enum.Enum):
    RIVER = 1
    SEA = 2
    LAKE = 3


# ----------------------------------------------
class Fish(animal.Animals):
    def __init__(self):
        """
         Initializing
        :argument self.name: fish name
        :argument self.weight: weight
        :argument self.type: fish type
        """
        self.name = ""
        self.weight = 0
        self.type = Kind

    def info_read(self, str_arr, ind):
        """
        Reading the string
        :param str_arr:  string array
        :param ind: number of possible values
        :return: int ind
        """
        if ind >= len(str_arr) - 2:
            return 0
        self.name = str_arr[ind]
        self.weight = int(str_arr[ind + 1])
        self.type = Kind(int(str_arr[ind + 2]))
        ind += 3
        return ind

    def random_read(self):
        """
        Random initializing
        """
        self.name = includes.rnd_string(11)
        self.weight = random.randrange(10, 100)
        self.type = Kind(random.randrange(1, 4))

    def print(self):
        """
        Print information
        """
        print("Fish: name = ", self.name, " weight = ", self.weight,
              " type = ", self.type.name, "ratio = ",
              round(self.ratio(), 2))
        pass

    def write(self, stream):
        """
        Recording information in a stream
        :param stream: stream
        """
        stream.write(
            "Fish: name = {}  weight = {}  type = {}, ratio = {}".format \
                (self.name, self.weight, self.type.name, round(self.ratio(), 2)))
        pass

    def ratio(self):
        """
        Calculation of the additional function
        :return: float result
        """
        count = 0
        lenght = len(self.name)
        for i in range(lenght):
            count += ord(self.name[i])
        return float(count) / float(self.weight)
