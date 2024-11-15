# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGenSurgeryRotationMonthlyPerformanceReviewLogLines(models.Model):
    _name = "orls.gen.surgery.monthly.perf.log.lines"
    _description = "Orls General Surgery Rotation Monthly Performance Review Log Lines"

    orls_operation_monthly_review_lines_log_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Monthly Performance Review"
    )

    month = fields.Selection(
        selection=[
            ("1", "ONE (1)"),
            ("2", "TWO (2)"),
            ("3", "THREE (3)"),
        ],
        string="Month",
        tracking=True
    )

    resident_comment = fields.Text(string="Resident's Comment", tracking=True)
    resident_comment_date = fields.Date(string="Resident's Comment Date", tracking=True)
    supervisor_comment = fields.Text(string="Supervisor's Comment", tracking=True)
    supervisor_comment_date = fields.Date(string="Supervisor's Comment Date", tracking=True)
    resident_coordinator_comment = fields.Text(string="Resident Coordinator's Comment", tracking=True)
    resident_coordinator_comment_date = fields.Date(string="Resident Coordinator's Comment Date", tracking=True)