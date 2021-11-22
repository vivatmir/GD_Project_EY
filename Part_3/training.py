import pandas as pd
df = pd.read_csv('gamedev38/events.csv')
df2 = pd.read_csv('gamedev38/purchase.csv')
total_events_df = pd.concat([df,df2],sort=False)
print(total_events_df['selected_level'].unique())
