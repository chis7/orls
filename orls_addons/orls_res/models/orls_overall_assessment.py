# -*- coding: utf-8 -*-
import base64
import csv
from datetime import date
from io import StringIO

from odoo import api, fields, models
from odoo.exceptions import UserError


class OrlsOverallAssessment(models.Model):
    _name = "orls.overall.assessment"
    _inherit = ["mail.thread"]
    _description = "Orls Overall Assessment"

    supervisor_comment = fields.Text(string="Supervisor Comment", tracking=True)
    supervisor_comment_date = fields.Date(string="Supervisor Comment Date", tracking=True)
    coordinator_comment = fields.Text(string="Coordinator Comment", tracking=True)
    coordinator_comment_date = fields.Date(string="Coordinator Comment Date", tracking=True)
    grading = fields.Selection(
        selection=[
            ("successful", "Successfully Completed Rotation"),
            ("unsuccessful", "Unsuccessful -(State Extension Period Recommended)")
        ],
        string="Status",
        tracking=True
    )
    overall_score = fields.Integer(string="Overall Score", tracking=True)
    orls_surgery_overall_assessment_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Overall Assessment"
    )


    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("coordinator", "Coordinator"),
        ],
        default='draft',
        string="Status",
        required=True,
        tracking=True
    )
    user_in_assigned_company_and_open_and_submitted = fields.Boolean(
        string="User in Assigned Company and Open and Submitted",
        compute="_compute_has_logged_in_user_company_submitted_record",
        store=True
    )
    lab_incharge_comment = fields.Char(string="Lab Incharge Comment", tracking=True)

    is_supervisor = fields.Boolean(compute='_compute_is_supervisor', store=False)

    csv_file = fields.Binary(string="CSV File")
    csv_filename = fields.Char(string="CSV Filename")
    user_in_assigned_company_and_open = fields.Boolean(
        string="User in Assigned Company and Open",
        compute='_compute_user_in_assigned_company_and_open'
    )
    user_in_assigned_company_and_results_published = fields.Boolean(
        string="User in Assigned Company and Results Published",
        compute='_compute_user_in_assigned_company_and_results_published'
    )
    sample_id = fields.Char(string="Test Sample ID", store=True)
    date_tested = fields.Date(string="Date Tested", store=True)

    # company_count = fields.Integer(string='Company Count', compute='_compute_company_count', store=True)

    def validate_csv_file(self, csv_content):
        csv_reader = csv.reader(StringIO(csv_content))
        headers = next(csv_reader, None)
        if headers != ['Company Name']:
            raise UserError("Invalid CSV format. The header should be 'Company Name'.")

        for row in csv_reader:
            if len(row) != 1:
                raise UserError("Invalid CSV format. Each row should have exactly one column.")
            if not row[0].strip():
                raise UserError("Invalid CSV format. Company name cannot be empty.")
    def action_submit_overall_assessment(self):
        pass
    def action_test_upload(self):
        if not self.csv_file:
            raise UserError("Please upload a CSV file first.")

        csv_content = base64.b64decode(self.csv_file).decode('utf-8')
        self.validate_csv_file(csv_content)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'CSV Validation',
                'message': 'The CSV file is valid.',
                'type': 'success',
                'sticky': False,
            }
        }

    # @api.depends('company_ids')
    # def _compute_company_count(self):
    #     for record in self:
    #         record.company_count = len(record.company_ids)

    def _compute_has_logged_in_user_company_submitted_record(self):
        for record in self:
            user_company = self.env.user.company_id
            record.user_in_assigned_company_and_open_and_submitted = (
                    user_company in record.company_ids and
                    record.state == 'open' and
                    self.env['zaneqas.tb.xpert.eqa.result'].search_count([
                        ('company_id', '=', user_company.id),
                        ('name', '=', record.name.id)
                    ]) > 0
            )

    def _compute_user_in_assigned_company_and_open(self):
        for record in self:
            user_company = self.env.user.company_id
            record.user_in_assigned_company_and_open = user_company in record.company_ids and record.state == 'open'

    def _compute_user_in_assigned_company_and_results_published(self):
        for record in self:
            user_company = self.env.user.company_id
            record.user_in_assigned_company_and_results_published = user_company in record.company_ids and record.state == 'resultsPublished'

    def download_csv_template(self):
        csv_content = StringIO()
        csv_writer = csv.writer(csv_content)
        csv_writer.writerow(['Company Name'])  # Add more headers if needed

        # Fetch all companies and write to CSV
        companies = self.env['res.company'].search([])
        for company in companies:
            csv_writer.writerow([company.name])

        csv_data = base64.b64encode(csv_content.getvalue().encode('utf-8'))
        csv_content.close()

        attachment = self.env['ir.attachment'].create({
            'name': 'company_template.csv',
            'datas': csv_data,
            'type': 'binary',
            'res_model': self._name,
            'res_id': self.id,
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }

    def import_companies_from_csv(self):
        if not self.csv_file:
            raise UserError("Please upload a CSV file first.")

        csv_content = base64.b64decode(self.csv_file).decode('utf-8')
        csv_reader = csv.reader(StringIO(csv_content))
        next(csv_reader)  # Skip headers
        company_ids = []
        for row in csv_reader:
            company_name = row[0]
            company = self.env['res.company'].search([('name', '=', company_name)], limit=1)
            if company:
                company_ids.append(company.id)
            else:
                raise UserError(f"Company '{company_name}' not found.")
        self.company_ids = [(6, 0, company_ids)]

    @api.depends('state')
    def _compute_current_state(self):
        for record in self:
            record.current_state = record.state

    @api.depends('create_uid')
    def _compute_is_supervisor(self):
        for record in self:
            record.is_supervisor = self.env.user == record.create_uid.parent_id and record.state == 'supervisor'

    @api.depends('create_uid')
    def _compute_is_labIncharge(self):
        for record in self:
            record.is_LabIncharge = self.env.user == record.create_uid.parent_id.parent_id and record.state == 'lab_incharge'

    def action_save_eqa_result_as_draft(self):
        self.write({'state': 'draft'})

    def action_submit_eqa_result_to_supervisor(self):
        self.write({'state': 'supervisor'})

    def action_supervisor_approve_eqa_result(self):
        self.write({'state': 'lab_incharge'})

    def action_supervisor_send_back_eqa_result(self):
        self.write({'state': 'draft'})

    def action_LabIncharge_send_back_eqa_result(self):
        self.write({'state': 'lab_incharge'})

    def action_LabIncharge_approve_eqa_result(self):
        self.write({'state': 'approved'})

    def action_open_eqa_result(self):
        self.write({'state': 'open'})
        self.action_send_email_to_companies()

    def action_extend_eqa_result(self):
        self.write({'state': 'extended'})

    def action_close_eqa_result(self):
        self.write({'state': 'closed'})

    def action_publish_results(self):
        self.write({'state': 'resultsPublished'})

    def action_send_email_to_companies(self):
        for company in self.company_ids:
            if company.email:
                mail_values = {
                    'subject': 'Notification of TB Gene Xpert EQA',
                    'body_html': """<p>Dear {company_name},</p>
                                    <p>Please be informed that you have been selected to participate in the TB Gene Xpert EQA.</p>
                                    <p>Thank you.</p>""".format(company_name=company.name),
                    'email_to': company.email,
                }
                mail = self.env['mail.mail'].create(mail_values)
                mail.send()
