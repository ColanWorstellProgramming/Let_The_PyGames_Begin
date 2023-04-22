#!/usr/bin/python3

from enum import Enum

class GameState(Enum):
    RUNNING = 1,
    ENDED = 2,
    NONE = 0