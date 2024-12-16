# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsClerkInvestigateManageEclampsiaPatientsLines(models.Model):
    _name = "orls.obs.clerk.inv.manage.eclampsia.patients.lines"
    _description = "Orls Obs Clerk Investigate and Manage Patients With PEclampsia Lines"

    orls_clerk_inv_manage_eclampsia_patients_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Be able to clerk, investigate and manage patients with eclampsia 2(p)"
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

