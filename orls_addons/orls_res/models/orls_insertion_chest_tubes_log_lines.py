# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError, AccessError
import random


class OrlsInsertionChestTubeLogLines(models.Model):
    _name = "orls.insertion.chest.tubes.log.lines"
    _description = "Orls Insertion Chest Tubes Log Lines"

    orls_insertion_chest_tubes_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Insertion of chest tubes 3(p)"
    )
    c_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    c_t_file_no = fields.Char(string="File No.", store=True)
    c_t_date = fields.Date(string="Date", store=True)
    c_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
    c_t_checkbox_field = fields.Boolean(string='Supervisor Check')
    c_t_supervisor_id = fields.Many2one('res.users', string="Supervisor's Name")
    c_t_sign_off_date = fields.Date(string="Sign-off Date", store=True)

    @api.model
    def create(self, vals):
        if vals.get('c_t_checkbox_field'):
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.parent_id.id if create_user.parent_id else False
            vals['s_t_supervisor_id'] = supervisor_id
            vals['sc_t_sign_off_date'] = date.today()
        return super(OrlsInsertionChestTubeLogLines, self).create(vals)

    def write(self, vals):
        if 's_t_checkbox_field' in vals:
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.employee_id.parent_id.id if create_user.employee_id.parent_id else False
            if not supervisor_id:
                raise AccessError("You are not allowed to modify this record.")
            vals['c_t_supervisor_id'] = supervisor_id
            vals['c_t_sign_off_date'] = date.today() if vals['c_t_checkbox_field'] else False
        return super(OrlsInsertionChestTubeLogLines, self).write(vals)

