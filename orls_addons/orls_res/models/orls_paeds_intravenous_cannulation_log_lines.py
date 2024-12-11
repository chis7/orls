# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsIntravenousLogLines(models.Model):
    _name = "orls.paeds.intravenous.cannulation.log.lines"
    _description = "Orls Paeds Intravenous Cannulation Log Lines"

    orls_paeds_intravenous_cannulation_log_id = fields.Many2one(
        'orls.paeds.resident.log',
        string="Intravenous Cannulation 1(p)"
    )
    i_v_number_of_cases = fields.Char(string="# of Cases", store=True)
    i_v_file_no = fields.Char(string="File No.", store=True)
    i_v_date = fields.Date(string="Date", store=True)
    i_v_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

