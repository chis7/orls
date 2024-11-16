# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGenSurgeryRotationProceduresOperationsMonthlyPerformanceReviewLines(models.Model):
    _name = "orls.gen.surgery.rotation.procedures.operations.cl.pres.lines"
    _description = "Orls Gen Surgery Clinical Presentations Lines"

    orls_operation_clinical_presentation_main_id = fields.Many2one(
        'orls.gen.surgery.rotation.procedures.operations',
        string="Clinical Presentations Made"
    )
    date = fields.Date(string="Date", store=True)
    topic = fields.Char(string="Topic", store=True)
    venue = fields.Char(string="Venue", store=True)
    consultant_id = fields.Many2one('res.employee', string="Consultant")