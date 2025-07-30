# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsClerkInvestigateAndManagePatientsWithHIVInPregnancyLogLines(models.Model):
    _name = "orls.obs.clerk.inv.manage.pats.with.hiv.in.preg.log.lines"
    _description = "Orls Obs Clerk Investigate And MAnage Patients With HIV In Pregnancy Log Lines"

    orls_obs_clerk_inv_manage_pats_with_hiv_in_preg_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Be able to clerk, investigate and manage patients with HIV in pregnancy 5(p)(EMTCT)"
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

