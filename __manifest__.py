# -*- coding: utf-8 -*-
{
    'name': "vit_sale_address",

    'summary': """
        Modul Untuk Perubahaan Delivery Address dan Invoicing Address Pada SAle""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Iqbal Abdurrahman",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'sale',
                ],

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
}