from django.shortcuts import render
from .scraper import fetch_airline_data
import json

def index(request):
    df, popular, trend = fetch_airline_data()

    chart_data = {
        'labels': trend['date'].astype(str).tolist(),
        'prices': trend['price'].tolist()
    }

    return render(request, 'market/index.html', {
        'flights': df.to_html(classes='table table-bordered'),
        'popular_routes': popular.to_html(classes='table table-bordered'),
        'chart_data': json.dumps(chart_data),
    })