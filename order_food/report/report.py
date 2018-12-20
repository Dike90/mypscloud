# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

class order_detail_report(models.Model):
    _name = 'order_food.report'
    _auto = False  # 不会在数据库中创建表

    food_name = fields.Char(string='菜名', readonly=True)
    order_date = fields.Datetime(string='订单日期', readonly=True)
    department_id = fields.Selection(selection=[(1, 'PS产品部'), (2, '战略产品部'), (3, '营销')], string='部门', readonly=True)
    quantity = fields.Integer(string='数量', readonly=True)
    sale_price = fields.Float(string='总价', readonly=True)

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'order_food_report')
        self._cr.execute("""
                create view order_food_report as (
                    SELECT 
                        d.id as id,
                        f.name as food_name,
                        o.order_date as order_date,
                        o.payment_info as department_id,
                        d.quantity as quantity,
                        (d.sale_price*d.quantity) as sale_price
                    FROM order_food_detail as d
                    LEFT JOIN order_food_order as o on d.order_id = o.id
                    LEFT JOIN order_food_food as f on d.food_id = f.id   
                )
            """)
