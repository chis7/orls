# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsMcDonaldStitchRemovalLines(models.Model):
    _name = "orls.obs.mcdonald.stitch.removal.lines"
    _description = "Orls Obs McDonald Stitch Removal Lines"

    orls_mcdonald_stitch_removal_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="McDonald Stitch removal 3(a) and 2(p)"
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

