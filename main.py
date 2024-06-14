# importing appropriate packages
import ndjson
import pandas as pd
import re

def convert_to_minutes(duration):
    """
    This function takes the duration, with the original format provided in the prepTime and cookTime fields,
    as an input and returns the duration in minutes

    Args:
    - duration (str): The duration string in ISO 8601 format.

    Returns:
    - int: Total duration in minutes.
    """
    hours_index = duration.find('H')
    minutes_index = duration.find('M')

    hours = 0
    minutes = 0

    if hours_index != -1:
        hours_start = duration.find('T') + 1
        hours = int(duration[hours_start:hours_index])

    if minutes_index != -1:
        if hours_index != -1:
            minutes_start = hours_index + 1 
        else:
            minutes_start = duration.find('T') + 1
        minutes = int(duration[minutes_start:minutes_index])

    total_minutes = (hours * 60) + minutes
    return total_minutes



# reading the ndjson format and converting to a list of dictionaries
with open(r'data/recipes.json') as json_file:
    recipes = ndjson.load(json_file)

# listing the possible variants of how 'chilies' or 'chilis' might be misspelled
chilies_variants = ['chilies', 'chiles', 'chili', 'chile', 'chillies', 'chilles', 'chilli', 'chille', 'chillie', 'chilie']

# initializing the list of recipes with chilies included in them
chilies_list = []

# iterating through the each recipe and adding the recipes with chilies into the list
for recipe in recipes:
    # splitting the ingredients text into list of words
    ingredients_string = recipe['ingredients']
    ingredients_words = ingredients_string.split()
    # when 'chilies' or a likely misspelling is found once in the list of words, save the recipe in the new list
    for word in ingredients_words:
        if word.lower() in chilies_variants:
            chilies_list.append(recipe)
            break


# convert to pandas dataframe
df = pd.DataFrame(chilies_list)

# replacing the adversely created characters in the ingredients field
replacements = {
    r'\n': "; ",                    
    r'&amp;': "and"
}
df = df.replace(replacements, regex=True)



# to apply the logic for creating the 'difficulty' column, I first convert the prepTime and cookTime into minutes using the function created
prep_time_mins = df['prepTime'].apply(convert_to_minutes)
cook_time_mins = df['cookTime'].apply(convert_to_minutes)

# if either the prepTime or cookTime values are incomplete, then the difficulty setting will be set to 'Unknown':

# mask conditions: prepTime and cookTime are both non-null, and both have at least one digit
mask = (df['prepTime'].str.contains(r'\d', na=False) & df['cookTime'].str.contains(r'\d', na=False)) & (df['prepTime'].notnull() & df['cookTime'].notnull())
df.loc[~mask, 'difficulty'] = 'Unknown'
df.loc[mask & (prep_time_mins + cook_time_mins > 60), 'difficulty'] = 'Hard'
df.loc[mask & (30 <= prep_time_mins + cook_time_mins) & (prep_time_mins + cook_time_mins <= 60), 'difficulty'] = 'Medium'
df.loc[mask & (prep_time_mins + cook_time_mins < 30), 'difficulty'] = 'Easy'


# saving the dataframe to a CSV file. This can be found in the data folder in this repo
df.to_csv('data/chili_recipes_with_difficulty.csv',encoding='utf-8-sig', index=False)