#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


def validate_username(username):
    if len(username) > 0:
        return username

def validate_password(password):
    if len(password):
        return password

def validate_verify_password(password):
    return password

def validate_email(email):
    return email


form = """
<form action="/welcome" method="post">
    <h1>Signup</h1>
    <label>Username:
        <input name="username"/><div><font color="red">%(error_username)s</font></div>
    </label>
    <br>
    <br>

    <label>Password:
        <input name="password"/><div><font color="red">%(error_password)s</font></div>
    </label>
    <br>
    <br>

    <label>Verify password:
        <input name="verify_password"/><div><font color="red">%(error_verify_password)s</font></div>
    </label>
    <br>
    <br>

    <label>Email (optional):
        <input name="email"/><div><font color="red">%(error_email)s</font></div>
    </label>
    <br>
    <br>

    <label>
        <input type="submit">
    </label>
</form>
"""



class MainHandler(webapp2.RequestHandler):

    def write_form(self, error_username="", error_password="", error_verify_password="", error_email=""):
        self.response.out.write(form % {"error_username": error_username,
                                        "error_password": error_password,
                                        "error_verify_password": error_verify_password,
                                        "error_email": error_email})

    def get(self):
        self.write_form()

class Welcome_User(webapp2.RequestHandler):
    def write_form(self, error_username="", error_password="", error_verify_password="", error_email=""):
        self.response.out.write(form % {"error_username": error_username,
                                        "error_password": error_password,
                                        "error_verify_password": error_verify_password,
                                        "error_email": error_email})

    def post(self):
        username = validate_username(self.request.get("username"))
        password = validate_password(self.request.get("password"))
        verify_password = validate_verify_password(self.request.get("verify_password"))
        email = validate_email(self.request.get("email"))

        if not username:
            self.write_form("That is not a valid username.")
        elif not password:
            self.write_form("", "That is not a valid password.")
        elif not verify_password:
            self.write_form("", "", "Passwords are not the same.")
        elif not email:
            self.write_form("", "", "", "That is not a valid email")
        else:
            self.response.out.write("Welcome, " + username + "!")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome_User)
], debug=True)
