# -*- coding: utf-8 -*-
import base64
import csv
from datetime import date
from io import StringIO

from odoo import api, fields, models
from odoo.exceptions import UserError


class OrlsGenSurgeryResidentLog(models.Model):
    _name = "orls.gen.surgery.resident.log"
    _inherit = ["mail.thread"]
    _description = "Orls Surgery Resident Log"

    internship_center_id = fields.Many2one('res.company',string="Internship Center")
    hpcz_Reg_No = fields.Integer(string="HPCZ Reg. No.")
    hpcz_license_No = fields.Char(string="HPCZ License No.")
    supervisor_id = fields.Many2one('res.employee',  string="Supervisor's Name", )
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    name = fields.Many2one('orls.medical.disciplines', string="Discipline")

    supervisor_comment = fields.Text(string="Supervisor Comment", tracking=True)
    pdf_file = fields.Binary(string="PDF File")
    pdf_filename = fields.Char(string="PDF Filename")

    orls_surgical_toilet_ids = fields.One2many(
        'orls.gen.surgical.toilet.log.lines',
        'orls_surgical_toilet_id',
        string="Surgical toilet-10(p)"
    )
    orls_suturing_wound_ids = fields.One2many(
        'orls.suturing.wound.log.lines',
        'orls_suturing_wound_id',
        string="Suturing Wound-10(p)"
    )
    orls_incision_drainage_abscess_ids = fields.One2many(
        'orls.incision.drainage.abscess.log.lines',
        'orls_incision_drainage_abscess_id',
        string="Incision and drainage of Abscess 1 (O) 2(p)"
    )
    orls_insertion_chest_tubes_ids = fields.One2many(
        'orls.insertion.chest.tubes.log.lines',
        'orls_insertion_chest_tubes_id',
        string="Insertion of chest tubes 3(p)"
    )

    orls_removal_of_stitches_ids = fields.One2many(
        'orls.removal.of.stitches.log.lines',
        'orls_removal_of_stitches_id',
        string="Removal of stitches 10(p)"
    )

    orls_operation_monthly_review_lines_ids = fields.One2many(
        'orls.gen.surgery.monthly.perf.log.lines',
        'orls_operation_monthly_review_id',
        string="Monthly review of the performance"
    )
    orls_operation_clinical_or_audit_meetings_presented_lines_ids = fields.One2many(
        'orls.gen.surgery.rotation.cl.pres.log.lines',
        'orls_operation_clinical_presentation_id',
        string="Details of Clinical/Audit Meetings Presented"
    )
    orls_operation_teaching_rounds_attended_lines_ids = fields.One2many(
        'orls.gen.surgery.teaching.rounds.attended.log.lines',
        'orls_operation_clinical_teaching_rounds_id',
        string="Teaching Rounds Attended"
    )

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("supervisor", "Supervisor"),
            ("approved", "Approved")
        ],
        default='draft',
        string="Status",
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

    def open_results_submission_wizard(self):
        self.ensure_one()
        # Set the values to blank except the samples
        # self.write({
        #     'supervisor_comment': '',
        #     'lab_incharge_comment': '',
        #     'date_panel_received': False,
        #     'date_of_last_gene_xpert_instrument_calibration_or_installation': False,
        #     'xpert_assay_used': False,
        #     'catridge_lot_number': '',
        #     'expiry_date': False,
        #     'date_results_received_at_CDL': False,
        #     'add_infor_number_of_tests_conducted_in_last_full_month': 0,
        #     'add_infor_number_of_errors_occurred': 0,
        #     'add_infor_was_monthly_maintenance_done_for_the_genexpert': False,
        #     'add_infor_monthly_maintenance_done_by_date': False,
        #     'add_infor_monthly_maintenance_done_by_technologist': '',
        #     'add_infor_gene_xpert_serial_number': '',
        #     'add_infor_date_gene_xpert_instrument_installed': False,
        #     'add_infor_instrument_user': '',
        #     'declaration_testing_personnel': '',
        #     'declaration_testing_personnel_date': False,
        #     'pdf_file': False,
        #
        # })
        # self.sample_ids.write({'facility_result_date_tested': False})
        # self.sample_ids.write({'facility_result_tb_detection_not_detected': False})
        # self.sample_ids.write({'facility_result_tb_detection_trace': False})
        # self.sample_ids.write({'facility_result_tb_detection_very_low': False})
        # self.sample_ids.write({'facility_result_tb_detection_low': False})
        # self.sample_ids.write({'facility_result_tb_detection_medium': False})
        # self.sample_ids.write({'facility_result_tb_detection_high': False})
        # self.sample_ids.write({'facility_result_rif_na': False})
        # self.sample_ids.write({'facility_result_rif_not_detected': False})
        # self.sample_ids.write({'facility_result_rif_detected': False})
        # self.sample_ids.write({'facility_result_rif_indeterminate': False})
        # self.sample_ids.write({'facility_result_uninterpretable_invalid': False})
        # self.sample_ids.write({'facility_result_uninterpretable_no_result': False})
        # self.sample_ids.write({'facility_result_uninterpretable_error': False})
        # self.sample_ids.write({'facility_result_uninterpretable_indeterminate': False})
        # self.sample_ids.write({'facility_result_uninterpretable_error_code': False})
        # self.sample_ids.write({'facility_result_ct_probe_d_ultra_spsc': False})
        # self.sample_ids.write({'facility_result_ct_probe_c_is1081_is6110': False})
        # self.sample_ids.write({'facility_result_ct_probe_e_rpob2': False})
        # self.sample_ids.write({'facility_result_ct_probe_b_rpoB1': False})
        # self.sample_ids.write({'facility_result_ct_spc_rpoB3': False})
        # self.sample_ids.write({'facility_result_ct_probe_a_rpob4': False})
        # self.sample_ids.write({'facility_result_ct_xpert_module_number': False})
        # Open the wizard
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

        pass


        # user_company_name = self.env.user.company_id.name
        # record_name = self.name.name
        # file_name = f'{record_name}_{user_company_name}.pdf'
        #
        # form_data = {
        #     'name': self.id,
        #     'supervisor_comment': self.supervisor_comment,
        #     'lab_incharge_comment': self.lab_incharge_comment,
        #     'date_panel_received': self.date_panel_received,
        #     'date_of_last_gene_xpert_instrument_calibration_or_installation': self.date_of_last_gene_xpert_instrument_calibration_or_installation,
        #     'xpert_assay_used': self.xpert_assay_used.id,
        #     'catridge_lot_number': self.catridge_lot_number,
        #     'expiry_date': self.expiry_date,
        #     'add_infor_number_of_tests_conducted_in_last_full_month': self.add_infor_number_of_tests_conducted_in_last_full_month,
        #     'add_infor_number_of_errors_occurred': self.add_infor_number_of_errors_occurred,
        #     'add_infor_was_monthly_maintenance_done_for_the_genexpert': self.add_infor_was_monthly_maintenance_done_for_the_genexpert,
        #     'add_infor_monthly_maintenance_done_by_date': self.add_infor_monthly_maintenance_done_by_date,
        #     'add_infor_monthly_maintenance_done_by_technologist': self.add_infor_monthly_maintenance_done_by_technologist,
        #     'add_infor_gene_xpert_serial_number': self.add_infor_gene_xpert_serial_number,
        #     'add_infor_date_gene_xpert_instrument_installed': self.add_infor_date_gene_xpert_instrument_installed,
        #     'add_infor_instrument_user': self.add_infor_instrument_user,
        #     'company_id': self.env.user.company_id.id,
        #     'state': 'draft',
        #     'site_id': self.env.user.company_id.id,
        #     'pdf_file': self.pdf_file,
        #     'pdf_filename': file_name,
        #
        # }
        #
        # new_record = self.env['zaneqas.tb.xpert.eqa.result'].create(form_data)
        # new_record_id = new_record.id
        # total_score = 0
        #
        # for sample in self.sample_ids:
        #     score = 0
        #     if (sample.tb_detection_not_detected == sample.facility_result_tb_detection_not_detected and
        #             sample.tb_detection_trace == sample.facility_result_tb_detection_trace and
        #             sample.tb_detection_very_low == sample.facility_result_tb_detection_very_low and
        #             sample.tb_detection_low == sample.facility_result_tb_detection_low and
        #             sample.tb_detection_medium == sample.facility_result_tb_detection_medium and
        #             sample.tb_detection_high == sample.facility_result_tb_detection_high and
        #             sample.rif_na == sample.facility_result_rif_na and
        #             sample.rif_not_detected == sample.facility_result_rif_not_detected and
        #             sample.rif_detected == sample.facility_result_rif_detected):
        #         score = 20
        #     elif (sample.tb_detection_not_detected == sample.facility_result_tb_detection_not_detected and
        #           sample.tb_detection_trace == sample.facility_result_tb_detection_trace and
        #           sample.tb_detection_very_low == sample.facility_result_tb_detection_very_low and
        #           sample.tb_detection_low == sample.facility_result_tb_detection_low and
        #           sample.tb_detection_medium == sample.facility_result_tb_detection_medium and
        #           sample.tb_detection_high == sample.facility_result_tb_detection_high and
        #           sample.rif_indeterminate):
        #         score = 10
        #     elif (sample.facility_result_uninterpretable_invalid or
        #           sample.facility_result_uninterpretable_no_result or
        #           sample.facility_result_uninterpretable_error or
        #           sample.facility_result_uninterpretable_indeterminate):
        #         score = 5
        #     elif (not sample.facility_result_tb_detection_not_detected and
        #           not sample.facility_result_tb_detection_trace and
        #           not sample.facility_result_tb_detection_very_low and
        #           not sample.facility_result_tb_detection_low and
        #           not sample.facility_result_tb_detection_medium and
        #           not sample.facility_result_tb_detection_high and
        #           not sample.facility_result_rif_na and
        #           not sample.facility_result_rif_not_detected and
        #           not sample.facility_result_rif_detected):
        #         score = 0
        #     total_score += score
        #     form_data_2 = {
        #         'zaneqas_tb_xpert_eqa_result_id': new_record_id,
        #         'sample_id': sample.sample_id,
        #         'facility_result_date_tested': sample.facility_result_date_tested,
        #         'facility_result_tb_detection_not_detected': sample.facility_result_tb_detection_not_detected,
        #         'facility_result_tb_detection_trace': sample.facility_result_tb_detection_trace,
        #         'facility_result_tb_detection_very_low': sample.facility_result_tb_detection_very_low,
        #         'facility_result_tb_detection_low': sample.facility_result_tb_detection_low,
        #         'facility_result_tb_detection_medium': sample.facility_result_tb_detection_medium,
        #         'facility_result_tb_detection_high': sample.facility_result_tb_detection_high,
        #         'facility_result_rif_na': sample.facility_result_rif_na,
        #         'facility_result_rif_not_detected': sample.facility_result_rif_not_detected,
        #         'facility_result_rif_detected': sample.facility_result_rif_detected,
        #         'facility_result_rif_indeterminate': sample.facility_result_rif_indeterminate,
        #         'facility_result_uninterpretable_invalid': sample.facility_result_uninterpretable_invalid,
        #         'facility_result_uninterpretable_no_result': sample.facility_result_uninterpretable_no_result,
        #         'facility_result_uninterpretable_error': sample.facility_result_uninterpretable_error,
        #         'facility_result_uninterpretable_indeterminate': sample.facility_result_uninterpretable_indeterminate,
        #         'facility_result_uninterpretable_error_code': sample.facility_result_uninterpretable_error_code,
        #         'facility_result_ct_probe_d_ultra_spsc': sample.facility_result_ct_probe_d_ultra_spsc,
        #         'facility_result_ct_probe_c_is1081_is6110': sample.facility_result_ct_probe_c_is1081_is6110,
        #         'facility_result_ct_probe_e_rpob2': sample.facility_result_ct_probe_e_rpob2,
        #         'facility_result_ct_probe_b_rpoB1': sample.facility_result_ct_probe_b_rpoB1,
        #         'facility_result_ct_spc_rpoB3': sample.facility_result_ct_spc_rpoB3,
        #         'facility_result_ct_probe_a_rpob4': sample.facility_result_ct_probe_a_rpob4,
        #         'facility_result_ct_xpert_module_number': sample.facility_result_ct_xpert_module_number,
        #         'score': score,
        #         'tb_detection_not_detected': sample.tb_detection_not_detected,
        #         'tb_detection_trace': sample.tb_detection_trace,
        #         'tb_detection_very_low': sample.tb_detection_very_low,
        #         'tb_detection_low': sample.tb_detection_low,
        #         'tb_detection_medium': sample.tb_detection_medium,
        #         'tb_detection_high': sample.tb_detection_high,
        #         'rif_na': sample.rif_na,
        #         'rif_not_detected': sample.rif_not_detected,
        #         'rif_detected': sample.rif_detected,
        #         'rif_indeterminate': sample.rif_indeterminate,
        #         'uninterpretable_invalid': sample.uninterpretable_invalid,
        #         'uninterpretable_no_result': sample.uninterpretable_no_result,
        #         'uninterpretable_error': sample.uninterpretable_error,
        #         'uninterpretable_indeterminate': sample.uninterpretable_indeterminate,
        #         'uninterpretable_error_code': sample.uninterpretable_error_code,
        #         'ct_probe_d_ultra_spsc': sample.ct_probe_d_ultra_spsc,
        #         'ct_probe_c_is1081_is6110': sample.ct_probe_c_is1081_is6110,
        #         'ct_probe_e_rpob2': sample.ct_probe_e_rpob2,
        #         'ct_probe_b_rpoB1': sample.ct_probe_b_rpoB1,
        #         'ct_spc_rpoB3': sample.ct_spc_rpoB3,
        #         'ct_probe_a_rpob4': sample.ct_probe_a_rpob4,
        #         'ct_xpert_module_number': sample.ct_xpert_module_number,
        #
        #     }

            # self.env['zaneqas.tb.xpert.eqa.result.lines'].create(form_data_2)
            # new_record.write({'total_score': total_score})
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
