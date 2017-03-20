# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "il_schools"
app_title = "IL_Schools"
app_publisher = "IL"
app_description = "IL Schools Tools"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "il@il.fr"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/il_schools/css/il_schools.css"
# app_include_js = "/assets/il_schools/js/il_schools.js"

# include js, css files in header of web template
# web_include_css = "/assets/il_schools/css/il_schools.css"
# web_include_js = "/assets/il_schools/js/il_schools.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "il_schools.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "il_schools.install.before_install"
# after_install = "il_schools.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "il_schools.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"il_schools.tasks.all"
# 	],
# 	"daily": [
# 		"il_schools.tasks.daily"
# 	],
# 	"hourly": [
# 		"il_schools.tasks.hourly"
# 	],
# 	"weekly": [
# 		"il_schools.tasks.weekly"
# 	]
# 	"monthly": [
# 		"il_schools.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "il_schools.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "il_schools.event.get_events"
# }

