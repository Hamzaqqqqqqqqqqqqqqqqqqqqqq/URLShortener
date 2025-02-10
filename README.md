# URL Shortener Service

## Overview
This is a simple URL shortener service built using Django. It allows users to submit a long URL and receive a shortened version. When the shortened URL is accessed, it redirects to the original long URL.

## Features
- *URL Shortening:* Converts long URLs into short, unique codes.
- *Redirection:* Redirects users to the original URL when they access the shortened link.
- *Database Storage:* Stores URL mappings in a database.
- *Validation:* Ensures only valid URLs are shortened.

## Requirements
- Python 3.x
- Django
- SQLite (default) or PostgreSQL (optional)

## Installation & Setup
1. *Clone the repository:*
   git clone https://github.com/your-repo/url-shortener.git
   cd url-shortener
   

2. *Activate a virtual environment:*
   source urlvenv/bin/activate  # On Windows use: urlvenv\Scripts\activate
   

3. *Install dependencies:*
   pip install -r requirements.txt
   

4. *Run database migrations:*
   python manage.py migrate
   

5. *Start the development server:*
   python manage.py runserver
   

## API Endpoints

### 1. Shorten a URL
- *Endpoint:* POST /shorten
- *Request Body:*
  
  {
    "long_url": "https://www.example.com"
  }
  
- *Response:*
  
  {
    "short_url": "http://short.ner/abc123"
  }
  

### 2. Redirect to the Original URL
- *Endpoint:* GET /<short_code>/
- *Example:* Accessing http://127.0.0.1:8000/abc123/ redirects to https://www.example.com.
