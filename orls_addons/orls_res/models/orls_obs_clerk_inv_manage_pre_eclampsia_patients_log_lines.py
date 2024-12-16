# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsClerkInvestigateManagePreEclampsiaPatientsLogLines(models.Model):
    _name = "orls.obs.clerk.inv.manage.pre.eclampsia.patients.log.lines"
    _description = "Orls Obs Clerk Investigate and Manage Patients WIth Pre-Eclampsia Log Lines"

    orls_obs_clerk_inv_manage_pre_eclampsia_patients_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Be able to clerk, investigate and manage patients with pre-eclampsia 3(a) and 5(p)"
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
