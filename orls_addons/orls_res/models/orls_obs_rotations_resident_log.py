# -*- coding: utf-8 -*-
import base64
import csv
from datetime import date
from io import StringIO

from odoo import api, fields, models
from odoo.exceptions import UserError


class OrlsObsResidentLog(models.Model):
    _name = "orls.obs.resident.log"
    _inherit = ["mail.thread"]
    _description = "Orls Obs Resident Log"

    internship_center_id = fields.Many2one('res.company', string="Internship Center")
    hpcz_Reg_No = fields.Char(string="HPCZ Reg. No.")
    hpcz_license_No = fields.Char(string="HPCZ License No.")
    supervisor_id = fields.Many2one('res.employee', string="Supervisor's Name", )
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    name = fields.Many2one('orls.medical.disciplines', string="Discipline")

    supervisor_comment = fields.Text(string="Supervisor Comment", tracking=True)
    pdf_file = fields.Binary(string="PDF File")
    pdf_filename = fields.Char(string="PDF Filename")
    rotation_id = fields.Many2one(
        'orls.obs.rotation.procedures',
        string='Rotation'
    )

    orls_obs_normal_delivery_log_ids = fields.One2many(
        'orls.obs.normal.delivery.log.lines',
        'orls_obs_normal_delivery_log_id',
        string="Normal delivery 10(p)"
    )

    orls_obs_episiotomy_log_ids = fields.One2many(
        'orls.obs.episotomy.log.lines',
        'orls_obs_episiotomy_log_id',
        string="Episiotomy / Repair- 5 (P)"
    )

    orls_obs_pph_log_ids = fields.One2many(
        'orls.obs.pph.log.lines',
        'orls_obs_pph_log_id',
        string="Management of PPH 3(a) 5(p)"
    )
    orls_obs_ceasarean_log_ids = fields.One2many(
        'orls.obs.ceasarean.log.lines',
        'orls_obs_ceasarean_log_id',
        string="Delivery by Caesarean Section10(p)"
    )

    orls_obs_vacuum_log_ids = fields.One2many(
        'orls.obs.vacuum.log.lines',
        'orls_obs_vacuum_log_id',
        string="Delivery by Vacuum Section10(p)"
    )

    orls_obs_multiple_delivery_log_ids = fields.One2many(
        'orls.obs.multiple.delivery.log.lines',
        'orls_obs_multiple_delivery_log_id',
        string="Delivery of multiple pregnancies 2(a) or 2(p)"
    )

    orls_obs_mcdonald_stitch_insertion_log_ids = fields.One2many(
        'orls.obs.mcdonald.stitch.insertion.log.lines',
        'orls_obs_mcdonald_stitch_insertion_log_id',
        string="McDonald Stitch insertion 3(a) and 2(p)*"
    )

    orls_obs_mcdonald_stitch_removal_log_id = fields.One2many(
        'orls.obs.mcdonald.stitch.removal.log.lines',
        'orls_obs_mcdonald_stitch_removal_log_id',
        string="McDonald Stitch removal 3(a) and 2(p)*"
    )

    orls_obs_postpartum_iud_insertion_log_ids = fields.One2many(
        'orls.obs.postpartum.iud.insertion.log.lines',
        'orls_obs_postpartum_iud_insertion_log_id',
        string="Postpartum family planning: PP- IUD Insertion"
    )

    orls_obs_counselling_on_family_planning_log_ids = fields.One2many(
        'orls.obs.counselling.family.planning.log.lines',
        'orls_obs_counselling_on_family_planning_log_id',
        string="Counselling clients on family planning methods 8(p)"
    )
    orls_obs_norplant_jadelle_insertion_and_removal_log_ids = fields.One2many(
        'orls.obs.norplant.jadelle.insertion.and.removal.log.lines',
        'orls_obs_norplant_jadelle_insertion_and_removal_log_id',
        string="Norplant/Jadelle insertion and Removal 5(a) and 5(p)"
    )

    orls_iucd_insertion_removal_log_ids = fields.One2many(
        'orls.obs.iucd.insertion.removal.log.lines',
        'orls_iucd_insertion_removal_log_id',
        string="Norplant/Jadelle insertion and Removal 5(a) and 5(p)"
    )

    orls_obs_prescribing_ora_or_injectable_fp_log_ids = fields.One2many(
        'orls.obs.prescribing.ora.or.injectable.fp.log.lines',
        'orls_obs_prescribing_ora_or_injectable_fp_log_id',
        string="Prescribing oral or injectable FP 5(P)"
    )

    orls_obs_clerk_inv_manage_pre_eclampsia_patients_log_ids = fields.One2many(
        'orls.obs.clerk.inv.manage.pre.eclampsia.patients.log.lines',
        'orls_obs_clerk_inv_manage_pre_eclampsia_patients_log_id',
        string="Be able to clerk, investigate and manage patients with pre-eclampsia 3(a) and 5(p)"
    )

    orls_management_of_malaria_in_pregnancy_log_ids = fields.One2many(
        'orls.obs.management.of.malaria.in.pregnancy.log.lines',
        'orls_management_of_malaria_in_pregnancy_log_id',
        string="management of Malaria in pregnancy 3(P)"
    )

    orls_obs_clerk_inv_manage_eclampsia_patients_log_ids = fields.One2many(
        'orls.obs.clerk.inv.manage.eclampsia.patients.log.lines',
        'orls_obs_clerk_inv_manage_eclampsia_patients_log_id',
        string="Be able to clerk, investigate and manage patients with eclampsia 2(p)"
    )

    orls_management_of_anemia_in_pregnancy_log_ids = fields.One2many(
        'orls.obs.management.of.anemia.in.pregnancy.log.lines',
        'orls_management_of_anemia_in_pregnancy_log_id',
        string="management of anemia in pregnancy 5(P)"
    )

    orls_obs_investigate_and_manage_pregnant_patients_with_cardiac_disease_log_ids = fields.One2many(
        'orls.obs.investigate.manage.preg.pat.with.cardiac.disease.log.lines',
        'orls_obs_investigate_and_manage_pregnant_patients_with_cardiac_disease_log_id',
        string="Investigate & manage pregnant patients with cardiac disease 2(p)"
    )

    orls_obs_clerk_investigate_manage_patients_with_hiv_in_pregnancy_log_ids = fields.One2many(
        'orls.obs.clerk.investigate.manage.patients.with.hiv.in.pregnancy.log.lines',
        'orls_obs_clerk_investigate_manage_patients_with_hiv_in_pregnancy_log_id',
        string="Be able to clerk, investigate and manage patients with HIV in pregnancy 5(p)(EMTCT)"
    )
    orls_manual_removal_of_retained_placenta_log_ids = fields.One2many(
        'orls.obs.clerk.investigate.manage.patients.with.hiv.in.pregnancy.log.lines',
        'orls_manual_removal_of_retained_placenta_log_id',
        string="Manual removal of retained placenta 2(a) and 2(p)"
    )

    orls_obs_repair_of_perineal_tears_log_ids = fields.One2many(
        'orls.obs.repair.of.perineal.tears.log.lines',
        'orls_obs_repair_of_perineal_tears_log_id',
        string="Repair of perineal tears 5(p)"
    )

    orls_obs_repair_of_cervical_tears_all_degrees_log_ids = fields.One2many(
        'orls.obs.repair.of.cervical.tears.all.degrees.log.lines',
        'orls_obs_repair_of_cervical_tears_all_degrees_log_id',
        string="Repair of cervical tears all degrees 2(a),2(p)"
    )

    orls_obs_obstetric_ultrasound_log_ids = fields.One2many(
        'orls.obs.obstetric.ultrasound.log.lines',
        'orls_obs_obstetric_ultrasound_log_id',
        string="Obstetric ultrasound 5(p) (Fetal presentation, placenta location, Fetal viability, liquor volume)."
    )




    r_l_state = fields.Selection(
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
