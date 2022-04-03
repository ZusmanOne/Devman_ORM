import datetime
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
    # entered = Visit.objects.all()
    # entered = Visit.objects.filter(passcard__is_active=True)  # покажет посещения активных пользователей
    # a = 0
    # for enter in entered:
    #     if not enter.leaved_at:
    #         print("Зашёл в хранилище, время по Москве:", localtime(enter.entered_at))
    #         date = localtime().replace(microsecond=0) - localtime(enter.entered_at).replace(microsecond=0)
    #         print('Находится в хранилище:', date, enter,  sep='\n')
    #     elif enter.leaved_at:
    #         time_visit = localtime(enter.leaved_at) - localtime(enter.entered_at)
    #         time = int(time_visit.total_seconds()) // 60
    #         # time = int(time_visit.total_seconds()) // 3600
    #         if time >= 1000:
    #             a += 1
    #         # limit_time = localtime(enter.entered_at) + datetime.timedelta(hours=1)
    #             print(enter.passcard.owner_name)
    # print(a)
    # my_visit = Passcard.objects.get(passcode="ceb148a6-fb27-4106-890c-89dc8cedfe83")
    # print(my_visit.passcode)
    # visit = Visit.objects.filter(passcard=my_visit)  # покажет все посещения клиента
    # for i in visit:
    #     if i.leaved_at:
    #         time_visit = localtime(i.leaved_at) - localtime(i.entered_at)
    #         time = time_visit.total_seconds() // 60
    #         if time >= 1000:
    #             print(time)
    # print(my_visit.owner_name)


