"""
Item class
Created by \
21 / 03 / 18
"""


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.w = None
        self.h = None

    def new_pos(self):
        self.y += self.vy
        self.x += self.vx

    def get_pos(self):
        pos = (self.x, self.y)
        return pos

    def check_collision_with(self, other):
        if self.y < other.y + other.h and self.y + self.h > other.y:
            if other.x <= self.x + self.w and other.x + other.w >= self.x:
                return True
        return False
