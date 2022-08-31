from flask import Blueprint, request

from service.voice import take_command, run_alexa
from service.voice_api import recognized_entities
from validation.voice import affix

voice_controller = Blueprint('voice', __name__)


@voice_controller.route('/command', methods=['POST'])
def api_voice_command():
    voice_command = take_command()

    if voice_command is None:
        return {"status": False, "message": "Please retry again", "command": None}
    else:
        run_alexa(voice_command)
        return {"status": True, "message": "Detect your command", "command": voice_command}


@voice_controller.route('/query', methods=['POST'])
def api_voice_query():
    validation = affix(request.form)
    if not validation['status']:
        return {"status": False, "message": "Please try again", "command": None}
    else:
        command = recognized_entities(validation['data']['command'])
        command['message'] = "Detect your command" if command['status'] else "Please try again"
        return command
