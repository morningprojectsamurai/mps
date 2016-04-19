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

"""Models related to user accounts such as profile, oauth2 access_token, etc.

Created on 16 April 2016
@author Junya Kaneko <junya@mpsamurai.org>
"""

from hashlib import md5
import random
import string
from django.db import models
from django.contrib.auth.models import User
from core.mixins.models import DateTimeMixin
from accounts.exceptions import InvalidUsernameError


__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


# Create your models here.
def generate_user_name(email):
    return md5((email + ''.join(random.sample([string.ascii_letters + string.digits] * 256, 256))).encode()).hexdigest()


def get_or_create_user(email, save=True, **kwargs):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        for i in range(0, 10):
            username = generate_user_name(email)
            if not User.objects.filter(username=username).exists():
                break
            username = None
        if username is None:
            raise InvalidUsernameError
        user = User.objects.create_user(username=username, email=email, **kwargs)
        user.set_password(''.join(random.sample(string.ascii_letters + string.digits, 32)))
        if save:
            user.save()
        return user


class GitHubAccount(DateTimeMixin):
    user = models.ForeignKey(User)
    github_id = models.IntegerField(unique=True)
    access_token = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    repos_url = models.URLField()

    def __str__(self):
        return self.user.email
