class City:
    def __init__(self, houses_prices):
        self.houses_prices = houses_prices

    # O(n)
    def bestPrice(self):
        total = 0
        is_visited = [0] * len(self.houses_prices)
        count = 0

        while count < len(self.houses_prices):
            max_index = self.findMaxNotVisited(is_visited)
            sum_of_neighbours = 0
            is_visited[max_index] = 1
            if max_index - 1 >= 0 and is_visited[max_index - 1] == 0:
                is_visited[max_index - 1] = 1
                sum_of_neighbours += self.houses_prices[max_index - 1]
                count += 1
            if max_index + 1 < len(self.houses_prices) and is_visited[max_index + 1] == 0:
                is_visited[max_index + 1] = 1
                sum_of_neighbours += self.houses_prices[max_index + 1]
                count += 1
            if sum_of_neighbours < self.houses_prices[max_index]:
                total += sum_of_neighbours
            else:
                total += self.houses_prices[max_index]
            count += 1

        return total

    def findMaxNotVisited(self, is_visited):
        i = 0
        while i < len(is_visited) and is_visited[i] == 1:
            i += 1
        if i == len(is_visited):
            return -1
        max_index = i
        while i < len(is_visited):
            if is_visited[i] == 0 and self.houses_prices[max_index] < self.houses_prices[i]:
                max_index = i
            i += 1

        return max_index

