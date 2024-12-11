# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsExchangeTransfusionLogLines(models.Model):
    _name = "orls.paeds.exchange.transfusion.log.lines"
    _description = "Orls Paeds Exchange Transfusion Log Lines"

    orls_paeds_exchange_transfusion_log_id = fields.Many2one(
        'orls.paeds.resident.log',
        string="Exchange Transfusion 2(p)*"
    )
    e_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    e_t_file_no = fields.Char(string="File No.", store=True)
    e_t_date = fields.Date(string="Date", store=True)
    e_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

