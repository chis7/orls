# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError, AccessError
import random


class OrlsSuturingWoundLogLines(models.Model):
    _name = "orls.suturing.wound.log.lines"
    _description = "Orls Suturing Wound Log Lines"

    orls_suturing_wound_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Suturing Wound"
    )
    s_w_number_of_cases = fields.Char(string="# of Cases", store=True)
    s_w_file_no = fields.Char(string="File No.", store=True)
    s_w_date = fields.Date(string="Date", store=True)
    s_w_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    s_w_supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
    s_w_checkbox_field = fields.Boolean(string='Supervisor Check')
    s_w_sign_off_date = fields.Date(string="Sign-off Date", store=True)

    @api.model
    def create(self, vals):
        if vals.get('s_w_checkbox_field'):
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.parent_id.id if create_user.parent_id else False
            vals['s_w_supervisor_id'] = supervisor_id
            vals['s_w_sign_off_date'] = date.today()
        return super(OrlsSuturingWoundLogLines, self).create(vals)

    def write(self, vals):
        if 's_w_checkbox_field' in vals:
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.employee_id.parent_id.id if create_user.employee_id.parent_id else False
            if not supervisor_id:
                raise AccessError("You are not allowed to modify this record.")
            vals['s_w_supervisor_id'] = supervisor_id
            vals['s_w_sign_off_date'] = date.today() if vals['s_w_checkbox_field'] else False
        return super(OrlsSuturingWoundLogLines, self).write(vals)

