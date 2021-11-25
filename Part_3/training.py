import pandas as pd
df = pd.read_csv('7_4_Events.csv')
df2 = pd.read_csv('purchase.csv')
total_events_df = pd.concat([df,df2],sort=False)
print(total_events_df['selected_level'].unique())
