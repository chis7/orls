# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGynViaViliLines(models.Model):
    _name = "orls.gyn.via.and.vili.lines"
    _description = "Orls Gyn VIA (visual inspection with acetic acid) and VILI (visual inspection using Lugol's iodine) Lines"

    orls_gyn_via_and_vili_main_id = fields.Many2one(
        'orls.gyn.rotation.procedures',
        string="VIA (visual inspection with acetic acid) and VILI (visual inspection using Lugol's iodine) 5(p)"
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

