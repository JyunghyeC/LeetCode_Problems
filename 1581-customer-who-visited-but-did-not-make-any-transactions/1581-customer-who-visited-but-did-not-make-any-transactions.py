import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    df = visits.merge(transactions, on='visit_id', how='left')
    df = df[df['transaction_id'].isna()]
    df = df.groupby(['customer_id']).agg(count_no_trans=('visit_id', 'count')).reset_index()
    return df[['customer_id', 'count_no_trans']]
