"""Вспомогательные функции для проверки прав пользователя"""

def is_manager(user):
    """Проверяет, является ли пользователь менеджером"""
    if not user.is_authenticated:
        return False
    try:
        from .models import Manager
        return Manager.objects.filter(user=user).exists()
    except:
        return False


def is_admin_or_manager(user):
    """Проверяет, является ли пользователь администратором или менеджером"""
    if not user.is_authenticated:
        return False
    return user.is_superuser or is_manager(user)


def can_manage_orders(user):
    """Проверяет, может ли пользователь управлять заказами"""
    return is_admin_or_manager(user)
