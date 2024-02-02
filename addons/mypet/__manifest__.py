# -*- coding: utf-8 -*-
{
    'name': "My pet - long.info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "long.info",
    'website': "https://long.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': ['security/ir.model.access.csv','views/my_pet_views.xml',],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}