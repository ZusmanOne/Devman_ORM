from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
    all_passcard = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_passcard,
    }
    return render(request, 'active_passcards.html', context)
