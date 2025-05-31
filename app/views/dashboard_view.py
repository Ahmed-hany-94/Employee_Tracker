import flet as ft
from flet import (
    ListView, Card, Column, Row, Container, Text, ElevatedButton, TextButton,
    MainAxisAlignment, CrossAxisAlignment, ScrollMode, padding, margin, border_radius
)
from app.config.colors import COLORS

class DashboardView:
    def __init__(self, app):
        self.app = app
    
    def build(self):
        # Create notifications list
        notifications_list = ListView(
            spacing=10,
            padding=10,
            divider_thickness=1,
        )
        
        # Add sample notifications
        notifications_list.controls.append(
            Card(
                content=Container(
                    content=Column([
                        Text("تم إضافة بدل نقل جديد", weight=ft.FontWeight.BOLD),
                        Text("تم إضافة بدل نقل بقيمة 300 ريال شهري", size=14),
                        Text("15/03/2023", size=12, color=COLORS['text']),
                    ]),
                    padding=padding.all(15),
                )
            )
        )
        
        notifications_list.controls.append(
            Card(
                content=Container(
                    content=Column([
                        Text("موعد صرف الرواتب", weight=ft.FontWeight.BOLD),
                        Text("سيتم صرف رواتب شهر مارس يوم 28/03/2023", size=14),
                        Text("20/03/2023", size=12, color=COLORS['text']),
                    ]),
                    padding=padding.all(15),
                )
            )
        )
        
        # Create service buttons
        salary_button = ElevatedButton(
            text=self.app.t('salary'),
            on_click=lambda e: self.app.navigate('/salary'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['primary'],
                padding=padding.all(20),
            ),
            width=150,
            height=100
        )
        
        expenses_button = ElevatedButton(
            text=self.app.t('expenses'),
            on_click=lambda e: self.app.navigate('/expenses'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['secondary'],
                padding=padding.all(20),
            ),
            width=150,
            height=100
        )
        
        settings_button = ElevatedButton(
            text=self.app.t('settings'),
            on_click=lambda e: self.app.navigate('/settings'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['success'],
                padding=padding.all(20),
            ),
            width=150,
            height=100
        )
        
        admin_button = None
        if self.app.current_user and self.app.current_user.get("is_admin"):
            admin_button = ElevatedButton(
                text=self.app.t('admin_panel'),
                on_click=lambda e: self.app.navigate('/admin'),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor=COLORS['text'],
                    padding=padding.all(20),
                ),
                width=150,
                height=100
            )
        
        buttons_row1 = Row(
            [salary_button, expenses_button],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )
        
        buttons_row2 = Row(
            [settings_button, admin_button] if admin_button else [settings_button],
            alignment=MainAxisAlignment.SPACE_BETWEEN
        )
        
        return Column(
            [
                Row(
                    [
                        Text(self.app.t('dashboard'), size=30, weight=ft.FontWeight.BOLD),
                        TextButton(
                            text="English" if self.app.language == 'ar' else "العربية",
                            on_click=self.app.toggle_language
                        )
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Text(self.app.t('notifications'), size=20, weight=ft.FontWeight.BOLD),
                    margin=margin.only(top=20, bottom=10)
                ),
                Container(
                    content=notifications_list,
                    height=200,
                    border_radius=border_radius.all(10),
                    bgcolor=ft.colors.WHITE,
                ),
                Container(
                    content=Text(self.app.t('services'), size=20, weight=ft.FontWeight.BOLD),
                    margin=margin.only(top=20, bottom=10)
                ),
                buttons_row1,
                buttons_row2
            ],
            spacing=15,
            scroll=ScrollMode.AUTO
        )