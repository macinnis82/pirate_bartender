The basic requirements

Create questions and ingredient dictionaries
The bartender should ask questions that determine your tastes and then identify ingredients to suit those tastes. If you like you can use our example bartender below, but feel free to customize!

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
Write a function to ask what style of drink a customer likes
The function should ask each of the questions in the questions dictionary, and gather the responses in a new dictionary. The new dictionary should contain the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean value. If the customer answers y or yes to the question then the value should be True, otherwise the value should be False. The function should return the new dictionary.

Remember that you can use the raw_input function to get an answer from the customer. If you can't remember how this works then take a look back over the instructions for the FizzBuzz project.

Write a function to construct a drink
The function should take the preferences dictionary created in the first function as a parameter. Inside the function you should create an empty list to represent the drink. For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink. Finally the function should return the drink.

To choose an ingredient from one of the ingredient lists you can use the random.choice function. This selects a random item from a list, for example:

import random

beatles = ["John", "Paul", "George", "Ringo"]
# Print the name of a random Beatle
print random.choice(beatles)
Provide a main function
Use if __name__ == '__main__': to run this function from the command line. The main function should call your two functions in order, passing your list of preferences to the drink creation function. It should then print out the contents of the drink.

Use version control
You should create a new git repo for this assignment. Be sure to commit your file when you've completed this project and push it up to Github.

Get feedback from your Mentor
Share a link to the project with your mentor and be sure to get feedback at your next mentor session.

Discussion

Once you've completed the basic requirements for the project, feel free to take a look at this sample solution. Compare and contrast your solution. What do you like better about the sample? What do you like better about yours?

Extra challenges

If you found completing the basic requirements fairly straightforward then you should try to extend your app to add the following features:

Give the cocktails a name
All good cocktails should have a memorable name. Try to write a function which will name your cocktails. The name should be a random combination of an adjective and a noun (for example your bartender could make a "Fluffy Chinchilla", a "Salty Sea-Dog", or a "Fluffy Sea-Dog").

Keep 'em coming
At the moment you can only get one drink at a time from the bartender. A well trained pirate bartender should offer his customer another drink when they've finished their previous one. Try adding a loop in the main function which will ask the customer whether they want another drink, and keep creating new recipes as long as they agree.
