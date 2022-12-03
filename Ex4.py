class Binary:
    def __init__(self, binaryArr):
        self.number = binaryArr

    # O(1)
    def increment(self):
        j = len(self.number) - 1
        while j >= 0 and self.number[j] == 1:
            self.number[j] = 0
            j -= 1
        if j >= 0:
             self.number[j] = 1
