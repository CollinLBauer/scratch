import os
import sys

def list_missing(folder, debug=False):
    files = os.scandir(folder)
    i = 0
    missing = []

    for file in files:
        temp = int(file.name.split()[0])
        i += 1
        while i != temp:
            missing.append(i)
            i += 1

    if debug:
        if len(missing) == 0:
            print("No missing tracks detected.")
        else:
            print("Missing {} tracks".format(len(missing)))
            for item in missing:
                print("  {:03}".format(item))
            print()

    return missing
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1 arguments expected; found {}.".format(len(sys.argv) - 1))
        exit()
    folder = sys.argv[1]
    list_missing(folder, debug=True)
