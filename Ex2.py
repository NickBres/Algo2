class City:
    def __init__(self, houses_prices):
        self.size = len(houses_prices)
        self.houses_prices = houses_prices
        self.to_repair = self.size * [False]
        self.price = self.bestPrice()

    # O(n)
    def bestPrice(self):
        i = 0
        j = 1
        while j < self.size:
            if self.houses_prices[i] <= self.houses_prices[j]:
                self.to_repair[i] = True
            else:
                self.to_repair[j] = True
            i += 2
            j += 2
        self.fillGaps()
        return self.calcTotal()

    def fillGaps(self):
        gap_index = self.findGap()
        while gap_index != -1:
            new_sum_from_left = 0
            i = gap_index
            j = i - 1
            while i >= 0 and not (self.to_repair[i]):
                new_sum_from_left += self.houses_prices[i]
                if j >= 0:
                    new_sum_from_left -= self.houses_prices[j]
                i -= 2
                j -= 2
            new_sum_from_right = 0
            i = gap_index + 1
            j = i + 1
            while i < self.size and not (self.to_repair[i]):
                new_sum_from_right += self.houses_prices[i]
                if j < self.size:
                    new_sum_from_right -= self.houses_prices[j]
                i += 2
                j += 2

            old_sum_from_left = self.houses_prices[gap_index]
            i = gap_index - 1
            while i >= 0 and not (self.to_repair[i]):
                old_sum_from_left += self.houses_prices[i]
                i -= 2
            old_sum_from_right = self.houses_prices[gap_index + 1]
            i = gap_index + 2
            while i < self.size and not (self.to_repair[i]):
                old_sum_from_right += self.houses_prices[i]
                i += 2

            minSum = min(new_sum_from_right, new_sum_from_left, old_sum_from_right, old_sum_from_left)

            if minSum == new_sum_from_right:
                i = gap_index + 1
                j = i + 1
                while i < self.size and not (self.to_repair[i]):
                    self.to_repair[i] = True
                    if j < self.size:
                        self.to_repair[j] = False
                    i += 2
                    j += 2
            elif minSum == new_sum_from_left:
                i = gap_index
                j = i - 1
                while i >= 0 and not (self.to_repair[i]):
                    self.to_repair[i] = True
                    if j >= 0:
                        self.to_repair[j] = False
                    i -= 2
                    j -= 2
            elif minSum == old_sum_from_left:
                self.to_repair[gap_index] = True
            else:
                self.to_repair[gap_index + 1] = True
            gap_index = self.findGap()

    def findGap(self):
        i = 0
        j = 1
        while j < self.size:
            if not (self.to_repair[i]) and not (self.to_repair[j]):
                return i
            i += 1
            j += 1
        return -1

    def calcTotal(self):
        total = 0
        for index, flag in enumerate(self.to_repair):
            if flag:
                total += self.houses_prices[index]
        return total
