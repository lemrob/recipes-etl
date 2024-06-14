# 🌶️🌶️ Chili-Based Recipes 🌶️🌶️

# Recipe ETL Script

## Overview

The script reads a JSON file containing recipes data, identifies recipes with "Chilies" (including likely misspellings) in their ingredients, adds a "difficulty" field based on preparation and cooking times, cleans the data and saves the filtered recipes into a CSV file.

In order to retrieve the CSV file, you need to run the main.py file! This will then output the CSV into the 'data' folder within this repository.


## Features

- Extracts recipes with "Chilies" from a JSON dataset and converts this to a cleaned pandas dataframe.
- Using a function to translate the prepTime and cookTime columns into minutes, calculates the 'difficulty' level of each recipe.
- Creates a new 'difficulty' field based on these time durations.
- Those recipes with missing values in prepTime or cookTime have an 'Unknown' difficulty.
- Outputs the filtered recipes into a CSV file, which is automatically saved in the 'data' folder in this repository


## Requirements

- Python 3 (any version 3)
- All the packages to be installed are listed in `requirements.txt`
- pip (package installer)


## Installation

### In  line with the assignment, this repository has been sent over as email attachments

1. **Download the project files:**

   Ensure you have downloaded all the necessary files included in the email attachment.

2. **Extract the files:**

   Extract the downloaded files to a directory on your computer.

3. **Navigate to the project directory:**

   Open your terminal or command prompt and navigate to the directory where you extracted the files.

4. **Install required packages:**

   Make sure you have `pip` installed. Then run the following in your terminal:

   ```sh
   pip install -r requirements.txt


## Running the Script

Make sure recipes.json is in the same directory as main.py and run the following in your terminal:

```sh
python main.py