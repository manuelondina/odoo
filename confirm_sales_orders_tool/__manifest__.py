# -*- coding: utf-8 -*-
{
    'name': "Herramienta de importacion de pedidos en CSV o Excel",

    'summary': """
        Herramienta Herramienta de importacion de pedidos en CSV o Excel.
        """,

    'description': """
        Herramienta que se encarga de importar pedidos que vienen con una sola columna donde contiene el nombre del pedido,
        este pedido sera agregado y luego confirmado automaticamente. Esta funcionalidad se encontrara en:
        Ventas → Pedidos → Arriba de presupuestos.
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
        'views/confirm_sales_orders_menu.xml',
        'views/confirm_sales_orders_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
