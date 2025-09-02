import frappe
from frappe.utils import now

@frappe.whitelist(allow_guest=False)
def update_heartbeat(student, focus_session):
    """
    Update heartbeat timestamp for a single student in a focus session.
    """
    att = frappe.get_doc("Attendance", {
        "student": student,
        "focus_session": focus_session
    })
    att.timestamp = now()
    att.status = "Active"
    att.save(ignore_permissions=True)

