# -*- coding: utf-8 -*-

from .base import *  # noqa

MANAGERS = ADMINS = ()

ALLOWED_HOSTS.extend(["{{ project_name }}.test.ailove.ru"])  # noqa

DATABASES["default"]["HOST"] = "db.test.ailove.ru"  # noqa
