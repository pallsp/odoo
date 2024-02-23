# -*- coding: utf-8 -*-
{
    'name': "Gestión Eventos",

    'summary': """
       Módulo para la gestión de eventos de empresas.""",

    'description': """
        Módulo para la gestión y visualización de eventos. Nos permitirá conocer qué eventos tiene nuestra empresa y cúando son, establecer relaciones con el coordinador y los espacios
        que utilice, así como su organización y su aforo.
    """,

    'author': "Pablo Pallas",
    'website': "http://www.gestioeventospallas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '1.2',

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
}
