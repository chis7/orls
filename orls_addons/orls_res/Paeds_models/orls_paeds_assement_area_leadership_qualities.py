# -*- coding: utf-8 -*-
from datetime import datetime, date

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
import random


class OrlsAssessmentAreaLeadershipQualities(models.Model):
    _name = "orls.overall.assessment.area.leadership.qualities.lines"
    _inherit = ["mail.thread"]
    _description = "Orls Assessment Area Leadership Qualities"

    name = fields.Selection(selection=[
        ("takesInitiative", "Takes initiative"),
        ("knowledgeAndAdherenceToInstitutionalPoliciesAndRegulations", "Knowledge and adherence to institutional policies and regulations"),
        ("mentorshipOfJuniorsAndOtherProfessionals", "Mentorship of juniors and other professionals")
    ], string="Leadership Qualities")
    grade = fields.Selection(selection=[
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3")
    ], string="Grade", required=True)
    remarks = fields.Text(string="Remarks", tracking=True)
    # orls_overall_grading_assessment_area_leadership_qualities_lines_id = fields.Many2one(
    #     'orls.overall.assessment',
    #     string="Leadership Qualities"
    # )

    def action_save_eqa_config_round_as_draft(self):

        self.write({
            'state': 'draft'
        })

    def action_submit_eqa_config_round_to_supervisor(self):
        self.write({'state': 'supervisor'})
        group = self.env.ref("zaneqas_tb.group_cdl_supervisor_approve_site_eqa_expected_results")
        users = group.users

        if users:
            selected_user = random.choice(users)
            self.supervisor_id = selected_user.id
            if selected_user.email:
                mail_values = {
                    'subject': 'Request for Approval',
                    'body_html': """<p>You have received a request for approval of a configuration. Click <a href='http://localhost:8069'>here</a> to log in and access the request.</p>""",
                    'email_to': selected_user.email,
                }
                mail = self.env['mail.mail'].create(mail_values)
                mail.send()

    def action_supervisor_approve_eqa_config_round(self):
        if self.env.user != self.supervisor_id:
            raise models.ValidationError("You are not authorized to approve this EQA configuration round.")
        user = self.create_uid.email
        if user:
            mail_values = {
                'subject': 'Your Request for Approval',
                'body_html': """<p>Your configuration has been approved. Click <a href='http://localhost:8069'>here</a> to log in and check the status.</p>""",
                'email_to': user,
            }
            mail = self.env['mail.mail'].create(mail_values)
            mail.send()

    def action_supervisor_send_back_eqa_config_round(self):
        self.write({'state': 'draft'})
        user = self.create_uid.email
        if user:
            mail_values = {
                'subject': 'Your Request for Approval',
                'body_html': """<p>Your configuration has been sent back for your review. Click <a href='http://localhost:8069'>here</a> to log in and check the status.</p>""",
                'email_to': user,
            }
            mail = self.env['mail.mail'].create(mail_values)
            mail.send()
