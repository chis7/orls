# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsInsertionChestTubeLogLines(models.Model):
    _name = "orls.insertion.chest.tubes.log.lines"
    _description = "Orls Insertion Chest Tubes Log Lines"

    orls_insertion_chest_tubes_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Insertion of chest tubes 3(p)"
    )
    c_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    c_t_file_no = fields.Char(string="File No.", store=True)
    c_t_date = fields.Date(string="Date", store=True)
    c_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")

