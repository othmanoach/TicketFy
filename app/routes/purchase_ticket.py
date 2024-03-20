import json
from flask import Blueprint, render_template, request, redirect, url_for, flash

purchase_ticket_bp = Blueprint('purchase_ticket', __name__)

# Load initial data from JSON files
with open('purchased_tickets.json', 'r') as file:
    purchased_tickets_data = json.load(file)

# Purchase ticket route
@purchase_ticket_bp.route('/purchase_ticket', methods=['GET', 'POST'])
def purchase_ticket():
    if request.method == 'POST':
        event_name = request.form.get('event_name')
        ticket_quantity = request.form.get('ticket_quantity')
        seat_preference = request.form.get('seat_preference')

        # Simulate successful payment
        payment_successful = True

        if payment_successful:
            # Generate a unique serial number for the ticket
            import uuid
            serial_number = str(uuid.uuid4())

            # Store ticket details in purchased_tickets.json
            new_ticket = {'event_name': event_name, 'ticket_quantity': ticket_quantity, 'seat_preference': seat_preference, 'serial_number': serial_number}
            purchased_tickets_data.append(new_ticket)
            with open('purchased_tickets.json', 'w') as file:
                json.dump(purchased_tickets_data, file, indent=4)

            flash(f'Purchase successful! Serial: {serial_number}', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Payment failed. Please try again.', 'error')

    return render_template('purchase_ticket.html')
