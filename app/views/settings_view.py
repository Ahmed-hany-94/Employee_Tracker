import flet as ft
from flet import (
    TextField, Column, Row, Container, Text, IconButton, ElevatedButton, 
    Dropdown, dropdown, icons, MainAxisAlignment, padding, margin, border_radius
)
from app.config.colors import COLORS

class SettingsView:
    def __init__(self, app):
        self.app = app
    
    def build(self):
        old_password = TextField(label=self.app.t('old_password'), password=True)
        new_password = TextField(label=self.app.t('new_password'), password=True)
        confirm_password = TextField(label=self.app.t('confirm_password'), password=True)
        
        def change_password(e):
            # Password validation and change
            if old_password.value and new_password.value and new_password.value == confirm_password.value:
                self.app.page.snack_bar = ft.SnackBar(ft.Text(self.app.t('password_changed')))
                self.app.page.snack_bar.open = True
                self.app.page.update()
                old_password.value = ""
                new_password.value = ""
                confirm_password.value = ""
                self.app.page.update()
            else:
                self.app.page.snack_bar = ft.SnackBar(ft.Text(self.app.t('check_passwords')))
                self.app.page.snack_bar.open = True
                self.app.page.update()
        
        save_button = ElevatedButton(
            text=self.app.t('save'),
            on_click=change_password,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['primary'],
                padding=padding.all(10),
            ),
        )
        
        # Language dropdown
        language_dropdown = Dropdown(
            options=[
                dropdown.Option("العربية", "ar"),
                dropdown.Option("English", "en")
            ],
            value="ar" if self.app.language == 'ar' else "en",
            width=200
        )
        
        def change_language(e):
            self.app.language = language_dropdown.value
            self.app.page.rtl = self.app.language == 'ar'
            self.app.page.update()
            self.app.navigate('/settings')
        
        language_dropdown.on_change = change_language
        
        # Logout button
        logout_button = ElevatedButton(
            text=self.app.t('logout'),
            on_click=lambda e: self.app.navigate('/'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['secondary'],
                padding=padding.all(10),
            ),
        )
        
        return Column(
            [
                Row(
                    [
                        IconButton(
                            icon=icons.ARROW_BACK,
                            on_click=lambda e: self.app.go_back()
                        ),
                        Text(self.app.t('settings'), size=30, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Column(
                        [
                            Text(self.app.t('change_password'), size=20, weight=ft.FontWeight.BOLD),
                            old_password,
                            new_password,
                            confirm_password,
                            save_button,
                        ],
                        spacing=15
                    ),
                    padding=padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border_radius=border_radius.all(10),
                    margin=margin.only(top=20)
                ),
                Container(
                    content=Column(
                        [
                            Text(self.app.t('language'), size=20, weight=ft.FontWeight.BOLD),
                            language_dropdown,
                        ],
                        spacing=15
                    ),
                    padding=padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border_radius=border_radius.all(10),
                    margin=margin.only(top=20)
                ),
                Container(
                    content=logout_button,
                    margin=margin.only(top=20)
                )
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )