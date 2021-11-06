# ----------------------------------------------
import includes

class Container:
    def __init__(self):
        self.store = []

    def static_rnd_in(self, amount):
        """
        Adding a random object
        :param amount: number of objects
        """
        i = 0
        while i < amount:
            self.store.append(includes.inRnd())
            i += 1

    def print(self):
        """
        Information output
        """
        print("Container is store", len(self.store), "animals:")
        for animal in self.store:
            animal.print()
        self.sort(0, len(self.store) - 1)
        print("\nSorted container:")
        for element in self.store:
            element.print()
        pass

    def write(self, stream):
        """
        Recording information from a container
        :param stream: stream
        """
        stream.write("Container is store {} animals:\n".format(len(self.store)))
        for shape in self.store:
            shape.write(stream)
            stream.write("\n")
        stream.write("\n")
        pass

    def sort(self,l, r):
        if (l < r) :
            m = l + (r - l) // 2
            self.sort(l, m)
            self.sort(m + 1, r)
            self.merge(l, m, r)


    def merge(self, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = Container()
        R = Container()
        for i in range(n1):
            L.store.append(self.store[l+i])
        for j in range(n2):
            R.store.append(self.store[m + 1 + j])
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if L.store[i].ratio() >= R.store[j].ratio():
                self.store[k] = L.store[i]
                i+=1
            else:
                self.store[k] = R.store[j]
                j+=1
            k+=1

        while (i < n1):
             self.store[k] = L.store[i]
             i+=1
             k+=1

        while (j < n2):
            self.store[k] = R.store[j]
            j+=1
            k+=1

