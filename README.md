# Customer Segmentation Using Django

## 📌 Overview
This is a **Django-based web application** that performs **customer segmentation** using **machine learning (Decision Trees & K-Means Clustering)**. The application allows users to **upload CSV files**, process data, and visualize results.

Users can **sign up, log in, and predict customer segmentation**, while **admins manage users and FAQs**.

🔗 **Live Demo:** [Customer Segmentation App](https://customer-segmentation-using-django.onrender.com)

---

## 🚀 Features

### 🔹 **User Panel**
✅ **User Signup & Login**: Secure authentication system  
✅ **Upload CSV Files**: Users can upload CSV files for segmentation  
✅ **Select Columns**: Choose **target** & **index columns** dynamically  
✅ **Segmentation Results**: View **feature importance** & **customer clusters**  
✅ **Download Results**: Users can **download processed results**  
✅ **FAQs**: View frequently asked questions  

### 🔹 **Admin Panel**
✅ **Admin Authentication**: Secure login for admin access  
✅ **Manage Users**: View all registered users  
✅ **Manage FAQs**: Add, update, or delete FAQs  
✅ **Dashboard Overview**: See system statistics and quick access links  

---

## 🖼️ Screenshots

### 📷 Home Page
![Home Page](![Screenshot (7)](https://github.com/user-attachments/assets/c661eed2-6b95-43c1-b8e1-9ba1c36cd32a))



### 📷 Segmentation Results
![Segmentation Results](![Screenshot (8)](https://github.com/user-attachments/assets/b67c7657-98be-4d21-a70c-37f422a62ff6)![Screenshot (9)](https://github.com/user-attachments/assets/a744a40f-d479-4336-8e85-dbe5a9b1b3c9)![Screenshot (10)](https://github.com/user-attachments/assets/bec8f06a-f205-4ee7-b58b-a6d17c4abe0d)


)

---

## 📂 Project Structure

```
customer_segmentation/
│── manage.py  
│── customer_segmentation/ (Main project settings)  
│── app/ (Django application)  
│   ├── migrations/  
│   ├── templates/ (HTML files)  
│   │   ├── base.html  
│   │   ├── userbase.html  
│   │   ├── adminbase.html  
│   │   ├── home.html  
│   │   ├── signup.html  
│   │   ├── userlogin.html  
│   │   ├── adminlogin.html  
│   │   ├── adminhome.html  
│   │   ├── userhome.html  
│   │   ├── segmentation.html  
│   │   ├── segmentation_results.html  
│   │   ├── adminviewusers.html  
│   │   ├── adminviewfaq.html  
│   │   ├── addfaq.html  
│   │   ├── logout.html  
│   ├── static/ (CSS, Images, Videos)  
│   ├── views.py (Application logic)  
│   ├── models.py (Database models)  
│   ├── urls.py (Routing)  
│── static/ (Static assets)  
│── db.sqlite3 (Database)  
│── requirements.txt (Dependencies)  
│── README.md (Project Documentation)  
```

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/kirand2002/customer_segmentation_using_django
cd customer-segmentation
```

### 2️⃣ **Set Up the Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run Migrations**
```sh
python manage.py migrate
```

### 5️⃣ **Start the Development Server**
```sh
python manage.py runserver
```

---

### 🎯 **Live Demo:**  
[Customer Segmentation App](https://customer-segmentation-using-django.onrender.com)  

---

