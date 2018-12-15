# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class food(models.Model):
    _name = 'order_food.food'

    def compute_today(self):
        return datetime.datetime.today().weekday()

    name = fields.Char(string='菜名')
    # name = fields.Many2one('order_food.order',string='菜名')
    price = fields.Float(string='价格')
    # stock = fields.Integer(string='库存')
    food_date = fields.Selection(string='菜谱日期', selection=[(0, '星期一'), (1, '星期二'), (2, '星期三'),
                                    (3, '星期四'), (4, '星期五'), (5, '星期六'), (6, '星期日')], default=compute_today)
    description = fields.Text(string='描述')
    food_image = fields.Binary(string='图片')


class order(models.Model):
    _name = 'order_food.order'

    # def get_order_no(self):
    #     # 年月日时分秒
    #     return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    def compute_today(self):
        return datetime.datetime.today().weekday()

    user_id = fields.Many2one('res.users', string="用户名称", default=lambda self: self.env.user, readonly=True)
    # order_no = fields.Char(string='订单编号', required=True, default=get_order_no)
    state = fields.Selection(selection=[(0, '点餐'), (1, '付款')])
    food_ids = fields.Many2many('order_food.food', string='点菜')  # ,domain=[('food_date', '=', datetime.datetime.today().weekday())]
    # food_names = fields.One2many('order_food.food', 'name')
    week_of_today = fields.Integer(default=compute_today)
    # 计算字段默认是不存储的，若需要存储需要加store=True
    amount = fields.Float(string='金额', compute='_calc_amount', store=True)
    payment_info = fields.Integer(string='支付信息')



    @api.depends()
    def _compute_today(self):
        self.week_of_today = datetime.datetime.today().weekday()

    # 依赖装饰器
    @api.depends('food_ids')
    def _calc_amount(self):
        for p in self.food_ids:
            self.amount += p.price


    #@api.depends('food_ids')
    def order_food(self):
        self.state = 1

# class order_detail(models.Model):
#     _name = 'order_food.detail'
#
#     food_id = fields.Many2one('order_food.food', string='菜名')
#     order_id = fields.Many2one('order_food.order')
#     quantity = fields.Integer(string='数量')
#     line_no = fields.Integer(string='行号')
