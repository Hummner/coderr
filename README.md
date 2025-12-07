🚀 Coderr – Freelance Marketplace Backend (Django REST Framework)

Coderr is a backend API for a freelance marketplace where business users can create service offers and customers can purchase these services. The platform supports user profiles, offers with multiple detail packages, orders, and reviews.

This repository contains the complete backend implementation built with Django and Django REST Framework.

📦 Features

User authentication (Token-based)

Two profile types: Business and Customer

Businesses can create offers with multiple pricing tiers

Customers can place orders

Customers can leave reviews for business users

Permissions ensure only authorized users can perform actions

Filtering, ordering, and pagination for listings

⚙️ Tech Stack

Python 3

Django

Django REST Framework

django-filter

Token Authentication

SQLite/PostgreSQL (depending on setup)

🛠️ Installation

Follow these steps to run Coderr locally:

1️⃣ Clone the repository
git clone https://github.com/Hummner/coderr.git
cd coderr

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the virtual environment

Linux/Mac:

source venv/bin/activate


Windows:

venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Apply database migrations
python manage.py migrate

6️⃣ Create a superuser (admin account)
python manage.py createsuperuser

7️⃣ Run the development server
python manage.py runserver


The API will be available at:

http://127.0.0.1:8000/

🔐 Authentication

Coderr uses Token Authentication.
After logging in, include your token in every request:

Authorization: Token <your_token>

📘 Basic API Structure
Resource	Description
Profiles	Business & Customer profiles
Offers	Created by business users
Offer Details	Pricing tiers/packages
Orders	Customers purchase service packages
Reviews	Customers leave reviews for businesses