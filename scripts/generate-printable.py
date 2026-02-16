#!/usr/bin/env python3
"""
generate-printable.py

Generates a simple printable HTML version of the day-of checklist
that can be printed on a single page to bring to the cleanup event.

Usage: python3 scripts/generate-printable.py [output_file]

Part of the Community Cleanup Toolkit
https://github.com/ai-village-agents/community-cleanup-toolkit
"""

import sys
import os

def generate_printable_checklist(output_path="printable-checklist.html"):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Day-of Cleanup Checklist — Printable</title>
    <style>
        @media print {
            body { font-size: 11pt; margin: 0.5in; }
            .no-print { display: none; }
        }
        body {
            font-family: Arial, Helvetica, sans-serif;
            max-width: 7.5in;
            margin: 0 auto;
            padding: 20px;
            color: #222;
            line-height: 1.4;
        }
        h1 { font-size: 1.4em; text-align: center; margin-bottom: 5px; color: #1a5c2a; }
        .subtitle { text-align: center; color: #666; font-size: 0.9em; margin-bottom: 15px; }
        h2 { font-size: 1.1em; margin-top: 12px; margin-bottom: 6px; color: #2d8a4e;
             border-bottom: 1px solid #ccc; padding-bottom: 3px; }
        .checklist { list-style: none; padding-left: 0; margin: 0; }
        .checklist li {
            padding: 3px 0 3px 28px;
            position: relative;
            font-size: 0.9em;
        }
        .checklist li::before {
            content: "☐";
            position: absolute;
            left: 5px;
            font-size: 1.1em;
        }
        .fill-in {
            border-bottom: 1px dotted #999;
            display: inline-block;
            min-width: 120px;
        }
        .two-col { columns: 2; column-gap: 30px; }
        .footer {
            margin-top: 15px;
            text-align: center;
            font-size: 0.75em;
            color: #999;
            border-top: 1px solid #ddd;
            padding-top: 8px;
        }
        .event-info {
            background: #e8f5ec;
            padding: 8px 12px;
            border-radius: 5px;
            margin-bottom: 12px;
            font-size: 0.9em;
        }
        .event-info strong { color: #1a5c2a; }
        .no-print {
            text-align: center;
            margin-bottom: 15px;
        }
        .no-print button {
            background: #2d8a4e;
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 5px;
            font-size: 1em;
            cursor: pointer;
        }
        .no-print button:hover { background: #1a5c2a; }
    </style>
</head>
<body>
    <div class="no-print">
        <button onclick="window.print()">🖨️ Print This Checklist</button>
    </div>

    <h1>🌿 Community Cleanup — Day-of Checklist</h1>
    <p class="subtitle">Print this page and bring it with you!</p>

    <div class="event-info">
        <strong>Event:</strong> <span class="fill-in">&nbsp;</span> &nbsp;
        <strong>Date:</strong> <span class="fill-in">&nbsp;</span> &nbsp;
        <strong>Time:</strong> <span class="fill-in">&nbsp;</span>
    </div>

    <div class="two-col">

    <h2>📦 Before You Leave (1-2 hrs before)</h2>
    <ul class="checklist">
        <li>Check weather — adjust plan if needed</li>
        <li>Charge phone for photos</li>
        <li>Pack trash bags (30+ gallon)</li>
        <li>Pack gloves (latex + work gloves)</li>
        <li>Pack grabber tools / litter pickers</li>
        <li>Pack hand sanitizer</li>
        <li>Pack first aid kit</li>
        <li>Pack sunscreen / bug spray</li>
        <li>Pack water bottles / snacks</li>
        <li>Pack sign-in sheet + pens</li>
        <li>Print this checklist!</li>
    </ul>

    <h2>📍 Arrival & Setup (30 min before)</h2>
    <ul class="checklist">
        <li>Arrive early to scout the area</li>
        <li>Take BEFORE photos (wide shots)</li>
        <li>Set up meeting point with visible sign</li>
        <li>Lay out supplies for volunteers</li>
        <li>Identify hazards to avoid (glass, needles)</li>
        <li>Mark bag collection point</li>
        <li>Test that signup form works on phone</li>
    </ul>

    <h2>👋 Volunteer Check-in</h2>
    <ul class="checklist">
        <li>Greet each volunteer by name</li>
        <li>Sign-in sheet: name + email</li>
        <li>Hand out gloves and bags</li>
        <li>Brief safety talk (2 min max):</li>
        <li>&nbsp;&nbsp;— Don't touch needles or chemicals</li>
        <li>&nbsp;&nbsp;— Work in pairs if possible</li>
        <li>&nbsp;&nbsp;— Stay hydrated</li>
        <li>Assign zones or areas</li>
        <li>Share phone number for emergencies</li>
    </ul>

    <h2>🧹 During the Cleanup</h2>
    <ul class="checklist">
        <li>Take DURING photos (action shots)</li>
        <li>Check on volunteers every 15-20 min</li>
        <li>Keep trash bags accessible</li>
        <li>Note interesting finds for the report</li>
        <li>Count filled bags as they accumulate</li>
        <li>Watch for volunteer fatigue — offer breaks</li>
        <li>Handle any hazardous items carefully</li>
    </ul>

    <h2>📸 Wrap-up (last 15 min)</h2>
    <ul class="checklist">
        <li>Announce "15 minutes left!"</li>
        <li>Collect all filled bags to central point</li>
        <li>Count total bags: <span class="fill-in">&nbsp;</span></li>
        <li>Take AFTER photos (same angles as before)</li>
        <li>Group photo with volunteers</li>
        <li>Thank everyone verbally</li>
        <li>Arrange bag pickup / disposal</li>
        <li>Make sure nothing is left behind</li>
    </ul>

    <h2>📋 After You Leave</h2>
    <ul class="checklist">
        <li>Send thank-you message within 24 hours</li>
        <li>Fill out Post-Event Report template</li>
        <li>Share before/after photos</li>
        <li>Post on social media (with permission)</li>
        <li>Note improvements for next time</li>
    </ul>

    </div>

    <div class="footer">
        Community Cleanup Toolkit — ai-village-agents.github.io/community-cleanup-toolkit<br>
        MIT License — Fork, customize, and use freely!
    </div>
</body>
</html>"""

    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"✅ Printable checklist generated: {output_path}")
    print(f"   Open in a browser and press Ctrl+P (or click the Print button) to print.")
    print(f"   Fill in your event details at the top before printing!")

if __name__ == "__main__":
    output = sys.argv[1] if len(sys.argv) > 1 else "printable-checklist.html"
    generate_printable_checklist(output)
