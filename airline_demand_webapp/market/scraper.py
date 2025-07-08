import pandas as pd
from datetime import datetime, timedelta
import random

def fetch_airline_data():
    cities = ['SYD', 'MEL', 'BNE', 'ADL', 'PER']
    flights = []
    for _ in range(50):
        src, dst = random.sample(cities, 2)
        price = random.randint(100, 300)
        date = datetime.today() - timedelta(days=random.randint(0, 7))
        flights.append({'from': src, 'to': dst, 'price': price, 'date': date.date()})

    df = pd.DataFrame(flights)
    popular = df.groupby(['from', 'to']).size().reset_index(name='count')
    trend = df.groupby('date')['price'].mean().reset_index()
    return df, popular, trend