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

"""Admin module for accounts application.

created on 19 April 2016
@author Junya Kaneko <junya@mpsamurai.org>
"""

from django.contrib import admin
from accounts import models


__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


# Register your models here.
class GitHubAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'repos_url', 'updated_at')
    list_display_links = ('repos_url', )
    readonly_fields = ('registered_at', 'updated_at',)

admin.site.register(models.GitHubAccount, GitHubAccountAdmin)