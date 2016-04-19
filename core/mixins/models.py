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

"""Models and Mixins that are basic for mps.

This module contains backends related to authentication.

created on 17 April 2016
@author Junya Kaneko <junya@mpsamurai.org>
"""


from django.db import models

__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


class DateTimeMixin(models.Model):
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
