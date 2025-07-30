# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsMcDonaldStitchRemovalLogLines(models.Model):
    _name = "orls.obs.mcdonald.stitch.removal.log.lines"
    _description = "Orls Obs McDonald Stitch Removal Log Lines"

    orls_obs_mcdonald_stitch_removal_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="McDonald Stitch removal 3(a) and 2(p)*"
    )
    m_s_number_of_cases = fields.Char(string="# of Cases", store=True)
    m_s_file_no = fields.Char(string="File No.", store=True)
    m_s_date = fields.Date(string="Date", store=True)
    m_s_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

