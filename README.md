# News Website

## Overview
This is a **Django-based News Website** that allows users to view the latest articles and news categorized by topics. It is designed to provide a clean and user-friendly experience for readers to access information quickly and efficiently.

## Features
- **Category-based News:** Users can explore news articles by categories such as Technology, News, Politics, etc.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Search Functionality:** Search for articles by keywords or topics.
- **Admin Panel:** Manage articles, categories, and user accounts through Django’s admin interface.
- **User Authentication:** Secure login and registration for personalized experiences.

## Technologies Used
- **Backend:** Django 5.x, Python 3.x
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default) / MySQL (optional)
- **Other Tools:**
  - Bootstrap for responsive UI
  - Django ORM for database management
  - Python-Decouple for environment variable management

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Esmat434/DjangoNewsApp.git
   cd DjangoNewsApp
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv virtual
   source virtual/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   SECRET_KEY=your-secret-key
   ```

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
   Access the website at `http://127.0.0.1:8000/`.

## How to Use
1. Navigate to the homepage to view the latest news articles.
2. Use the menu to filter articles by category.
3. Admin users can log in to the admin panel at `/admin` to manage content.

## Project Structure
```
NewsWebsite/
|— home/          # Main application containing models, views
|— static/            # Static files (CSS, JS, Images)
|— templates/         # HTML templates
|— db.sqlite3         # SQLite database file
|— manage.py          # Django project management script
|— .env               # Environment variables
|— requirements.txt   # Project dependencies
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them to your fork.
4. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or feedback, please reach out to:
- **Email:** hadelesmatullah@gmail.com
- **GitHub:** [Esmat434](https://github.com/Esmat434)