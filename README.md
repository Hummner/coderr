# 🚀 Coderr -- Backend API

## 🧾 Description

Coderr is the **backend API** for a freelance marketplace platform.
Business users can create service offers, and customers can purchase
those services.

This backend is built with **Django** and **Django REST Framework**,
featuring authentication, profiles, offers, orders, and reviews.

📌 **Frontend and backend are in separate repositories.** This
repository contains only the backend code.

------------------------------------------------------------------------

## ✨ Features

-   🔐 Token-based user authentication
-   👤 Business & Customer profiles
-   🛍️ Businesses can create offers with multiple pricing tiers
-   📦 Customers can purchase services
-   ⭐ Customers can rate businesses with reviews
-   🧩 Filtering, searching, ordering, and pagination
-   🔐 Strong permission system for secure actions
-   🧪 Ready for Postman & API testing

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3.10+
-   Django
-   Django REST Framework
-   django-filter
-   Token Authentication
-   SQLite or PostgreSQL

------------------------------------------------------------------------

## 📁 Project Structure

``` plaintext
coderr/
├── auth_app/
├── offer_app/
├── order_app/
├── profile_app/
├── review_app/
│
├── core/              # Django project settings
├── requirements.txt
├── manage.py
└── README.md
```

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/Hummner/coderr.git
cd coderr
```

### 2️⃣ Create a virtual environment

``` bash
python -m venv venv
```

### 3️⃣ Activate the environment

**Windows:**

``` bash
venv\Scripts\activate
```

**macOS / Linux:**

``` bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 5️⃣ Apply database migrations

``` bash
python manage.py migrate
```

### 6️⃣ Create a superuser

``` bash
python manage.py createsuperuser
```

### 7️⃣ Run the server

``` bash
python manage.py runserver
```

Your API is now running at: 👉 http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🔐 Authentication

Coderr uses **Token Authentication**. After logging in, include your
token in every request:

``` http
Authorization: Token your_token_here
```

------------------------------------------------------------------------

## 📘 Main API Modules

-   👤 Profile system
-   🛍️ Offers & Offer Details
-   📦 Orders
-   ⭐ Reviews
-   🔐 Role-based permissions

------------------------------------------------------------------------

## 📄 License

MIT License --- open for personal and commercial use.
