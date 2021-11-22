import pandas as pd
df = pd.read_csv('events.csv')
df2 = pd.read_csv('purchase.csv')
cond = (df.start_time>='2018-01-01') & (df.start_time<'2019-01-01') & (df.event_type=='registration')
registered = df[cond]['user_id'].to_list()
events = df[df.user_id.isin(registered)]
events.start_time = pd.to_datetime(events.start_time, format='%Y-%m-%dT%H:%M:%S')
df2['event_type'] = 'purchase'
purchase = df2[df2.user_id.isin(registered)]
total_events_df = pd.concat([events,purchase],sort=False)
users_with_easy_level = total_events_df[total_events_df['selected_level'] == 'easy']
users_with_medium_level = total_events_df[total_events_df['selected_level'] == 'medium']
users_with_hard_level = total_events_df[total_events_df['selected_level'] == 'hard']
user_groups = [
    {'easy': users_with_easy_level},
    {'medium': users_with_medium_level},
    {'hard': users_with_hard_level}]
for group in user_groups:
    level = list(group.keys())[0]
    group_users = group[level]
    count_of_users_in_group = len(group_users)
    purchase_df_slice = purchase[purchase['user_id'].isin(group_users['user_id'])]
    percent_of_purchase = purchase_df_slice['user_id'].nunique()/count_of_users_in_group
    print ('Процент оплативших пользователей, выбравших уровень сложности {}: {:.2%}'.format(level,percent_of_purchase))
    print ()
    