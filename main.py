from flask import Flask, render_template, request, redirect, url_for
import os
import json
from datetime import datetime, timedelta
from threading import Timer
import logging
from logging_config import configure_logging

app = Flask(__name__)

TICKETS_FILE = 'tickets.json'

def remove_old_tickets():
    """Remove tickets that are older than 24 hours."""
    try:
        with open(TICKETS_FILE, 'r+') as file:
            tickets = json.load(file)
            current_time = datetime.now()
            tickets = {k: v for k, v in tickets.items() if current_time - datetime.fromisoformat(v['time']) < timedelta(hours=24)}
            file.seek(0)
            json.dump(tickets, file)
            file.truncate()
    except FileNotFoundError:
        pass
    Timer(3600, remove_old_tickets).start()

@app.route("/")
def root_route():
    return render_template('index.html')

@app.route("/book_ticket")
def book_ticket():
    return render_template('book_ticket.html')

@app.route("/submit_ticket", methods=['POST'])
def submit_ticket():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    tickets = request.form['tickets']
    serial_number = os.urandom(8).hex()
    ticket_info = {'name': name, 'phone': phone, 'email': email, 'tickets': tickets, 'time': datetime.now().isoformat(), 'serial_number': serial_number}
    try:
        with open(TICKETS_FILE, 'r+') as file:
            tickets = json.load(file)
            tickets[serial_number] = ticket_info
            file.seek(0)
            json.dump(tickets, file)
    except FileNotFoundError:
        with open(TICKETS_FILE, 'w') as file:
            json.dump({serial_number: ticket_info}, file)
    # Generate a simple text-based ticket for printing or saving as PDF
    # Generate a simple HTML page that can be printed or saved as PDF
    ticket_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ticket Confirmation</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .ticket-container {{ margin: auto; width: 600px; border: 1px solid #ccc; padding: 20px; }}
            .ticket-info {{ margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="ticket-container">
            <h2>Ticket Confirmation</h2>
            <div class="ticket-info"><strong>Serial Number:</strong> {serial_number}</div>
            <div class="ticket-info"><strong>Name:</strong> {name}</div>
            <div class="ticket-info"><strong>Phone:</strong> {phone}</div>
            <div class="ticket-info"><strong>Email:</strong> {email}</div>
            <div class="ticket-info"><strong>Number of Tickets:</strong> {ticket_info['tickets']}</div>
            <div class="ticket-info"><strong>Time:</strong> {datetime.now().isoformat()}</div>
        </div>
    </body>
    </html>
    """
    ticket_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ticket Confirmation</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            .ticket-container {{ margin: auto; width: 600px; border: 1px solid #ccc; padding: 20px; }}
            .ticket-info {{ margin: 10px 0; }}
        </style>
    </head>
    <body>
        <div class="ticket-container">
            <h2>Ticket Confirmation</h2>
            <div class="ticket-info"><strong>Serial Number:</strong> {serial_number}</div>
            <div class="ticket-info"><strong>Name:</strong> {name}</div>
            <div class="ticket-info"><strong>Phone:</strong> {phone}</div>
            <div class="ticket-info"><strong>Email:</strong> {email}</div>
            <div class="ticket-info"><strong>Number of Tickets:</strong> {ticket_info['tickets']}</div>
            <div class="ticket-info"><strong>Time:</strong> {datetime.now().isoformat()}</div>
            <button onclick="window.print()">Print this page</button>
        </div>
    </body>
    </html>
    """
    return ticket_html

@app.route("/verify_ticket")
def verify_ticket():
    return render_template('verify_ticket.html')

@app.route("/check_ticket", methods=['POST'])
def check_ticket():
    serial = request.form['serial']
    try:
        with open(TICKETS_FILE, 'r') as file:
            tickets = json.load(file)
            if serial in tickets:
                del tickets[serial]
                with open(TICKETS_FILE, 'w') as file:
                    json.dump(tickets, file)
                return "Ticket is valid."
            else:
                return "Ticket is not valid."
    except FileNotFoundError:
        return "Ticket is not valid."

if __name__ == "__main__":
    configure_logging()
    remove_old_tickets()
    options = {"bind": "%s:%s" % ("0.0.0.0", "8080"), "workers": 4, "loglevel": "warn"}
    app.run(host="0.0.0.0", port=8080, debug=True)
