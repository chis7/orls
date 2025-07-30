# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsObsMultipleDeliveryLogLines(models.Model):
    _name = "orls.obs.multiple.delivery.log.lines"
    _description = "Orls Obs Delivery Of Multiple Pregnancies Log Lines"

    orls_obs_multiple_delivery_log_id = fields.Many2one(
        'orls.obs.resident.log',
        string="Delivery of multiple pregnancies 2(a) or 2(p)"
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

