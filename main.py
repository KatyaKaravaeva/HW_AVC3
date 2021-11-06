import sys
import time
from container import Container
from includes import in_lines

if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) != 5:
        print("Incorrect command line!\n"
              "  Waited:\n"
              "     command -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     command -n number outfile01 outfile02\n")
        exit()
    print("\nIn: ", sys.argv)
    print('==> Start')
    # Creating a container
    container = Container()
    if sys.argv[1] == "-f":
        # Reading the source file
        input = sys.argv[2]
        try:
            infile = open(input)
        except IOError:
            # If the file does not exist, we create it
            infile = open(input, 'w')
        # Opening the stream
        input_line = infile.read()
        # Closing the stream
        infile.close()
        # Forming an array of strings
        strArray = input_line.replace("\n", " ").split(" ")
        figNum = in_lines(container, strArray)
        # Opening a stream to write to the first objects file
        out_file = open(sys.argv[3], 'w+')
        container.write(out_file)
        out_file.close()
        # Time output
        print("Time when objects were written to the file: ",
              round(time.time() - start, 5), " seconds")
        # Opening a stream to write to the second file
        outfile_two = open(sys.argv[4], 'w+')
        container.sort(0, len(container.store)-1)
        container.write(outfile_two)
        outfile_two.close()
        # Time output
        print("Time when the sorting occurred and the result was written to the file: ",
              round(time.time() - start, 5), " seconds")
    elif sys.argv[1] == "-n":
        length = int(sys.argv[2])
        # Checking for correct data
        if length < 1 or length > 10000:
            print("Incorrect number of animals = {}. Set 0 < number <= 10000\n", length)
            exit()
        # Randomization
        container.static_rnd_in(length)
        out_file = open(sys.argv[3], 'w+')
        container.write(out_file)
        out_file.close()
        # Time output
        print("Time when objects were written to the file: ",
              round(time.time() - start, 5), " seconds")
        outfile_two = open(sys.argv[4], 'w+')
        container.sort(0, len(container.store)-1)
        container.write(outfile_two)
        # Time output
        print("Time when the sorting occurred and the result was written to the file: ",
              round(time.time() - start, 5), " seconds")
        outfile_two.close()
    else:
        print("Incorrect qualifier value!\n"
              "  Waited:\n"
              "     command -f <infile> <outfile01> <outfile02>\n"
              "  Or:\n"
              "     command -n <number> <outfile01> <outfile02>\n")
        exit()
print('==> Finish')
