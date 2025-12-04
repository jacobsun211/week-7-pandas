import json
import pandas as pd




def create_csv():
    with open('orders_simple.json') as f:
        json_data = json.load(f)
    df = pd.read_json('orders_simple.json')
    df.to_csv('csv_handeling/data.csv', index=False)
    df = pd.DataFrame(df)
    return df





