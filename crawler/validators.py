from django.core.exceptions import ValidationError
import jdatetime
def valid_space(value):
    if value not in range(30,4000):
        raise ValidationError('متراژ خانه مورد تأیید نمی‌باشد.')

def valid_room(value):
    if value not in range(6):
        raise ValidationError('تعداد خواب مورد تأیید نمی‌باشد.')


def valid_year_of_constructions(value):
    if value not in range(1300,int(jdatetime.datetime.now().year)+1):
        raise ValidationError('سال ساخت مورد تأیید نمی‌باشد.')


