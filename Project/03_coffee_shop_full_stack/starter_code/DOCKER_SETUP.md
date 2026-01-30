# Docker Setup for Coffee Shop Application

This guide will help you run the Coffee Shop application using Docker containers.

## Prerequisites

- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository** (if not already done)
   ```bash
   git clone <repository-url>
   cd Project/03_coffee_shop_full_stack/starter_code
   ```

2. **Update the .env file** with your Auth0 configuration
   ```bash
   cp .env.template .env
   ```
   Edit the .env file with your actual Auth0 values:
   - AUTH0_DOMAIN: Your Auth0 domain (e.g., your-domain.auth0.com)
   - AUTH0_ALGORITHMS: RS256 (default)
   - AUTH0_API_AUDIENCE: Your API audience (e.g., https://coffee-shop.example.com)
   - FLASK_PORT: 5000 (default)

3. **Build and run the containers**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:8100
   - Backend API: http://localhost:5000

## Docker Compose Services

### backend
- **Image**: Python 3.9 slim
- **Port**: 5000
- **Volume**: Mounts the backend source code for hot reloading
- **Environment Variables**: Read from .env file

### frontend
- **Image**: Node 14 alpine + nginx alpine
- **Port**: 8100
- **Build**: Uses multi-stage build to optimize size
- **Depends On**: backend service

## Network

Both services are connected to a bridge network called `coffee-shop-network` which allows them to communicate with each other.

## Stopping the Containers

To stop the containers, press Ctrl+C in the terminal where docker-compose is running.

To stop and remove the containers, use:
```bash
docker-compose down
```

## Troubleshooting

### Container Not Starting
Check the container logs:
```bash
docker-compose logs backend
docker-compose logs frontend
```

### Hot Reloading
The backend volume is mounted, so changes to the backend code should be reflected without rebuilding the container.

### Updating Dependencies
If you change the requirements.txt or package.json, rebuild the containers:
```bash
docker-compose up --build --no-deps backend
docker-compose up --build --no-deps frontend