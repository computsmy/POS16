# -*- coding: utf-8 -*-
# from odoo import http


# class DhOperation(http.Controller):
#     @http.route('/dh_operation/dh_operation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_operation/dh_operation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_operation.listing', {
#             'root': '/dh_operation/dh_operation',
#             'objects': http.request.env['dh_operation.dh_operation'].search([]),
#         })

#     @http.route('/dh_operation/dh_operation/objects/<model("dh_operation.dh_operation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_operation.object', {
#             'object': obj
#         })
