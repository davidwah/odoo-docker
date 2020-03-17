# -*- coding: utf-8 -*-
{
    'name': "Sample Addons",

    'summary': """
        Mount addons on Docker Volume""",

    'description': """
        Sample addons mount on docker volume
    """,

    'author': "DWP",
    'website': "https://github.com/davidwah/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Docker Volume',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'images': ['static\description\icon.png'],

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
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}