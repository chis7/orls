# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsManualRemovalOfRetainedPlacentaLogLines(models.Model):
    _name = "orls.obs.manual.removal.of.retained.placenta.log.lines"
    _description = "Orls Obs Manual Removal Of Retained Placenta Log Lines"

    orls_manual_removal_of_retained_placenta_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Manual removal of retained placenta 2(a) and 2(p)"
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

