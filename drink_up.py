import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}
 
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = [ "Admirable", "Beloved", "Definitive", "Klutzy", "Rusty" ]
nouns = [ "Flower", "Beast", "Kiss", "Volcano", "Dock" ]

def drink_choice():
    cust_drink = {}
    print "Please answer yes or no to the following questions:"
    
    strong = raw_input(questions['strong'])
    if strong[0] == 'y' or strong[0] == 'Y':
        cust_drink['strong'] = True
    else:
        cust_drink['strong'] = False
    
    salty = raw_input(questions['salty'])
    if salty[0] == 'y' or salty[0] == 'Y':
        cust_drink['salty'] = True
    else:
        cust_drink['salty'] = False
    
    bitter = raw_input(questions['bitter'])
    if bitter[0] == 'y' or bitter[0] == 'Y':
        cust_drink['bitter'] = True
    else:
        cust_drink['bitter'] = False
        
    sweet = raw_input(questions['sweet'])
    if sweet[0] == 'y' or sweet[0] == 'Y':
        cust_drink['sweet'] = True
    else:
        cust_drink['sweet'] = False
    
    fruity = raw_input(questions['fruity'])
    if fruity[0] == 'y' or fruity[0] == 'Y':
        cust_drink['fruity'] = True
    else:
        cust_drink['fruity'] = False
        
    return cust_drink
    
def make_drink(preferences):
    drink = {}
    
    if preferences['strong'] == True:
        drink['strong'] = random.choice(ingredients['strong'])
    
    if preferences['salty'] == True:
        drink['salty'] = random.choice(ingredients['salty'])
    
    if preferences['bitter'] == True:
        drink['bitter'] = random.choice(ingredients['bitter'])
    
    if preferences['sweet'] == True:
        drink['sweet'] = random.choice(ingredients['sweet'])
    
    if preferences['fruity'] == True:
        drink['fruity'] = random.choice(ingredients['fruity'])
        
    return drink
    
def drink_name():
    name = random.choice(adjectives) +" "+ random.choice(nouns)
    return name
    
if __name__ == '__main__':
	answers = drink_choice()
	#print answers
	drink = make_drink(answers)
	#print drink
	print "Drink up ... your drink contains the following ingredients:"
	for things in drink:
		print 'A ' + drink['{}'.format(things)]
	print "Your drink will be called {}!".format(drink_name())
	
    