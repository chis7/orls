from odoo import api, fields, models
from odoo.exceptions import AccessError
from datetime import date

class OrlsSurgicalToiletLogLines(models.Model):
    _name = "orls.gen.surgical.toilet.log.lines"
    _description = "Orls Surgical Toilet Log Lines"

    orls_surgical_toilet_id = fields.Many2one(
        'orls.gen.surgery.resident.log',
        string="Surgical Toilet"
    )
    s_t_number_of_cases = fields.Char(string="# of Cases", store=True)
    s_t_file_no = fields.Char(string="File No.", store=True)
    s_t_date = fields.Date(string="Date", store=True)
    s_t_resident_involvement = fields.Selection(
        selection=[
            ("P", "Performed"),
            ("A", "Assisted"),
            ("O", "Observed"),
        ],
        string="Resident Involvement",
        tracking=True
    )
    # s_t_checkbox_field = fields.Boolean(string='Supervisor Check', groups='orls_res.group_supervisors')
    s_t_checkbox_field = fields.Boolean(string='Supervisor Check')
    s_t_supervisor_id = fields.Many2one('res.user', string="Supervisor's Name")
    s_t_sign_off_date = fields.Date(string="Sign-off Date", store=True)

    @api.model
    def create(self, vals):
        if vals.get('s_t_checkbox_field'):
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.parent_id.id if create_user.parent_id else False
            vals['s_t_supervisor_id'] = supervisor_id
            vals['s_t_sign_off_date'] = date.today()
        return super(OrlsSurgicalToiletLogLines, self).create(vals)

    def write(self, vals):
        if 's_t_checkbox_field' in vals:
            create_user = self.env['res.users'].browse(self.env.uid)
            supervisor_id = create_user.employee_id.parent_id.id if create_user.employee_id.parent_id else False
            if not supervisor_id:
                raise AccessError("You are not allowed to modify this record.")
            vals['s_t_supervisor_id'] = supervisor_id
            vals['s_t_sign_off_date'] = date.today() if vals['s_t_checkbox_field'] else False
        return super(OrlsSurgicalToiletLogLines, self).write(vals)