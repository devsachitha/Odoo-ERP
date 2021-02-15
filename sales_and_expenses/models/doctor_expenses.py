from odoo import api, fields, models, tools, SUPERUSER_ID, _


class DoctorExpenses(models.Model):
    _name = 'doctor.expenses'
    _description = "Doctor Expense"

    doctor_id = fields.Many2one('res.partner', 'Doctor',required=True, copy=True)
    date = fields.Date('Date', required=True)
    product_id = fields.Many2one('product.product', 'Expense Type', required=True)
    thirdparty_payee = fields.Many2one('res.partner', 'Service Provider')
    unit_amount = fields.Float("Unit Price", required=True, copy=True, digits='Product Price')
    quantity = fields.Float(required=True, digits='Product Unit of Measure', default=1)
    total_amount = fields.Monetary("Total", compute='_compute_amount', currency_field='currency_id', tracking=True)
    currency_id = fields.Many2one('res.currency', compute='_compute_amount', string='Currency',default=lambda self: self.env.company.currency_id)

    @api.depends('quantity', 'unit_amount', 'currency_id')
    def _compute_amount(self):
        for expense in self:
            expense.total_amount = expense.unit_amount * expense.quantity
