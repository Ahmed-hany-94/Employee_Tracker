import flet as ft
from flet import (
    TextField, Checkbox, ElevatedButton, TextButton, 
    Column, Row, Container, Text, MainAxisAlignment, CrossAxisAlignment,
    padding, margin
)
from app.config.colors import COLORS

class LoginView:
    def __init__(self, app):
        self.app = app
    
    def build(self):
        file_number = TextField(label=self.app.t('file_number'), autofocus=True)
        phone = TextField(label=self.app.t('phone'))
        password = TextField(label=self.app.t('password'), password=True)
        remember_me = Checkbox(label=self.app.t('remember_me'))
        
        def login_click(e):
            # Simple login validation
            if file_number.value == "12345" and phone.value == "0555555555" and password.value == "password":
                self.app.current_user = {"file_number": file_number.value, "is_admin": True}
                self.app.navigate('/dashboard')
            else:
                self.app.page.snack_bar = ft.SnackBar(ft.Text(self.app.t('invalid_login')))
                self.app.page.snack_bar.open = True
                self.app.page.update()
        
        login_button = ElevatedButton(
            text=self.app.t('login'),
            on_click=login_click,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['primary'],
                padding=padding.all(15),
            ),
            width=400
        )
        
        language_button = TextButton(
            text="English" if self.app.language == 'ar' else "العربية",
            on_click=self.app.toggle_language
        )
        
        return Container(
            content=Column(
                [
                    Container(
                        content=Text(self.app.t('login'), size=30, weight=ft.FontWeight.BOLD),
                        alignment=ft.alignment.center,
                        margin=margin.only(top=50, bottom=20)
                    ),
                    file_number,
                    phone,
                    password,
                    Row([remember_me], alignment=MainAxisAlignment.START),
                    login_button,
                    Container(
                        content=language_button,
                        alignment=ft.alignment.center,
                        margin=margin.only(top=20)
                    )
                ],
                spacing=20,
                horizontal_alignment=CrossAxisAlignment.CENTER
            ),
            padding=padding.all(30),
            width=400,
            alignment=ft.alignment.center
        )