class FancyFood_ER:

    def __init__(self, food_name, amount):
        self.__food_name = food_name
        self.__amount = amount
        self.__standardPrice = 0.00
        self.__calculated_price = 0.00
   

    def __standardPriceList_ER(self):
        if self.__food_name == "Dry Cured Iberian Ham":
            self.__standardPrice = 177.80

        elif self.__food_name == "Wagyu Steaks":
            self.__standardPrice = 450.00

        elif self.__food_name == "Matsutake Mushrooms":
            self.__standardPrice = 272.00

        elif self.__food_name == "Kopi Luwak Coffee":
            self.__standardPrice = 306.50

        elif self.__food_name == "Moose Cheese":
            self.__standardPrice = 487.20

        elif self.__food_name == "White Truffles":
            self.__standardPrice = 3600.00

        elif self.__food_name == "Blue Fin Tuna":
            self.__standardPrice = 3603.00

        elif self.__food_name == "Le Bonnotte Potatoes":
            self.__standardPrice = 270.81

        else:
            self.__standardPrice = 0.00
    

    #getters
    def get_food_name_ER(self):
        return self.__food_name
    
    def get_amount_ER(self):
        return self.__amount
    
    def get_standard_price_ER(self):
        self.__standardPriceList_ER()
        return self.__standardPrice
    
    def get_calculated_price_ER(self):
        return self.__calculated_price
    
    #calculate cost 
    def calculate_price_ER(self):
        self.__standardPriceList_ER()
        return (self.__amount * self.__standardPrice)
    
    #str functions
    def __str__(self):
        return f"Item: {self.get_food_name_ER()} \nAmount ordered: {self.get_amount_ER()} pounds \nPrice per pound: ${self.get_standard_price_ER():.2f} \nPrice of order: ${self.calculate_price_ER():.2f}"



