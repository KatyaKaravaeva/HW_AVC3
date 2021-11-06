import random
import string

from beast import Beast
from bird import Bird
from fish import Fish


def in_lines(container, str_array):
    """
    :param container: Contains objects
    :param str_array: Input
    :return: string
    """
    array_len = len(str_array)
    i = 0
    count = 0
    while i < array_len:
        line = str_array[i]
        key = int(line)
        if key == 1:
            i += 1
            animal = Beast()
            i = animal.info_read(str_array, i)
        elif key == 2:
            i += 1
            animal = Bird()
            i = animal.info_read(str_array, i)
        elif key == 3:
            i += 1
            animal = Fish()
            i = animal.info_read(str_array, i)
        else:
            return count
        if i == 0:
            return count
        count += 1
        container.store.append(animal)
    return count


def inRnd():
    """
    Selecting a randomly generated object
    :return: object
    """
    key = random.randrange(1, 4)
    if key == 1:
        animal = Beast()
        animal.random_read()
        return animal
    elif key == 2:
        animal = Bird()
        animal.random_read()
        return animal
    else:
        animal = Fish()
        animal.random_read()
        return animal


def rnd_string(length_str):
    """
    Randomization
    :param length_str: string length
    :return: random string
    """
    letters = string.ascii_uppercase + string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length_str))
    return result