#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implements Info About the Command
"""

from bot.commands.base import BaseCommand


class Command(BaseCommand):

    name = 'help'

    version = '1.0.0'

    author = 'Camilo Castro'

    # Short Description
    about = 'Entrega Información de Ayuda'

    # Long
    description = 'Help Command'
