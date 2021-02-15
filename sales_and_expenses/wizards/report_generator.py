from odoo import api, fields, models, tools, SUPERUSER_ID, _


class SalesAndExpensesWizard(models.TransientModel):
    _name = 'sales.expenses.wizard'

    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')