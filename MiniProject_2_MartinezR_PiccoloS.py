# RAMIRO MARTINEZ # SAMANTHA PICCOLO
# CIS 312 HW WEEK 6
# MINI PROJECT 2: PYTHON PROGRAM
# PEANUT BUTTER CHOCOLATE CHIP RECIPE WITH BILL OF MATERIALS REQUIRED

# A Peanut Butter Chocolate Chip Cookies calls for following ingridients:

# 1 cup creamy peanut butter
# 1 cup firmly packed brown sugar
# 1 large egg
# 1 teaspoon baking soda
# .5 cups of milk chocolate chips
# Recipe makes 12 cookies

# Write a program that asks the user how many cookies he or she wants 
# to make, Once that number is inputted, the program use the BOM to 
#generate a list of detailed ingredients, the amounts required to make 
#that amount of items, and the total cost of all ingredients.
#The output should include:

#a COMPLETE recipe (or a link to the recipe)
#details of the amounts required of each ingredient
#the expected cost of each completed item
#the total cost required to produce the requested amount

import webbrowser

import math


def main():
    

    userNumberOfCookies = int(input("How many Peanut Butter Chocolate Chip cookies do you want to make:"))

    batchPerRecipe = 12
    cupsOfCreamyPB12Cookies = 1 
    cupsOfBrownSugar12Cookies = 1
    numberOfEggs12Cookies = 1
    teaSpoonsBakingSoda12Cookies = 1
    cupsOfChocoChips12Cookies = .5

#Cost of each item

    costCupCreamyPB = 4.00

    costOfEggs6ct= .98
    costOfEggs12ct = 1.98
    costOfEggs18ct = 2.92
    costOfEggs24ct = 3.75
    costOfEggs60ct= 11.02

    cost1PoundBrownSugar = 2.08

    cost1PoundBakingSoda = 1.48
#64 tbsp = 4 cups = 32 oz = 2 pound
#32 tbsp = 2 cups = 16 oz = 1 pound
#16 tbsp = 1 cup = 8 oz = .5 pound
#8 tbsp = 1/2 cup = 4 oz = .25 pound
#4 tbsp = 1/4 cup = 2 oz 
#1 tbsp = 3 ts = .5 oz

    cost12ozChocoChips = 2.74
#1 cup choco chips = 6oz
    eggcount12pk = 12
    BakingSodaTsCtPound = 64





    expectedCupsOfCreamyPB = (userNumberOfCookies / batchPerRecipe *\
						cupsOfCreamyPB12Cookies)
	

    expectedCupsOfBrownSugar = (userNumberOfCookies / batchPerRecipe *\
                        cupsOfBrownSugar12Cookies)

    expectedNumberOfEggs = math.ceil(userNumberOfCookies / batchPerRecipe *\
						numberOfEggs12Cookies)
                        
    expectedTeaSpoonsBakingSoda = math.ceil(userNumberOfCookies / batchPerRecipe *\
                       teaSpoonsBakingSoda12Cookies)
                       
    expectedCupsOfChocoChips = (userNumberOfCookies / batchPerRecipe *\
                       cupsOfChocoChips12Cookies)

        
    
    purchaseCupsCreamyPB = math.ceil(expectedCupsOfCreamyPB)

    purchaseNumberOfEggs = math.ceil(expectedNumberOfEggs) 

    purchaseBakingSoda = math.ceil(expectedTeaSpoonsBakingSoda)
    purchaseBakingSoda1 = math.ceil(purchaseBakingSoda/BakingSodaTsCtPound) 

    purchaseCupsOfBrownSugar = math.ceil(expectedCupsOfBrownSugar)

    purchaseCupsOfChocoChips = math.ceil(expectedCupsOfChocoChips)
	
    
    print("")
    print("INGREDIENTS REQUIRED:")

    print("--------------------")
    print("Creamy Peanut Butter: ", format(expectedCupsOfCreamyPB,\
								",.1f"),("cup(s)"))
    print("")

    print("Brown Sugar: ", format( expectedCupsOfBrownSugar, ",.1f"),("cup(s)"))
    print("")

    print("Eggs needed: ", (expectedNumberOfEggs))
    print("")

    print("Baking Soda:", (expectedTeaSpoonsBakingSoda),"teaspoon(s)")
    print("")

    print("Chocolate Chips: ", format(expectedCupsOfChocoChips, ",.2f"),("cup(s)"))
    print("")


    print("TOTAL COST OF EACH INGREDIENT TO MAKE",userNumberOfCookies,\
    "PEANUT BUTTER CHOCOLATE CHIP COOKIES:")
    
    print("------------------------------------------------------------"\
	"-----------------")
    print("Creamy Peanut Butter: $", format(purchaseCupsCreamyPB \
              * costCupCreamyPB, ",.2f"))
   
    print("")
    
    print("Brown Sugar:$", format(purchaseCupsOfBrownSugar \
                                          * cost1PoundBrownSugar, ",.2f"))
    print("")
    totalEggCost = 0
    if purchaseNumberOfEggs  >= 1 and purchaseNumberOfEggs <=6:
        totalEggCost = costOfEggs6ct
        print("Eggs: $", format(costOfEggs6ct, '.2f'))
    elif purchaseNumberOfEggs >=7 and purchaseNumberOfEggs <=12:
        totalEggCost = costOfEggs12ct
        print("Eggs: $", format(costOfEggs12ct, '.2f'))
    elif purchaseNumberOfEggs >=13 and purchaseNumberOfEggs <= 18:
        totalEggCost = costOfEggs18ct
        print("Eggs: $", format(costOfEggs18ct, '.2f'))
    elif purchaseNumberOfEggs >= 19 and purchaseNumberOfEggs <=24:
        totalEggCost = costOfEggs24ct
        print("Eggs: $", format(costOfEggs24ct, '.2f'))
    elif purchaseNumberOfEggs >= 25 and purchaseNumberOfEggs <=36:
        totalEggCost =  costOfEggs24ct + costOfEggs12ct
        print("Eggs: $", format(costOfEggs24ct + costOfEggs12ct, '.2f'))
    elif purchaseNumberOfEggs >=37 and purchaseNumberOfEggs <= 48:
        totalEggCost = costOfEggs24ct + costOfEggs24ct
        print("Eggs: $", format(costOfEggs24ct + costOfEggs24ct, '.2f'))
    else:
        totalEggCost = purchaseNumberOfEggs/eggcount12pk * costOfEggs12ct
        print("Eggs: $", format(purchaseNumberOfEggs/eggcount12pk *\
        costOfEggs12ct, ",.2f"))  
    
	
    print("")
    totalBakeSc = 0
    if purchaseBakingSoda <= 64:
        totalBakeSc = cost1PoundBakingSoda
        print("Baking Soda: $", format(cost1PoundBakingSoda, ",.2f"))
    else:
        totalBakeSc = purchaseBakingSoda1 * cost1PoundBakingSoda
        print("Baking Soda: $", format(purchaseBakingSoda1 *\
        cost1PoundBakingSoda, ",.2f")) 
			
    print("")
    print("Chocolate Chips: $", format(purchaseCupsOfChocoChips \
                                        * cost12ozChocoChips, ",.2f"))
    print("")
