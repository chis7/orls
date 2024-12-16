# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsRepairOfPerinealTearsLines(models.Model):
    _name = "orls.obs.repair.of.perineal.tears.lines"
    _description = "Orls Obs Repair Of Perineal Tears Lines"

    orls_repair_of_perineal_tears_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Repair of perineal tears 5(p)"
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

