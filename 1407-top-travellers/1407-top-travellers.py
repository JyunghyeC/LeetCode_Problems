import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = rides.groupby('user_id')['distance'].sum().reset_index(name='travelled_distance')
    base = users.merge(df, left_on='id', right_on='user_id', how='left')
    base['travelled_distance'] = base['travelled_distance'].fillna(0)
    result = base[['name', 'travelled_distance']].sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    return result