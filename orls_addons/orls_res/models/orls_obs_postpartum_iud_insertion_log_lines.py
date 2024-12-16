# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsPostPartumIudInsertionLogLines(models.Model):
    _name = "orls.obs.postpartum.iud.insertion.log.lines"
    _description = "Orls Obs Postpartum Family Planning IUD Insertion Log Lines"

    orls_obs_postpartum_iud_insertion_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Postpartum family planning: PP- IUD Insertion"
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

