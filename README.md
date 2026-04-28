## 📦 GOIT CS HW-06
Simple web application without frameworks using:
- HTTP server (Python)
- Socket server (TCP)
- MongoDB
- Docker + Docker Compose

## 🚀 Project Features
Pure Python HTTP server (no frameworks)
Routing for pages:
/ → index page
/message → form page
404 error page
- Static file handling (CSS, images)
- Form submission via HTTP → Socket
- TCP socket server for processing data
- MongoDB storage with timestamps
- Dockerized environment

## Build and start project
```
docker-compose up --build
```

## 2. Open in browser
```
http://localhost:3000
```

## ✉️ How it works
Open /message page
Submit form (username + message)
Data flow:
```
Browser → HTTP server → Socket server → MongoDB
```
Message is stored with timest

Each record looks like:
```
{
  "username": "John",
  "message": "Hello world",
  "date": "2026-04-28T12:34:56"
}
```

## 🛑 Stop project
```
docker-compose down
```

## ⚙️ Requirements

Docker
Docker Compose
