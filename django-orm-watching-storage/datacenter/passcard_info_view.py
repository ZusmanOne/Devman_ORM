from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .storage_information_view import format_duration, get_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visit = Visit.objects.filter(passcard=passcard)

    # Программируем здесь

    this_passcard_visits = []
    for client in visit:
        is_strange = get_duration(client) // 3600 >= 1
        this_passcard_visits.append({'entered_at':client.entered_at,
                                     'duration': format_duration(get_duration(client)),
                                     'is_strange' : is_strange,
                                     })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
