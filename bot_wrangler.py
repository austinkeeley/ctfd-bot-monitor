"""bot_rangler"""

import redis
from datetime import datetime

class Bot(object):
    """A bot object as displayed in the bot monitor"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.checkin = None
        self.current_action = None

    def __repr__(self):
        return "ID: %s\tName: %s\tCheckin: %s\tCurrent Action\t%s" % (self.id, self.name, self.checkin, self.current_action)


class BotWrangler(object):
    def __init__(self, redis_url='localhost:6379', namespace='ctfd:bot:'):
        redis_host, redis_port = redis_url.split(':')
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        self.namespace = namespace

        self._all_bots = dict()
        bot_ids = self._get_bot_ids()

        for bot_id in bot_ids:
            bot_name = self.redis_client.hget(bot_id, 'name')
            bot_checkin = self.redis_client.hget(bot_id, 'checkin')
            bot_current_action = self.redis_client.hget(bot_id, 'current_action')
            b = Bot(bot_id, bot_name)
            b.checkin = datetime.strptime(bot_checkin, '%Y-%m-%dT%H:%M:%S')
            b.current_action = bot_current_action


            self._all_bots[bot_id] = b

    def _get_bot_ids(self):
        """Gets all the bot IDs"""
        bot_ids = self.redis_client.keys(self.namespace + '*')
        return bot_ids

    def get_bot(self, bot_id):
        """Gets a specific bot object"""
        return self._all_bots.get(bot_id)

    def get_all_bots(self):
        print(self._all_bots)
        return self._all_bots

    def __str__(self):
        return str(self._all_bots)

# Sanity check
if __name__ == '__main__':
    print('Bot wrangler')
    bot_wrangler = BotWrangler()
    print(bot_wrangler)
