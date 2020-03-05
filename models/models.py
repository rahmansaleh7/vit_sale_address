# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleAddress(models.Model):

    _name = "sale.order"
    _inherit = "sale.order"


    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1, help="You can find a customer by its Name, TIN, Email or Internal Reference.")
    partner_invoice_id = fields.Many2one('res.partner', string='Invoice Address', readonly=True, required=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]}, help="Invoice address for current sales order.")
    partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address', readonly=True, required=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]}, help="Delivery address for current sales order.")


#     @api.multi
#     @api.onchange('partner_id')
#     def onchange_partner_id(self):
#         super(SaleAddress, self).onchange_partner_id()
#         partners_invoice = []
#         partners_shipping = []
#         domain = {}
#         for record in self:
#             if record.partner_id:
#                 if record.partner_id.child_ids:
#                     for partner in record.partner_id.child_ids:
#                         if partner.type == 'invoice':
#                             partners_invoice.append(partner.street)
#                         if partner.type == 'delivery':
#                             partners_shipping.append(partner.street)
#                 if partners_invoice:
#                     domain['partner_invoice_id'] =  [('street', 'in', partners_invoice)]
#                 else:
#                     domain['partner_invoice_id'] =  []
#                 if partners_shipping:
#                     domain['partner_shipping_id'] = [('street', 'in', partners_shipping)]
#                 else:
#                     domain['partner_shipping_id'] =  []
#             else:
#                 domain['partner_invoice_id'] =  [('type', '=', 'invoice')]
#                 domain['partner_shipping_id'] =  [('type', '=', 'delivery')]

#         return {'domain': domain}
