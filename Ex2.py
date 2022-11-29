class City:
    def __init__(self, houses_prices):
        self.size = len(houses_prices)
        self.houses_prices = houses_prices

        self.chosen = self.size * [False]  # array of chosen houses
        self.chooseBetterOption(0)  # calculate which houses to chose
        self.totalPrice = self.calcTotal()  # calculate total price of chosen houses

    def chooseBetterOption(self, i):  # O(n) - runs one time on array of prices
        if i + 2 >= self.size:  # less than three houses left
            if i + 1 < self.size:  # two houses left
                if self.houses_prices[i] < self.houses_prices[i + 1]:  # choose cheapest
                    self.chosen[i] = True
                else:
                    self.chosen[i + 1] = True
            return
        best_price_for_3 = min(self.houses_prices[i + 1], self.houses_prices[i] + self.houses_prices[i + 2])
        if best_price_for_3 == self.houses_prices[i] + self.houses_prices[i + 2]:  # side houses are cheaper
            self.chosen[i] = True
            self.chosen[i + 2] = True
            if i > 2:  # check if need to change houses that were chosen before
                if self.chosen[i - 1] and self.houses_prices[i - 1] > self.houses_prices[i - 2]:
                    self.chosen[i - 2] = True
                    self.chosen[i - 1] = False
            return self.chooseBetterOption(i + 3)  # go to the next not chosen house
        else:  # middle house is cheapest
            self.chosen[i + 1] = True
            return self.chooseBetterOption(i + 2)  # go to the next not chosen house

    def calcTotal(self):
        total = 0
        for index, flag in enumerate(self.chosen):
            if flag:
                total += self.houses_prices[index]
        return total
