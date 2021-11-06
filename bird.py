import random
import includes
import animal


# ----------------------------------------------
class Bird(animal.Animals):
    def __init__(self):
        """
        Initializing
        :argument self.name: beast name
        :argument self.weight: weight
        :argument self.flyOrStay: the parameter whether the bird flies or not
        """
        self.name = ""
        self.weight = 0
        self.flyOrStay = False

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
        self.flyOrStay = int(line_arr[ind + 2]) == 0
        ind += 3
        return ind

    def random_read(self):
        """
        Random initialization
        """
        self.name = includes.rnd_string(10)
        self.weight = random.randrange(10, 100)
        self.flyOrStay = random.randrange(0, 2) == 0

    def print(self):
        """
        Information output
        """
        print("Bird: name = ", self.name, " weight = ", self.weight,
              " flyOrStay = ", self.flyOrStay, ", ratio = ",
              round(self.ratio(), 2))
        pass

    def write(self, stream):
        """
        Recording to the stream
        :param stream: stream
        """
        stream.write(
            "Bird: name = {}  weight = {} flyOrStay = {}, ratio = {}".format \
                (self.name, self.weight, self.flyOrStay,
                 round(self.ratio(), 2)))
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
