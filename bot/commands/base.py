#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Base classes for Commands and Views
"""

from telegram import Bot, Update, ParseMode
from emoji import emojize
from unipath import Path


class BaseCommand(object):

    name = ''
    author = ''
    version = ''
    about = ''
    description = ''
    url = ''

    @staticmethod
    def path():

        return Path(__file__)


class BaseController(object):
    pass


class BaseView(object):

    _content = None
    context = None
    emojize = True
    mode = ParseMode.MARKDOWN

    def __init__(self, content: str, context: Update, mode: ParseMode = ParseMode.MARKDOWN, should_emojize: bool = True):

        self._content = content
        self.mode = mode
        self.emojize = should_emojize
        self.context = context

    def text(self, raw: bool = False):

        if self.emojize and not raw:
            return emojize(self._content)

        return self._content

    def render(self):

        self.context.message.reply_text(self.text(), parse_mode=self.mode)
