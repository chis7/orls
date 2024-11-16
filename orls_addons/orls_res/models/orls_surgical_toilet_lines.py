# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsSurgicalToiletLines(models.Model):
    _name = "orls.gen.surgical.toilet.lines"
    _description = "Orls Surgical Toilet Lines"

    orls_surgical_toilet_main_id = fields.Many2one(
        'orls.gen.surgery.rotation.procedures.operations',
        string="Surgical Toilet"
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

