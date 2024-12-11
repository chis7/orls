# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsNgTubeInsertionLogLines(models.Model):
    _name = "orls.paeds.ng.tube.insertion.log.lines"
    _description = "Orls Paeds NG Tube Insertion Log Lines"

    orls_paeds_ng_tube_insertion_log_id = fields.Many2one(
        'orls.paeds.resident.log',
        string="NG Tube insertion (NBU) 10(p)"
    )
    n_g_number_of_cases = fields.Char(string="# of Cases", store=True)
    n_g_file_no = fields.Char(string="File No.", store=True)
    n_g_date = fields.Date(string="Date", store=True)
    n_g_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

