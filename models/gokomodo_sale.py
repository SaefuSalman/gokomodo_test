from odoo import models, fields, api

class GokomodoSale(models.Model):
    _inherit = 'sale.order'

    # create field for objective 1
    bisnis_model = fields.Selection([
        ('RT', 'Retail'),
        ('CORP', 'Corporate'),
        ('SUB', 'Subscription'),
    ], string='Bisnis Model', required=True)

    # objective 2
    def name_get(self):
        result = []
        for rec in self:
            name = rec.name
            if rec.bisnis_model:
                name = "[%s] - %s" % (rec.bisnis_model, rec.name)
            result.append((rec.id, name))
        return result

    # objective 4
    @api.onchange('bisnis_model')
    def _onchange_bisnis_model(self):
        if self.bisnis_model:
            for line in self.order_line:
                taxes = self.env['account.tax'].search([('taxes_gokomodo', '=', self.bisnis_model)]).ids    
                if taxes:
                    line.tax_id = taxes
                else:
                    line.tax_id = [(5,0,0)]
            

            
