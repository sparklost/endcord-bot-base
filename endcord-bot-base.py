import logging
import os
import threading
import time

from endcord import utils

EXT_NAME = "Bot Base"
EXT_VERSION = "0.1.0"
EXT_ENDCORD_VERSION = "1.4.1"
EXT_DESCRIPTION = "Minimal discord bot with iteractions"
EXT_SOURCE = "https://github.com/sparklost/endcord-bot-base"
EXT_COMMAND_ASSIST = (
    ("bot_register_commands - register all bot commands from commands.json", "bot_register_commands"),
)
logger = logging.getLogger(__name__)


class Extension:
    """Main extension class"""

    def __init__(self, app):
        self.app = app

        self.run = True
        if not self.app.token.startswith("Bot"):
            logger.info("Not running on user accounts!")
            self.run = False
            del type(self).on_execute_command
            return

        extension_dir = os.path.dirname(os.path.abspath(__file__))
        self.commands = utils.load_json("commands.json", dir_path=extension_dir)

        threading.Thread(target=self.bot, daemon=True).start()


    def on_execute_command(self, command_text, chat_sel, tree_sel):   # noqa
        """Handle commands"""
        if command_text.startswith("bot_register_commands"):
            if not self.commands:
                return False
            for command in self.commands:
                self.app.discord.bot_register_command(command)
            return True
        return False


    def bot(self):
        """Main bot loop"""
        while self.run:
            interaction = self.app.gateway.bot_get_interactions()
            if interaction:
                interaction_id = interaction["id"]
                interaction_token = interaction["token"]
                if interaction["type"] == 1:   # PING
                    self.app.discord.bot_respond_interaction(1, None, interaction_id, interaction_token)   # PONG
                elif interaction["type"] == 2:   # APPLICATION_COMMAND
                    if interaction["data"]["name"] == "ping":
                        data = {"content": "Pong!"}
                        self.app.discord.bot_respond_interaction(4, data, interaction_id, interaction_token)   # CHANNEL_MESSAGE_WITH_SOURCE
                    # elif ...
                continue
            time.sleep(0.1)
