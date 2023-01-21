import random
from argparse import ArgumentParser
import math

class User:
    """ A user in the world hunger app

    Attributes:
        name(str) : the person's name.
        
    """
    def __init__(self,name):
        """Initializes the world hunger app.
        
        Side Effects:
            Sets the name attribute

        """
        self.name = name
        self.orders = 0 
        self.order_list = {}
        self.order_total = 0
        self.reward_points = 0
        self.countries = ['Yemen','Indonesia','Sierra Leone','Ecuador','Colombia']
        self.items = {'rice':15,'water':12,'beans':8,'corn':7,'chicken':19,'grain':5,'squash':9}
        
    def selection_stage(self):
        """Allows users to set their name,country/countries, and item/items to donate. 
        
        Side Effects: 
            sets the name attribute, and updates the orders and order_total variables based on the countries and items selection
            
        """
        username = input("Enter your username: ")
        self.name = username
        country_select = input(f"choose the country to donate to from the list provided.{self.countries}")
        item_select = input(f"choose an item to donate.{self.items}")
        order_status = input("Continue Order?(Yes or No)")
        while country_select in self.countries and item_select in self.items:
            self.countries = country_select
            self.order_list.append(item_select)
            while order_status == "Yes" or "yes":
                item_select = input(f"choose an item to donate.{self.items}")
                self.order_list.append(item_select)
        
        return self.order_list
        
        
    def accumulation_total(self,accumulation_val):
        accumulation_val = sum(self.order_list[item] for item in self.order_list)
        self.order_total = accumulation_val
        return self.order_total
    
    def rewards_calc(self):
        """1 reward point is given for every $0.10 spent"""
        self.reward_points = self.order_total*10
        return self.reward_points
            
    def rewards_redemption(self):
        reward_select = input("Choose reward(s): 1)Playstation 5 (5,000), 2)65 inch smart T.V. (4,500), 3)$100 Visa gift card(1,000), 4)Moped Segway(12,000)")
        if self.reward_points >= 5000 and reward_select == "Playstation 5" or 1:
            self.reward_points-=5000
        elif self.reward_points >= 4500 and reward_select == "65 inch smart T.V." or 2:
            self.reward_points-=4500
        elif self.reward_points >= 1000 and reward_select == "Visa gift card" or 3:
            self.reward_points-=1000
        elif self.reward_points >= 12000 and reward_select == "Moped Segway" or 4:
            self.reward_points-=12000
        else:
            print("Insufficient points. Keep shopping to earn more reward ponints!")