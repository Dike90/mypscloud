# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class food(models.Model):
    _name = 'order_food.food'

    def compute_today(self):
        return datetime.datetime.today().weekday()

    name = fields.Char(string='菜名' , index=True)
    # name = fields.Many2one('order_food.order',string='菜名')
    order_detail_ids = fields.One2many('order_food.detail','food_id')
    price = fields.Float(string='价格')
    # stock = fields.Integer(string='库存')
    food_date = fields.Selection(string='菜谱日期', selection=[(0, '星期一'), (1, '星期二'), (2, '星期三'),
                                    (3, '星期四'), (4, '星期五'), (5, '星期六'), (6, '星期日')], default=compute_today)
    description = fields.Text(string='描述')
    food_image = fields.Binary(string='图片')

    _sql_constraints = [
             ('食物唯一索引', 'unique (name)','不能创建重复的菜!')]

class order(models.Model):
    _name = 'order_food.order'

    # def get_order_no(self):
    #     # 年月日时分秒
    #     return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    def compute_today(self):
        return datetime.datetime.today().weekday()

    user_id = fields.Many2one('res.users', string="用户名称", default=lambda self: self.env.user, readonly=True)
    # order_no = fields.Char(string='订单编号', required=True, default=get_order_no)
    detail_ids = fields.One2many('order_food.detail','order_id',string='订单明细')
    state = fields.Selection(selection=[(0, '点餐'), (1, '付款')], default=0)
    # food_ids = fields.Many2many('order_food.food', string='点菜')  # ,domain=[('food_date', '=', datetime.datetime.today().weekday())]
    # food_names = fields.One2many('order_food.food', 'name')
    order_date = fields.Datetime(string='订单日期', required=True, readonly=True, default=fields.Datetime.now)
    week_of_today = fields.Integer(default=compute_today)
    # 计算字段默认是不存储的，若需要存储需要加store=True
    amount = fields.Float(string='金额', compute='_calc_amount', store=True)
    payment_info = fields.Selection(string='所属部门',selection=[(1,'PS产品部'),(2,'战略产品部'),(3,'营销')],default=1)
    _sql_constraints = [
             ('部门非空', 'CHECK(payment_info >0)', '所属部门不能为空!')]


    @api.depends()
    def _compute_today(self):
        self.week_of_today = datetime.datetime.today().weekday()

    # 依赖装饰器
    @api.depends('detail_ids')
    def _calc_amount(self):
        for p in self.detail_ids:
            self.amount += p.sale_price

    @api.multi
    def order_food(self):
        self.state = 1
        if self.payment_info:
            # print(self.payment_info)
            pay_info = self.env["order_food.qrimage"].search([("department", "=", self.payment_info)])
            params = {'department': pay_info.department, 'image': pay_info.QRimage}
            # print(pay_info.QRimage)
            view_id = self.env['order_food.wizard']
            new = view_id.create(params)

            return {
                'type': 'ir.actions.act_window',
                'name': '付款码',
                'res_model': 'order_food.wizard',
                'view_type': 'form',
                'view_mode': 'form',
                'res_id': new.id,
                'view_id': self.env.ref('order_food.my_order_food_wizard', False).id,
                'target': 'new',
            }



class order_detail(models.Model):
    _name = 'order_food.detail'

    detail_date = fields.Datetime(readonly=True, default=fields.Datetime.now)
    food_id = fields.Many2one('order_food.food', string='菜名')
    order_id = fields.Many2one('order_food.order', ondelete='cascade')
    quantity = fields.Integer(string='数量', default=1)
    # readony=True，代码中也不可修改它的值,update也不行???
    sale_price = fields.Float(string='销售价格')
    sequence = fields.Integer(string='行号', default=1)


    @api.multi
    @api.onchange('food_id')
    def get_default_price(self):
        # print('trigger once')
        # print(self.food_id)
        # vals={}
        if self.food_id:
            self.sale_price = self.food_id.price
            # vals['sale_price'] = self.food_id.price
            # self.update(vals)
            # print('updated')

class pay_QRimage(models.Model):
    _name = 'order_food.qrimage'

    department = fields.Selection(selection=[(1, 'PS产品部'), (2, '战略产品部'), (3, '营销')], string='部门', index=True)
    owner = fields.Many2one('res.users', string="二维码归属", default=lambda self: self.env.user)
    QRimage = fields.Binary(string='付款二维码')

    _sql_constraints = [
             ('部门唯一索引', 'unique (department)','不能创建重复的部门!')]



