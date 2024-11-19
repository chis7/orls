
# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGenSurgeryRotationTeachingRoundsAttendedLines(models.Model):
    _name = "orls.gen.surgery.teaching.rounds.attended.log.lines"
    _description = "Orls Gen Surgery Teaching Rounds Attended Lines"

    orls_operation_clinical_teaching_rounds_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Teaching Rounds Attended"
    )
    t_r_date = fields.Date(string="Date", store=True)
    t_r_ward_round = fields.Char(string="Ward Round", store=True)
    t_r_venue = fields.Char(string="Venue", store=True)
    t_r_consultant_id = fields.Many2one('res.employee', string="Consultant/Supervisor")