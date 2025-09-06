# FOSSEE Workshop Booking — UI/UX Enhancement

**Project:** FOSSEE Python Screening Task 1 — UI/UX Enhancement

**Author:** Ayush Mann — [@AyushMann29](https://github.com/AyushMann29)

---

## Overview

This repository contains my UI/UX enhancement for the **FOSSEE Workshop Booking** project. **Important:** this is a Django application — there is no external `index.html`. I made changes to the existing Django templates, static files (CSS/JS), and views to improve the mobile-first UI/UX while keeping the core backend structure intact.

The main login page for the project (after running the server) is:

```
http://127.0.0.1:8000/workshop/login
```

---

## Demo / Preview

<img width="1919" height="1032" alt="Screenshot 2025-09-06 143027" src="https://github.com/user-attachments/assets/857dce42-1d59-4020-8531-f8600d2de600" />
<img width="1919" height="993" alt="Screenshot 2025-09-06 143039" src="https://github.com/user-attachments/assets/6d1dcf30-13a4-46b2-bead-0a024a66a84a" />
<img width="1919" height="997" alt="Screenshot 2025-09-06 143046" src="https://github.com/user-attachments/assets/189983ae-5b78-4f33-aa44-fb64c8811907" />
<img width="1919" height="996" alt="Screenshot 2025-09-06 143054" src="https://github.com/user-attachments/assets/2a6fcaa7-242d-455a-bde3-0af0b1c8e97e" />
<img width="390" height="856" alt="Screenshot 2025-09-06 143112" src="https://github.com/user-attachments/assets/257a96e6-0f08-4075-b40b-473df90efada" />
<img width="384" height="856" alt="Screenshot 2025-09-06 143118" src="https://github.com/user-attachments/assets/30f18826-0be8-4d12-b93a-18a5b3318a13" />
<img width="388" height="856" alt="Screenshot 2025-09-06 143323" src="https://github.com/user-attachments/assets/2155ef93-c9ab-4245-a6b7-a9efb0af0bf7" />
<img width="393" height="860" alt="Screenshot 2025-09-06 143331" src="https://github.com/user-attachments/assets/6088a5a6-7454-4883-951b-24dd3a13b6e5" />
<img width="388" height="852" alt="Screenshot 2025-09-06 143451" src="https://github.com/user-attachments/assets/3c3b527f-d2a4-4c4e-bde3-1bd5000a8859" />
<img width="389" height="861" alt="image" src="https://github.com/user-attachments/assets/8995c7ae-c5e0-4b77-af2d-f861dae7bdb0" />
<img width="391" height="863" alt="image" src="https://github.com/user-attachments/assets/fdf88245-c18c-4e9f-af7d-a90cfc30dcc9" />
<img width="382" height="853" alt="image" src="https://github.com/user-attachments/assets/dfaeea4e-b06f-47fb-901e-29f14ac335ba" />


---

## Guide to install and get this website running

### Follow the steps below

> **NOTE**: Use Python 3

1. **Clone this repo**:

```bash
git clone https://github.com/FOSSEE/workshop_booking.git
cd workshop_booking
```

2. **Create a virtual environment and install required packages**:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
# on Windows PowerShell use: venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. **Make migrations and migrate**:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create superuser**:

```bash
python manage.py createsuperuser
```

5. **Start the development server**:

```bash
python manage.py runserver
```

6. **Admin page**: open `http://127.0.0.1:8000/admin` and login using the superuser credentials.

7. **Groups**: In the admin panel, go to *Groups* and create a group called `instructor` and assign the required permissions to it.

8. **Set user roles**: By default new users are assigned a coordinator role. Using the admin panel, update the required users' profile position to `instructor` and add them to the `instructor` group with the appropriate permissions.

9. **Check settings**: Open `settings.py` and ensure required variables (for example `DATABASES`, `SECRET_KEY`, `ALLOWED_HOSTS`, static/media settings, email settings if used) are configured for your environment.

### Instructor specific steps

1. An instructor can create workshops as per his/her availability in the **Create Workshop** tab.
2. An instructor can see monthly workshop count, upcoming workshops, etc. under **Statistics > Workshop Statistics**.
3. Instructors can view and post comments on a coordinator's profile from **Profile Statistics** or **Workshop Status** pages.

### Coordinator specific steps

1. A coordinator can send a workshop proposal under **Workshops > Propose a Workshop**.

> **Main page / Login**: After starting the server, the main page (login) is located at:

`http://127.0.0.1:8000/workshop/login`

---

## What I changed (high level)

* Reworked layout to be **mobile-first** and responsive.
* Improved typography, spacing, and visual hierarchy for faster scanning on small screens.
* Redesigned the booking table for mobile (stacked / card-style rows) to improve legibility.
* Ensured form elements (inputs, buttons) are large enough for comfortable tapping.
* Minimized assets (used SVGs / CSS where possible) to keep load times fast.
* Ensured accessible contrast and keyboard navigability.

---

## Design Reasoning

These are the answers requested in the task brief — include them in your README so reviewers see your thought process.

### 1. What design principles guided your improvements?

* **Mobile-first design:** I prioritized the smallest screen widths first and progressively enhanced for larger screens.
* **Clear visual hierarchy:** Larger, bolder headings and clear spacing help users quickly scan and find actions (e.g., Book, Register, Login).
* **Simplicity & affordance:** Controls (buttons, inputs) are visually obvious and sized for touch.
* **Accessibility-first:** High contrast, readable font sizes, and clear focus styles.

### 2. How did you ensure responsiveness across devices?

* **CSS Flexbox and grid** were used for layout so components naturally reflow.
* **Relative units** (%, rem, em) ensure components scale across resolutions.
* **Media queries** adjust the UI at common breakpoints; on small screens tables become stacked card-like views.
* **Full-width tappable controls** on mobile for easy interaction.

### 3. What trade-offs did you make between design and performance?

* I avoided large UI frameworks (e.g., full Bootstrap bundle) in favor of lightweight, custom CSS to reduce payload size.
* Minimal images and use of inline SVGs reduce HTTP requests and improve load times.
* Some micro-interactions (heavy JS animations) were intentionally omitted to favour snappy performance on low-end devices.

### 4. What was the most challenging part and how did you approach it?

* **Making the table usable on mobile**: Traditional tables are hard to read on small screens. I converted rows into stacked card-like blocks via CSS at smaller viewports, and added label text to each cell for clarity. I also used `aria` attributes to help screen readers.

---

## Accessibility & Performance Notes

* Use `rel="preload"` for important fonts if you add custom fonts.
* Keep images compressed and use modern formats (WebP) if needed.
* Use semantic HTML (`<header>`, `<main>`, `<nav>`, `<button>`) to improve accessibility.
* Add `alt` text for all images and ensure color contrast is WCAG friendly.

---


## Contact

Repository owner: [@AyushMann29](https://github.com/AyushMann29)

---
