from odoo import http, exceptions
from odoo.http import request
import json


class JSONDataController(http.Controller):

    @http.route('/json_data', type='http', auth='public', methods=['POST'], csrf=False)
    def process_json_data(self, **kwargs):
        try:
            json_data = json.loads(request.httprequest.data.decode('utf-8'))
            customer_data = json_data.get('customer')
            order_lines_data = json_data.get('orderLines')
            fiscal_position = json_data.get('fiscal_position')

            # Create the customer record
            customer_type = customer_data.get('customerType', 'individual')
            nif = customer_data.get('NIF', '00000000A')
            company_name = customer_data.get('companyName', 'Individual Customer')
            street = customer_data.get('street', 'Unknown')
            additional_street = customer_data.get('additionalStreet', '')
            postal_code = customer_data.get('postalCode', '00000')
            city = customer_data.get('city', 'Unknown')
            country = customer_data.get('country', 'ES')
            phone = customer_data.get('phone', '')
            mobile_phone = customer_data.get('mobilePhone', '')
            email = customer_data.get('email', '')

            country_id = request.env['res.country'].search([('code', '=', country)], limit=1)
            if not country_id:
                country_id = request.env.ref('base.es')
            else:
                country_id = country_id[0]

            customer = request.env['res.partner'].create({
                'customer_type': customer_type,
                'nif': nif,
                'name': company_name,
                'street': street,
                'street2': additional_street,
                'zip': postal_code,
                'city': city,
                'country_id': country_id.id,
                'phone': phone,
                'mobile': mobile_phone,
                'email': email,
            })

            # Crea el order record
            order = request.env['sale.order'].create({
                'fiscal_position': fiscal_position,
                'partner_id': customer.id,
            })

            # Crea el order line record
            for order_line_data in order_lines_data:
                order_product_data = order_line_data.get('orderProduct')
                quantity = order_line_data.get('quantity')
                unit_price = order_line_data.get('unitPrice')

                product_name = order_product_data.get('name', 'Unknown')
                product_sku = order_product_data.get('sku', '00000000')
                product_type = order_product_data.get('type', 'product')

                product = request.env['product.product'].create({
                    'name': product_name,
                    'default_code': product_sku,
                    'type': product_type,
                })

                order_line = request.env['sale.order.line'].create({
                    'order_product_name': product_name,
                    'order_product_sku': product_sku,
                    'order_product_type': product_type,
                    'quantity': quantity,
                    'price_unit': unit_price,
                    'product_id': product.id,
                    'order_id': order.id,
                })

            return json.dumps({'success': True})

        except Exception as e:
            raise exceptions.ValidationError(e)