# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    sale_order_line_id = fields.Many2one('sale.order.line', string="Sale Order Line", required=True, ondelete='cascade', index=True)

