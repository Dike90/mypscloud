# -*- coding: utf-8 -*-
from odoo import http

# class OrderFood(http.Controller):
#     @http.route('/order_food/order_food/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/order_food/order_food/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('order_food.listing', {
#             'root': '/order_food/order_food',
#             'objects': http.request.env['order_food.order_food'].search([]),
#         })

#     @http.route('/order_food/order_food/objects/<model("order_food.order_food"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('order_food.object', {
#             'object': obj
#         })