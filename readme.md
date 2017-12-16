# Flask ReCaptcha - Contact Form


Quickstart

 * Download / Clone Repository
 * Navigate to `Flask-ReCaptcha-Contact-Form`
 * Install Requirements : `pip -r requirements.txt`
 * Run Application : `python contact_form.py`
 * Access it : [https//localhost:5000](https//localhost:5000)


## [How it works](https://techmonger.github.io/5/python-flask-recaptcha/)


### Register for Google ReCaptcha
[https://www.google.com/recaptcha/admin](https://www.google.com/recaptcha/admin)


### Configure Site Key in `contact_form.py`

```python
 def contact():
    
    # Configure site-key here
    sitekey = "your-site-key-here"
```

### Configure Secret Key in `contact_form.py`

```python
def is_human(captcha_response):

    # Configure secret-key here
    secret = "your-secret-key-here"
```

[https://techmonger.github.io/5/python-flask-recaptcha/](https://techmonger.github.io/5/python-flask-recaptcha/)

