# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

import openerp

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

class pos_config(osv.osv):
    _inherit = 'pos.config' 
    _columns = {
        'chef_iface_discount': fields.boolean('Chefbakers Discounts', help='Allow the cashier to give discounts on the whole order.'),
        'chef_discount_pc': fields.float('Chefbakers Discount Percentage', help='The default discount percentage'),
        'chef_discount_amount': fields.float('Chefbakers Discount Amount', help='The default discount percentage'),
        'chef_discount_product_id': fields.many2one('product.product', 'Discount Product', domain="[('available_in_pos', '=', True)]", help='The product used to model the discount'),
    }
    _defaults = {
        'chef_iface_discount': True,
        'chef_discount_pc': 10,
    }
