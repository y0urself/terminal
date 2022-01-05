# Copyright (C) 2019-2021 Greenbone Networks GmbH
# Copyright (C) 2021-2022 y0urself (jaspar.loechte@greenbone.net)
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

import math

class Loader:
    def __init__(self, width: int, msg: str, total: int) -> None:
        self.width = width
        self.msg = msg
        self.total = total

    def finish(self) -> None:
        fix = "[] 100% []"
        bar_len = self.width - len(self.msg) - len(fix)
        return f"[{self.msg}] Done [{'#' * bar_len}]"

    def load(self, current: int):
        percent = int(current / self.total * 100)
        return self.__template(percent)

    def __template(self, percent) -> None:
        """ [file.name.ext] x20% [###########                                ] """
        fix = "[] 100% []"
        bar_len = self.width - len(self.msg) - len(fix)
        hash_len =  int(math.floor(bar_len * (percent / 100)))
        space_len = bar_len - hash_len
        return f"[{self.msg}] {percent:03}% [{'#' * hash_len}{' ' * space_len}]"
