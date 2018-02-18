ctfd-bot-monitor
=================

A dashboard for monitoring bots used alongside CTFd.

To register a bot with this plugin, have it create a hash in the `ctfd:bot:` namespace.

The following fields are used in the hash:

  * `name` - A friendly name for your bot
  * `checkin` - A date field in the form of YYYY-mm-ddThh:mm:ss for when the bot last interacted with the Redis cache 
  * `current_action` - Tells the user what the bot's up to

