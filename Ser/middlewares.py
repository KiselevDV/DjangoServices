from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class CheckUserIsBlockedMiddleware(MiddlewareMixin):
    """Блокировка пользователя на уровне Middleware"""

    def process_request(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_blocked:
                logout(request)
                return HttpResponseRedirect('/')
