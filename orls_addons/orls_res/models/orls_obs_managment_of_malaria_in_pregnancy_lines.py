# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsManagementOfMalariaInPregnancyLines(models.Model):
    _name = "orls.obs.management.of.malaria.in.pregnancy.lines"
    _description = "Orls Obs Management Of Malaria In Pregnancy Lines"

    orls_management_of_malaria_in_pregnancy_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="management of Malaria in pregnancy 3(P)"
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

