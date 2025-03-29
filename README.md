# DailyApp

**DailyApp** is a web-based daily dashboard built with Flask and styled in HTML/CSS. It fetches and displays a daily quote, notable historical events, famous births and deaths, all styled in a modern, responsive layout. This project was created as part of a 14-day Python learning challenge.

---

## Features

- Displays the current day and date.
- Fetches the quote of the day from the ZenQuotes API.
- Lists 3 historical events that happened on this day.
- Highlights 3 notable births and 3 notable deaths.
- Responsive 2×2 grid layout that adapts for mobile.
- Dark-themed design with soft hover effects and visual polish.
- Hosted online and embeddable into GitHub Pages via `<iframe>`.

---

## How It Works

1. The Flask app makes two API requests:
   - One for the quote of the day.
   - One for historical events, births, and deaths.
2. The data is passed into a Jinja2 template.
3. The frontend renders it in a fully styled HTML grid.
4. Hosted via PythonAnywhere and embedded on GitHub Pages.

---



## Running Locally

To run the app on your local machine:

```bash
pip install flask requests
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Live Demo

Hosted on [PythonAnywhere](https://yourusername.pythonanywhere.com)  
Embedded via GitHub Pages at: `https://yourusername.github.io/daily.html`

---

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5 + CSS3 (responsive grid)
- **APIs:** ZenQuotes, Today API

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

##  Author

Created by [Trevor Browning](https://github.com/TrevorBrowning)