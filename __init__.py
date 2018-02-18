import os
import redis
from flask import render_template_string
from flask_humanize import Humanize

from .bot_wrangler import BotWrangler

REDIS_BOT_NAMESPACE = 'ctfd:bot'

def load(app):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(dir_path, 'bots.html')

    Humanize(app)



    @app.route('/admin/bots/', methods=['GET'])
    def bot_monitor():
        with open(template_path) as template_file:
            template = template_file.read()

        bot_wrangler = BotWrangler()
        bots = bot_wrangler.get_all_bots()
        print(bots)

        return render_template_string(template, bots=bots)

