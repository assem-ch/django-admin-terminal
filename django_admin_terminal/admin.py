from django.contrib import admin
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
import subprocess

from django.urls import path


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def terminal(request):
    """
    Serves the console at /admin/console
    TERMINAL_SECURE
        values: True/False
        Defined in settings to denote whether to allow access from http or https
        default: False - ALLOW access to ALL.
    TERMINAL_WHITELIST
        values: list of ip strings
        defines list of ips to be allowed
        default: ALLOW ALL ips unless defined.

    """
    try:
        v1 = request.is_secure() == settings.TERMINAL_SECURE
    except AttributeError:
        v1 = True
    try:
        v2 = get_client_ip(request) in settings.TERMINAL_WHITELIST
    except AttributeError:
        v2 = True
    except:
        print("TERMINAL_WHITELIST needs to be a list of ip addresses to be allowed access")
        v2 = True
    try:
        v3 = not (not settings.DEBUG and settings.TERMINAL_DEBUG_ONLY)
    except AttributeError:
        v3 = False

    settings_variables = v1 and v2 and v3
    if request.user.is_superuser and settings_variables:
        context = {
            'STATIC_URL': settings.STATIC_URL
        }
        context.update(csrf(request))
        return render_to_response("django_admin_terminal/admin/index.html", context)
    else:
        return HttpResponse("Unauthorized.", status=403)


def terminal_post(request):
    """
    Accepts POST requests from the web console, processes it and returns the result.
    """
    if request.user.is_superuser and request.POST:
        command = request.POST.get("command")
        if command:
            try:
                data = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                data = e.output
            data = data.decode('utf-8')
            output = "%c(@olive)%" + data + "%c()"
        else:
            output = "%c(@orange)%Try `ls` to start with.%c()"
        return HttpResponse(output)
    return HttpResponse("Unauthorized attempt.", status=403)


def get_admin_urls(urls):
    """
    Appends the terminal and post urls to the url patterns
    """

    def get_urls():
        my_urls = [
            path('terminal/', admin.site.admin_view(terminal)),
            path('terminal/post/', admin.site.admin_view(terminal_post))
        ]
        return my_urls + urls

    return get_urls


admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls
