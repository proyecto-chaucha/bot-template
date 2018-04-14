#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implements messages returned as the result
of the command
"""
from telegram import Update
from bot.commands.base import BaseView
from bot.bot import commands


class View(BaseView):

    @classmethod
    def help_message(cls, context: Update):

        command_list = ''

        for key in sorted(commands.keys()):
            command = commands[key]
            command_list += '- {handler} : {about}\n'.format(handler=command.handler, about=command.about)

        content = '''
Hola soy *Quirquincho* <')))~ :thumbs_up:

Soy el protector de las chauchas.

Ésta es mi lista de comandos:

''' + command_list

        return cls(content, context)
