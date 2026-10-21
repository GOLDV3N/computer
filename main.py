'''Computer Price
Outline:
Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.'''

class computer:
    def __init__(self):
       self.__max_price = 200000

    def sell(self):
        print("selling price:" , self.__max_price)

    def setmaxprice(self,price):
        self.__max_price = price


c = computer()
c.sell()

c.__max_price = 1000
c.sell()
c.setmaxprice(1000)
c.sell()

