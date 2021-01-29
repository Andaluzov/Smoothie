def get_smoothie_info(smoothie):
    '''создать метод get_smoothie_info, который в качестве параметра
    будет принимать объект типа (класса) Smoothie,
    и будет выводить в консоль информацию о смузи - текст:
    Name: {название смузи}
    Ingredients: {ингридиенты через запятую}
    Cost: ${стоимость}
    Price: ${цена}'''

    ingredients = ''
    spisok = smoothie.get_name().split()
    for ingred in spisok[:-1]:
        ingredients += ingred + ','

    print('Name:', smoothie.get_name())
    print('Ingredients:', ingredients[:-1])
    print('Cost:', smoothie.get_cost())
    print('Price:', smoothie.get_price())
