import json
from datetime import datetime, date, timedelta
from googlesearch import search
import wikipedia


def current_date():
    return date.today().strftime("%B %d %Y")


def yesterday_date():
    yesterday = date.today() - timedelta(days=1)
    return yesterday.strftime("%B %d %Y")


def current_time():
    now = datetime.now()
    return now.time().strftime('%H %M %S %p')


def local_timezone():
    now = datetime.now()
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    return local_tzname


def youtube_url(query):
    return "https://www.youtube.com/results?search_query=" + query.strip()


def generate_return_response(status=False, source="api", destination=None, data=""):
    return {"status": status, "source": source, "destination": destination, "data": data}


def get_data_from_wikipedia(query):
    try:
        response = generate_return_response(True, "api", "wiki", wikipedia.summary(query, sentences=1))
        response['is_correct'] = True
        return response
    except Exception as e:
        data_list = wikipedia.search(query)
        for data in data_list:
            if data.strip().lower() == query:
                data_list.remove(data)

        response = generate_return_response(True, "api", "wiki", data_list)
        response['is_correct'] = False
        return response


def get_data_from_google_search(query):
    return_list = []
    try:
        result_list = search(query, num_results=10)
        for result in result_list:
            return_list.append(result)
        response = generate_return_response(True, "api", "google", return_list)
        response['is_correct'] = True
        return response
    except:
        response = generate_return_response(True, "api", "google", [])
        response['is_correct'] = False
        return response

