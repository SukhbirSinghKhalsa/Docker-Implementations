# 🚀 Debugging Issues & Fixes

## 1. MySQL Connection Timeout
**Error:**
Can't connect to MySQL server (timed out)

**Cause:**
Used MySQL driver for Azure SQL (MSSQL)

**Fix:**
Switched to MSSQL with pyodbc and port 1433


---

## 2. Missing pyodbc / ODBC Driver
**Error:**
ModuleNotFoundError: No module named 'pyodbc'

**Cause:**
ODBC driver not installed in Docker

**Fix:**
Installed:
- msodbcsql18
- unixodbc
- pyodbc


---

## 3. Login Failed (18456)
**Error:**
Login failed for user 'ssk-admin'

**Cause:**
Incorrect username format

**Fix:**
ssk-admin → ssk-admin@ssk-inc-sql-server-001


---

## 4. Database Not Found (4060)
**Error:**
Cannot open database "dbname"

**Cause:**
Database does not exist / wrong name

**Fix:**
Created and used correct DB:
todo_db


---

## 5. Service Unavailable (503)
**Error:**
503 Service Unavailable

**Cause:**
Containers not in same Docker network

**Fix:**
docker network create mynet  
Run all containers with:
--network mynet


---

## 6. DNS Resolution Error
**Error:**
Could not resolve host: task-service

**Cause:**
Containers not connected to same network

**Fix:**
Used Docker network + service names instead of localhost


---

## 7. 307 Temporary Redirect
**Error:**
307 Temporary Redirect

**Cause:**
Trailing slash mismatch (/tasks vs /tasks/)
Gateway was removing '/'

**Fix:**
Kept consistent routes with trailing slash  
Removed:
if url.endswith("/"): url = url[:-1]


---

## 8. 422 Unprocessable Entity
**Error:**
Validation error / missing fields

**Cause:**
Request body missing required fields

**Fix:**
Send complete payload:
{
  "title": "...",
  "completed": false
}

OR set default in backend model


---

## 9. JSON Forwarding Issue (Gateway)
**Error:**
Input should be a valid dictionary

**Cause:**
Gateway forwarded raw string instead of JSON

**Fix:**
req = client.build_request(method, url, json=json.loads(body.decode()) if body else None)


---

## 🧠 Key Learnings
- Use correct DB driver (MySQL ≠ MSSQL)
- Docker containers need same network
- API routes must match exactly (/ matters)
- Gateway must forward proper JSON
- Debug flow:
  Frontend → Gateway → Service → Database


---

## 🎉 Final Result
✔ Frontend (React) working  
✔ Gateway routing working  
✔ Task & User services working  
✔ Azure SQL connected  
✔ Docker networking fixed  