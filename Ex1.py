class Hills:
    def __init__(self, heights):
        self.heights = heights

    # O(n)
    def waterLevel(self):
        hp = self.heights.index(max(self.heights))
        if hp == -1:
            return 0

        return self.waterLevelBeforeHighestPoint(hp) + self.waterLevelAfterHighestPoint(hp)

    def waterLevelBeforeHighestPoint(self, hp):
        total = start = 0

        while start < hp and self.heights[start] == 0:
            start += 1

        while start < hp:
            end = start + 1
            while self.heights[start] > self.heights[end]:
                total += self.heights[start] - self.heights[end]
                end += 1
            start = end

        return total

    # same as before but backwards
    def waterLevelAfterHighestPoint(self, hp):
        total = 0
        start = len(self.heights) - 1

        while start > hp and self.heights[start] == 0:
            start -= 1

        while start > hp:
            end = start - 1
            while self.heights[start] > self.heights[end]:
                total += self.heights[start] - self.heights[end]
                end -= 1
            start = end

        return total
