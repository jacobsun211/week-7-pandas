import pandas as pd

import utils

file = pd.read_csv('csv_handeling/data.csv')
df = pd.DataFrame(file)



# ---------------- < STAGE 1 > ----------------

df = utils.convert_dtypes(df)



# ---------------- < STAGE 2 > ----------------

#                                                                                                      !                
df['items_html'] = df['items_html'].str.replace('<b>', '').str.replace('<br>', '').str.replace('</b>',' ')



# ---------------- < STAGE 3 > ----------------


df['coupon_used'].fillna('no coupon', inplace = True)
# it writes a warning but still works for some reason


# ---------------- < STAGE 4 > ----------------


df['order_month'] = pd.to_datetime(df['order_date']).dt.month


# ---------------- < STAGE 5 > ----------------

average = df['total_amount'].mean()
df['high_value_order'] = df['total_amount'] > average
sorted = df.sort_values('total_amount',ascending=False)


# ---------------- < STAGE 6 > ----------------

df['avg_rating'] = df.groupby('country')['rating'].transform('mean')


# ---------------- < STAGE 7 > ----------------


df = df[df['total_amount'] > 1000]
df = df[df['rating'] > 4.5]


# ---------------- < STAGE 8 > ----------------

df['delivery_status'] = df['shipping_days'] > 7
df['delivery_status'] = df['delivery_status'].astype(str)
df['delivery_status'] = df['delivery_status'].str.replace('True', 'delayed').str.replace('False', 'on time')






utils.saving_to_csv(df)


