import pandas as pd

def convert_dtypes(df):
    df['total_amount']  = df['total_amount'].str.replace('$', '').astype(float)
    df['shipping_days'] = df['shipping_days'].astype(int)
    df['customer_age'] = df['customer_age'].astype(int)
    df[['order_date']] = df[['order_date']].apply(pd.to_datetime)
    return df


def saving_to_csv(df):
    df.to_csv('csv_handeling/clean_orders_[ID_NUMBER].csv', index=False)

# df.to_csv(file_name, sep='\t', encoding='utf-8', index=False, header=True)
