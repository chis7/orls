# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsClerkInvestigateAndManagePatientsWithHIVInPregnancyLines(models.Model):
    _name = "orls.obs.clerk.inv.manage.pats.with.hiv.in.preg.lines"
    _description = "Orls Obs Clerk Investigate And MAnage Patients With HIV In Pregnancy Lines"

    orls_obs_clerk_investigate_manage_patients_with_hiv_in_pregnancy_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Be able to clerk, investigate and manage patients with HIV in pregnancy 5(p)(EMTCT)"
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

