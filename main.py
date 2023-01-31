import sys

with open('filename.txt', 'w') as f:
    sys.stdout = f
    print('This message will be written to a file.')
