#!/usr/bin/env python3
"""
Zigma 360 Automation Client — Sifab AS

Automates common Zigma ERP tasks:
  - Create new sales projects (Salgsprosjekt)
  - Add project lines with pricing
  - Navigate between views

Requirements: pywinauto, Pillow
Usage:
    python tools/zigma_client.py screenshot              — Take screenshot of Zigma
    python tools/zigma_client.py new-project <json>      — Create a new project from JSON
    python tools/zigma_client.py list-projects            — Screenshot current project list
"""

import sys
import time
import json
import os
from pathlib import Path
from datetime import datetime

try:
    from pywinauto import Application, Desktop
    from pywinauto.keyboard import send_keys
except ImportError:
    print("Installer pywinauto: python -m pip install pywinauto")
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = REPO / "temp"
SCREENSHOT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# Connection helpers
# ---------------------------------------------------------------------------

def find_zigma_window():
    """Find the main Zigma 360 window."""
    desktop = Desktop(backend="win32")
    for w in desktop.windows():
        title = w.window_text()
        if title == "SIFAB AS":
            pid = w.element_info.process_id
            # Verify it's actually Zigma by checking class name
            cls = w.class_name()
            if "WindowsForms10" in cls:
                return w
    return None


def connect():
    """Connect to the running Zigma 360 instance and return (app, window)."""
    win = find_zigma_window()
    if not win:
        print("ERROR: Zigma 360 is not running or window not found.")
        print("Start Zigma 360 and try again.")
        sys.exit(1)
    handle = win.handle
    app = Application(backend="win32").connect(handle=handle)
    window = app.window(handle=handle)
    return app, window


def focus(win):
    """Bring Zigma window to foreground."""
    win.set_focus()
    time.sleep(0.3)


def screenshot(win, name=None):
    """Take a screenshot of the Zigma window. Returns the file path."""
    img = win.capture_as_image()
    if name is None:
        name = f"zigma_{datetime.now().strftime('%H%M%S')}"
    path = SCREENSHOT_DIR / f"{name}.png"
    img.save(str(path))
    return str(path)


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

# Toolbar button approximate X positions (from left edge of window)
TOOLBAR = {
    "lukk": 30,
    "redigeringsmodus": 100,
    "lagre": 150,
    "angre": 178,
    "slett_prosjekt": 225,
    "legg_til_prosjekt": 275,
    "rediger_prosjekt": 325,
    "oppdater": 420,
    "utskrift": 475,
    "handlinger": 595,
    "sok": 640,
    "endre_prosjektfase": 700,
}
TOOLBAR_Y = 65

# Right sidebar menu approximate Y positions
SIDEBAR = {
    "salgsprosjekt": 135,
    "service": 153,
    "utgaende_faktura": 169,
    "salgsrapport": 187,
    "innkjop": 695,
    "kontakter": 710,
    "artikler": 725,
}
SIDEBAR_X = 1150

# Filter tabs approximate X positions
FILTER_TABS = {
    "alle": 25,
    "mal": 50,
    "tilbudsarkiv": 100,
    "forespørsel": 160,
    "tilbud": 210,
    "ordre": 250,
    "klar_delfakt": 310,
    "klar_fakt": 390,
    "ferdig": 440,
}
FILTER_Y = 100


def click_toolbar(win, button_name):
    """Click a toolbar button by name."""
    x = TOOLBAR.get(button_name)
    if x is None:
        print(f"Unknown toolbar button: {button_name}")
        return False
    focus(win)
    win.click_input(coords=(x, TOOLBAR_Y))
    time.sleep(0.5)
    return True


def click_sidebar(win, menu_name):
    """Click a sidebar menu item by name."""
    y = SIDEBAR.get(menu_name)
    if y is None:
        print(f"Unknown sidebar menu: {menu_name}")
        return False
    focus(win)
    win.click_input(coords=(SIDEBAR_X, y))
    time.sleep(1)
    return True


def navigate_to_project_list(win):
    """Navigate to the Salgsprosjekt list view."""
    focus(win)
    # Click the Velkommen tab first to reset, then Salgsprosjekt
    # Or directly click Salgsprosjekt in sidebar
    click_sidebar(win, "salgsprosjekt")
    time.sleep(1)
    return True


def type_text(win, text, clear_first=True):
    """Type text into the currently focused field."""
    if clear_first:
        send_keys("^a")
        time.sleep(0.1)
    send_keys(text, with_spaces=True, pause=0.02)
    time.sleep(0.1)


def tab_next():
    """Press Tab to move to next field."""
    send_keys("{TAB}")
    time.sleep(0.2)


def press_enter():
    """Press Enter."""
    send_keys("{ENTER}")
    time.sleep(0.3)


def press_escape():
    """Press Escape."""
    send_keys("{ESCAPE}")
    time.sleep(0.2)


