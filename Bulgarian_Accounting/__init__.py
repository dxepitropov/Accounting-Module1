# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def load_translations(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref('l10n_bg.l10nbg_chart_template').process_coa_translations()
