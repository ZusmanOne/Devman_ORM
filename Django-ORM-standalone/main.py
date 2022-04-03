import os
from django.utils.timezone import localtime
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    # client = Passcard.objects.get(id=1)
    # active_client = []
    # for client in Passcard.objects.all():
    #     if client.is_active:
    #         active_client.append(client)
    # print("Всего пропусков:", Passcard.objects.count())
    # print("Активных пропусков:", len(Passcard.objects.filter(is_active=True)))
    # print(Visit.objects.filter(leaved_at=None))
    entered = Visit.objects.get(pk=27160)
    # duration = duration(entered)
    # for enter in entered:
    #     print("Зашёл в хранилище, время по Москве:", localtime(enter.entered_at))
    #     date = localtime() - localtime(enter.entered_at)
    #     print('Находится в хранилище:', date, sep='\n')
    print(dir(entered))


