# Copyright (C) 2016 Morning Project Samurai
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Exceptions related to operations on accounts.

Created on 16 April 2016
@author Junya Kaneko <junya@mpsamurai.org>
"""

__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


class EmailDuplicationError(Exception):
    pass


class InvalidUsernameError(Exception):
    pass