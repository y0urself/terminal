# Copyright (C) 2019-2021 Greenbone Networks GmbH
# Copyright (C) 2021 y0urself
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


from contextlib import contextmanager
from enum import Enum
from shutil import get_terminal_size
from typing import Callable, Generator

import colorful as cf

from terminal.loader import Loader

TERMINAL_SIZE_FALLBACK = (80, 24)  # use a small standard size as fallback


GB_ASCII = [
"                         @@     @@@                  ",
"                         @{g}%{b}@   @{g}(#{b}%@                 ".format(g=cf.green, b=cf.reset),
"                         @{g}%##{b}@@@{g}(###{b}@@               ".format(g=cf.green, b=cf.reset),
"                         @{g}##{b}#@&&{g}(####{b}&@              ".format(g=cf.green, b=cf.reset),
"                         @#{g}((({b}@{g}((#####{b}@@@            ".format(g=cf.green, b=cf.reset),
"                      @{g}(((############{b}@@{g}#({b}@          ".format(g=cf.green, b=cf.reset),
"                   @{g}(#################{b}%@{g}##({b}@         ".format(g=cf.green, b=cf.reset),
"                @{g}((##{b}@@@{g}%##################({b}@        ".format(g=cf.green, b=cf.reset),
"              &{g}((###{b}@/    @{g}#########{b}&@@@@@&{g}#({b}@       ".format(g=cf.green, b=cf.reset),
"            #{g}((####{b}@      &{g}######{b}@@%{g}#####{b}%@#@@&@     ".format(g=cf.green, b=cf.reset),
"          ({g}((#####{b}@,   @@{g}######{b}%@{g}########{b}#@@@{g}#((({b}@@  ".format(g=cf.green, b=cf.reset),
"        &{g}((#####################{b}@@{g}###########{b}&@@@@@@@".format(g=cf.green, b=cf.reset),
"      @{g}(((########################{b}@{g}############{b}@@{g}##{b}(@".format(g=cf.green, b=cf.reset),
"     &{g}((#######################{b}@@@@%{g}###########{b}@#{g}##{b}&@".format(g=cf.green, b=cf.reset),
"   @{g}(/#&####################{b}@@   @@@@{g}#########{b}&@@@@  ".format(g=cf.green, b=cf.reset),
"  @{g}((#@@@@{g}################{b}@@    @@  @&{g}#######{b}@       ".format(g=cf.green, b=cf.reset),
" @{g}(###################{b}#@@&   %@    @&{g}######{b}@@        ".format(g=cf.green, b=cf.reset),
" @{g}##############{b}@@     .@@&    @%{g}######{b}&@            ".format(g=cf.green, b=cf.reset),
"   @%{g}##########{b}@&   @       &@{g}#######{b}@@@             ".format(g=cf.green, b=cf.reset),
"     @@%{g}#####{b}&@@%        @&{g}######{b}#@@                 ".format(g=cf.green, b=cf.reset),
"                  @#&@@#{g}######{b}@@@                    ".format(g=cf.green, b=cf.reset),
"                    #{g}###{b}#&@@                         ".format(g=cf.green, b=cf.reset),
]

class Signs(Enum):
    FAIL = '\N{HEAVY MULTIPLICATION X}'
    ERROR = '\N{MULTIPLICATION SIGN}'
    WARNING = '\N{WARNING SIGN}'
    OK = '\N{CHECK MARK}'
    INFO = '\N{INFORMATION SOURCE}'
    NONE = ' '

    def __str__(self):
        return f'{self.value}'


STATUS_LEN = 2


class Terminal:
    def __init__(self, welcome:bool = False) -> None:
        self._indent = 0
        if welcome:
            self._print_welcome()
        self.loader = None

    @staticmethod
    def get_width() -> int:
        """
        Get the width of the terminal window
        """
        width, _ = get_terminal_size(TERMINAL_SIZE_FALLBACK)
        return width

    def _print_welcome(self):
        whitespaces = int((self.get_width() - 54 - 2) / 2)
        print(f"+{(int(self.get_width() / 2) * 2 - 2) * '-'}+")
        for line in GB_ASCII:
            print(f"|{whitespaces * ' '}{line}{whitespaces * ' '}|")
        print(f"+{(int(self.get_width() / 2) * 2 - 2) * '-'}+")
        print(f"{(whitespaces + 18) * ' '}Greenbone Terminal{(whitespaces + 18) * ' '}")


    def _print_status(
        self,
        message: str,
        status: Signs,
        color: Callable,
        style: Callable,
        *,
        new_line: bool = True,
        overwrite: bool = False,
    ) -> None:
        first_line = ''
        if overwrite:
            first_line = '\r'
        output = ''
        width = self.get_width()
        if status == Signs.NONE:
            first_line += '  '
        else:
            first_line += f'{color(status)} '
        if self._indent > 0:
            first_line += ' ' * self._indent
        usable_width = width - STATUS_LEN - self._indent
        while usable_width < len(message):
            part_line = ' ' * (self._indent + STATUS_LEN)
            part = message[:usable_width]
            message = message[usable_width:]
            output += f'{part_line}{part}\n'
        output += f'{first_line}{message}'
        if new_line:
            print(style(output))
        else:
            print(style(output), end='', flush=True)

    @contextmanager
    def indent(self, indentation: int = 4) -> Generator:
        current_indent = self._indent
        self.add_indent(indentation)

        yield self

        self._indent = current_indent

    def add_indent(self, indentation: int = 4) -> None:
        self._indent += indentation

    def reset_indent(self) -> None:
        self._indent = 0

    def print(self, *messages: str, style: Callable = cf.reset) -> None:
        """ Print the prepared message """
        message = ''.join(messages)
        self._print_status(message, Signs.NONE, cf.white, style)

    def print_overwrite(
        self, *messages: str, style: Callable = cf.reset, new_line: bool = False
    ) -> None:
        message = ''.join(messages)
        self._print_status(
            message,
            Signs.NONE,
            cf.white,
            style,
            new_line=new_line,
            overwrite=True,
        )

    def ok(self, message: str, style: Callable = cf.reset, new_line: bool = True, overwrite: bool = False) -> None:
        self._print_status(message=message, status=Signs.OK, color=cf.green, style=style, new_line=new_line, overwrite=overwrite)

    def fail(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message=message, status=Signs.FAIL, color=cf.red, style=style)

    def error(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message=message, status=Signs.ERROR, color=cf.red, style=style)

    def warning(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message=message, status=Signs.WARNING, color=cf.yellow, style=style)

    def info(self, message: str, style: Callable = cf.reset) -> None:
        self._print_status(message=message, status=Signs.INFO, color=cf.cyan, style=style)

    def bold_info(self, message: str, style: Callable = cf.bold) -> None:
        self._print_status(message=message, status= Signs.INFO, color=cf.cyan, style=style)

    def load_status(
        self,
        current: int = None,
        total: int = None,
        msg: str = None,
        done: bool = False
    ) -> None:
        print_this = ''
        if not self.loader:
            if not total:
                self.fail("You need to specify a total number (int) for the Loader")
            if not msg:
                self.fail("You need to specify a file name / msg for the Loader")
            self.loader = Loader(
                width=self.get_width() - self._indent - 2,
                msg = msg,
                total = total,
            )
        if done:
            self.ok(self.loader.finish(), overwrite=True)
            self.loader = None
        if current:
            self.print_overwrite(self.loader.load(current=current))
