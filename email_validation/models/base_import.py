from odoo import models


class BaseImport(models.TransientModel):
    _inherit = 'base_import.import'

    def execute_import(self, fields, columns, options, dryrun=False):
        return super(
            BaseImport,
            self.with_context(import_filename=self.file_name)
        ).execute_import(
            fields, columns, options, dryrun=dryrun
        )
