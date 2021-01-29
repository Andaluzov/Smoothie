"Смузи"
---------------------------

Дан список ингридиентов и их стоимость:

Strawberries  1.50
Banana  0.50
Mango  2.50
Blueberries  1.00
Raspberries  1.00
Apple  1.75
Pineapple  3.50

Нужно написать программу, которая будет высчитывать цену и стоимость напитков, созданных на основе этих ингридиентов.

Требования:
В отдельном файле создать класс Smoothie. У этого класса должны быть:
- конструктор, который принимает в качестве параметра список ингридиентов для этого смузи;
- аттрибут ingredients (аттрибут экземпляра, не аттрибут класса);
- метод get_cost - вычисляет общую стоимость ингредиентов, используемых для приготовления смузи;
- метод get_price - вычисляет цену смузи: общая стоимость ингридиентов (из метода выше) + общая стоимость * 1.5. Округлить до 2 цифр после запятой;
- метод get_name - Формирует и возвращает строку: располагает ингредиенты в алфавитном порядке, если игредиентов много - добавляет слово "Fusion" в конец, иначе - добавляет "Smoothie" (ингредиенты, заканчивающиеся на '-berries', нужно изменить так, что они будут заканчиваться на "-berry").

В другом файле:
- создать объект, который будет хранить список ингридиентов, описанных выше; 
- создать метод get_smoothie_info, который в качестве параметра будет принимать объект типа (класса) Smoothie, и будет выводить в консоль информацию о смузи - текст:
    Name: {название смузи}
    Ingredients: {ингридиенты через запятую}
    Cost: ${стоимость}
    Price: ${цена}
- создать 3 экземпляра класса Smoothie с разными ингридиентами (при этом один из них должен содержать 1 игридиент). Для каждого из них вывести в консоль информацию о коктейле (с помощью метода get_smoothie_info).










