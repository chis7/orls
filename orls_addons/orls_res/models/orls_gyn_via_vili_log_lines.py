# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGynViaViliLogLines(models.Model):
    _name = "orls.gyn.via.and.vili.log.lines"
    _description = "Orls Gyn VIA (visual inspection with acetic acid) and VILI (visual inspection using Lugol's iodine) Log Lines"

    orls_gyn_via_and_vili_log_id = fields.Many2one(
        'orls.gyn.resident.log',
        string="VIA (visual inspection with acetic acid) and VILI (visual inspection using Lugol's iodine) 5(p)"
    )
    a_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    a_t_file_no = fields.Char(string="File No.", store=True)
    a_t_date = fields.Date(string="Date", store=True)
    a_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

