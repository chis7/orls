# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError, AccessError
import random


class OrlsIncisionDrainageAbscessLogLines(models.Model):
    _name = "orls.incision.drainage.abscess.log.lines"
    _description = "Orls Incision Drainage Abscess Log Lines"

    orls_incision_drainage_abscess_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Incision and drainage of Abscess 1 (O) 2(p)"
    )
    a_d_number_of_cases = fields.Char(string="# of Cases", store=True)
    a_d_file_no = fields.Char(string="File No.", store=True)
    a_d_date = fields.Date(string="Date", store=True)
    a_d_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    a_d_supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
    a_d_checkbox_field = fields.Boolean(string='Supervisor Check')
    a_d_sign_off_date = fields.Date(string="Sign-off Date", store=True)

    @api.model
    def create(self, vals):
        if vals.get('a_d_checkbox_field'):
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.parent_id.id if create_user.parent_id else False
            vals['a_d_supervisor_id'] = supervisor_id
            vals['a_d_sign_off_date'] = date.today()
        return super(OrlsIncisionDrainageAbscessLogLines, self).create(vals)

    def write(self, vals):
        if 'a_d_checkbox_field' in vals:
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.employee_id.parent_id.id if create_user.employee_id.parent_id else False
            if not supervisor_id:
                raise AccessError("You are not allowed to modify this record.")
            vals['a_d_supervisor_id'] = supervisor_id
            vals['a_d_sign_off_date'] = date.today() if vals['a_d_checkbox_field'] else False
        return super(OrlsIncisionDrainageAbscessLogLines, self).write(vals)

