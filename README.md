# customer_segmentation_using_django


# Customer Segmentation Using Django

## 📌 Overview
This is a **Django-based web application** that performs **customer segmentation** using **machine learning (Decision Trees & K-Means Clustering)**. The application allows users to **upload CSV files**, process data, and visualize results.

Users can **sign up, log in, and predict customer segmentation**, while **admins manage users and FAQs**.

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

## 📂 Project Structure

customer_segmentation/
│── manage.py
│── customer_segmentation/ (Main project settings)
│── app/ (Django application) │ ├── migrations/ │ ├── templates/ (HTML files) │ │ ├── base.html │ │ ├── userbase.html │ │ ├── adminbase.html │ │ ├── home.html │ │ ├── signup.html │ │ ├── userlogin.html │ │ ├── adminlogin.html │ │ ├── adminhome.html │ │ ├── userhome.html │ │ ├── segmentation.html │ │ ├── segmentation_results.html │ │ ├── adminviewusers.html │ │ ├── adminviewfaq.html │ │ ├── addfaq.html │ │ ├── logout.html │ ├── static/ (CSS,Images,videos)
│ ├── views.py (Application logic)
│ ├── models.py (Database models)
│ ├── urls.py (Routing)
│── static/ (Static assets)
│── db.sqlite3 (Database)
│── requirements.txt (Dependencies)
│── README.md (Project Documentation)



## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/kirand2002/customer_segmentation_using_django
cd customer-segmentation


🌍 Live Demo

Click below link to view the live demo
https://customer-segmentation-using-django.onrender.com

📷 Screenshots

![Screenshot (7)](https://github.com/user-attachments/assets/b554ebd1-afbe-4313-9a10-0bd07d07e641)


![Screenshot (8)](https://github.com/user-attachments/assets/1fb3a271-a435-4450-9c44-eb06bc49ed06)

![Screenshot (9)](https://github.com/user-attachments/assets/afc2a978-4ff9-4138-a722-268d29eddb12)

![Screenshot (10)](https://github.com/user-attachments/assets/1633f9c1-726c-48be-b110-57f6083124e4)


🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.
