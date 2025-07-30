# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsIntMedBoneMarrowAspirateLogLines(models.Model):
    _name = "orls.intmed.bone.marrow.aspirate.log.lines"
    _description = "Orls Internal Medicine Bone Marrow Aspirate Log Lines"

    orls_intmed_bone_marrow_aspirate_log_id = fields.Many2one(
        'orls.gyn.resident.log',
        string="Bone marrow aspirate 2(a)"
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

