from datacenter.models import Passcard, Visit
from django.shortcuts import render
from .storage_information_view import format_duration, get_duration


SECONDS_IN_HOUR = 3600


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    serialized_visits = []
    allowable_hour = 1
    for client in visits:
        is_strange = get_duration(client) // SECONDS_IN_HOUR >= allowable_hour
        serialized_visits.append({'entered_at': client.entered_at,
                                 'duration': format_duration(get_duration(client)),
                                  'is_strange': is_strange,
                                  }
                                 )

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
