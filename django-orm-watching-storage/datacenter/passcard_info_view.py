from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_duration, get_duration


def passcard_info_view(request, passcode, second_hour=3600):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    limit_hour = 1
    for client in visits:
        is_strange = get_duration(client) // second_hour >= limit_hour
        this_passcard_visits.append({'entered_at': client.entered_at,
                                     'duration': format_duration(get_duration(client)),
                                     'is_strange': is_strange,
                                     })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
