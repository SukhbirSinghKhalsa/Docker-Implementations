# 3 Tier To-do Microservices Deployment

## Prerequisites

1. GitHub CLI installed  
To check if it is already installed:
```bash
git --version
```

2. Docker Desktop  
Alternatively, you can use:
- Killercoda  
- A Virtual Machine created on Azure, AWS, or GCP  

To check if Docker is installed:
```bash
docker --version
```

3. An Azure account to create a MySQL server and database.  
Alternatively, if you already have a MySQL database and its connection string, you can use that.

5. Basic understanding of:
- Docker  
- Dockerfile  
- Git commands  
- Azure Cloud  
- MySQL Database CRUD operations  

---

## Project Context

3 tier microservices to-do app is divided into 3 parts:

- Backend database → MySQL  
- Frontend → React  
- Backend → Python  

---

## Steps to get started

### 1. Creating the SQL Server and Database in Azure Cloud

- Login to Azure Portal  
- Search: **SQL Server**  
- Click on **Create New**  

---

### 2. Fill Required Details

Provide the following details:

- Resource Group  
- Server Name  
- Region   

<img width="1849" height="786" alt="image" src="https://github.com/user-attachments/assets/39f707e1-1f3b-4642-952e-b0fae7b34856" />

---

### 3. Authentication Details

- Select: **MySQL Authentication Only**  
- Enter:
  - Admin Login Name  
  - Password
  
<img width="1704" height="540" alt="image" src="https://github.com/user-attachments/assets/78757304-313d-46ac-a174-f25cf5b45373" />

⚠️ Keep the admin login name and password stored safely.  
It will be needed later in the connection string for the backend.

- Connection string from MySQL server will be used in backend  
- Make sure database is accessible (check firewall settings in Azure)  
---

### 4. ARM Template (For Reference)

You can also use ARM Template for automating the MySQL server creation.

Refer to Azure ARM Template documentation for more details.   
https://github.com/SukhbirSinghKhalsa/Docker-Implementations/blob/main/3-tier-todo-microservices/arm_template.md   

### 5. SQL Server

<img width="1905" height="823" alt="image" src="https://github.com/user-attachments/assets/37c3574a-f08a-4170-bb9d-321514988afc" />

