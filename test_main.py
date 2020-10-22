import unittest
import main
def add(x,y):
   return x + y
   
class test_main(unittest.TestCase):
   def testAdd1(self):
      self.assertEqual(main.Add(4,5),9)
   def testAdd2(self):
      self.assertEqual(main.Add(10,30),40)   
   def testAdd3(self):
      self.assertEqual(main.Add(10,300),310)      
   def testSub1(self):
      self.assertEqual(main.Subtract(10,5),5)
   def testSub2(self):
      self.assertEqual(main.Subtract(5,10),-5)
   def testPrint(self):
      self.assertEqual(main.PrintTest(),"Hello")  
if __name__ == '__main__':
   unittest.main()
