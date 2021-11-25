# PROJECT. Исследование поведения пользователей (SF_38.9)
## Описание гипотезы

Проверим два предположения:

* Зависит ли вероятность оплаты от выбранного пользователем уровня сложности бесплатных тренировок?
* Существует ли разница во времени между пользователями с разным уровнем сложности и их первой оплатой?

Проверку будем производить на основе данных пользователей, которые зарегистрировались в 2018 году.

## Ход проверки

[Часть 1. Произведем преобразование типов](https://github.com/vivatmir/GD_Project_EY/blob/main/Part_1/user2018.py)

[Часть 2. Сделаем объединенный датафрейм из событий и оплат](https://github.com/vivatmir/GD_Project_EY/blob/main/Part_2/events_purchase.py)

[Часть 3 Находим группы пользователей по уровню сложности, который был выбран для тренировок](https://github.com/vivatmir/GD_Project_EY/blob/main/Part_3/training.py)

[Часть 4 Сформируем группы](https://github.com/vivatmir/GD_Project_EY/blob/main/Part_4/group.py)

## Выводы 
Процент оплативших пользователей, выбравших уровень сложности easy: 7.72%. Среднее время между выбором уровня сложности и оплатой для пользователей, выбравших уровень сложности easy: 3 days 14:58:52.941798941

Процент оплативших пользователей, выбравших уровень сложности medium: 20.86%. Среднее время между выбором уровня сложности и оплатой для пользователей, выбравших уровень сложности medium: 3 days 23:14:13.165118679

Процент оплативших пользователей, выбравших уровень сложности hard: 35.39%. Среднее время между выбором уровня сложности и оплатой для пользователей, выбравших уровень сложности hard: 3 days 07:20:41.420814479




