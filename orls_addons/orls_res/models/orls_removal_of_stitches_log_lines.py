# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsRemovalOfStitchesLogLines(models.Model):
    _name = "orls.removal.of.stitches.log.lines"
    _description = "Orls Removal of Stitches Log Lines"

    orls_removal_of_stitches_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Removal of stitches 10(p)"
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

