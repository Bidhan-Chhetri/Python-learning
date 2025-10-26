import sys

from hello import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

