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
    print("2 : " + str(ex2.totalPrice))
    print(ex2.chosen)
    prices2 = [10, 1000000, 30, 50, 60, 40, 1000000, 1000, 20, 30]
    ex2 = Ex2.City(prices2)
    print("2 : " + str(ex2.totalPrice))
    print(ex2.chosen)

    words = ["chen", "che", "nadav", "wave"]
    ex3 = Ex3.Lang(words)
    sentence = ex3.splitWords("chenadavchenwavechenchenadav")
    print("3: " + sentence)

    ex4 = Ex4.Binary([1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1])
    ex4.increment()
    print("4: " + str(ex4.number))
