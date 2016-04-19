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

"""Views related to accounts such as login, logout, sign-up, etc.

Created on 16 April 2016
@author Junya Kaneko <junya@mpsamurai.org>
"""
import json
import random
import string
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from django.shortcuts import render
from django.http.response import HttpResponseBadRequest, HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from mps import settings


__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


# Create your views here.
class LoginView(View):
    def get(self, request):
        state = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        request.session['state'] = state
        params = {'client_id': settings.GITHUB_CLIENT_ID, 'redirect_uri': settings.GITHUB_CALLBACK_URL,
                  'scope': 'user,user:email', 'state': state}
        url = 'https://github.com/login/oauth/authorize?' + urlencode(params)
        return render(request, 'accounts/login.html', {'github_oauth2_url': url})


class GitHubOauth2CallbackView(View):
    def get(self, request):
        try:
            code = request.GET['code']
            state = request.GET['state']
            if state != request.session['state']:
                raise HttpResponseBadRequest
        except KeyError:
            raise HttpResponseBadRequest
        req = Request('https://github.com/login/oauth/access_token')
        req.add_header('Accept', 'application/json')
        response = urlopen(req, urlencode({'client_id': settings.GITHUB_CLIENT_ID, 'client_secret': settings.GITHUB_CLIENT_SECRET,
                                           'code': code, 'redirect_uri': settings.GITHUB_CALLBACK_URL, 'state': state}).encode('ascii'))
        data = json.loads(response.read().decode('utf-8'))
        user = authenticate(access_token=data['access_token'])
        if user is not None:
            login(request, user)
            return HttpResponse('OK')
        else:
            return HttpResponse('NG')