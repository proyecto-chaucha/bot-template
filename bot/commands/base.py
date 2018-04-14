#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Base classes for Commands and Views
"""

from telegram import Bot, Update, ParseMode
from telegram.ext import Dispatcher

from emoji import emojize
from unipath import Path


class BaseCommand(object):

    # Required
    name = None
    about = None

    # Canonical Handler used by Telegram
    # Example /help
    handler = None

    # Optional
    author = ''
    version = ''
    description = ''
    url = ''
    info = ''

    def __init__(self, name: str, about: str, handler: str):
        self.name = name
        self.about = about
        self.handler = handler

    @staticmethod
    def path():

        return Path(__file__)

    def get_name(self):

        if not self.name or self.name.strip() == '':
            raise ValueError('name must be set')

        return self.name.strip()

    def get_handler(self):

        if not self.handler or self.handler.strip() == '':
            raise ValueError('handler must be set')

        return self.handler.strip()

    def get_about(self):

        if not self.about or self.about.strip() == '':
            raise ValueError('about must be set')

        return self.about.strip()


class BaseController(object):

    @classmethod
    def run(cls, bot: Bot, update: Update):
        """
        Runs the command
        :param bot: Bot Send by dispatcher
        :param update: Update Context Send by dispatcher
        :return:
        """
        raise NotImplementedError('run method must be implemented')

    @classmethod
    def init(cls, dispatcher: Dispatcher):
        """
        Inits the command
        :param dispatcher:
        :return dispatcher:
        """
        raise NotImplementedError('init method must be implemented')


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

    def content(self, raw: bool = False):

        if self.emojize and not raw:
            return emojize(self._content)

        return self._content

    def render(self, raw: bool = False):

        self.context.message.reply_text(self.content(raw), parse_mode=self.mode)
