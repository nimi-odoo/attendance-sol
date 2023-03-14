# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    attendance_ids = fields.One2many(
        'hr.attendance', 'sale_order_line_id') #, groups="hr_attendance.group_hr_attendance_user"
    last_attendance_id = fields.Many2one(
        'hr.attendance', compute='_compute_last_attendance_id', store=True,
        groups="hr_attendance.group_hr_attendance_kiosk,hr_attendance.group_hr_attendance")
    attendance_state = fields.Selection(
        string="Attendance Status", compute='_compute_attendance_state',
        selection=[('checked_out', "Checked out"), ('checked_in', "Checked in")],
        groups="hr_attendance.group_hr_attendance_kiosk,hr_attendance.group_hr_attendance")
    
    @api.depends('last_attendance_id.check_in', 'last_attendance_id.check_out', 'last_attendance_id')
    def _compute_attendance_state(self):
        for sol in self:
            att = sol.last_attendance_id.sudo()
            sol.attendance_state = att and not att.check_out and 'checked_in' or 'checked_out'

    @api.depends('attendance_ids')
    def _compute_last_attendance_id(self):
        for employee in self:
            employee.last_attendance_id = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id),
            ], limit=1)

    def action_sol_kiosk_confirm(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'name': 'Confirm',
            'tag': 'hr_attendance_kiosk_confirm',
            'sale_order_line_id': self.id,
            'sol_name': self.name,
            'sol_state': self.attendance_state,
            # 'employee_hours_today': self.hours_today,
            'employee_id': self.env.user.employee_id.id,
            'employee_name': self.name,
            'employee_state': self.attendance_state
        }
    