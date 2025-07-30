# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsInvestigateAndManagePregnantPatientsWithCardiacDiseaseLines(models.Model):
    _name = "orls.obs.inv.manage.preg.pat.with.cardiac.lines"
    _description = "Orls Obs Investigate And Manage Pregnant Patients With Cardiac Disease Lines"

    orls_obs_inv_and_manage_preg_pats_with_cardiac_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Investigate & manage pregnant patients with cardiac disease 2(p)"
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

