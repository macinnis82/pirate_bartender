The basic requirements

Create questions and ingredient dictionaries
    The bartender should ask questions that determine your tastes and then identify ingredients to suit those tastes.

Write a function to ask what style of drink a customer likes
    The function should ask each of the questions in the questions dictionary, and gather the responses in a new dictionary. The new dictionary should contain the type of ingredient (for example "salty", or "sweet"), mapped to a Boolean value. If the customer answers y or yes to the question then the value should be True, otherwise the value should be False. The function should return the new dictionary.

Remember that you can use the raw_input function to get an answer from the customer. If you can't remember how this works then take a look back over the instructions for the FizzBuzz project.

Write a function to construct a drink
    The function should take the preferences dictionary created in the first function as a parameter. Inside the function you should create an empty list to represent the drink. For each type of ingredient which the customer said they liked you should append a corresponding ingredient from the ingredients dictionary to the drink. Finally the function should return the drink.

To choose an ingredient from one of the ingredient lists you can use the random.choice function.

Extra challenges

Give the cocktails a name
    All good cocktails should have a memorable name. Try to write a function which will name your cocktails. The name should be a random combination of an adjective and a noun (for example your bartender could make a "Fluffy Chinchilla", a "Salty Sea-Dog", or a "Fluffy Sea-Dog").
