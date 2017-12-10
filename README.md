Twitter Mute Them All
=====================

A cli / command-line / terminal program to mute everyone you follow on Twitter.

Developed with Python. Supports Windows, OS X, and Linux.

Installation
------------

Pre-compiled binaries for Windows and OS X are available under [releases](https://github.com/katekligman/twitter-mute-them-all/releases/latest).

Before you run this application you'll need to set environment variables for CONSUMER_KEY,
CONSUMER_SECRET, ACCESS_TOKEN_KEY and ACCESS_TOKEN_SECRET.

A walkthrough on how to setup this environment follows.

Environment Setup
-----------------

In order to run this program, you'll need to get four account codes from twitter and set
them in your environment. To get these four codes, you'll need to create a
personal (private) twitter application. Note you won't be making a real app, it's
just something Twitter requires.

Here's how to do it:

1. From a desktop browser sign into twitter, then go to https://apps.twitter.com/ and
click on the 'Create a new app' button in the upper right corner of the screen.

2. Next, fill out the create an application form as follows:

* Enter any name. Note the name of the application must be unique across all of twitter.
If you get an error, try using:  <yourtwittername> - Mute them all

* Description can be anything.

* The website can be any site starting with https:// ex: https://www.google.com

* Leave the Callback URL field blank.

* Check the checkbox for the developer agreement and submit the form.

3. You should now be in a settings area for the application.  Under
Application Settings, click "manage keys and access tokens"

4. Next, click on "Keys and Access Tokens" in the tabs area directly under the top heading.

5. Note your Consumer Key and Consumer Secret codes from the top table. These are the first two.

6. Now scroll down to the very bottom of the page and click on the
'Create my access token' button.  Note your access token key and access token secret codes.

Next, set your environment with these values.

On OS X and Linux open a terminal and enter:
```shell
export CONSUMER_KEY=consumer_key_from_above
export CONSUMER_SECRET=consumer_secret_from_above
export ACCESS_TOKEN_KEY=access_key_from_above
export ACCESS_TOKEN_SECRET=access_secret_from_above
```

On Windows open a cmd prompt and enter:
```shell
set CONSUMER_KEY=consumer_key_from_above
set CONSUMER_SECRET=consumer_secret_from_above
set ACCESS_TOKEN_KEY=access_key_from_above
set ACCESS_TOKEN_SECRET=access_secret_from_above
```
Now you are ready to run the program.

You can download releases for [Windows and Mac here](https://github.com/katekligman/twitter-mute-them-all/releases/latest).

Running from Source (for developers)
------------------------------------
```python
pip -r requirements.txt
python main.py
```

Contributing
------------

Contributions are welcome! Please create or locate a related issue and reference it your pull request.

Contributors
------------

Created by Kate Kligman. Inspired by go-twitter-mute-them-all by ledyba.

License
-------

GPL v2.0
