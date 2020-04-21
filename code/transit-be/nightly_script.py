from app.functions import *
from app import create_app
"""
Nightly script that will run to push tickets to people without tickets.
"""

app = create_app()
with app.app_context():
        nightly_ticket_issue()
