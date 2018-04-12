#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib

from bot import config
from bot import logger
from bot.events import BotEvents, SystemEvents

from unipath import Path
from telegram import Bot, Update
from telegram.ext import Updater

commands = {}
disabled = []


class EventHandler(object):

    @staticmethod
    def on_command_loaded(name: str):
        logger.log.debug('Loaded Command: %s' % name)

    @staticmethod
    def on_message_received(bot: Bot, update:Update):
        logger.log.debug('Message Received: %s' % update.message.text)

    @staticmethod
    def on_reply(bot: Bot, update:Update, message):
        logger.log.debug('Bot sent reply %s' % message)

    @staticmethod
    def on_error(bot:Bot, update:Update, err):
        logger.log.warning('Update: "%s" - Error: "%s"' % (update, err))


def init():

    # Telegram Bot
    updater = Updater(config.telegram_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register Commands
    global commands
    global disabled
    directories = []

    # Traverse commands directory
    # and append any command to the list like this
    # commands = ['help']

    files = Path('{0}/commands'.format(
        Path(__file__).absolute().ancestor(1)
    )).walk()

    for item in files:

        # Get the file name and directory
        name = Path(item).components()[-1].lower().strip()[:-3]
        folder = Path(item).components()[-2].lower().strip()

        if name == 'controller':
            if folder not in disabled:
                directories.append(folder)

    bot_events = BotEvents.instance()
    bot_events.on_command_loaded += EventHandler.on_command_loaded
    bot_events.on_message_received += EventHandler.on_message_received
    bot_events.on_reply += EventHandler.on_reply

    # Log all errors
    dispatcher.add_error_handler(EventHandler.on_error)

    for folder in directories:

        # Import the module
        module = importlib.import_module('bot.commands.%s.controller' % folder)

        # Get class and call init method
        cls = getattr(module, 'Controller')
        cls().init(dispatcher)

        command = importlib.import_module('bot.commands.%s' % folder)
        command_instance = getattr(command, 'Command')
        commands[folder] = command_instance

    events = SystemEvents.instance()
    events.ready()

    # Main loop
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

