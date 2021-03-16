import pandas as pd 
import numpy as np


class bmi(object):

    def __init__(self,filename):
        self.filename = filename
        self.df = self.read_inpt()

    def read_inpt(self):
        self.df = pd.read_json(self.filename)
        print('------------------raw input-------------------')
        print(self.df.to_string(index=False))
        return self.df 
        
    def bmi_calc(self):
        self.df['BMI'] = self.df['WeightKg']/((self.df['HeightCm']/100)**2)
        print('---------------table with calculated BMI-------------')
        print(self.df.to_string(index=False))
        return self.df

    def bmi_conditioning_labelling(self):    
        conditions = [(self.df['BMI'] <= 18.4),
                        (self.df['BMI'] >= 18.5) & (self.df['BMI'] <= 24.9),
                        (self.df['BMI'] >= 25) & (self.df['BMI'] <= 29.9),
                        (self.df['BMI'] >= 30) & (self.df['BMI'] <= 34.9),
                        (self.df['BMI'] >= 35) & (self.df['BMI'] <= 39.9),
                        (self.df['BMI'] >= 40)] 
        bmi_category = ['underweight','normalweight','overweight','moderatelyobese','severelyobese','veryseverelyobese']
        health_risk  = ['malnutrition','low','enhanced','medium','high','veryhigh']
        self.df['bmi_category'] = np.select(conditions,bmi_category) 
        self.df['health_risk'] = np.select(conditions,health_risk)
        print('----------Conditioned table with appropriate labels-----------')
        print(self.df.to_string(index=False))
        self.df.to_csv('e:/CV-Profile/PHASE2_DEC-2020/VAMSTAR/Test/code-20210316-abhishekpanda/Table1.csv',sep=",", header=True, index=False)
        return self.df


    def inference_operator(self): 
        self.df1 = self.df.copy() 
        self.df2 = self.df1.groupby(['bmi_category', 'health_risk']).agg({'BMI': ['mean'],'bmi_category':['count']})
        self.df2.columns = ['mean_bmi', 'count']
        self.df2 = self.df2.reset_index()
        print("-----------inference table-----------")
        print(self.df2.to_string(index=False))
        self.df2.to_csv('e:/CV-Profile/PHASE2_DEC-2020/VAMSTAR/Test/code-20210316-abhishekpanda/Inference_Table.csv',sep=",", header=True, index=False)
        return self.df2


def main():
    name = input("Enter input file along with full path:\n")
    # for example enter the following:- e:/CV-Profile/PHASE2_DEC-2020/VAMSTAR/Test/code-20210316-abhishekpanda/input_data.json
    x = bmi(name)
    x.bmi_calc()
    x.bmi_conditioning_labelling()
    x.inference_operator()


if __name__ == '__main__':
        main()
        print('\n')
        input("Press ENTER to close the terminal")

