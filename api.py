import frappe
from frappe.utils import now

@frappe.whitelist(allow_guest=False)
def update_heartbeat(student, focus_session):
    """
    Update Attendance timestamp when student is active.
    """
    att = frappe.get_doc("Attendance", {"student": student, "focus_session": focus_session})
    att.timestamp = now()  # current time
    att.save(ignore_permissions=True)
