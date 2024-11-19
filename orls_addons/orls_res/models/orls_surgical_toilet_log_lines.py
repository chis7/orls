# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsSurgicalToiletLogLines(models.Model):
    _name = "orls.gen.surgical.toilet.log.lines"
    _description = "Orls Surgical Toilet Log Lines"

    orls_surgical_toilet_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Surgical Toilet"
    )
    s_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    s_t_file_no = fields.Char(string="File No.", store=True)
    s_t_date = fields.Date(string="Date", store=True)
    s_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    s_t_supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

