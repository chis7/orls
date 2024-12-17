# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGynTubalLigationSurgeryLogLines(models.Model):
    _name = "orls.gyn.tubal.ligation.surgery.log.lines"
    _description = "Orls Gyn Tubal Ligation Surgery Log Lines"

    orls_gyn_tubal_ligation_surgery_log_id = fields.Many2one(
        'orls.gyn.resident.log',
        string="Tubal ligation surgery 3(a/p)"
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

