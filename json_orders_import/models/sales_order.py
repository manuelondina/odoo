from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_type = fields.Selection([
        ('individual', 'Individual'),
        ('company', 'Company'),
    ], string='Customer Type')
    nif = fields.Char(string='NIF')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fiscal_position = fields.Selection([
        ('national', 'National'),
        ('intracomunitary', 'Intracomunitary'),
    ], string='Fiscal Position')
    customer_id = fields.Many2one('res.partner', string='Customer')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    order_product_name = fields.Char(string='Product Name')
    order_product_sku = fields.Char(string='Product SKU')
    order_product_type = fields.Selection([
        ('product', 'Product'),
        ('service', 'Service'),
    ], string='Product Type')
    quantity = fields.Float(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    order_id = fields.Many2one('sale.order', string='Order')
