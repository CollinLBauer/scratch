# This is from me trying to figure out the jankty way Python does relative imports.

from sys import path
path.insert(0,)

for item in path:
    print(item)