# ---------------------------------------------------------------------------
# Project creation
# ---------------------------------------------------------------------------

def create_project(win, project_data: dict):
    """
    Create a new sales project in Zigma.

    project_data keys:
        name        — Project name/description (required)
        customer    — Customer/company name (required)
        contact     — Contact person name
        currency    — NOK, USD, EUR, GBP (default: NOK)
        delivery    — Delivery terms
        reference   — Your/their reference

    Returns the SP-number of the created project (if detectable).
    """
    name = project_data.get("name", "")
    customer = project_data.get("customer", "")

    if not name or not customer:
        print("ERROR: 'name' and 'customer' are required fields.")
        return None

    focus(win)

    # Step 1: Ensure we're in the project list
    print("Navigating to project list...")
    navigate_to_project_list(win)
    time.sleep(1)

    # Step 2: Enable edit mode if not already
    print("Enabling edit mode...")
    click_toolbar(win, "redigeringsmodus")
    time.sleep(0.5)

    # Step 3: Click 'Legg til prosjekt'
    print("Creating new project...")
    click_toolbar(win, "legg_til_prosjekt")
    time.sleep(1.5)

    # Step 4: Take screenshot to see current state
    path = screenshot(win, "new_project_created")
    print(f"Screenshot: {path}")

    # Step 5: The new project row should be selected in the grid.
    # The project name field in the grid row should be editable.
    # Type the project name.
    print(f"Setting project name: {name}")
    # The new row should have the name column active — type directly
    type_text(win, name)
    tab_next()

    # Step 6: Now we need to set the customer.
    # The 'Firma' (Company) column might be next, or we may need
    # to navigate to the bottom 'Felter' tab.
    # For now, take a screenshot to show the user what happened.
    path = screenshot(win, "after_name_entry")
    print(f"Screenshot after name: {path}")

    # Step 7: Save
    print("Saving...")
    click_toolbar(win, "lagre")
    time.sleep(1)

    path = screenshot(win, "after_save")
    print(f"Final screenshot: {path}")

    return True


def add_project_line(win, line_data: dict):
    """
    Add a project line to the currently open project.

    line_data keys:
        name        — Line item description (required)
        quantity    — Quantity (default: 1)
        unit_price  — Override price (Overstyrt pris)
        cost        — Cost price (Kost)
        currency    — NOK, USD, etc.
    """
    name = line_data.get("name", "")
    if not name:
        print("ERROR: 'name' is required for project line.")
        return False

    focus(win)

    # Navigate into the project's Prosjektlinjer view
    # Assume we're already looking at a project's lines

    # Click 'Legg til prosjektlinje'
    print(f"Adding project line: {name}")
    click_toolbar(win, "legg_til_prosjekt")  # Reuses same position in line view
    time.sleep(1)

    # Type line name
    type_text(win, name)
    tab_next()

    # Take screenshot
    path = screenshot(win, "new_line_added")
    print(f"Screenshot: {path}")

    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def cmd_screenshot():
    """Take and display a screenshot of Zigma."""
    _, win = connect()
    focus(win)
    path = screenshot(win)
    print(f"Screenshot saved: {path}")


def cmd_new_project(json_str):
    """Create a new project from JSON data."""
    data = json.loads(json_str)
    _, win = connect()
    create_project(win, data)


def cmd_list_projects():
    """Navigate to project list and take screenshot."""
    _, win = connect()
    navigate_to_project_list(win)
    time.sleep(1)
    path = screenshot(win, "project_list")
    print(f"Project list screenshot: {path}")


def cmd_inspect():
    """Inspect visible controls in Zigma for debugging."""
    _, win = connect()
    focus(win)

    def dump_visible(ctrl, depth=0, max_depth=4):
        if depth > max_depth:
            return
        txt = ctrl.window_text()[:100]
        cls = ctrl.class_name()
        rect = ctrl.rectangle()
        w = rect.right - rect.left
        h = rect.bottom - rect.top
        if rect.left >= 0 and rect.top >= 0 and w > 10 and h > 10:
            if txt or "EDIT" in cls or "BUTTON" in cls or "COMBO" in cls:
                indent = "  " * depth
                print(f'{indent}[{cls[-35:]}] "{txt}" ({rect.left},{rect.top} {w}x{h})')
        for child in ctrl.children():
            dump_visible(child, depth + 1, max_depth)

    dump_visible(win)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "screenshot":
        cmd_screenshot()
    elif cmd == "new-project":
        if len(sys.argv) < 3:
            print('Usage: zigma_client.py new-project \'{"name": "...", "customer": "..."}\'')
            sys.exit(1)
        cmd_new_project(sys.argv[2])
    elif cmd == "list-projects":
        cmd_list_projects()
    elif cmd == "inspect":
        cmd_inspect()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
