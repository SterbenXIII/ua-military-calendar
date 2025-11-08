# UA Military & Defenders Calendar 🇺🇦

[![ICS validated](https://img.shields.io/github/actions/workflow/status/SterbenXIII/ua-military-calendar/validate-ics.yml?label=ICS%20validated)](https://github.com/SterbenXIII/ua-military-calendar/actions)
![Made in Ukraine](https://img.shields.io/badge/Made%20in-Ukraine-0057B7?labelColor=FFD700)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

Public and community-maintained calendar of Ukrainian military, professional, and remembrance days in **ICS** format.

**Languages:** 🇺🇦 Українська · 🇬🇧 English

---

## 🇺🇦 Українською

Публічний календар військових свят, професійних днів та днів пам’яті, пов’язаних із захисниками України.  
Формат: **ICS**, з можливістю підписки по URL 📅

Мета:

- підтримати військових, ветеранів, волонтерів;
- допомогти вчасно вітати й вшановувати захисників;
- мати відкритий, прозорий, версіонований календар, який можна перевірити та доповнювати.

### 🔗 Доступні календарі

1. **Повний календар** — офіційні професійні дні + дні памʼяті:

   `https://raw.githubusercontent.com/SterbenXIII/ua-military-calendar/main/calendars/ua-military-full.ics`

2. **Офіційні професійні дні** (ЗСУ, НГУ, НПУ, ДПСУ, ДСНС тощо):

   `https://raw.githubusercontent.com/SterbenXIII/ua-military-calendar/main/calendars/ua-military-official.ics`

3. **Дні памʼяті та вшанування** (Крути, Небесна Сотня, полеглі захисники тощо):

   `https://raw.githubusercontent.com/SterbenXIII/ua-military-calendar/main/calendars/ua-military-memory.ics`

### ✅ Як підписатися

**Apple Calendar (iOS / macOS)**

1. Відкрийте налаштування Календаря / облікові записи.
2. Оберіть «Додати підписний календар» (Subscribed Calendar).
3. Вставте одну з адрес вище.
4. Збережіть.

**Google Calendar**

1. Зліва: «Інші календарі» → `+` → «За URL-адресою».
2. Вставте адресу відповідного `.ics`.
3. Натисніть «Додати календар».

Після підписки оновлення з цього репозиторію будуть підвантажуватися автоматично (частота залежить від сервісу).

### 📂 Структура репозиторію

- `calendars/ua-military-full.ics` — повний календар (офіційні + памʼятні дні).
- `calendars/ua-military-official.ics` — тільки офіційні професійні дні.
- `calendars/ua-military-memory.ics` — дні памʼяті, вшанування, символічні дати.
- `.github/workflows/validate-ics.yml` — автоматична валідація `.ics` файлів.
- `CONTRIBUTING.md` — правила додавання й оновлення подій.
- `LICENSE` — ліцензія (MIT).

### 📚 Джерела

Дати формуються та перевіряються на основі:

- офіційних указів, законів і повідомлень державних органів;
- офіційних ресурсів сил безпеки та оборони України;
- відкритих публікацій і календарів військових дат з посиланнями на офіційні джерела.

> 🛡️ **Важливо:** цей календар не є офіційним нормативним документом.  
> Якщо ви знаходите неточність, зміни в законодавстві або новий офіційний день — створіть Pull Request з посиланнями на джерела.

### 🤝 Як зробити Pull Request

1. Зробіть форк репозиторію.
2. Оновіть відповідний файл у `calendars/`:
   - використовуйте `DTSTART;VALUE=DATE:YYYYMMDD`,
   - додавайте `RRULE` для щорічних подій,
   - у `SUMMARY` — коротка назва українською без емодзі.
3. У описі PR додайте посилання на офіційні джерела.
4. Переконайтеся, що GitHub Actions (валідація `.ics`) пройшла успішно.

Детальні вимоги дивіться у [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## 🇬🇧 English

The **UA Military & Defenders Calendar** provides public ICS feeds with:

- official professional days of the Armed Forces of Ukraine and other security agencies;
- remembrance and memorial days dedicated to Ukrainian defenders;
- a combined “full” calendar for convenient subscription and integration.

These feeds are useful for:

- NGOs and volunteers,
- journalists and researchers,
- international supporters who want to track key Ukrainian military and remembrance dates.

### 🔗 Available Feeds

- **Full calendar (official + memory)**  
  `https://raw.githubusercontent.com/SterbenXIII/ua-military-calendar/main/calendars/ua-military-full.ics`

- **Official professional days only**  
  `https://raw.githubusercontent.com/SterbenXIII/ua-military-calendar/main/calendars/ua-military-official.ics`

- **Memory & remembrance days**  
  `https://raw.githubusercontent.com/SterbenXIII/ua-military-calendar/main/calendars/ua-military-memory.ics`

### ✅ How to Subscribe

**Apple Calendar / iOS / macOS**

- Add a *Subscribed Calendar* and paste one of the URLs above.

**Google Calendar**

- Go to **Other calendars → + → From URL**, paste the chosen URL.

### 📌 Notes

- This project is **community-maintained** and **not an official legal source**.
- Each change should be supported by reliable sources (laws, presidential decrees, official announcements).
- Contributions are welcome via Pull Requests — see [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## 🔑 License

This project is licensed under the [MIT License](./LICENSE).

You are free to use, copy, modify, and integrate these ICS files in your systems and services, with attribution to the repository and contributors.
Event dates as factual information are not subject to copyright; the structure and curation of this calendar are shared openly.

