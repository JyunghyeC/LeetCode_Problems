import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]

    df = df[['author_id']].rename(columns={'author_id': 'id'})
    
    result = df.sort_values(by=['id']).drop_duplicates()
    
    return result
    