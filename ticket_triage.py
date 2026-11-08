"""Prioritize fictional help desk tickets without modifying any system."""
import csv
from pathlib import Path

INPUT = Path(__file__).with_name('tickets.csv')

def priority(impact, urgency):
    score = int(impact) * int(urgency)
    return 'Critical' if score >= 9 else 'High' if score >= 6 else 'Medium' if score >= 3 else 'Low'

def main():
    with INPUT.open(newline='', encoding='utf-8') as fh:
        tickets = list(csv.DictReader(fh))
    for ticket in tickets:
        ticket['priority'] = priority(ticket['impact'], ticket['urgency'])
    open_tickets = [t for t in tickets if t['status'] != 'Resolved']
    ranks = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3}
    open_tickets.sort(key=lambda t: (ranks[t['priority']], t['ticket_id']))
    print('OPEN TICKETS — SYNTHETIC PRACTICE DATA')
    for t in open_tickets:
        print(f"{t['ticket_id']:7} {t['priority']:8} {t['category']:9} {t['summary']}")
    print(f'\nOpen: {len(open_tickets)} | Resolved: {len(tickets)-len(open_tickets)}')

if __name__ == '__main__':
    main()
