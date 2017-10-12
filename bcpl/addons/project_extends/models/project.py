# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml import etree

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval




class Task(models.Model):
    _inherit = "project.task"



    task_type = fields.Selection([('scheduled', 'Scheduled'),('adhoc', 'Ad-Hoc'),('selfgenerated', 'Self-Generated')], string='Type')
