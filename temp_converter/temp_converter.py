#!/usr/bin/python3
"""
created by: Jeffrey Cano Deleon
course : csc 138
created on: 9-5-24
"""

# process
def c2f(c):
    return c * (9 / 5) + 32

def main(cel):
    return c2f(cel)

if __name__ == "__main__":
    cel = 100         # input
    print(main(cel))  # output
