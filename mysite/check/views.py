from django.views import generic
from .models import CheckQuestion, CheckClassroom


class IndexView(generic.ListView):
    template_name = 'check/rooms.html'
    context_object_name = 'rooms_to_check'

    def get_queryset(self):
        return CheckClassroom.objects.order_by('room_name')


class RoomView(generic.ListView):
    template_name = 'check/form.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return CheckQuestion.objects.order_by('check_id')

