# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsPaedsExchangeTransfusionLines(models.Model):
    _name = "orls.paeds.exchange.transfusion.lines"
    _description = "Orls Paeds Exchange Transfusion Lines"

    orls_paeds_exchange_transfusion_main_id = fields.Many2one(
        'orls.paeds.rotation.procedures',
        string="Exchange Transfusion 2(p)*"
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

