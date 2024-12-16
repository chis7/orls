# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsManagementOfAnemiaInPregnancyLogLines(models.Model):
    _name = "orls.obs.management.of.anemia.in.pregnancy.log.lines"
    _description = "Orls Obs Management Of Anemia In Pregnancy Log Lines"

    orls_management_of_anemia_in_pregnancy_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="management of anemia in pregnancy 3(P)"
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

