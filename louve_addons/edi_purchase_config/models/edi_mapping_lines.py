# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: Druidoo (<http://www.druidoo.io/>)
# @author: Druidoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html

from openerp import models, api, fields


class EdiMappingLines(models.Model):
    _name = 'edi.mapping.lines'
    _order = 'position'

    config_id = fields.Many2one(comodel_name="edi.config.system")
    sequence = fields.Integer(string="Sequence", required=True, default=1)
    value = fields.Char(string="Value", help="Python code expression", required=True)
    position = fields.Integer(string="Position", required=True)
    delimiter = fields.Char(string="Delimiter", required=True)
    required_field = fields.Boolean(string="Required")
    size = fields.Integer(string="Size", required=True)
    decimal_precision = fields.Integer(string="Decimal precision")