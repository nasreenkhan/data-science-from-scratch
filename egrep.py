import sys, re

regex = sys.argv[1]

# For every line passed into the script
for line in sys.stdin:
    # If it matches the regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
