# -*- coding: UTF-8 -*-
"""
@author: Sébastien Renard (sebastien.renard@digitalfox.org)
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from .pydici_celery import app as celery_app

__all__ = ('celery_app',)
