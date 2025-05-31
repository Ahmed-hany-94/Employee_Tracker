import flet as ft
from flet import (
    AppBar, ElevatedButton, Page, Text, TextField, Column, Row, 
    Container, Checkbox, Dropdown, dropdown, ListView, Divider,
    Icon, icons, TextButton, Card, MainAxisAlignment, CrossAxisAlignment,
    ScrollMode, IconButton, colors, border_radius, padding, margin
)

# Translation dictionary
translations = {
    'ar': {
        'login': 'تسجيل الدخول',
        'file_number': 'رقم الملف',
        'phone': 'رقم الهاتف',
        'password': 'كلمة المرور',
        'remember_me': 'تذكرني',
        'dashboard': 'لوحة التحكم',
        'notifications': 'الإشعارات',
        'services': 'الخدمات',
        'salary': 'الرواتب',
        'expenses': 'المصروفات',
        'settings': 'الإعدادات',
        'admin_panel': 'لوحة الإدارة',
        'back': 'رجوع',
        'select_month': 'اختر الشهر:',
        'select_period': 'اختر الفترة:',
        'item': 'البند',
        'amount': 'المبلغ',
        'date': 'التاريخ',
        'total': 'الإجمالي',
        'basic_salary': 'الراتب الأساسي',
        'housing_allowance': 'بدل سكن',
        'change_password': 'تغيير كلمة المرور',
        'old_password': 'كلمة المرور القديمة',
        'new_password': 'كلمة المرور الجديدة',
        'confirm_password': 'تأكيد كلمة المرور',
        'save': 'حفظ',
        'language': 'اللغة',
        'logout': 'تسجيل الخروج',
        'months': ['يناير 2023', 'فبراير 2023', 'مارس 2023', 'أبريل 2023'],
        'periods': ['الربع الأول 2023', 'الربع الثاني 2023', 'الربع الثالث 2023'],
        'sar': 'ريال'
    },
    'en': {
        'login': 'Login',
        'file_number': 'File Number',
        'phone': 'Phone Number',
        'password': 'Password',
        'remember_me': 'Remember Me',
        'dashboard': 'Dashboard',
        'notifications': 'Notifications',
        'services': 'Services',
        'salary': 'Salary',
        'expenses': 'Expenses',
        'settings': 'Settings',
        'admin_panel': 'Admin Panel',
        'back': 'Back',
        'select_month': 'Select Month:',
        'select_period': 'Select Period:',
        'item': 'Item',
        'amount': 'Amount',
        'date': 'Date',
        'total': 'Total',
        'basic_salary': 'Basic Salary',
        'housing_allowance': 'Housing Allowance',
        'change_password': 'Change Password',
        'old_password': 'Old Password',
        'new_password': 'New Password',
        'confirm_password': 'Confirm Password',
        'save': 'Save',
        'language': 'Language',
        'logout': 'Logout',
        'months': ['January 2023', 'February 2023', 'March 2023', 'April 2023'],
        'periods': ['Q1 2023', 'Q2 2023', 'Q3 2023'],
        'sar': 'SAR'
    }
}

# App colors
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'success': '#F18F01',
    'background': '#F5F7FA',
    'text': '#2C3E50',
    'neutral': '#ECF0F1'
}

