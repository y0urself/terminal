# -*- coding: utf-8 -*-
# Copyright (C) 2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .terminal import Terminal
from .example import main

__terminal = None

__all__ = [
    'main',
    'init_terminal',
    'error',
    'fail',
    'info',
    'bold_info',
    'ok',
    'out',
    'warning',
    'load_status',
]

def init_terminal(welcome: bool = False) -> None:
    global __terminal  # pylint: disable=global-statement, invalid-name
    if not __terminal:
        __terminal = Terminal(welcome=welcome)

def get_terminal() -> Terminal:
    if not __terminal:
        init_terminal()
    return __terminal

def ok(message: str) -> None:
    __terminal.ok(message)


def fail(message: str) -> None:
    __terminal.fail(message)


def error(message: str) -> None:
    __terminal.error(message)


def warning(message: str) -> None:
    __terminal.warning(message)


def info(message: str) -> None:
    __terminal.info(message)


def bold_info(message: str) -> None:
    __terminal.bold_info(message)


def out(message: str):
    __terminal.print(message)


def overwrite(message: str, new_line: bool = False):
    __terminal.print_overwrite(message, new_line=new_line)

def load_status(msg=None, current=None, total=None, done=False):
    __terminal.load_status(msg=msg, current=current, total=total, done=done)