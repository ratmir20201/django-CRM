from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = """
Настраивает предустановленные роли пользователей в системе CRM.

Доступные роли:

1. Администратор:
   - Управление пользователями (создание, редактирование, назначение ролей).
   - Реализуется через административную панель Django.

2. Оператор:
   - Может создавать, просматривать и редактировать потенциальных клиентов (Lead).

3. Маркетолог:
   - Может создавать, просматривать и редактировать предоставляемые услуги (Product) и рекламные кампании (Ad).

4. Менеджер:
   - Может создавать, просматривать и редактировать контракты (Contract).
   - Имеет доступ к просмотру потенциальных клиентов и переводу их в активных.

5. Все роли:
   - Имеют доступ к просмотру статистики рекламных кампаний.

После запуска команда создаст соответствующие группы и назначит им необходимые разрешения.
"""

    def handle(self, *args, **options):
        roles_permissions = {
            "Оператор": ["add_lead", "change_lead", "delete_lead", "view_lead"],
            "Маркетолог": [
                "add_product",
                "change_product",
                "delete_product",
                "view_product",
                "add_ads",
                "change_ads",
                "delete_ads",
                "view_ads",
            ],
            "Менеджер": [
                "add_contract",
                "change_contract",
                "delete_contract",
                "view_contract",
                "view_lead",
                "add_customer",
                "change_customer",
                "delete_customer",
                "view_customer",
            ],
        }

        for role, codenames in roles_permissions.items():
            group, created = Group.objects.get_or_create(name=role)
            permissions = Permission.objects.filter(codename__in=codenames)
            group.permissions.set(permissions)
            self.stdout.write(
                self.style.SUCCESS(f"Роль '{role}' создана и настроена успешно.")
            )
