# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError, AccessError
import random


class OrlsRemovalOfStitchesLogLines(models.Model):
    _name = "orls.removal.of.stitches.log.lines"
    _description = "Orls Removal of Stitches Log Lines"

    orls_removal_of_stitches_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Removal of stitches 10(p)"
    )
    r_s_number_of_cases = fields.Char(string="# of Cases", store=True)
    r_s_file_no = fields.Char(string="File No.", store=True)
    r_s_date = fields.Date(string="Date", store=True)
    r_s_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    r_s_supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
    r_s_checkbox_field = fields.Boolean(string='Supervisor Check')
    r_s_sign_off_date = fields.Date(string="Sign-off Date", store=True)

    @api.model
    def create(self, vals):
        if vals.get('r_s_checkbox_field'):
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.parent_id.id if create_user.parent_id else False
            vals['r_s_supervisor_id'] = supervisor_id
            vals['r_s_sign_off_date'] = date.today()
        return super(OrlsRemovalOfStitchesLogLines, self).create(vals)

    def write(self, vals):
        if 'r_s_checkbox_field' in vals:
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.employee_id.parent_id.id if create_user.employee_id.parent_id else False
            if not supervisor_id:
                raise AccessError("You are not allowed to modify this record.")
            vals['r_s_supervisor_id'] = supervisor_id
            vals['r_s_sign_off_date'] = date.today() if vals['r_s_checkbox_field'] else False
        return super(OrlsRemovalOfStitchesLogLines, self).write(vals)

