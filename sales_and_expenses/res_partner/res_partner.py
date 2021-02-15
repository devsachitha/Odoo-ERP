from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.modules import get_module_resource
from odoo.osv.expression import get_unaccent_wrapper
from odoo.exceptions import UserError, ValidationError


class Partner(models.Model):
    _inherit = ['res.partner']

    partner_type = fields.Selection(
        [('doctor', 'Doctor'),
         ('pharmacy', 'Pharmacy'),
         ], string='Type of the Customer',
        default=False)

    # doctor_id = fields.Many2one('res.partner',string='Doctor')
    # pharmacies = fields.One2many('res.partner','doctor_id', string='Pharmacies')
    depend_pharmacies = fields.Many2many('res.partner', 'doctors_pharmacies_rel',
                                         column1='doctor_id',
                                         column2='pharmacy_id',
                                         string='Pharmacies')

    expenses = fields.One2many(comodel_name='doctor.expenses',
                               inverse_name='doctor_id',
                               string='Expenses')
