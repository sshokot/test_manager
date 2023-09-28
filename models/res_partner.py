from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    test_manager_id = fields.Many2one(
        'test.manager',
        string="Test Manager",
    )

    def action_test_managers(self):
        self.ensure_one()
        action = self.test_manager_id.action_open_test_manager_list()
        return action
