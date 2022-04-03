from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    now = localtime()
    if visit.leaved_at:
        visit_at = localtime(visit.leaved_at) - localtime(visit.entered_at)
        return visit_at.total_seconds()
    else:
        visit_at = now - localtime(visit.entered_at)
        return visit_at.total_seconds()


def format_duration(duration):
    duration_hours = int(duration) // 3600
    duration_minutes = int((duration % 3600)) // 60
    return "%sч : %sм " % (duration_hours, duration_minutes)


def storage_information_view(request):
    # Программируем здесь
    enter = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for i in enter:
        non_closed_visits.append({'who_entered': i.passcard,
                                  'entered_at': i.entered_at,
                                  'duration': format_duration(get_duration(i)),
                                  }),

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context,)
