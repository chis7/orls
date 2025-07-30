# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsIUCDInsertionRemovalLogLines(models.Model):
    _name = "orls.obs.iucd.insertion.removal.log.lines"
    _description = "Orls Obs IUCD insertion/removal Log Lines"

    orls_iucd_insertion_removal_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="IUCD insertion/removal 5(a) and 5(p)"
    )
    a_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    a_t_file_no = fields.Char(string="File No.", store=True)
    a_t_date = fields.Date(string="Date", store=True)
    a_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

