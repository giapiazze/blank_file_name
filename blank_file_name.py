import getopt
import sys
import os
from os import listdir
from os.path import isfile, isdir, join


def run(folder, recursive):
    """
    Function to execute the search
    :param folder: The folder to search in
    :type folder: string
    :param recursive: Recursive search
    :type folder: boolean
    :return: file name found
    :rtype: array
    """
    result = []

    if listdir(folder):
        only_files = [f for f in listdir(folder) if isfile(join(folder, f))]
        only_folders = [d for d in listdir(folder) if isdir(join(folder, d))]

        if recursive:
            for d in only_folders:
                destination = folder + "/" + d
                result += run(destination, recursive)

        for f in only_files:
            if f.find(" .") != -1:
                result.insert(len(result), [f, folder])

    return result


# Main module to read start option parameter
# Option parameter: -d 'C:/Documents/' => The folder to search in)


if "__main__" == __name__:
    # Default params options
    path = os.getcwd()
    recur = True

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:r:", ["directory", "grammar="])
    except getopt.GetoptError as err:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-d", "--directory"):
            if arg != 0 or arg is not None:
                path = arg
        elif opt in ("-r", "--recursive"):
            if arg != 1 or arg == 0:
                recur = False

    array_result = run(path, recur)
    for x in array_result:
        print("File: ", x[0], " in: ", x[1])
        print("\n")
    a = 3