class EmployeeManagementApp:
    def __init__(self):
        self.language = 'ar'  # Default language is Arabic
        self.current_user = None
        self.page = None
        
    def t(self, key):
        """Helper function for translation"""
        return translations[self.language].get(key, key)
    
    def toggle_language(self, e):
        """Toggle language between Arabic and English"""
        self.language = 'en' if self.language == 'ar' else 'ar'
        self.page.rtl = self.language == 'ar'
        self.page.update()
        self.navigate(self.page.route)
    
    def navigate(self, route):
        """Navigate to a specific route"""
        self.page.views.clear()
        
        if route == '/':
            self.page.views.append(
                ft.View(
                    route='/',
                    controls=[self.login_view()],
                    padding=padding.all(0),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/dashboard':
            self.page.views.append(
                ft.View(
                    route='/dashboard',
                    controls=[self.dashboard_view()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/salary':
            self.page.views.append(
                ft.View(
                    route='/salary',
                    controls=[self.salary_view()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/expenses':
            self.page.views.append(
                ft.View(
                    route='/expenses',
                    controls=[self.expenses_view()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/settings':
            self.page.views.append(
                ft.View(
                    route='/settings',
                    controls=[self.settings_view()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        elif route == '/admin':
            self.page.views.append(
                ft.View(
                    route='/admin',
                    controls=[self.admin_view()],
                    padding=padding.all(20),
                    bgcolor=COLORS['background']
                )
            )
        
        self.page.update()
    
    def on_view_pop(self, view):
        """Handle back button press"""
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
    
    def login_view(self):
        """Login page"""
        file_number = TextField(label=self.t('file_number'), autofocus=True)
        phone = TextField(label=self.t('phone'))
        password = TextField(label=self.t('password'), password=True)
        remember_me = Checkbox(label=self.t('remember_me'))
        
        def login_click(e):
            # Simple login validation
            if file_number.value == "12345" and phone.value == "0555555555" and password.value == "password":
                self.current_user = {"file_number": file_number.value, "is_admin": True}
                self.navigate('/dashboard')
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text("Invalid login credentials"))
                self.page.snack_bar.open = True
                self.page.update()
        
        login_button = ElevatedButton(
            text=self.t('login'),
            on_click=login_click,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['primary'],
                padding=padding.all(15),
            ),
            width=400
        )
        
        language_button = TextButton(
            text="English" if self.language == 'ar' else "العربية",
            on_click=self.toggle_language
        )
        
        return Container(
            content=Column(
                [
                    Container(
                        content=Text(self.t('login'), size=30, weight=ft.FontWeight.BOLD),
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
    
    def dashboard_view(self):
        """Main dashboard page"""
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
                        Text("New transportation allowance added", weight=ft.FontWeight.BOLD),
                        Text("A transportation allowance of 300 SAR monthly has been added", size=14),
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
                        Text("Salary payment date", weight=ft.FontWeight.BOLD),
                        Text("March salaries will be paid on 28/03/2023", size=14),
                        Text("20/03/2023", size=12, color=COLORS['text']),
                    ]),
                    padding=padding.all(15),
                )
            )
        )
        
        # Create service buttons
        salary_button = ElevatedButton(
            text=self.t('salary'),
            on_click=lambda e: self.navigate('/salary'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['primary'],
                padding=padding.all(20),
            ),
            width=150,
            height=100
        )
        
        expenses_button = ElevatedButton(
            text=self.t('expenses'),
            on_click=lambda e: self.navigate('/expenses'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['secondary'],
                padding=padding.all(20),
            ),
            width=150,
            height=100
        )
        
        settings_button = ElevatedButton(
            text=self.t('settings'),
            on_click=lambda e: self.navigate('/settings'),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=COLORS['success'],
                padding=padding.all(20),
            ),
            width=150,
            height=100
        )
        
        admin_button = None
        if self.current_user and self.current_user.get("is_admin"):
            admin_button = ElevatedButton(
                text=self.t('admin_panel'),
                on_click=lambda e: self.navigate('/admin'),
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
                        Text(self.t('dashboard'), size=30, weight=ft.FontWeight.BOLD),
                        TextButton(
                            text="English" if self.language == 'ar' else "العربية",
                            on_click=self.toggle_language
                        )
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Text(self.t('notifications'), size=20, weight=ft.FontWeight.BOLD),
                    margin=margin.only(top=20, bottom=10)
                ),
                Container(
                    content=notifications_list,
                    height=200,
                    border_radius=border_radius.all(10),
                    bgcolor=ft.colors.WHITE,
                ),
                Container(
                    content=Text(self.t('services'), size=20, weight=ft.FontWeight.BOLD),
                    margin=margin.only(top=20, bottom=10)
                ),
                buttons_row1,
                buttons_row2
            ],
            spacing=15,
            scroll=ScrollMode.AUTO
        )
    
    def salary_view(self):
        """Salary page"""
        # Month dropdown
        month_dropdown = Dropdown(
            options=[dropdown.Option(m) for m in translations[self.language]['months']],
            value=translations[self.language]['months'][0],
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
                    Text(self.t('basic_salary'), size=16),
                    Text(f"5,000 {self.t('sar')}", size=16, color=COLORS['text']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        salary_items.controls.append(
            Row(
                [
                    Text(self.t('housing_allowance'), size=16),
                    Text(f"1,500 {self.t('sar')}", size=16, color=COLORS['text']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        # Total row
        total_row = Container(
            content=Row(
                [
                    Text(self.t('total'), size=20, weight=ft.FontWeight.BOLD),
                    Text(f"6,500 {self.t('sar')}", size=20, weight=ft.FontWeight.BOLD, color=COLORS['primary']),
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
                            on_click=lambda e: self.navigate('/dashboard')
                        ),
                        Text(self.t('salary'), size=30, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Row(
                    [
                        Text(self.t('select_month')),
                        month_dropdown
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Column(
                        [
                            Row(
                                [
                                    Text(self.t('item'), weight=ft.FontWeight.BOLD),
                                    Text(self.t('amount'), weight=ft.FontWeight.BOLD),
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
    
    def expenses_view(self):
        """Expenses page"""
        # Period dropdown
        period_dropdown = Dropdown(
            options=[dropdown.Option(p) for p in translations[self.language]['periods']],
            value=translations[self.language]['periods'][0],
            width=200
        )
        
        # Expenses items list
        expenses_items = ListView(
            spacing=10,
            padding=10,
            divider_thickness=1,
        )
        
        # Add expense items
        expenses_items.controls.append(
            Row(
                [
                    Text("15/01/2023", size=14),
                    Text("Health Insurance", size=14),
                    Text(f"500 {self.t('sar')}", size=14, color=COLORS['secondary']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        expenses_items.controls.append(
            Row(
                [
                    Text("22/02/2023", size=14),
                    Text("Training", size=14),
                    Text(f"750 {self.t('sar')}", size=14, color=COLORS['secondary']),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
        
        # Total row
        total_row = Container(
            content=Row(
                [
                    Text(self.t('total'), size=20, weight=ft.FontWeight.BOLD),
                    Text(f"1,250 {self.t('sar')}", size=20, weight=ft.FontWeight.BOLD, color=COLORS['secondary']),
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
                            on_click=lambda e: self.navigate('/dashboard')
                        ),
                        Text(self.t('expenses'), size=30, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Row(
                    [
                        Text(self.t('select_period')),
                        period_dropdown
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ),
                Container(
                    content=Column(
                        [
                            Row(
                                [
                                    Text(self.t('date'), weight=ft.FontWeight.BOLD),
                                    Text(self.t('item'), weight=ft.FontWeight.BOLD),
                                    Text(self.t('amount'), weight=ft.FontWeight.BOLD),
                                ],
                                alignment=MainAxisAlignment.SPACE_BETWEEN
                            ),
                            Divider(),
                            Container(
                                content=expenses_items,
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
    
    def settings_view(self):
        """Settings page"""
        old_password = TextField(label=self.t('old_password'), password=True)
        new_password = TextField(label=self.t('new_password'), password=True)
        confirm_password = TextField(label=self.t('confirm_password'), password=True)
        
        def change_password(e):
            # Password validation and change
            if old_password.value and new_password.value and new_password.value == confirm_password.value:
                self.page.snack_bar = ft.SnackBar(ft.Text("Password changed successfully"))
                self.page.snack_bar.open = True
                self.page.update()
                old_password.value = ""
                new_password.value = ""
                confirm_password.value = ""
                self.page.update()
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text("Please check your passwords"))
                self.page.snack_bar.open = True
               
