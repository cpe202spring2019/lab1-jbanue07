import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_0(self):
        """Tests for a raised value error when list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_1(self):
        """Tests for max value of input list"""
        tlist = [1,2,3,4,5,6,7,8]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_max_list_iter_2(self):
        """Tests for max in an unsorted list"""
        tlist = [20,19]
        self.assertEqual(max_list_iter(tlist), 20)
        
    def test_max_list_iter3(self):
        """Tests functionality of a list of 1"""
        tlist = [5]
        self.assertEqual(max_list_iter(tlist), 5)

    def test_max_list_iter4(self):
        """Tests for None return when list is empty"""
        tlist=[]
        self.assertEqual(max_list_iter(tlist),None)

    def test_max_list_iter5(self):
        """"""
        tlist = [-5, 5, -7, 6, 0]
        self.assertEqual(max_list_iter(tlist), 6)

    def test_max_list_iter6(self):
        """"""
        tlist = [-4,-10,-20,-15,-6]
        self.assertEqual(max_list_iter(tlist), -4)

    def test_max_list_iter7(self):
        """"""
        tlist = [-20,-10,-20,-10,-20]
        self.assertEqual(max_list_iter(tlist),-10)

    def test_max_list_iter8(self):
        """"""
        tlist = [-4,-10,-20,-1,-6]
        self.assertEqual(max_list_iter(tlist), -1)

    def test_reverse_rec_0(self):
        """Verifies ordered input list is reversed"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_1(self):
        """Verifies ValueError is raised when a list equal to None is entered"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_reverse_rec_2(self):
        """Verifies ordered input list of even length is reversed"""
        self.assertEqual(reverse_rec([1,4,6,8,9,10]),[10,9,8,6,4,1])

    def test_reverse_rec_2(self):
        """Verifies ordered input list of odd length is reversed"""
        self.assertEqual(reverse_rec([1,4,6,8,9,10]),[10,9,8,6,4,1])

    def test_reverse_rec_3(self):
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search_0(self):
        """Verifies bin_search is able to sort to find target integer"""
        target = 8
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(target, low, high, list_val), 6)

    def test_bin_search_1(self):
        """Verifies bin_search returns None if target cannot be found"""
        list_val =[0,1,2,3,4,6,7,8,9,10]
        target = 11
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_2(self):
        """Verifies functionality in case of list of size 1"""
        list_val = [5]
        target = 5
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(target,low,high,list_val),0)

    def test_bin_search_3(self):
        """Verifies bin_search raises ValueError when list entered is None"""
        list_val = None
        target = 2
        low = 0
        high = 1
        with self.assertRaises(ValueError):
            bin_search(target,low,high,list_val)

    def test_bin_search_4(self):
        """Tests function with a list of two, target is low"""
        list_val = [1,2]
        target = 1
        low = 0
        high = 1
        self.assertEqual(bin_search(target,low,high,list_val),0)

    def test_bin_search_5(self):
        """Tests function with a list of two, target is high"""
        list_val = [1,2]
        target = 2
        low = 0
        high = 1
        self.assertEqual(bin_search(target,low,high,list_val),1)

    def test_bin_search_6(self):
        """Verifies bin_search is able to sort to find target integer left of mid"""
        target = 1
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(target, low, high, list_val), 1)

    def test_bin_search_7(self):
        """Verifies bin_search is able to sort to find target integer left of mid"""
        list_val = [1,2]
        target = 3
        low = 0
        high = 1
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_8(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 3
        high = 5
        target = 0
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_9(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = 3
        high = 5
        target = 7
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_10(self):
        list_val=[]
        low = 11
        high = 12
        target = 7
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_11(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = 12
        high = 11
        target = 7
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_12(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = -12
        high = -11
        target = 7
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_12(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = -12
        high = 11
        target = 7
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_13(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = 6
        high = 4
        target = 6
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_14(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = 6
        high = 14
        target = 6
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_15(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = 13
        high = 20
        target = 6
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_16(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = -3
        high = 5
        target = 6
        self.assertEqual(bin_search(target,low,high,list_val),None)

    def test_bin_search_17(self):
        list_val=[1,2,3,4,5,6,7,8,9]
        low = 5
        high = 20
        target = 6
        self.assertEqual(bin_search(target,low,high,list_val),None)

if __name__ == "__main__":
        unittest.main()

    
