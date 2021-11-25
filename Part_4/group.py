import pandas as pd
df = pd.read_csv('events.csv')
df2 = pd.read_csv('purchase.csv')
cond = (df.start_time>='2018-01-01') & (df.start_time<'2019-01-01') & (df.event_type=='registration')
cond2 = (df2.event_datetime>='2018-01-01') & (df2.event_datetime<'2019-01-01')
registered = df[cond]['user_id'].to_list()
events = df[df.user_id.isin(registered)]
events.start_time = pd.to_datetime(events.start_time, format='%Y-%m-%dT%H:%M:%S')
df2['event_type'] = 'purchase'
purchase = df2[df2.user_id.isin(registered)]
purchase.event_datetime = pd.to_datetime(purchase.event_datetime, format='%Y-%m-%dT%H:%M:%S')
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
    level_choice_df = total_events_df[(total_events_df['event_type'] == 'level_choice') & (total_events_df['user_id'].isin(group_users['user_id']))]
    if (level_choice_df['user_id'].value_counts().mean()) == [1]:
        level_choice_df = level_choice_df[['user_id','start_time']].rename(columns={'start_time':'level_choice_time'})
        #Исправила
        purchase_df_slice_2 = purchase_df_slice[['user_id','event_datetime']].rename(columns={'event_datetime':'purchase_time'})
        merged_df = purchase_df_slice_2.merge(level_choice_df,on='user_id',how='inner')
        merged_df['timedelta'] = merged_df['purchase_time'] - merged_df['level_choice_time']
        mean_time = merged_df['timedelta'].mean()
        print ('Среднее время между выбором уровня сложности и оплатой для пользователей, выбравших уровень сложности {}: {}'.format(level,mean_time))
        print ('Характеристики времени:')
        print (merged_df['timedelta'].describe())
    else:
        print ('Более 1 события выбора уровня сложности')