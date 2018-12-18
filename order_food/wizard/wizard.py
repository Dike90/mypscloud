# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class MyWizard(models.TransientModel):
    _name = 'order_food.wizard'

    # def _default_sessions(self):
    #     return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    department = fields.Selection(selection=[(1, 'PS产品部'), (2, '战略产品部'), (3, '营销')],readonly=True)
    image = fields.Binary(readonly=True)



    def confirm_pay(self):
        _logger.debug(' \n\n \t 确定付款了\n\n\n')


