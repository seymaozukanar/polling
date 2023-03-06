from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from polling.polls.models import Poll
from polling.polls.serializers import PollSerializer



def list_polls(request):

    if request.method == "GET":

        polls = Poll.objects.all()
        context = {"polls": polls}

        return render(request, "polls/list_polls.html", context)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PollSerializer(data=data)
        if serializer.is_valid:
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def poll_detail(request, id):

    try:
        obj = Poll.objects.get(id=id)
    except Poll.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = PollSerializer(obj)

        return JsonResponse(serializer.data)
