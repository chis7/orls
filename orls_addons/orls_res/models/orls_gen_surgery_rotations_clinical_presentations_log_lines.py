# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsGenSurgeryRotationClinicalPresentationsLogLines(models.Model):
    _name = "orls.gen.surgery.rotation.cl.pres.log.lines"
    _description = "Orls General Surgery Rotation Clinical Presentations Log Lines"

    orls_operation_clinical_presentation_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Clinical Presentations Made"
    )
    c_a_date = fields.Date(string="Date", store=True)
    c_a_topic = fields.Char(string="Topic", store=True)
    c_a_venue = fields.Char(string="Venue", store=True)
    c_a_consultant_id = fields.Many2one('res.employee', string="Consultant")