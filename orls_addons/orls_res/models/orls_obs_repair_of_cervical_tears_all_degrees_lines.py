# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsRepairOfCervicalTearsAllDegreesLines(models.Model):
    _name = "orls.obs.repair.of.cervical.tears.all.degrees.lines"
    _description = "Orls Obs Repair Of Cervical Tears All Degrees Lines"

    orls_repair_of_cervical_tears_all_degrees_main_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string="Repair of cervical tears all degrees 2(a),2(p)"
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

