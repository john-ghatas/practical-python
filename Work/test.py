#!/usr/bin/env python
import argparse

def greetings(message, user):
    print(f'{user} says: {message}')

def parse_args():
    parser = argparse.ArgumentParser()          
    parser.add_argument("-u", "--user", help="Specify user")
    parser.add_argument("-m", "--message", help="Message")
    return parser.parse_args()

def main(argv):
    args = parse_args()
    greetings(args.message, args.user)

if __name__ == '__main__':
    import sys
    main(sys.argv)
