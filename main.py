import Ex1
import Ex2
import Ex3
import Ex4

if __name__ == '__main__':
    heights = [0, 0, 1, 0, 0, 3, 5, 6, 5, 4, 1, 3, 2, 2, 4, 6, 10, 9, 9, 11, 8, 3, 5, 4, 4, 6, 2, 0, 0, 1, 1, 0, 3, 3,
               2, 0, 0, 1]
    ex1 = Ex1.Hills(heights)
    print("1: " + str(ex1.waterLevel()))

    prices1 = [50, 30, 40, 60, 10, 30, 10]
    ex2 = Ex2.City(prices1)
    print("2: " + str(ex2.price))
    print(prices1)
    print(ex2.to_repair)
    prices2 = [30, 50, 60, 40, 100000000000, 1000, 20, 30]
    ex2 = Ex2.City(prices2)
    print("2: " + str(ex2.price))
    print(prices2)
    print(ex2.to_repair)

    words = ["hell", "hello", "low", "world", "my", "name", "is", "nick"]
    ex3 = Ex3.Lang(words)
    sentence = ex3.splitWords("helloworldmynameisnicknickismynamelowworldishelllowlowlowisisnicknickhellhellolow")
    print("3: " + sentence)

    ex4 = Ex4.Binary([1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1])
    ex4.increment()
    print("4: " + str(ex4.number))
