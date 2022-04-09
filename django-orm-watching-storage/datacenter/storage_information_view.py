from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

seconds_in_hour = 3600
minutes_in_hour = 60


def get_duration(visit):
    now_time = localtime()
    if visit.leaved_at:
        visit_time = localtime(visit.leaved_at) - localtime(visit.entered_at)
        return visit_time.total_seconds()
    else:
        visit_active = now_time - localtime(visit.entered_at)
        return visit_active.total_seconds()


def format_duration(duration):
    duration_hours = int(duration) // seconds_in_hour
    duration_minutes = int(duration % seconds_in_hour) // minutes_in_hour
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
