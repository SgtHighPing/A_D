from typing import Any

class Liste:
    def __init__(self):
        self.first = None
    def __str__(self):
        return f"[]"
    # def __repr__(self):

class Wagon:
    def __init__(self,value: Any):
        self.next = None
        self.value = value
