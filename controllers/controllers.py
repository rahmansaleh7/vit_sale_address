# -*- coding: utf-8 -*-
from odoo import http

# class VitSaleAddress(http.Controller):
#     @http.route('/vit_sale_address/vit_sale_address/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_sale_address/vit_sale_address/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_sale_address.listing', {
#             'root': '/vit_sale_address/vit_sale_address',
#             'objects': http.request.env['vit_sale_address.vit_sale_address'].search([]),
#         })

#     @http.route('/vit_sale_address/vit_sale_address/objects/<model("vit_sale_address.vit_sale_address"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_sale_address.object', {
#             'object': obj
#         })