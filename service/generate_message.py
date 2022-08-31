from utils.utility import generate_return_response


def generate_message(command):
    if command == "hi":
        return generate_return_response(True, "api", "basic", "Hello")
    elif command == "how are you":
        return generate_return_response(True, "api", "basic", "I'm fine, you?")
    elif command == "bye":
        return generate_return_response(True, "api", "basic", "Bye, Have a nice day")
    elif command == "good night":
        return generate_return_response(True, "api", "basic", "Good night, sweet dreams")
    else:
        return generate_return_response(True, "api", "basic", command.capitalize())