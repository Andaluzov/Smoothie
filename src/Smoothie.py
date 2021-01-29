class Smoothie:
    def __init__(self, ingredients):     # конструктор принимает параметр ingredients ("ингредиенты")
        self.ingredients = ingredients

    def get_cost(self):
        sum = 0
        for ingredient in self.ingredients:
            sum += ingredient["cost"]
        return sum

    def get_price(self):            #вычисляет цену смузи
        all_sum = self.get_cost() + self.get_cost()*1.5
        return all_sum

    def get_name(self):
#Формирует и возвращает строку
#располагает ингредиенты в алфавитном порядке,
# если игредиентов много - добавляет слово "Fusion" в конец, иначе - добавляет "Smoothie"
# (ингредиенты,
# заканчивающиеся на '-berries', нужно изменить так, что они будут заканчиваться на "-berry").

        new_spisok = []
        stroka = ''
        len_ingr = len(self.ingredients)
        ingred = ''

        for ingredient in self.ingredients:
            new_spisok.append(ingredient["name"])

        new_spisok = sorted(new_spisok)
        for ingredient in new_spisok:
            if "berries" in ingredient:
                ingredient = ingredient[:-3] + 'y'
            stroka +=  ingredient +' '
        if len_ingr >1:
            stroka += 'Fusion'
        else:
            stroka += 'Smoothie'
        return   stroka

