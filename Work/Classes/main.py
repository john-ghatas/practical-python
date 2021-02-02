#!/usr/bin/env python
import sys
import os
from lib.player import Player

def main(argv):
    player = Player(100,500)
    player.move(1, 3)
    print(player.__dict__())
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    main(sys.argv)
