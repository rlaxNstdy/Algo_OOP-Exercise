class Food :
    def __init__(self, food, amount):
        self._food_name = food
        self._food_amountpound = amount
        self._price_per_pound = None
        self._calculated_price = None

    def updatefoodname(self,food):
       self.update__foodname = food
       return self._food_name
    
    def updateamount(self,amount):
        self.update__amount = amount 
        return self._food_amountpound
    
    def getpricelist(self):
        return self._price_per_pound
    
    def getcalulated(self):
        return self._calculated_price
    
    def pricelist(self):
        if self._food_name == 'Dry Cured Iberian Ham' :
           self._price_per_pound = 177.80
        elif self._food_name == 'Wagyu Steaks' :
           self._price_per_pound = 450.00
        elif self._food_name == 'Matsutake Mushrooms' :
           self._price_per_pound = 272.00
        elif self._food_name == 'Kopi Luwak Coffee' :
           self._price_per_pound = 306.50
        elif self._food_name == 'Moose Cheese' :
           self._price_per_pound = 487.20
        elif self._food_name == 'White Truffles' :
           self._price_per_pound = 3600.00
        elif self._food_name == 'Blue Fin Tuna' :
           self._price_per_pound = 3603.00
        elif self._food_name == 'Le Bonnotte Potatoes' :
           self._price_per_pound = 270.81

    def calculate_cost(self) :
       if self._food_name in self._price_per_pound:
          self._calculated_price =  self._food_amountpound * self._price_per_pound[self._food_name]
          return self._calculated_price
       
    def get_food_name(self):
        return self._food_name

    def get_amount(self):
        return self._food_amountpound

    def get_standard_price_per_pound(self):
        return self._price_per_pound

    def __str__(self):
        return f"Food: {self._food_name}, Amount: {self._food_amountpound} pounds, " \
               f"Standard Price per Pound: {self._price_per_pound}, " \
               f"Calculated Price: {self._calculated_price}"
          
           
        

        

        



        