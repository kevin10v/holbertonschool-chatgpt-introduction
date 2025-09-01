#!/usr/bin/python3
import sys

# Loop nga argumenti i parë (skip sys.argv[0] që është emri i file)
for arg in sys.argv[1:]:
    print(arg)
