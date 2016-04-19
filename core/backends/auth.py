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

"""Django backends module related to authentication.

This module contains backends related to authentication.

created on 16 April 2016
@author Junya Kaneko <junya@mpsamurai.org>
"""

from django.contrib.auth.models import User
from accounts.models import GitHubAccount, get_or_create_user
from github import Github
from github.GithubException import BadCredentialsException


__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


class EmailAuthenticationBackend:
    """Authentication by using email and password.

    Created on 16 April 2016
    @author Junya Kaneko <junya@mpsamurai.org>
    """
    def authenticate(self, email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


class GitHubOauth2AuthenticationBackend:
    """Authentication by using GitHub OAuth2.

    Created on 16 April 2016
    @author Junya Kaneko <junya@mpsamurai.org>
    """
    def authenticate(self, access_token):
        github = Github(access_token)
        github_user = github.get_user()
        try:
            return GitHubAccount.objects.get(github_id=github_user.id).user
        except GitHubAccount.DoesNotExist:
            user = get_or_create_user(email=github_user.get_emails()[0]['email'])
            GitHubAccount.objects.create(user=user, github_id=github_user.id, access_token=access_token, name=github_user.name, repos_url=github_user.repos_url)
            return user
        except BadCredentialsException:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None