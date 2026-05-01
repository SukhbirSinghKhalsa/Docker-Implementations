# Docker-Implementations
All the docker related projects will be added here

## 3-tier-todo-microservices
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2fc024c8-ad8b-4234-87d4-5a603b8378c9" />

## File Structure
``` bash
│   
└───3-tier-todo-microservices
    │   arm_template.md
    │   instructions.md
    │   debugging.md
    │   
    ├───frontend
    │   │   .env
    │   │   Dockerfile
    │   │   index.html
    │   │   package.json
    │   │   vite.config.js
    │   │   
    │   └───src
    │           App.jsx
    │           main.jsx
    │           
    ├───gateway-service
    │       Dockerfile
    │       main.py
    │       requirements.txt
    │       
    ├───task-service
    │   │   database.py
    │   │   Dockerfile
    │   │   main.py
    │   │   requirements.txt
    │   │   
    │   ├───models
    │   │       task.py
    │   │       
    │   └───routes
    │           task_routes.py
    │           
    └───user-service
        │   Dockerfile
        │   main.py
        │   requirements.txt
        │   
        ├───models
        │       user.py
        │       
        └───routes
                user_routes.py
```
