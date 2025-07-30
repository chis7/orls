# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsCounsellingOnFamilyPlanningLines(models.Model):
    _name = "orls.obs.counselling.family.planning.lines"
    _description = "Orls Obs Counselling On Family Planning Methods Lines"

    orls_counselling_on_family_planning_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Counselling clients on family planning methods 8(p)"
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

