# -*- coding: utf-8 -*-
{
    'name': "order_food",

    'summary': """
        订餐系统""",

    'description': """
        PS产品部内部使用的订餐系统
    """,

    'author': "DK",
    'website': "http://www.mypscloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'order food',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
