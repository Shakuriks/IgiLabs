from django.contrib.admin.utils import model_ngettext
from django.contrib.admin import AdminSite
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType

def update_model_from_admin(model_instance, request):
    admin_site = AdminSite()
    change_message = 'Updated via API'  # Сообщение об изменении
    content_type = ContentType.objects.get_for_model(model_instance)
    object_id = model_instance.pk

    # Сохранение изменений модели
    model_instance.save()

    # Создание записи в журнале администратора
    LogEntry.objects.log_action(
        user_id=request.user.pk,
        content_type_id=content_type.pk,
        object_id=object_id,
        object_repr=str(model_instance),
        action_flag=CHANGE,
        change_message=change_message,
    )

    # Получение текстового представления объекта модели
    object_name = model_ngettext(model_instance)

    # Возврат сообщения об успешном обновлении
    return f"{object_name} успешно обновлен(а) из кода."