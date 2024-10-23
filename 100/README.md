# 100 - Introduction

# Flask Application

## Summary

This Flask application is a modular web application designed to manage various entities such as Users, Games, Characters, Fields, and Boards. It features a robust backend using SQLAlchemy for database management, Flask-WTF for form handling, and Flask-Bcrypt for secure password hashing. The application supports user registration and login, and allows users to create, read, update, and delete entities through a user-friendly interface.

### Features

- User registration and authentication
- Management of games, characters, fields, and boards
- Categorization of fields using field types
- Responsive forms for creating and editing entities
- Secure password management using bcrypt
- Database migrations using Flask-Migrate

## Getting Started

### Prerequisites

Make sure you have Python 3.x and pip installed on your machine. You will also need a PostgreSQL database set up for the application.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vanHeemstraSystems/flask-motion-picture.git
   cd flask_app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your configuration:

   ```plaintext
   SECRET_KEY='your_secret_key_here'
   DATABASE_URL='postgresql://username:password@localhost:5432/yourdatabase'
   FLASK_DEBUG=True  # Set to 'False' for production environment
   ```

   **WARNING**: For a more secure solution use ```exports``` of variables which then get read into the application instead of storing them in files.

### Database Setup

1. **Create the database:**
   Ensure that your PostgreSQL database is created and accessible.

2. **Run migrations:**

   ```bash
   flask db upgrade
   ```

3. **Seed the database (optional):**

   You can run the seed scripts to populate initial data:

   ```bash
   python seeds/seed_camera_types.py
   python seeds/seed_cameras.py
   python seeds/seed_character_roles.py
   python seeds/seed_field_types.py
   python seeds/seed_fields.py  
   python seeds/seed_player_roles.py
   python seeds/seed_shot_types.py
   python seeds/seed_stories.py
   python seeds/seed_tags.py
   python seeds/seed_user_roles.py
   ```

### Running the Application

1. **Start the Flask application:**

   ```bash
   flask run
   ```

2. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Contributing

Feel free to contribute to this project! Please open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.