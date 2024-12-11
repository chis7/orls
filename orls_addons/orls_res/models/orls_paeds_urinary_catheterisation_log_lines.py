# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsUrinaryCatheterisationLogLines(models.Model):
    _name = "orls.paeds.urinary.catherterisation.log.lines"
    _description = "Orls Paeds Urinary Catheterisation Log Lines"

    orls_paeds_urinary_catheterisation_log_id = fields.Many2one(
        'orls.paeds.resident.log',
        string="Urinary Catheterisation 5(a)"
    )
    u_c_number_of_cases = fields.Char(string="# of Cases", store=True)
    u_c_file_no = fields.Char(string="File No.", store=True)
    u_c_date = fields.Date(string="Date", store=True)
    u_c_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
