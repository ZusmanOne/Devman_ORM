from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

SECONDS_IN_HOUR = 3600
MINUTES_IN_HOUR = 60


def get_duration(visit):
    now_time = localtime()
    if visit.leaved_at:
        visit_time = localtime(visit.leaved_at) - localtime(visit.entered_at)
        return visit_time.total_seconds()
    else:
        visit_active = now_time - localtime(visit.entered_at)
        return visit_active.total_seconds()


def format_duration(duration):
    duration_hours = int(duration) // SECONDS_IN_HOUR
    duration_minutes = int(duration % SECONDS_IN_HOUR) // MINUTES_IN_HOUR
    return "%sч : %sм " % (duration_hours, duration_minutes)


def storage_information_view(request):
    not_outs = Visit.objects.filter(leaved_at=None)
    serialized_visits = []
    for i in not_outs:
        serialized_visits.append({'who_entered': i.passcard,
                                  'entered_at': i.entered_at,
                                  'duration': format_duration(get_duration(i)),
                                  }),

    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context,)
