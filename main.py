
import webapp2
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def validate_username(username):
    return USER_RE.match(username)

def validate_password(password):
    return PASS_RE.match(password)

def validate_verify_password(password1, password2):
        if password1 == password2:
            return password2

def validate_email(email):
    return EMAIL_RE.match(email)


form = """
<form action="/welcome" method="post">
    <h1>Signup</h1>
    <label>Username:
        <input name="username" value="%(username)s"/><font color="red">%(error_username)s</font>
    </label>
    <br>
    <br>

    <label>Password:
        <input type="password" name="password"/><font color="red">%(error_password)s</font>
    </label>
    <br>
    <br>

    <label>Verify password:
        <input type="password" name="verify_password"/><font color="red">%(error_verify_password)s</font>
    </label>
    <br>
    <br>

    <label>Email (optional):
        <input name="email"/ value="%(email)s"><font color="red">%(error_email)s</font>
    </label>
    <br>
    <br>

    <label>
        <input type="submit">
    </label>
</form>
"""



class MainHandler(webapp2.RequestHandler):

    def write_form(self, username="", email="", error_username="", error_password="", error_verify_password="", error_email=""):
        self.response.out.write(form % {"username": username,
                                        "email": email,
                                        "error_username": error_username,
                                        "error_password": error_password,
                                        "error_verify_password": error_verify_password,
                                        "error_email": error_email})

    def get(self):
        self.write_form()

class Welcome_User(webapp2.RequestHandler):

    def write_form(self, username="", email="", error_username="", error_password="", error_verify_password="", error_email=""):
        self.response.out.write(form % {"username": username,
                                        "email": email,
                                        "error_username": error_username,
                                        "error_password": error_password,
                                        "error_verify_password": error_verify_password,
                                        "error_email": error_email})

    def post(self):

        user_username = self.request.get("username")
        user_email = self.request.get("email")

        username = validate_username(self.request.get("username"))
        password = validate_password(self.request.get("password"))
        verify_password = validate_verify_password(self.request.get("password"), self.request.get("verify_password"))
        email = validate_email(self.request.get("email"))

        if not (username and password):
            if username:
                self.write_form(user_username, user_email, "", "That is not a valid password.")
            elif password:
                self.write_form(user_username, user_email, "That is not a valid username.")
            else:
                self.write_form(user_username, user_email, "That is not a valid username.", "That is not a valid password.")
        elif not username:
            self.write_form(user_username, user_email, "That is not a valid username.")
        elif not password:
            self.write_form(user_username, user_email, "", "That is not a valid password.")
        elif not verify_password:
            self.write_form(user_username, user_email, "", "", "Passwords are not the same.")
        elif not email:
            self.write_form(user_username, user_email, "", "", "", "That is not a valid email")
        else:
            self.response.out.write("Welcome, " + user_username + "!")




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome_User)
], debug=True)
