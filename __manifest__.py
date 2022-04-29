# -*- coding: utf-8 -*-
{
    'name': 'add_inquiryLlist',
    'category': 'add_inquiryLlist',
    'description': """
            add_inquiryLlist
            """,
    'author': 'CodeFire Technologies',
    'website': 'https://www.codefire.org/',
    'version': '14.0.1.1',
    'license': 'AGPL-3',
    'images': ['static/description/odoo-free.jpg'],
    'depends': [
        'purchase',
    ],
    "data": [
        "views/sale_enquiry.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
