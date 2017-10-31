# -*- coding: utf-8 -*-
# Copyright (c) 2017 dXFactory OOD http://dxfactory.eu
{
    'name': 'Bulgarian - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
    This is the base module to load a reference Bi-Lingual (BG-EN) Chart of Accounts & VAT sets for Bulgaria in Odoo.
    This is the initial version and the module will be further extended in the upcoming month which will include separating Bulgarian from English translations""",
    'author': 'dxFactory OOD',
    'depends': ['account'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/l10n_bg_chart_data.xml',
        'data/fiscal_templates_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_data.yml'
    ],
    'website': 'https://dxfactory.eu',
}
