from Smoothie import Smoothie
import infosmoothie as info


ingredients = [
    {"name": "Strawberries", "cost": 1.50},
    {"name": "Banana", "cost": 0.50},
    {"name": "Mango", "cost": 2.50},
    {"name": "Blueberries", "cost": 1.00},
    {"name": "Raspberries", "cost": 1.00},
    {"name": "Apple", "cost": 1.75},
    {"name": "Pineapple", "cost": 3.50}
    ]

smoothie1 = Smoothie([ingredients[0], ingredients[1]])
info.get_smoothie_info(smoothie1)

smoothie2 = Smoothie([ingredients[3] ])
info.get_smoothie_info(smoothie2)

smoothie3 = Smoothie([ingredients[0], ingredients[6],ingredients[2], ingredients[5]])
info.get_smoothie_info(smoothie3)