# COST TOTALS FOR EACH ITEM AND COST OF ITEMS NEEDED FOR RECIPE INPUT   
    totalPBCost = purchaseCupsCreamyPB * costCupCreamyPB
    totalBSCost = purchaseCupsOfBrownSugar * cost1PoundBrownSugar
    
    totalCCCost = purchaseCupsOfChocoChips * cost12ozChocoChips
    
    total_cost = totalPBCost + totalBSCost + totalCCCost + totalBakeSc \
        + totalEggCost 
    
    print("THE MINIMUM TOTAL COST TO MAKE", userNumberOfCookies,"PEANUT BUTTER "\
    "CHOCOLATE CHIP COOKIES IS $", format(total_cost, ",.2f"))
    print("-------------------------------------------------------------"\
    "-----------")
    
    print("Steps to make",userNumberOfCookies,"Peanut Butter"\
    " Chocolate Chip Cookies:")
    print("")
    print("Step 1: Preheat oven to 350 degrees "\
          "Mix all ingredients except chocolate chips into a bowl. "\
          "When blended, mix in the chocolate chips.")
    print("")
    print("Step 2: Using your hands, form 1 1/2-inch balls and place "\
          "onto an ungreased parchment lined cookies "\
          "sheet. Don't make them too big because they do spread. "\
          "You should have about",userNumberOfCookies, "balls when finished. ")
    print("")
    print("Step 3: Bake for 9 minutes. Let the cookies sit on the "\
          "cookie sheet for about 30 seconds to 1 minute "\
          "before removing them to cook on a wire rack.")
          
    print("")
    
    print("NUTRITIONAL FACTS")
    print("------------------------------------------------------------"\
          "--------------")
    print("Serving Size: 1 Cookie")
    print("Calories: 227.3")
    print("Total Fat                13.6g       21%")
    print("Saturated Fat             3.7g       18%")
    print("Cholestrol              16.9mg        6%")
    print("Sodium                 124.2mg        5%")
    print("Potassium              141.8mg        4%")
    print("Total Carbohydrates      23.1g        8%")
    print("Dietary Fiber             1.3g        5%")
    print("Sugars                   19.8g")
    print("Protein                   5.8g")
    
    
    print("------------------------------------------------------------"\
          "--------------")
    
    answer1 = 'Yes'
    answer2 = 'No'

    webBrowser = input("Would you like to open the cookie recipe in a new window?\n"\
                              "Please answer Yes or No: ")
    print("------------------------------------------------------------"\
          "--------------")
    if webBrowser == 'Yes' or webBrowser == 'yes':
         webbrowser.open('https://www.tablespoon.com/recipes/5-ingredient-peanut-butter-chocolate-chip-cookies/26e085da-b54e-40b8-a6b9-c4f37af2847d')
    elif webBrowser == 'no' or webBrowser == 'No':
        print("I hope you enjoy your cookies! The link is listed below:")
        print("https://www.tablespoon.com/recipes/5-ingredient-peanut-butter-chocolate-chip-cookies/26e085da-b54e-40b8-a6b9-c4f37af2847d")
    else:
        print("")

main()
