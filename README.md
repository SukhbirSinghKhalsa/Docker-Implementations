# Docker-Implementations
All the docker related projects will be added here

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