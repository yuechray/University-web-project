"""Custom Admin Site с защитой от менеджеров"""

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .helpers import is_manager

class ProtectedAdminSite(admin.AdminSite):
    """Admin site с защитой - менеджеры не могут попасть в админку"""
    
    def has_permission(self, request):
        """Проверяет, есть ли у пользователя доступ в админку"""
        # Если менеджер - запретить доступ
        if is_manager(request.user):
            return False
        # Если суперюзер - разрешить доступ
        return request.user.is_active and request.user.is_staff
    
    def index(self, request, extra_context=None):
        """Главная страница админки"""
        if not self.has_permission(request):
            if is_manager(request.user):
                return HttpResponseRedirect(reverse('manager_dashboard'))
            return HttpResponseRedirect(reverse('login'))
        return super().index(request, extra_context)
