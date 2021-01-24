import unittest
import math
import scipy.stats as st
from hypothesis_test import Hypothesis 

class TestSkills(unittest.TestCase):     
    def setup(self):
        self.s = 6
        self.n = 10
        self.alpha = 2
        self.h0 = 10
   
    def test_basic_stats(self): #driver: mia navigater: affan
        hts = Hypothesis()
        self.assertEqual(hts.basic_stats()[0], 8.0, "wrong amount for mode")
        self.assertEqual(hts.basic_stats()[1], 7.3, "wrong amount for median")
        self.assertEqual(hts.basic_stats()[2], 6.7, "wrong amount for mean")
    
    def test_translate_z(self):
        arr1 = [[25,5,8,2,56], [60,14,14,40,6]]
        self.score1 = st.zscore(arr1, axis=0)
    
    def test_generate_test_stats(self): #driver: mia
       hts = Hypothesis()
       self.assertEqual(hts.generate_test_stats(), -48.0,
                        "wrong amount for the test stats")
       self.assertNotEqual(hts.generate_test_stats(), 40,
                           "wrong amount for the test stats, but the code" \
                            "evaluates as a right answer")
    
    def test_compare_test_stats(self):
        hts = Hypothesis()
        self.assertEqual(hts.compare_test_stats(),
                         ["The test statistics is greater than z-score, "
                          "therefore we do not reject HO.\n "], "wrong result")
        self.assertNotEqual(hts.compare_test_stats(), 
                            ["The test statistics is less than z-score, "
                            "therefore we reject HO.\n "], "wrong result, \
                            but the code evaluate as a right answer")
        
    def test_standard_error(self):
        h = Hypothesis()
        self.assertEqual(h.standard_error()[0], 0.3, "standard error")
        self.assertNotEqual(h.standard_error()[0], 0.7, "wrong standard error")
            
    def test_confidence_interval(self):
        hts=Hypothesis()
        
        self.assertEqual(hts.confidence_interval()[0], 7.01, "The lower limit")
        self.assertEqual(hts.confidence_interval()[1], 7.6, "The mean ") 
        self.assertEqual(hts.confidence_interval()[2], 8.19, "The upper limit")
        self.assertNotEqual(hts.confidence_interval()[0], 6.23, \
                            "The wrong lower limit")
        self.assertNotEqual(hts.confidence_interval()[1], 5.60, "wrong mean") 
        self.assertNotEqual(hts.confidence_interval()[2],8, "wrong upper limit")

    def test_margin_error(self):
        ht = Hypothesis()
        self.assertEqual(ht.margin_error(), 2.1, "right")
        self.assertNotEqual(ht.margin_error(), 3.4, "wrong")

    
if __name__ == '__main__':
    unittest.main()

