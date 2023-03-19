import base64
import csv
import xlrd
from io import StringIO, BytesIO
from odoo import http, exceptions
from odoo.http import request
from odoo.tools import pycompat


class ConfirmSalesOrderTool(http.Controller):

    @http.route('/confirm_sales_orders', type='http', auth='user', website=True)
    def confirm_sales_orders(self, **kw):
        return request.render('confirm_sales_orders.confirm_sales_orders', {})

    @http.route('/confirm_sales_orders/import', type='http', auth='user', website=True)
    def import_sales_orders(self, file=None, **kw):
        if not file:
            return request.redirect('/confirm_sales_orders?error=No file selected')

        try:
            file_name, file_content = file.filename, file.read()
            if file_name.endswith('.csv'):
                csv_data = pycompat.to_text(base64.b64decode(file_content), encoding='utf-8')
                reader = csv.reader(StringIO(csv_data), delimiter=',')
                sales_order_names = [row[0] for row in reader]
            else:
                xls_data = base64.b64decode(file_content)
                workbook = xlrd.open_workbook(file_contents=xls_data)
                worksheet = workbook.sheet_by_index(0)
                sales_order_names = [worksheet.cell_value(i, 0) for i in range(1, worksheet.nrows)]

            sales_orders = request.env['sale.order'].search([('name', 'in', sales_order_names)])
            for sale_order in sales_orders:
                if not sale_order.state == 'draft':
                    raise exceptions.UserError('Sales order %s is not in draft state' % sale_order.name)
                sale_order.action_confirm()

            return request.redirect('/confirm_sales_orders?success=true')
        except Exception as e:
            return request.redirect('/confirm_sales_orders?error=%s' % str(e))