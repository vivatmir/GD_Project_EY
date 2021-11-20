# PROJECT. Исследование поведения пользователей (SF_38.9)
## Описание гипотезы

Проверим два предположения:

* Зависит ли вероятность оплаты от выбранного пользователем уровня сложности бесплатных тренировок?
* Существует ли разница во времени между пользователями с разным уровнем сложности и их первой оплатой?

Проверку будем производить на основе данных пользователей, которые зарегистрировались в 2018 году.

## Ход проверки

Произведем преобразование типов (user.py)
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
