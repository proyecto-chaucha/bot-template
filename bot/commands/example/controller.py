#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implements the main logic of the command and
coordinates with model, view, requester and validator
"""

from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler


from bot.helpers import Chat
from bot.stickers import Quirquincho
from bot.events import BotEvents

from bot.commands.example.view import View
from bot.commands.example import Command


class Controller(object):

    @staticmethod
    def run(bot: Bot, update: Update):
        """
        Runs the command
        :param bot: Bot Send by dispatcher
        :param update: Update Context Send by dispatcher
        :return:
        """
        events = BotEvents.instance()
        events.message_received(bot, update)

        if Chat.is_private(update):

            response = View.help_message(update)
            response.render()

            bot.send_sticker(update.message.chat.id, Quirquincho.ok)

            events.reply(bot, update, response.text())

    @classmethod
    def init(cls, dispatcher: Dispatcher):
        """
        Inits the command
        :param dispatcher:
        :return dispatcher:
        """
        dispatcher.add_handler(CommandHandler('help', cls.run))
        dispatcher.add_handler(CommandHandler('h', cls.run))
        dispatcher.add_handler(CommandHandler('?', cls.run))
        dispatcher.add_handler(CommandHandler('ayuda', cls.run))

        events = BotEvents.instance()
        events.command_loaded(Command)

        return dispatcher
