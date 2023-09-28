from odoo import models, fields


class DynamicPurchaseReport(models.Model):
    _name = 'test.manager'

    name = fields.Char()

    def action_open_test_manager_list(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("test_manager.test_manager_action")
        return action

