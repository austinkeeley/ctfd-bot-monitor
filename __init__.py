import os
import redis
from flask import render_template_string

REDIS_BOT_NAMESPACE = 'ctfd:bot'

def load(app):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, 'bots.html')

    @app.route('/admin/bots/', methods=['GET'])
    def bot_monitor():
        with open(template_path) as template_file:
            template = template_file.read()
        return render_template_string(template)

