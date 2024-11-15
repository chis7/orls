# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGenSurgeryRotationClinicalPresentationsLogLines(models.Model):
    _name = "orls.gen.surgery.rotation.cl.pres.log.lines"
    _description = "Orls General Surgery Rotation Clinical Presentations Log Lines"

    orls_operation_clinical_presentation_log_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Clinical Presentations Made"
    )
    date = fields.Date(string="Date", store=True)
    topic = fields.Char(string="Topic", store=True)
    venue = fields.Char(string="Venue", store=True)
    consultant_id = fields.Many2one('res.employee', string="Consultant")