# -*- coding: utf-8 -*-
# from odoo import http


# class Gokomodo(http.Controller):
#     @http.route('/gokomodo/gokomodo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gokomodo/gokomodo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gokomodo.listing', {
#             'root': '/gokomodo/gokomodo',
#             'objects': http.request.env['gokomodo.gokomodo'].search([]),
#         })

#     @http.route('/gokomodo/gokomodo/objects/<model("gokomodo.gokomodo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gokomodo.object', {
#             'object': obj
#         })
