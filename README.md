#django-terminal

bash console in the browser for django devops!

##IMPORTANT

Service needs to be running on ```https``` to securely POST commands to the server. 

![django-terminal](https://raw.githubusercontent.com/assem-ch/django-terminal/master/django-terminal/static/images/screenshot.png)

Did a quick update on the code; need to pull the code and restart the server, and waiting for server admin to do that? 
django-terminal is for you!

## Installation

**Step 1**
> pip install django-terminal

**Step 2**

include __django_terminal__ into INSTALLED_APPS ```settings.py```

```python
INSTALLED_APPS = (
    # add to the existing apps
    'django_terminal'
)
```

**Step 3**

include two more variables to ```settings.py```

> Even without these settings, it will work.

> allows requests from all ips, and works even when not in https **(NOT GOOD).**

```python
SECURE_TERMINAL = True  # False to allow http
TERMINAL_WHITELIST = [
                "127.0.0.1"
]  # List of IPs to be allowed - NB: All allowed by default
```
**Step 4**

run
> python manage.py collectstatic

Done!

in your browser, goto http://127.0.0.1:8000/admin/terminal/ to access the web terminal.

NB: make sure you got superuser privileges.


##Tip
To run sudo tasks, you can use

```bash
echo mypassword | sudo -S command
```

Example commands 
```bash
$ echo pa$$w0rD | sudo -S service nginx restart

$ git pull origin master

$ ls -al
```

##Caveats

> all the **django superusers** can access this portal, so make sure only the right guys have got access before deploying django-terminal to live.

> long running tasks and interactive commands won't probably work.


## License

BSD License - checkout LICENSE file for the complete license document


## Author
[Anoop Thomas Mathew](https://twitter.com/atmb4u "atmb4u")
