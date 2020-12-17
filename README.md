# 533lab4
![CI-potterworld](https://github.com/cfbanks/data-533-lab4/workflows/CI-potterworld/badge.svg)

## **Continuous Integration:**
- See screenshot (`actions_screenshot.png`) of the github actions page used for CI. 
- See `.github/workflows/main.yml` file for the CI workflow script (used instead of Travis CI)

## **Github Collaboration:**
- See `Git_Collaboration_history.png` for github collaboration history and branches. Some work was completed on another github repository prior to migrating files to this final repository.

## **Testing Notes:**

User Defined Exception 1: 'InsufficientBalance' in hogwarts.py    
User Defined Exception 2: 'InvalidRating' in quidditch.py


**Exception handling in other functions:**

hogwarts.py 
 - gringotts()
 - get_wand()

wizard.py
 - night_crawl() 
 - play_quidditch()
 - fight_voldemort()

duel.py
 - duel_voldemort()

learn_spells.py
 - get_wand_movement_pattern()

quidditch.py
 - raise InvalidRating
 - quidditch() 

**Testing files for reference:**

testing_naveen.ipynb
connor_testing.ipynb

## **Coverage:**
- See `screenshot_coverage.png` and `htmlcov` folder for coverage summary.
- See `test_coverage.py` for testing script.

## **Package:**
- Package name uploaded to PyPI: potterworld
- **Important**: To start using the package, write `from potterworld import *`, If you just write "import potterworld", the package may not work properly.

____________

# potterworld package
### Names: Connor Fairbanks, Naveen Chalasani
### Date: December 17, 2020

## General description
This package allows the user to experience the magical world of Harry Potter. By using the functions/methods, the user assumes a magical identity, joins the hogwarts school of witchcraft and wizardry, and experieces other joys of magical life by playing games like Quidditch, duelling Lord Voldemort, etc.

The user begins using the package by initiating themselves as a wizard (object in the wizard class) and follows printed instructions from there onwards. 

## Map of Steps: 

The wizard will perform the following tasks in order:

1. Initiate the wizard
2. Exchange Currency
3. Buy a wand
4. Be sorted into a house
5. Learn Spells

The following tasks can be repeated multiple times and their order doesn't matter:

6. Play a quidditch match
7. Sneak out at night to explore the castle
8. Duel Voldemort

9. The user can finish by finding out who wins the house cup. 

## Functions:
- gringotts : Converts canadian dollar number to wizarding currency
- get_wand : Uses the superclass to assign a wand to the wizard and print the wand details
- sorting_hat : Sorts the wizard into a Hogwarts house (Gryffindor, Hufflepuff, Ravenclaw, Slytherin)
- learn_spells : Allows wizard to learn several spells, and also allows them to create their own special spell.
- night_crawl : Takes the wizard through a narrative simulating a late night exploration of hogwarts castle.
- play_quidditch : Different houses at Hogwarts compete with each other by playing Quidditch using this function. 
- fight_voldemort : The wizard fights Lord Voldemort to death in this duel.
- display : Displays the current class object attributes and gives the user instructions for the next step.
- house_cup_winner : Outputs house cup points score and the winner of the house cup. 
    
See documentation of classes and functions for further details.
