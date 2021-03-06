# -*- coding: utf-8 -*-
# Copyright (c) 2020, Bloom Stack, Inc and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class PackageTag(Document):
	def validate(self):
		if self.source_package_tag:
			self.validate_source_package_tag()
			self.update_coa_batch_no()

	def validate_source_package_tag(self):
		source_package_tag = frappe.db.get_value("Package Tag", self.source_package_tag, "source_package_tag")
		if self.name == source_package_tag:
			frappe.throw(_("Invalid package tag. {0} is already the source package for {1}.".format(self.name, self.source_package_tag)))

	def update_coa_batch_no(self):
		self.coa_batch_no = frappe.db.get_value("Package Tag", self.source_package_tag, "coa_batch_no")
