# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Mattobell (<http://www.mattobell.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    "name" : "Receipts / Voucher For Bank/Cash Payment",
    "version" : "1.0",
    "depends" : ["base", "account_voucher"],
    "author" : "Mattobell",
    "website" : "http://www.mattobell.com",
    'category': 'Finance',
    "description": """
Receipts / Voucher For Bank/Cash Payment

This module allow user to select cash/bank account on sale/purchase receipts and pay directly.
    """,
    "data" : [
        "voucher_view.xml",
    ],
    "auto_install": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
