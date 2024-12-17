# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGynTubalLigationSurgeryLines(models.Model):
    _name = "orls.gyn.tubal.ligation.surgery.lines"
    _description = "Orls Gyn Tubal Ligation Surgery Lines"

    orls_gyn_tubal_ligation_surgery_main_id = fields.Many2one(
        'orls.gyn.rotation.procedures',
        string="Tubal ligation surgery 3(a/p)"
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

