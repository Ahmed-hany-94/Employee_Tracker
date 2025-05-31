import flet as ft
from flet import (
    TextField, Column, Row, Container, Text, IconButton, ElevatedButton, 
    ListView, Card, icons, MainAxisAlignment, padding, margin, border_radius
)
from app.config.colors import COLORS

class AdminView:
    def __init__(self, app):
        self.app = app
        self.notifications = [
            {
                "title": "تم إضافة بدل نقل جديد",
                "content": "تم إضافة بدل نقل بقيمة 300 ريال شهري",
                "date": "15/03/2023"
            },
            {
                "title": "موعد صرف الرواتب",
                "content": "سيتم صرف رواتب شهر مارس يوم 28/03/2023",
                "date": "20/03/2023"
            }
        ]
    
    def build(self):
        # Notifications list
        notifications_list = ListView(
            spacing=10,
            padding=10,
            divider_thickness=1,
        )
        
        # Add notifications with edit/delete buttons
        for i, notification in enumerate(self.notifications):
            notifications_list.controls.append(
                Card(
                    content=Container(
                        content=Column([
                            Row(
                                [
                                    Text(notification["title"], weight=ft.FontWeight.BOLD),
                                    Row(
                                        [
                                            IconButton(
                                                icon=icons.EDIT,
                                                icon_color=COLORS['primary'],
                                                tooltip=self.app.t('edit'),
                                                on_click=lambda e, idx=i: self.edit_notification(idx)
                                            ),
                                            IconButton(
                                                icon=icons.DELETE,
                                                icon_color=COLORS['secondary'],
                                                tooltip=self.app.t('delete'),
                                                on_click=lambda e, idx=i: self.delete_notification(idx)
                                            )
                                        ]
                                    )
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            ),
                            Text(notification["content"], size=14),
                            Text(notification["date"], size=12, color=COLORS['text']),
                        ]),
                        padding=padding.all(15),
                    )
                )
            )
        
        # Add notification form
        title_field = TextField(label=self.app.t('notification_title'))
        content_field = TextField(label=self.app.t('notification_content'), multiline=True, min_lines=3)
        
        def add_notification(e):
            if title_field.value and content_field.value:
                self.notifications.append({
                    "title": title_field.value,
                    "content": content_field.value,
                    "date": "01/04/2023"  # Example date
                })
                title_field.value = ""
                content_field.value = ""
                self.app.page.update()
                self.app.navigate('/admin')
        
        add_button = ElevatedButton(
            text=self.app.t('add'),
            on_click=add_notification,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['primary'],
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
                        Text(self.app.t('admin_panel'), size=30, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Column(
                        [
                            Text(self.app.t('notifications'), size=20, weight=ft.FontWeight.BOLD),
                            Container(
                                content=notifications_list,
                                height=300,
                            ),
                        ],
                        spacing=10
                    ),
                    padding=padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border_radius=border_radius.all(10),
                    margin=margin.only(top=20)
                ),
                Container(
                    content=Column(
                        [
                            Text(self.app.t('add_notification'), size=20, weight=ft.FontWeight.BOLD),
                            title_field,
                            content_field,
                            add_button,
                        ],
                        spacing=15
                    ),
                    padding=padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border_radius=border_radius.all(10),
                    margin=margin.only(top=20)
                )
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )
    
    def edit_notification(self, index):
        # In a real app, this would open an edit dialog
        self.app.page.snack_bar = ft.SnackBar(ft.Text(f"Edit notification {index+1}"))
        self.app.page.snack_bar.open = True
        self.app.page.update()
    
    def delete_notification(self, index):
        # In a real app, this would show a confirmation dialog
        self.notifications.pop(index)
        self.app.page.snack_bar = ft.SnackBar(ft.Text("Notification deleted"))
        self.app.page.snack_bar.open = True
        self.app.page.update()
        self.app.navigate('/admin')