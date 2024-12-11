# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsLumbarPunctureLines(models.Model):
    _name = "orls.paeds.lumbar.puncture.lines"
    _description = "Orls Paeds Lumbar Puncture Lines"

    orls_paeds_lumbar_puncture_main_id = fields.Many2one(
        'orls.paeds.rotation.procedures',
        string="Lumbar puncture 3(p)"
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

