import time
import random

class MySet:
    def __init__(self) -> None:
        self.map = set()
    
    def insert(self, value):
        self.map.add(value)
    
    def remove(self, value):
        self.map.remove(value)
    
    def getRandom(self):
        return random.choice(list(self.map))

# global vars

# quicksort
# https://www.geeksforgeeks.org/python-program-for-quicksort/

def main() -> None:
    set1 = MySet()
    set1.insert(2)
    set1.insert(5)
    set1.remove(5)
    set1.insert(45)
    set1.insert(-5)
    set1.insert(0)
    print(str(set1.getRandom()))
    return

if __name__ == "__main__":
    main()
