# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document
from erpnext.controllers.print_settings import print_settings_for_item_table

class SalesOrderItem(Document):
	def __setup__(self):
		print_settings_for_item_table(self)

def on_doctype_update():
	frappe.db.add_index("Sales Order Item", ["item_code", "warehouse"])

@frappe.whitelist()
def get_customer_item_ref_code(item,customer_name):
    	customer_names = frappe.get_all("Item Customer Detail", filters={
    		"parent": item,
    		"customer_name": customer_name
    	}, fields=["ref_code"])    	
    	if customer_names:
    		return customer_names[0].ref_code

def get_customer_item_ref_code(item,customer_name):
    """Fetches the Customer Item Code for the given Item

	Args:
		item (varchar) : Item Code for the Sales Item 
		customer_name (varchar) : Customer Name Of Sales Order

	Returns:
		Customer Item Code (varchar) : Returns the Customer Item Reference Code
	"""  	
		customer_names = frappe.get_all("Item Customer Detail", filters={
    		"parent": item,
    		"customer_name": customer_name
    	}, fields=["ref_code"])    	

    	if customer_names:
    		return customer_names[0].ref_code

