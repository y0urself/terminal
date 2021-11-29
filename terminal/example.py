# -*- coding: utf-8 -*-
# Copyright (C) 2020 - 2021 Greenbone Networks GmbH
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
#

import terminal
import requests

def main(args=None):
    terminal.init_terminal(welcome=True)
    terminal.ok('Nice!')

    url = "https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip"

    file_name = url.split('/')[-1]
    u = requests.get(url, stream=True, timeout=10000)
    f = open(file_name, 'wb')

    file_size_dl = 0
    chunk_size = 8192

    file_size = u.headers.get('content-length')
    terminal.load_status(msg=file_name, total=int(file_size))
    for content in u.iter_content(chunk_size=chunk_size):

        file_size_dl += len(content)
        f.write(content)

        terminal.load_status(current=file_size_dl)
    terminal.load_status(done=True)

    f.close()

if __name__ == '__main__':
    main()
