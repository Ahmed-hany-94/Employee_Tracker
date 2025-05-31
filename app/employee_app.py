import flet as ft
from flet import Page, View, padding
from app.config.colors import COLORS
from app.config.translations import translations
from app.views.login_view import LoginView
from app.views.dashboard_view import DashboardView
from app.views.salary_view import SalaryView
from app.views.expenses_view import ExpensesView
from app.views.settings_view import SettingsView
from app.views.admin_view import AdminView

class EmployeeManagementApp:
    def __init__(self):
        self.language = 'ar'  # Default language is Arabic
        self.current_user = None
        self.page = None
        
    def t(self, key):
        """Helper function for translation"""
        return translations[self.language].get(key, key)
    
    def toggle_language(self, e=None):
        """Toggle language between Arabic and English"""
        self.language = 'en' if self.language == 'ar' else 'ar'
        self.page.rtl = self.language == 'ar'
        self.page.update()
        self.navigate(self.page.route)
    
    def initialize(self):
        """Initialize the app with the login view"""
        self.navigate('/')
    
    def navigate(self, route):
        """Navigate to a specific route"""
        if route == '/':
            self.page.views.clear()
            self.page.views.append(
                View(
                    route='/',
                    controls=[LoginView(self).build()],
                    padding=padding.all(0),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/dashboard':
            self.page.views.clear()
            self.page.views.append(
                View(
                    route='/dashboard',
                    controls=[DashboardView(self).build()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/salary':
            self.page.views.append(
                View(
                    route='/salary',
                    controls=[SalaryView(self).build()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/expenses':
            self.page.views.append(
                View(
                    route='/expenses',
                    controls=[ExpensesView(self).build()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/settings':
            self.page.views.append(
                View(
                    route='/settings',
                    controls=[SettingsView(self).build()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/admin':
            self.page.views.append(
                View(
                    route='/admin',
                    controls=[AdminView(self).build()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        
        self.page.update()
    
    def route_change(self, route):
        """Handle route changes"""
        self.page.views.clear()
        self.navigate(route.route)
        
    def go_back(self):
        """Go back to previous view"""
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)
        else:
            self.navigate('/dashboard')