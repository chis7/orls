# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsIncisionDrainageAbscessLogLines(models.Model):
    _name = "orls.incision.drainage.abscess.log.lines"
    _description = "Orls Incision Drainage Abscess Log Lines"

    orls_incision_drainage_abscess_log_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Incision and drainage of Abscess 1 (O) 2(p)"
    )
    number_of_cases = fields.Char(string="# of Cases", store=True)
    file_no = fields.Char(string="File No.", store=True)
    date = fields.Date(string="Date", store=True)
    resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

