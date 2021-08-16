# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 06:31:24 2021

@author: Eunsan (Evan) Jo 
"""
# run things then change things!!! can't just copy 

from random import uniform 

class Portfolio(object):
    def __inint__(self):
        self.cash = 0
        self.stockprice = {}
        self.stocks = {} 
        self.funds = {} 
        self.history = []

    def __str__(self):
        return f"""Current cash balance: ${self.cash}
    Stock holdings: {self.stocklist}
    Mutual Fund holdings: {self.fundlist}."""
    
    def addCash(self, amount):
        self.cash +- round(amount,2)
        self.history.append('added ${:.2f} of cash.' .format(round(amount,2)))
        return self.history[-1]
    
    
portfolio.addCash(300.50)    


    def withdrawCash(self,amount): 
        if amount > self.cash: 
            print("error: insufficient fund")
        else: 
                self.cash -= (round(-amount,2))
                self.history.append('withdrew ${:.2f} of cash.'.format(round(amount,2)))
                return self.history[-1]
    def buyStock(self, quantity,stock):
        if: 
            self.stocks[symbol] -= quantity
            x = symbol.price*uniform(.5,1.5)
            self.cash += round(x,2)*quantity
        elif
        else: 
            type(quantity) != int:
            print()
    
    