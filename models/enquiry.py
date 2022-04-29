from odoo import api, fields, models, tools, _

class Enquiry(models.Model):
    _inherit = 'purchase.order'

    x_many2many = fields.Many2many('purchase.order.line',domain="[('partner_id', '=', '线下采购')]",string=u'多选')