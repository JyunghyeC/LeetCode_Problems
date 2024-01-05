import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    join_table = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    
    no_order_mask = join_table['customerId'].isna()
    
    result_df = join_table[no_order_mask]
    
    result = result_df[['name']].rename(columns={'name':'Customers'})
    
    return result
    
