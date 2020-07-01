import pyinputplus as pyip

costOfEach = {"wheat": 0.49, "white": 0.69, "sourdough": 79,
         "chicken": 1.02, "turkey": 1, "ham": 0.5, "tofu": 2.03,
         "cheddar": 1.6, "Swiss": 1.3, "mozzarella": 1.5,
         "mayo": 0.25, "mustard": 0.10, "lettuce": 0.10, "tomato": 0.25} #credit to Affectionate-Lettuce on reddit for dictionary


price = 0.00

bread = pyip.inputMenu(["wheat", "white", "sourdough"])

price += costOfEach[bread]

protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])

price += costOfEach[protein]


cheese = pyip.inputYesNo("Do you want cheese?")
if cheese == "yes":
    whichCheese = pyip.inputMenu(["cheddar", "Swiss",  "mozzarella"])
    price += costOfEach[whichCheese]



condiment1 = pyip.inputYesNo("Do you want mayo? ")
if condiment1 == "yes":
    price += costOfEach["mayo"]
condiment2 = pyip.inputYesNo("Do you want mustard? ")
if condiment2 == "yes":
    price += costOfEach["mustard"]
condiment3 = pyip.inputYesNo("Do you want lettuce? ")
if condiment3 == "yes":
    price += costOfEach["lettuce"]
condiment4 = pyip.inputYesNo("Do you want  tomato's? ")
if condiment4 == "yes":
    price += costOfEach["tomato"]





numberOfSandwiches = pyip.inputInt("How many sendwiches would you like? ", default=1)

print("Your total price comes to %s€ for %i Sandwich/Sandwiches" % (price, numberOfSandwiches))
