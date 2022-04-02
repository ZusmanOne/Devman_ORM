import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    # client = Passcard.objects.get(id=1)
    # active_client = []
    # for client in Passcard.objects.all():
    #     if client.is_active:
    #         active_client.append(client)
    print("Всего пропусков:", Passcard.objects.count())
    print("Активных пропусков:", len(Passcard.objects.filter(is_active=True)))
    #print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
