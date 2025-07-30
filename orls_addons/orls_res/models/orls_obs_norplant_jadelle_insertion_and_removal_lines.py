# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsNorplantJadelleInsertionAndRemovalnLines(models.Model):
    _name = "orls.obs.norplant.jadelle.insertion.and.removal.lines"
    _description = "Orls Obs Norplant/Jadelle insertion and Removal Lines"

    orls_norplant_jadelle_insertion_and_removal_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Norplant/Jadelle insertion and Removal 5(a) and 5(p)"
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

