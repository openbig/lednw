# -*- encoding: utf-8 -*-
##############################################################################
#
#    sale_layout_customization
#    (C) 2014 big-consulting GmbH
#    Author: Jan Dasenbrock (openBIG.org)
#
#    All Rights reserved
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields

class SaleLayoutCategory(osv.Model):
    _name = "sale_layout.category"
    _inherit = ["sale_layout.category"]
    _columns = {
    	'name' : fields.char(translate=True),
    }