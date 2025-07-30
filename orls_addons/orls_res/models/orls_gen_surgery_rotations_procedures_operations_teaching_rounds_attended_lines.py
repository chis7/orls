# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGenSurgeryRotationProceduresOperationsMonthlyPerformanceReviewLines(models.Model):
    _name = "orls.gen.surgery.rotation.teaching.rounds.attended.lines"
    _description = "Orls Gen Surgery Teaching Rounds Attended Lines"

    orls_operation_clinical_teaching_rounds_main_id = fields.Many2one(
        'orls.gen.surgery.rotation.procedures.operations',
        string="Teaching Rounds Attended"
    )
    date = fields.Date(string="Date", store=True)
    ward_round = fields.Char(string="Ward Round", store=True)
    venue = fields.Char(string="Venue", store=True)
    consultant_id = fields.Many2one('res.employee', string="Consultant/Supervisor")