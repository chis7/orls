# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsVacuumLogLines(models.Model):
    _name = "orls.obs.vacuum.log.lines"
    _description = "Orls Obs Vacuum Delivery Log Lines"

    orls_obs_vacuum_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Delivery by Vacuum Section10(p)"
    )
    v_d_number_of_cases = fields.Char(string="# of Cases", store=True)
    v_d_file_no = fields.Char(string="File No.", store=True)
    v_d_date = fields.Date(string="Date", store=True)
    v_d_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

