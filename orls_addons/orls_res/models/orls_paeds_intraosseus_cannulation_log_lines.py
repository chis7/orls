# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsExchangeTransfusionLogLines(models.Model):
    _name = "orls.paeds.intraosseus.cannulation.log.lines"
    _description = "Orls Paeds Intraosseus Cannulation Log Lines"

    orls_paeds_intraosseus_cannulation_log_id = fields.Many2one(
        'orls.paeds.resident.log',
        string="Intraosseus Cannulation 1(p)"
    )
    i_o_number_of_cases = fields.Char(string="# of Cases", store=True)
    i_o_file_no = fields.Char(string="File No.", store=True)
    i_o_date = fields.Date(string="Date", store=True)
    i_o_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

