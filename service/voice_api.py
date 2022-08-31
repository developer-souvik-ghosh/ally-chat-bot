from service.generate_message import generate_message
from utils import utility
from utils.utility import *


def recognized_entities(command):
    if command in ['hi', "hello", "bye", "good night", "good morning", "how are you"]:
        return generate_message(command)

    for entity in ['wiki', 'wikipedia']:
        if entity in command:
            query = command.replace(entity, "").strip()
            if query == "":
                return generate_return_response(False, "api", None, "")
            else:
                return get_data_from_wikipedia(query)

    for entity in ['search', 'google search', 'google', 'give me']:
        if entity in command:
            query = command.replace(entity, "").strip()
            if query == "":
                return generate_return_response(False, "api", None, "")
            else:
                return get_data_from_google_search(query)

    for entity in ['yt', 'play', 'play song', 'youtube']:
        if entity in command:
            query = command.replace(entity, "").strip()
            if query == "":
                command = "https://www.youtube.com"
            else:
                command = youtube_url(query)
            return utility.generate_return_response(True, "api", "yt", command)

    for entity in ["today date", "current date"]:
        if entity in command:
            today_date = utility.current_date()
            return utility.generate_return_response(True, "api", "basic", today_date)

    for entity in ["yesterday date"]:
        if entity in command:
            yesterday_date = utility.yesterday_date()
            return utility.generate_return_response(True, "api", "basic", yesterday_date)

    for entity in ["current time"]:
        if entity in command:
            current_time = utility.current_time()
            return utility.generate_return_response(True, "api", "basic", current_time)

    for entity in ["current timezone", "my timezone", "my local timezone", "timezone"]:
        if entity in command:
            return utility.generate_return_response(True, "api", "basic", utility.local_timezone())

    return utility.generate_return_response()
