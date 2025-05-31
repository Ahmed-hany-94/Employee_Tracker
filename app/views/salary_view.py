import flet as ft
from flet import (
    ListView, Dropdown, dropdown, Column, Row, Container, Text, IconButton, 
    Divider, icons, MainAxisAlignment, ScrollMode, padding, margin, border_radius
)
from app.config.colors import COLORS

class SalaryView:
    def __init__(self, app):
        self.app = app
    
    def build(self):
        # Month dropdown
        month_dropdown = Dropdown(
            options=[dropdown.Option(m) for m in self.app.t('months')],
            value=self.app.t('months')[0],
            width=200
        )
        
        # Salary items list
        salary_items = ListView(
            spacing=10,
            padding=10,
            divider_thickness=1,
        )
        
        # Add salary items
        salary_items.controls.append(
            Row(
                [
                    Text(self.app.t('basic_salary'), size=16),
                    Text(f"5,000 {self.app.t('sar')}", size=16, color=COLORS['text']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        salary_items.controls.append(
            Row(
                [
                    Text(self.app.t('housing_allowance'), size=16),
                    Text(f"1,500 {self.app.t('sar')}", size=16, color=COLORS['text']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        # Total row
        total_row = Container(
            content=Row(
                [
                    Text(self.app.t('total'), size=20, weight=ft.FontWeight.BOLD),
                    Text(f"6,500 {self.app.t('sar')}", size=20, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=padding.all(15),
            bgcolor=COLORS['neutral'],
            border_radius=border_radius.all(10)
        )
        
        return Column(
            [
                Row(
                    [
                        IconButton(
                            icon=icons.ARROW_BACK,
                            on_click=lambda e: self.app.go_back()
                        ),
                        Text(self.app.t('salary'), size=30, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Row(
                    [
                        Text(self.app.t('select_month')),
                        month_dropdown
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Column(
                        [
                            Row(
                                [
                                    Text(self.app.t('item'), weight=ft.FontWeight.BOLD),
                                    Text(self.app.t('amount'), weight=ft.FontWeight.BOLD),
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            ),
                            Divider(),
                            Container(
                                content=salary_items,
                                height=300,
                            ),
                            total_row
                        ],
                        spacing=10
                    ),
                    padding=padding.all(15),
                    bgcolor=ft.colors.WHITE,
                    border_radius=border_radius.all(10),
                    margin=margin.only(top=20)
                )
            ],
            spacing=15,
            scroll=ScrollMode.AUTO
        )
