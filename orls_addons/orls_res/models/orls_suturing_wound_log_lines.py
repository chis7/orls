# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
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

