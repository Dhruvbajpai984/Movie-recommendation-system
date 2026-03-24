# Movie Recommendation System (Python)
​A simple, interactive command-line interface (CLI) that suggests similar movies based on a user's input. This project demonstrates the use of Python dictionaries, loops, and basic user-input handling.
​## Features
​Curated Suggestions: Provides a list of three similar titles for every movie in the database.
​Case-Insensitive Search: Users can type "AVENGERS" or "avengers" and still get results.
​Interactive Loop: Allows users to perform multiple searches without restarting the script.
​Clean Interface: Simple text-based output for quick recommendations.
​## How It Works
​The system operates on a predefined dictionary where the keys are the movies the user searches for, and the values are lists of recommended titles.
​### Logic Flow:
​Displays the list of available movies to the user.
​Prompts the user for a movie name.
​Converts input to lowercase to match dictionary keys.
​If found, it iterates through the associated list and prints the recommendations.
​Asks the user if they wish to continue or exit.
​## Usage
