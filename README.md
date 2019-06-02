#django-admin-terminal

A terminal in the browser for lazy django devops!.

![django-admin-terminal](https://raw.githubusercontent.com/assem-ch/django-admin-terminal/master/django-admin-terminal/static/images/screenshot.png)


## Installation

**Step 1**
> pip install django-admin-terminal

**Step 2**

include __django_admin_terminal__ into INSTALLED_APPS ```settings.py```

```python
INSTALLED_APPS = (
    # add to the existing apps
    'django_admin_terminal'
)
```

**Step 3**

run
> python manage.py collectstatic

Done!

in your browser, goto http://127.0.0.1:8000/admin/terminal/ to access the web terminal.

**note:** make sure you got superuser privileges.


## Configuration

Include two more variables to ```settings.py```

```python
SECURE_TERMINAL = True  # False to allow http
TERMINAL_WHITELIST = [
                "127.0.0.1"
]  # List of IPs to be allowed - NB: All allowed by default
```


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

> all the **django superusers** can access this portal, so make sure only the right guys have got access before deploying django-admin-terminal to live.

> long running tasks and interactive commands won't probably work.


## License

BSD License - checkout LICENSE file for the complete license document


## Author
- ( Django Console ) : [Anoop Thomas Mathew](https://twitter.com/atmb4u "atmb4u") 
- [Assem_Chelli](https://github.com/assem-ch "assem-ch") 
