""" 
Contact form : Implementing ReCaptcha with Flask.

Read how it works at : http://techmonger.github.io/5/python-flask-recaptcha/
"""

from flask import Flask, request, redirect, render_template, url_for, flash, get_flashed_messages
import requests, json


app = Flask(__name__)

# Secret for message flashing

app.secret_key = 'change-this'


@app.route("/", methods=["GET", "POST"])
def home():
    """ Redirecting from home to contact form """
    return redirect(url_for("contact"))


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    """ Renders contact form on get and processes it on post. """
    
    sitekey = "your-site-key-here"

    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']
        captcha_response = request.form['g-recaptcha-response']
        
        if is_human(captcha_response):
            # Process request here
            status = "Detail submitted successfully."
        else:
             # Log invalid attempts
            status = "Sorry ! Bots are not allowed."

        flash(status)
        return redirect(url_for('contact'))

    return render_template("contact.html", sitekey=sitekey)
                

                
def is_human(captcha_response):
    """ Validating recaptcha response from google server.
        Returns True captcha test passed for the submitted form 
        else returns False.
    """
    secret = "your-secret-key-here"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


if __name__ == '__main__':
    app.run()
