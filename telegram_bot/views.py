import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from telegram import Update
from .handler import bot, dispatcher


class UpdateHandler(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            update = Update.de_json(data, bot)
            dispatcher.process_update(update)
            return JsonResponse(data={'success': True}, status=200)
        except ValueError:
            return HttpResponseBadRequest('Malformed request body')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateHandler, self).dispatch(request, *args, **kwargs)

