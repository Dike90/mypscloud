# -*- coding: utf-8 -*-

from odoo import models, fields, api

class order(models.Model):
    _name = 'order_food.order'

    id = fields.Integer()
    order_no = fields.Integer()
    user_id = fields.Many2one('res.users', ondelete='set null', string="用户")
    #shipping_id = fields.Many2one()
    payment = fields.Float()
    payment_time = fields.Datetime(string="支付时间")
    payment_status = fields.Integer(string='支付状态')

class food_menu(models.Model):
    _name = 'order_food.food_menu'

    name = fields.Char(string='菜谱名称')
    id = fields.Integer()
    menu_date = fields.Date(string='日期')
    food_ids = fields.One2many('order_food.food_info','id', string='菜品')

class food_info(models.Model):
    _name = 'order_food.food_info'

    id = fields.Integer()
    name = fields.Char(string='菜名')
    price = fields.Float(string='价格')
    detials = fields.Text(string='菜品描述')
    food_menu_id = fields.Many2one('order_food.food_menu')

