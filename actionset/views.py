# coding: utf-8
"""
Pydici action set views. Http request are processed here.
@author: Sébastien Renard (sebastien.renard@digitalfox.org)
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

import json

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

from actionset.models import ActionSet, ActionState
from core.decorator import pydici_non_public, pydici_feature


@pydici_non_public
@pydici_feature("management")
def update_action_state(request, action_state_id, state):
    """Update action status.
    This view is designed to be called in ajax only
    @return: 0 on success, 1 on error/permission limitation"""
    error = HttpResponse(json.dumps({"error": True}), content_type="application/json")
    try:
        actionState = ActionState.objects.get(id=action_state_id)
    except ActionState.DoesNotExist:
        return error
    if request.user != actionState.user:
        return error
    if state == "DELEGUATE" and "username" in request.GET:
        try:
            user = User.objects.get(id=request.GET["username"])
        except User.DoesNotExist:
            return error
        actionState.user = user
        actionState.save()
        return HttpResponse(json.dumps({"error": False, "id": action_state_id}), content_type="application/json")
    elif state in (i[0] for i in ActionState.ACTION_STATES):
        actionState.state = state
        actionState.save()
        return HttpResponse(json.dumps({"error": False, "id": action_state_id}), content_type="application/json")
    else:
        return error


@pydici_non_public
@pydici_feature("management")
def actionset_catalog(request):
    """Catalog of all action set"""
    if request.user.has_perm("actionset.change_action") and request.user.has_perm("actionset.change_actionset"):
        can_change = True
    else:
        can_change = False
    return render(request, "actionset/actionset_catalog.html",
                  {"actionsets": ActionSet.objects.all(),
                   "can_change": can_change})