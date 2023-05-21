# every thing is object
# x = 'welcom'
# x.upper()
# x.lower()
# l = [1, 2, 3, 4, 5]
# l.pop()
# print(l)
# print(x)

# print(type(x))
# class Iphone:
#      def open_camera():
#           print('open camera')
         
#      def passlock(self):
#          pass
    
    
# my_iphone = Iphone
# my_iphone.open_camera()

# yourIphone = Iphone
# yourIphone.passlock()


class Main_calc:
     
      def __init__(self):
          print("welcome in your calculator")
          
      def sum(self, x, y):
          # print(self)
          print(x+y)
     


class Calculator:
          
     def mul(self, x, y):
          print(x*y)
          
          
          
my_calc = Calculator()
# print(my_calc)
my_calc.mul(5,6)

your_calc = Calculator()
your_calc.mul(10, 11)


class Sintific_calc(Calculator, Main_calc):
     
     def power(self, x, y):
          print(x**y)
     
     
     
one = Sintific_calc()
one.sum(8, 8)
one.mul(8, 8)
one.power(2, 5)
