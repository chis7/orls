# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGynVescicleVaginalFistulaRepairLines(models.Model):
    _name = "orls.gyn.vescicle.vag.fistula.repair.lines"
    _description = "Orls Gyn Vescicle Vaginal Fistula Repair Lines"

    orls_gyn_vescicle_vaginal_fistula_repair_main_id = fields.Many2one(
        'orls.gyn.rotation.procedures',
        string="Vescicle Vaginal Fistula repair 1(a)"
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

