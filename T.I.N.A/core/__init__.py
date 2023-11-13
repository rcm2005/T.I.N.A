import datetime


class SystemInfo:
    def __init__():
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f"São {now.hour} horas e {now.minute} minutos"
        print(now.year, now.month, now.day, now.hour, now.minute, now.second)
        return answer

