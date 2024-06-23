from odoo import fields, api, models


class GokomodoTaxes(models.Model):
    _inherit = 'account.tax'

    # objective 4
    taxes_gokomodo = fields.Selection([
        ('RT', 'Retail'),
        ('CORP', 'Corporate'),
        ('SUB', 'Subscription'),
    ], string='Taxes Gokomodo')