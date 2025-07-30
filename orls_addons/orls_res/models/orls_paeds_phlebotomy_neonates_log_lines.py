# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsPhlebotomyNeonatesLogLines(models.Model):
    _name = "orls.paeds.phlebotomy.neonates.log.lines"
    _description = "Orls Paeds Phlebotomy Neonates Log Lines"

    orls_paeds_phlebotomy_neonates_log_id = fields.Many2one(
        'orls.paeds.resident.log',
        string="Phlebotomy in neonates(5p)"
    )
    p_n_number_of_cases = fields.Char(string="# of Cases", store=True)
    p_n_file_no = fields.Char(string="File No.", store=True)
    p_n_date = fields.Date(string="Date", store=True)
    p_n_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
