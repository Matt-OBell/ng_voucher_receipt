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

from openerp.osv import osv, fields

class account_voucher(osv.osv):
    _inherit = 'account.voucher'
    
    def onchange_account(self, cr, uid, ids, account_id, context=None):
        res = {}
        if account_id:
            account = self.pool.get('account.account').browse(cr, uid, account_id, context=context)
            if account.type == 'liquidity':
                journals = self.pool.get('account.journal').search(cr, uid, [('default_debit_account_id', '=', account_id)])
                if journals:
                    res.update({'value': {'journal_id': journals[0]}})
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
