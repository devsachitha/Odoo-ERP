{
    'name' : 'Sale Promotion Expenses',
    'version' : '1.1',
    'summary': 'Sales and Expenses in promotions',
    'sequence':170,
    'depends' : ['base_setup','base'],
    'data': [
            'views/sales_expenses_view.xml',
            # 'wizards/report_generator.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
