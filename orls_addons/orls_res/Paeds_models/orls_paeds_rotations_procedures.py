# -*- coding: utf-8 -*-
import base64
import csv
from datetime import date
from io import StringIO

from odoo import api, fields, models
from odoo.exceptions import UserError


class OrlsPaedsRotationProcedures(models.Model):
    _name = "orls.paeds.rotation.procedures"
    _inherit = ["mail.thread"]
    _description = "Orls Paeds Rotation Procedures"

    internship_center_id = fields.Many2one('res.company', string="Internship Center", required=True)
    hpcz_Reg_No = fields.Char(string="HPCZ Reg. No.", required=True)
    hpcz_license_No = fields.Char(string="HPCZ License No.", required=True)
    supervisor_id = fields.Many2one('res.employee', string="Supervisor's Name", )
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    name = fields.Many2one('orls.medical.disciplines', string="Discipline", required=True)
    user_in_assigned_rotation = fields.Boolean(
        string="User in Assigned Rotation",
        compute='_compute_user_in_assigned_rotation'
    )

    supervisor_comment = fields.Text(string="Supervisor Comment", tracking=True)
    pdf_file = fields.Binary(string="PDF File")
    pdf_filename = fields.Char(string="PDF Filename")

    disciplines = fields.Many2many(
        'orls.gen.surgery.discipline',
        string="Disciplines",
        required=True
    )
    notebook_pages_ids = fields.One2many(
        'orls.gen.surgery.notebook.page',
        'notebook_pages_id',
        string="Notebook Pages"
    )

    @api.onchange('disciplines')
    def _onchange_disciplines(self):
        self.notebook_pages = [(5, 0, 0)]  # Clear existing pages
        for discipline in self.disciplines:
            self.notebook_pages = [(0, 0, {
                'name': discipline.name,
                'discipline_id': discipline.id
            })]

    orls_ascitic_tap_main_ids = fields.One2many(
        'orls.paeds.ascitic.tap.lines',
        'orls_ascitic_tap_main_id',
        string="Ascitic Tap 2(p)"
    )

    orls_paeds_exchange_transfusion_main_ids = fields.One2many(
        'orls.paeds.exchange.transfusion.lines',
        'orls_paeds_exchange_transfusion_main_id',
        string="Exchange Transfusion  2(p)*"
    )

    orls_paeds_blood_transfusion_main_ids = fields.One2many(
        'orls.paeds.blood.transfusion.lines',
        'orls_paeds_blood_transfusion_main_id',
        string="Blood Transfusion 10(p)"
    )
    orls_paeds_urinary_catherterisation_main_ids = fields.One2many(
        'orls.paeds.urinary.catheterisation.lines',
        'orls_paeds_urinary_catherterisation_main_id',
        string="Urinary Catheterisation 5(a)"
    )

    orls_paeds_phlebotomy_neonates_main_ids = fields.One2many(
        'orls.paeds.phlebotomy.neonates.lines',
        'orls_paeds_phlebotomy_neonates_main_id',
        string="Phlebotomy in neonates(5p)"
    )








    user_id = fields.Many2one('res.users', string="User", related='create_uid', store=True)

    csv_file = fields.Binary(string="CSV File")
    csv_filename = fields.Char(string="CSV Filename")

    def _compute_user_in_assigned_rotation(self):
        for record in self:
            user_assigned = self.env.user.employee_id
            record.user_in_assigned_rotation = user_assigned in record.employee_ids

    def download_csv_template(self):
        csv_content = StringIO()
        csv_writer = csv.writer(csv_content)
        csv_writer.writerow(['employee_id', 'employee_name'])  # Updated headers

        # Fetch all employees and write to CSV
        employees = self.env['hr.employee'].search([])
        for employee in employees:
            csv_writer.writerow([employee.id, employee.name])

        csv_data = base64.b64encode(csv_content.getvalue().encode('utf-8'))
        csv_content.close()

        attachment = self.env['ir.attachment'].create({
            'name': 'employee_template.csv',
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

    def import_assignments_from_csv(self):
        if not self.csv_file:
            raise UserError("Please upload a CSV file first.")

        csv_content = base64.b64decode(self.csv_file).decode('utf-8')
        csv_reader = csv.reader(StringIO(csv_content))
        headers = next(csv_reader, None)
        if headers != ['employee_id', 'employee_name']:
            raise UserError("Invalid CSV format. The header should be 'employee_id, employee_name'.")

        employee_ids = []
        for row in csv_reader:
            if len(row) != 2:
                raise UserError("Invalid CSV format. Each row should have exactly two columns.")
            employee_id, employee_name = row
            employee = self.env['hr.employee'].browse(int(employee_id))
            if not employee.exists():
                raise UserError(f"Employee with ID {employee_id} does not exist.")
            employee_ids.append(employee.id)

        self.employee_ids = [(6, 0, employee_ids)]

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'CSV Import',
                'message': 'Employees have been successfully assigned.',
                'type': 'success',
                'sticky': False,
            }
        }

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("supervisor", "Supervisor"),
            ("approved", "Approved")
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

    # csv_file = fields.Binary(string="CSV File")
    # csv_filename = fields.Char(string="CSV Filename")
    user_in_assigned_company_and_open = fields.Boolean(
        string="User in Assigned Company and Open",
        compute='_compute_user_in_assigned_company_and_open'
    )
    employee_ids = fields.Many2many('hr.employee', string="Assigned Employees")
    user_in_assigned_company_and_results_published = fields.Boolean(
        string="User in Assigned Company and Results Published",
        compute='_compute_user_in_assigned_company_and_results_published'
    )
    sample_id = fields.Char(string="Test Sample ID", store=True)
    date_tested = fields.Date(string="Date Tested", store=True)

    user_has_created_log = fields.Boolean(
        string='User Has Created Log',
        compute='_compute_user_has_created_log'
    )

    @api.depends()
    def _compute_user_has_created_log(self):
        for record in self:
            log_exists = self.env['orls.gen.surgery.resident.log'].search_count([
                ('name', '=', self.env.user.id),
                ('r_l_rotation_id', '=', record.id)
            ]) > 0
            record.user_has_created_log = log_exists

    # company_count = fields.Integer(string='Company Count', compute='_compute_company_count', store=True)

    def open_results_submission_wizard(self):
        self.ensure_one()
        # Set the values to blank except the samples
        self.write({
            'supervisor_comment': '',
            'pdf_file': False,
            'pdf_filename': '',
            'orls_surgical_toilet_ids': [
                (1, line.id, {'resident_involvement': '', 'file_no': '', 'date': '', 'supervisor_id': False}) for line
                in self.orls_surgical_toilet_ids],
            'orls_suturing_wound_ids': [
                (1, line.id, {'resident_involvement': '', 'file_no': '', 'date': '', 'supervisor_id': False}) for line
                in self.orls_suturing_wound_ids],
            'orls_incision_drainage_abscess_ids': [
                (1, line.id, {'resident_involvement': '', 'file_no': '', 'date': '', 'supervisor_id': False}) for line
                in self.orls_incision_drainage_abscess_ids],
            'orls_insertion_chest_tubes_ids': [
                (1, line.id, {'resident_involvement': '', 'file_no': '', 'date': '', 'supervisor_id': False}) for line
                in self.orls_insertion_chest_tubes_ids],
            'orls_removal_of_stitches_ids': [
                (1, line.id, {'resident_involvement': '', 'file_no': '', 'date': '', 'supervisor_id': False}) for line
                in self.orls_removal_of_stitches_ids],
            'orls_operation_monthly_review_lines_ids': [(1, line.id, {'month': '', 'resident_comment': '',
                                                                      'resident_comment_date': '',
                                                                      'supervisor_comment': '',
                                                                      'supervisor_comment_date': '',
                                                                      'resident_coordinator_comment': '',
                                                                      'resident_coordinator_comment_date': ''}) for line
                                                        in self.orls_operation_monthly_review_lines_ids],
            'orls_operation_clinical_or_audit_meetings_presented_lines_ids': [
                (1, line.id, {'date': '', 'topic': '', 'venue': '', 'consultant_id': False}) for line in
                self.orls_operation_clinical_or_audit_meetings_presented_lines_ids],
            'orls_operation_teaching_rounds_attended_lines_ids': [
                (1, line.id, {'date': '', 'ward_round': '', 'venue': '', 'consultant_id': False}) for line in
                self.orls_operation_teaching_rounds_attended_lines_ids],
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rotations Log',
            'res_model': 'orls.gen.surgery.rotation.procedures.operations',
            'view_mode': 'form',
            'view_id': self.env.ref('orls_res.orls_gen_surgery_rotation_procedures_operations_wizard_form').id,
            'res_id': self.id,
            'target': 'new'
        }

    def action_submit_results(self):
        # Ensure the referenced record exists
        my_rotation = self.env['orls.gen.surgery.rotation.procedures.operations'].browse(self.id)
        if not my_rotation.exists():
            raise UserError("Referenced record does not exist.")

        form_data = {
            'name': self.name.id,
            'r_l_internship_center_id': self.internship_center_id.id,
            'r_l_hpcz_Reg_No': self.hpcz_Reg_No,
            'r_l_hpcz_license_No': self.hpcz_license_No,
            'r_l_start_date': self.start_date,
            'r_l_end_date': self.end_date,
            'r_l_state': 'draft',
            'r_l_pdf_file': self.pdf_file,
            'r_l_pdf_filename': self.pdf_filename,
        }

        new_record = self.env['orls.gen.surgery.resident.log'].create(form_data)
        new_record_id = new_record.id

        form_data2 = [{
            'orls_surgical_toilet_id': new_record_id,
            's_t_resident_involvement': line.resident_involvement,
            's_t_number_of_cases': line.number_of_cases,
            's_t_date': line.date,
            's_t_file_no': line.file_no,
        } for line in self.orls_surgical_toilet_ids]
        self.env['orls.gen.surgical.toilet.log.lines'].create(form_data2)

        form_data3 = [{
            'orls_suturing_wound_id': new_record_id,
            's_w_resident_involvement': line.resident_involvement,
            's_w_number_of_cases': line.number_of_cases,
            's_w_date': line.date,
            's_w_file_no': line.file_no,
        } for line in self.orls_suturing_wound_ids]
        self.env['orls.suturing.wound.log.lines'].create(form_data3)

        form_data4 = [{
            'orls_incision_drainage_abscess_id': new_record_id,
            'a_d_number_of_cases': line.number_of_cases,
            'a_d_date': line.date,
            'a_d_file_no': line.file_no,
            'a_d_resident_involvement': line.resident_involvement,
        } for line in self.orls_incision_drainage_abscess_ids]
        self.env['orls.incision.drainage.abscess.log.lines'].create(form_data4)

        form_data5 = [{
            'orls_insertion_chest_tubes_id': new_record_id,
            'c_t_resident_involvement': line.resident_involvement,
            'c_t_number_of_cases': line.number_of_cases,
            'c_t_date': line.date,
            'c_t_file_no': line.file_no,
        } for line in self.orls_insertion_chest_tubes_ids]
        self.env['orls.insertion.chest.tubes.log.lines'].create(form_data5)

        form_data6 = [{
            'orls_removal_of_stitches_id': new_record_id,
            'r_s_resident_involvement': line.resident_involvement,
            'r_s_number_of_cases': line.number_of_cases,
            'r_s_date': line.date,
            'r_s_file_no': line.file_no,
        } for line in self.orls_removal_of_stitches_ids]
        self.env['orls.removal.of.stitches.log.lines'].create(form_data6)

        form_data7 = [{
            'orls_operation_monthly_review_id': new_record_id,
            'm_p_month': line.month,
            'm_p_resident_comment': line.resident_comment,
            'm_p_resident_comment_date': line.resident_comment_date,
            'm_p_supervisor_comment': line.supervisor_comment,
            'm_p_supervisor_comment_date': line.supervisor_comment_date,
            'm_p_resident_coordinator_comment': line.resident_coordinator_comment,
            'm_p_resident_coordinator_comment_date': line.resident_coordinator_comment_date,
        } for line in self.orls_operation_monthly_review_lines_ids]
        self.env['orls.gen.surgery.monthly.perf.log.lines'].create(form_data7)

        form_data8 = [{
            'orls_operation_clinical_presentation_id': new_record_id,
            'c_a_date': line.date,
            'c_a_topic': line.topic,
            'c_a_venue': line.venue,
            'c_a_consultant_id': line.consultant_id.id,
        } for line in self.orls_operation_clinical_or_audit_meetings_presented_lines_ids]
        self.env['orls.gen.surgery.rotation.cl.pres.log.lines'].create(form_data8)

        form_data9 = [{
            'orls_operation_clinical_teaching_rounds_id': new_record_id,
            't_r_date': line.date,
            't_r_ward_round': line.ward_round,
            't_r_venue': line.venue,
            't_r_consultant_id': line.consultant_id.id,
        } for line in self.orls_operation_teaching_rounds_attended_lines_ids]
        self.env['orls.gen.surgery.teaching.rounds.attended.log.lines'].create(form_data9)

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

    # def download_csv_template(self):
    #     csv_content = StringIO()
    #     csv_writer = csv.writer(csv_content)
    #     csv_writer.writerow(['Company Name'])  # Add more headers if needed
    #
    #     # Fetch all companies and write to CSV
    #     companies = self.env['res.company'].search([])
    #     for company in companies:
    #         csv_writer.writerow([company.name])
    #
    #     csv_data = base64.b64encode(csv_content.getvalue().encode('utf-8'))
    #     csv_content.close()
    #
    #     attachment = self.env['ir.attachment'].create({
    #         'name': 'company_template.csv',
    #         'datas': csv_data,
    #         'type': 'binary',
    #         'res_model': self._name,
    #         'res_id': self.id,
    #     })
    #
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': f'/web/content/{attachment.id}?download=true',
    #         'target': 'self',
    #     }

    # def import_companies_from_csv(self):
    #     if not self.csv_file:
    #         raise UserError("Please upload a CSV file first.")
    #
    #     csv_content = base64.b64decode(self.csv_file).decode('utf-8')
    #     csv_reader = csv.reader(StringIO(csv_content))
    #     next(csv_reader)  # Skip headers
    #     company_ids = []
    #     for row in csv_reader:
    #         company_name = row[0]
    #         company = self.env['res.company'].search([('name', '=', company_name)], limit=1)
    #         if company:
    #             company_ids.append(company.id)
    #         else:
    #             raise UserError(f"Company '{company_name}' not found.")
    #     self.company_ids = [(6, 0, company_ids)]

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
