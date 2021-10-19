from config import *
import joblib, pandas as pd

def wealth_groups(x):
    '''
    x: This is a value from df['Monthly_Income']
    returns each as a new categorical value of 20s or 30s
    
    The range for categorizing income class
    
    - Poor Class: ₹2500-₹6500 per month

    - Lower Class: ₹6500-₹15000 per month

    - Middle Class: ₹15000-₹100000 per month

    - Upper Class: ₹100000-₹350000 per month
    
    '''
    x = float(x)

    if x <= 6500:
        return 'poor'
    elif x <= 15000:
        return 'lower'
    elif x <= 100000:
        return 'middle'
    else:
        return 'upper'

def household_groups(x):
    '''
    x: This is a value from df['FamilyMembers']
    returns each as a new categorical value of 20s or 30s
    
    The range for categorizing income class
    
    - 1 = single 
    
    - 2-4 = small

    - 5-10 = medium

    - >10 = large
    
    '''
    x = int(x)
    if x == 1:
        return 'single'
    elif x <= 4:
        return 'small'
    elif x <= 10:
        return 'medium'
    else:
        return 'large'


def get_model_prediction(customer):
    print(customer.graduate)
    customer_attribute = pd.DataFrame()
    customer_attribute.loc[1,'GraduateOrNot']                                 = 1 if customer.graduate == 'Yes' else 0
    customer_attribute.loc[1,'ChronicDiseases']                               = 1 if customer.disease == 'Yes' else 0 
    customer_attribute.loc[1,'FrequentFlyer']                                 = 1 if customer.frequent == 'Yes' else 0 
    customer_attribute.loc[1,'EverTravelledAbroad']                           = 1 if customer.abroad == 'Yes' else 0  
    customer_attribute.loc[1,'Age_Groups_20s']                                = 0 if int(customer.age) < 30 else 0
    customer_attribute.loc[1,'Age_Groups_30s']                                = 0 if int(customer.age) >= 30 else 0
    customer_attribute.loc[1,'Employment Type_Government Sector']             = 0 if int(customer.employment) == 1 else 0
    customer_attribute.loc[1,'Employment Type_Private Sector/Self Employed']  = 0 if int(customer.employment) == 0 else 0
    customer_attribute.loc[1,'Income_Class_middle']                           = 1 if wealth_groups(customer.income) == 'middle' else 0
    customer_attribute.loc[1,'Income_Class_upper']                            = 1 if wealth_groups(customer.income) == 'upper' else 0
    customer_attribute.loc[1,'Household_Size_medium']                         = 1 if household_groups(customer.family) == 'medium' else 0
    customer_attribute.loc[1,'Household_Size_small']                          = 1 if household_groups(customer.family) == 'small' else 0

    loaded_model = joblib.load(f'./models/{customer.model}.sav')
    prop_result = loaded_model.predict_proba(customer_attribute)[:, 1][0]
    
    return f'{float(prop_result):0.3f}'

class Customer():
    def __init__(self, **input_values):
        cut_off_value = 0.5
        self.age         = input_values['age']
        self.employment  = input_values['employment']
        self.graduate    = input_values['graduate']
        self.income      = input_values['income']
        self.family      = input_values['family']
        self.disease     = input_values['disease']
        self.frequent    = input_values['frequent']
        self.abroad      = input_values['abroad']
        self.model       = input_values['model']
        self.prop        = get_model_prediction(self) 
        self.status = 'green' if float(self.prop) > cut_off_value else 'red'


def post_values_to_page(**input_values):
    customer = Customer(**input_values)
    output = {
        'value_prop'       : customer.prop,
        'prop_box_style'   : get_prop_style(customer.status),
        'placeholder_age'  : 'Age',
        'value_age'        : customer.age,
        'value_income'     : customer.income,
        'value_family'     : customer.family,
        'val0ue_employment': customer.employment,
        'value_graduate'   : customer.graduate,
        'value_frequent'   : customer.frequent,
        'value_model'      : customer.model
    }
    
    return output

    