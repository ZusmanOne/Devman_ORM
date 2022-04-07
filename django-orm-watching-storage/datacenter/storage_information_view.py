from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    now = localtime()
    if visit.leaved_at:
        visit_time = localtime(visit.leaved_at) - localtime(visit.entered_at)
        return visit_time.total_seconds()
    else:
        visit_active = now - localtime(visit.entered_at)
        return visit_active.total_seconds()


def format_duration(duration, second_hour=3600, minute_hour=60):
    duration_hours = int(duration) // second_hour
    duration_minutes = int(duration % second_hour) // minute_hour
    return "%sч : %sм " % (duration_hours, duration_minutes)


def storage_information_view(request):
    not_outs = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for i in not_outs:
        non_closed_visits.append({'who_entered': i.passcard,
                                  'entered_at': i.entered_at,
                                  'duration': format_duration(get_duration(i)),
                                  }),

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context,)
