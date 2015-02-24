# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import orm, fields


class procurement_order(orm.Model):
    _inherit = "procurement.order"

    def create_procurement_purchase_order(self, cr, uid, procurement, po_vals, line_vals, context=None):
        address = self.pool.get('res.partner')
        if procurement.dest_address_id:
            po_vals.update({'warehouse_id': False})
            supplier = address.browse(cr, uid, procurement.dest_address_id.id)
            if supplier:
                location_id = supplier.property_stock_customer.id
                po_vals.update({'location_id': location_id})
            po_vals.update({
                'dest_address_id': procurement.dest_address_id.id
            })
        return super(procurement_order, self).\
            create_procurement_purchase_order(cr, uid, procurement, po_vals,
                                              line_vals, context=context)
