from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import timedelta




class Building(models.Model):
    _name = 'building'
    _description = 'Building'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    number = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    name = fields.Char()
    value_1 = fields.Float('Value 1')
    value_2 = fields.Float('Value 2')
    percentage = fields.Float('Percentage', compute='_compute_percentage', store=True,digits=(0,0))

    active = fields.Boolean(default='true',string='active')
    # total_amount = fields.Float(string='Total Amount',compute='_compute_total_amount')
    # percentage2 = fields.Float(string='Percentage', compute='_compute_percentage2', store=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'pending'),
        ('sold', 'sold')
    ], default='draft')

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print(" inside in sold ")
            rec.state = 'sold'

    @api.depends('value_1', 'value_2')
    def _compute_percentage(self):
        for record in self:
            if record.value_2 != 0:
                record.percentage = (record.value_1 / record.value_2) * 100
            else:
                record.percentage = 0

    # @api.onchange('value_1', 'value_2')
    # def _compute_total_amount(self):
    #     for record in self:
    #         record.total_amount = record.value_1 + record.value_2 * 100
    #
    # @api.depends('total_amount')
    # def _compute_percentage2(self):
    #     for record in self:
    #         if record.total_amount:
    #             record.percentage2 = (record.total_amount / 100) * 10
    #         else:
    #             record.percentage = 0.0




