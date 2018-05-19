#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implements Info About the Command
"""

from bot.commands.base import BaseCommand


class Command(BaseCommand):

    # Required Properties
    name = 'help'

    # Short Description
    about = 'Entrega Información de Ayuda'

    # Command as used in Telegram
    # Include params if necessary
    handler = '/help'

    # Optional
    version = '1.0.0'

    author = 'Camilo Castro'
