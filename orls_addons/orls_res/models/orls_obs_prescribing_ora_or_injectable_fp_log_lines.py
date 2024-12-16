# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsPrescribingOralOrInjectableFPLogLines(models.Model):
    _name = "orls.obs.prescribing.ora.or.injectable.fp.log.lines"
    _description = "Orls Obs Prescribing oral or injectable FP Log Lines"

    orls_obs_prescribing_ora_or_injectable_fp_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Prescribing oral or injectable FP 5(P)"
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

