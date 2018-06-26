import argparse


# load a file in and return a list of the lines
def load_file(filename):

    fileLines = []
    try:
        with open(filename) as readfile:
            for line in readfile:
                fileLines.append(line.strip())
    except IOError as msg:
        print("Error opening file " + filename)
        print(msg)

    return fileLines


# create the parser and return args
def parser():

    # Create the argument parser
    parser = argparse.ArgumentParser(description=(
        'Scott Cuthbert - Count Unique'))
    parser.add_argument('-t', dest='file', nargs='?',
                        action='store', default='no_file',
                        help='defines a filename to run against')

    # Create object args to reference
    args = parser.parse_args()

    return args


def main():

    args = parser()

    # if a filename was not specified with args, request input
    if args.file == 'no_file':
        filename = input("Enter the name of the file to check: ")
    else:
        filename = args.file

    # load list then sort
    lines = load_file(filename)
    unique = []
    counts = []
    lines.sort()
    # only add the first instance of a line and increment count
    for line in lines:
        if line not in unique:
            counts.append(lines.count(line))
            unique.append(line)
    index = 0

    # zip the two lists and reverse the sort to print highest count first
    counts, unique = (list(t) for t in zip(*sorted(zip(counts, unique))))
    counts.reverse()
    unique.reverse()

    # print it out
    print("COUNT\t|\tITEM")
    for item in counts:
        print("%s\t|\t%s" % (counts[index], unique[index]))
        index += 1


main()
