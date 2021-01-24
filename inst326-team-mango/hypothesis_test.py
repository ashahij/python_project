import sys
from argparse import ArgumentParser
import pandas as pd
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
class Hypothesis(): 
    """Determine the result of hypothesis test for population mean
    Attributes:
        hO(float): H naught
        s(float): sample standard deviation 
        n(int): sample size
        x(float): sample mean(x̄)
        critical(float): the value of an independent variable corresponding to 
                        a crticial point of a function
    """
    
    def __init__(self): 
        self.x = 1
        self.hO = 10
        self.s = 3
        self.n = 4
        self.critical = 6 
        df = pd.read_csv("2.12_Health_systems.csv")  
        df3= df.drop(['Country_Region','Province_State'],axis= 'columns')
        self.df4 = df3.dropna()

    #Affan  
    def basic_stats(self):
        """Basic Statistic
        Return: 
            basic (list): mode, median, mean
        """ 
        total= self.df4['Health_exp_pct_GDP_2016'].count()
        basic = []         
        #Mean
        mean = round(self.df4['Health_exp_pct_GDP_2016'].sum()/ total)
        #Mode
        health = self.df4['Health_exp_pct_GDP_2016']
        mode = health.iloc[0]
        #Median
        sort = sorted(health)
        if len(health) % 2 == 0:
            even = (len(sort) // 2 )- 1 #bigger number 
            median =  (sort[even] + sort[even + 1])/ 2
        else:
            odd = (len(sort) // 2) 
            median =sort[odd]
    
        basic.append(mean)
        basic.append(median)
        basic.append(mode)

        return basic

    #Gagandeep
    def translate_z(self):
        """Translate the z-score table to specific number
        Return:
            score (list): z-score of 0.01, 0.05, 0.1
        """
        df = pd.read_csv("ztable.csv")
        #df.head()
        df.head(1)
        score = []
        score1= df.iloc[0,2]
        score2 = df.iloc[0,6]
        score3 =df.iloc[1,1]
        score.append(score1)
        score.append(score2)
        score.append(score3)
        return score
    
    #Mia
    def generate_test_stats(self): 
        """Calculating the test statistic
        Return:
            z(float): test statistics
        """
        z = (self.x - self.hO) / (self.s/self.n**2)
        return z

    #Mia
    def compare_test_stats(self):
        """Determine the result of the hypothesis test by 
            comparing the test statistic with the z_score 
        Return:
            response(list): the result of the hypothesis test 
                whether we reject HO or not 
        """
        one = self.translate_z()[0]
        two = self.translate_z()[1]
        three = self.translate_z()[2]
        response = []
        if (self.generate_test_stats() > one, two, three):
            response.append("The test statistics is greater than z-score, "
                            "therefore we do not reject HO.\n ")
        else:
            response.append("The test statistics is less than z-score, "
                            "therefore we reject HO.\n ")
        return response
          
    #Gagandeep
    def standard_error(self):
        """Calculate the standard error
        Return:
            stan(float): calculation of the standard error
        """
        total = self.df4['Health_exp_pct_GDP_2016'].count()
        stan = round((self.df4.std()/ (total)**(1/2)), 2)
        return stan

    #Affan
    def confidence_interval(self):
        """Shows the upper and lower limit for a confidence interval of 95% 
        Return:
            confid (list): upper limit, lower limit, mean
        """
        #The Confidence level is preset to 95%
        #Therefore the z value will always equal 1.96
        total= self.df4['Health_exp_pct_GDP_2016'].count()
        mean = round((self.df4['Health_exp_pct_GDP_2016'].sum()/ total), 2)
        z95=1.96 #(integer)
        om = self.standard_error()['Health_exp_pct_GDP_2016'] 

        h= z95 * om
        upper_limit=round(mean+h, 2)
        lower_limit=round(mean-h, 2)
        confid = []
        confid.append(lower_limit)
        confid.append(mean)
        confid.append(upper_limit)
        return confid
    
    #AJ
    def margin_error(self):
        """Provide results for a user by their specified number 
        Return:
            me(float): calculation of margin error 
        """
        confidence = 1.96
        critical = (1 - ((confidence)/100))
        me = round((critical * self.standard_error() \
                    ['Health_exp_public_pct_2016']), 2)
        return me
   
    #AJ
    def graph(self):
        """Provide the user visualization of the two columns
        Side effect:
            Make a bar graph with kind = 'bar',title = "Health",
                                figsize = (16, 11), legend=True, fontsize=15
        """
        a = self.df4[['Health_exp_pct_GDP_2016','Health_exp_public_pct_2016']]
        ax = a.plot(kind='bar',title ="Health", figsize=(16, 11),
                    legend=True, fontsize=15)
        ax.set_xlabel("Percentage of GDP", fontsize=15)
        ax.set_ylabel("Percentage of Current Health Expenses", fontsize=15)
        plt.show()

#Mia
def main(path):
    """Provide results for a user by his/her specified number
    Side effects:
        Display results by each user's specified number
    """
    hs = Hypothesis() 
    m1 = (f"\nMean: {hs.basic_stats()[0]} \nMedian: {hs.basic_stats()[1]} \n"
        f"Mode: {hs.basic_stats()[2]}  \n")
    m2 = (f"\nZ-score of 0.01: {hs.translate_z()[0]} \n"
        f"Z-score of 0.05: {hs.translate_z()[1]} \n" 
        f"Z-score of 0.1: {hs.translate_z()[2]} \n")
    m3 = (f"\nThe result of the hypothsis test: \n"
        f"{hs.compare_test_stats()[0]}")
    m4 = (f"\nStandard Error: {hs.standard_error()[0]} \n")
    m5 = (f"\nLower Limit: {hs.confidence_interval()[0]} \n"
        f"Mean: {hs.confidence_interval()[1]} \n"
        f"Upper Limit: {hs.confidence_interval()[2]} \n")
    m6 = (f"\nThe margin of error is {hs.margin_error()} \n")

    while True:
        response = input("\n-------------------------------\n"
                    "What would you like to see? \n"
                    "Enter:\n"
                    "1 for determine mean, mode, and median \n" #demo
                    "2 for determine z-score of the hypothesis test \n"
                    "3 for result of the hypothesis test \n"
                    "4 for determine the standard error \n" #demo
                    "5 for determine the confidence interval \n" #demo
                    "6 for determine the margin of error  \n"
                    "7 for the bar graph \n" #demo
                    "8 for all of the results \n"
                    "0 to Exit \n-------------------------------\n")

        if response == "1":
            print(m1)
        elif response == "2":
            print(m2)
        elif response == "3":
            print(m3)
        elif response == "4":
            print(m4)
        elif response == "5":
            print(m5)
        elif response == "6":
            print(m6)
        elif response == "7":
            hs.graph()
        elif response == "8":
            print(m1, m2, m3, m4, m5, m6)
            hs.graph()
        elif response == "0":
            break
        else:
            print("\n Invalid input!! \n")   

if __name__ == "__main__":
    main(sys.argv[1:])