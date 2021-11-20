# PROJECT. Исследование поведения пользователей (SF_38.9)
## Описание гипотезы

Проверим два предположения:

* Зависит ли вероятность оплаты от выбранного пользователем уровня сложности бесплатных тренировок?
* Существует ли разница во времени между пользователями с разным уровнем сложности и их первой оплатой?

Проверку будем производить на основе данных пользователей, которые зарегистрировались в 2018 году.

## Ход проверки

* [Часть 1. Произведем преобразование типов] (https://github.com/vivatmir/GD_Project_EY/blob/main/%D0%A7%D0%B0%D1%81%D1%82%D1%8C%201/user2018.py)
import pandas as pd
df = pd.read_csv('gamedev38/events.csv')
df2 = pd.read_csv('gamedev38/purchase.csv')
cond = (df.start_time>='2018-01-01') & (df.start_time<'2019-01-01') & (df.event_type=='registration')
cond2 = (df2.event_datetime>='2018-01-01') & (df2.event_datetime<'2019-01-01') & (df.event_type=='registration')
registered = df[cond]['user_id'].to_list()
registered2 = df2[cond2]['user_id'].to_list()
events = df[df.user_id.isin(registered)]
events.start_time = pd.to_datetime(events.start_time, format='%Y-%m-%dT%H:%M:%S')
df2['event_type'] = 'purchase'
purchase = df2[df2.user_id.isin(registered2)]
purchase.event_datetime = pd.to_datetime(purchase.event_datetime, format='%Y-%m-%dT%H:%M:%S')
print(events.start_time)
print(purchase.event_datetime)

### Часть 2. Сделаем объединенный датафрейм из событий и оплат (events_purchase.py)
import pandas as pd
df = pd.read_csv('gamedev38/events.csv')
df2 = pd.read_csv('gamedev38/purchase.csv')
total_events_df = pd.concat([df,df2],sort=False)
print(total_events_df)

### Часть 3. Сделаем группы пользователей по уровню сложности, который был выбран для тренировок (training.py)

#### Часть 3.1 Уровни
import pandas as pd
df = pd.read_csv('gamedev38/events.csv')
df2 = pd.read_csv('gamedev38/purchase.csv')
total_events_df = pd.concat([df,df2],sort=False)
print(total_events_df['selected_level'].unique())

Результат: [nan 'hard' 'easy' 'medium']

#### Сформируем группы (group.py)



