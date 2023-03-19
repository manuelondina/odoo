# -*- coding: utf-8 -*-
{
    'name': "JSON parse de Sales orders",

    'summary': """
        Procesador de peticiones JSON de orden de ventas.
        """,

    'description': """
        Este modulo se encarga de recibir una peticion JSON y guardar el orden de venta, el cliente
        y el producto lo almacena si no existe alguno de ellos.
    """,

    'author': "Manuel Ondina",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sales'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
