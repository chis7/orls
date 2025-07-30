from odoo import models, fields


class SurgeryNotebookPage(models.Model):
    _name = 'orls.gen.surgery.notebook.page'
    _description = 'Surgery Notebook Page'

    name = fields.Char(string="Page Name", required=True)
    discipline_id = fields.Many2one(
        'orls.gen.surgery.discipline',
        string="Discipline"
    )
    notebook_pages_id = fields.Many2one(
        'orls.gen.surgery.rotation.procedures.operations',
        string="Operation"
    )
