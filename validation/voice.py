def affix(request_obj):
    if "command" not in request_obj:
        return {"status": False, "message": "Command not found", "error_type": "Key not found"}

    command = request_obj['command'].strip()

    if command == '':
        return {"status": False, "message": "Command be blank", "error_type": "Invalid data found"}

    return {"status": True, "data": {"command": command.lower()}}
