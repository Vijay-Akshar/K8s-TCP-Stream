# K8s-TCP-Stream
A scalable, distributed client-server system using Python, Docker, and Kubernetes. This project implements a TCP-based architecture where multiple clients continuously stream data to a server inside a Kubernetes-managed environment.

### Features
- Distributed TCP Communication: Clients connect to the server over a TCP socket.
- Automated Scaling & Recovery: Kubernetes ensures high availability and automatic pod recovery.
- Containerized Deployment: Uses Docker for portable and reproducible environments.
- Efficient Keep-Alive Mechanism: Clients send periodic heartbeat messages to maintain connectivity.

---

## How It Works
### 1. Server
The server:
- Listens on port 12345 for incoming TCP connections.
- Accepts connections from multiple clients.
- Logs messages received from clients.
- Handles keep-alive signals from clients to maintain persistent connections.

### 2. Clients
- The even-number client sends even numbers to the server.
- The odd-number client sends odd numbers to the server.
- Each client also sends a keep-alive signal every 10 seconds to ensure the connection remains active.

---

## Containerization (Docker)
Each component (server & clients) is containerized using Docker.

To build Docker images:
```sh
docker build -t akshar-server -f Server/Server_Dockerfile .
docker build -t akshar-client-even -f Client_Even/Client_even_Dockerfile .
docker build -t akshar-client-odd -f Client_Odd/Client_odd_Dockerfile .
```

---

## Kubernetes Orchestration
### 1. Deploying the Server
The server is deployed using a Kubernetes Deployment, which ensures it runs in a container and restarts if it fails.

### 2. Creating a Service for the Server
A Kubernetes Service is used to expose the server within the cluster so clients can connect.

### 3. Deploying Clients
Each client runs in its own pod and connects to `server-service`.

---

## Getting Started
### 1. Prerequisites
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Kubernetes (`kubectl`)](https://kubernetes.io/docs/tasks/tools/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

### 2. Start Minikube and Set Up Kubernetes
```sh
minikube start --driver=docker
kubectl create namespace akshar
```

### 3. Build and Deploy Containers
```sh
docker build -t akshar-server -f Server/Server_Dockerfile .
docker build -t akshar-client-even -f Client_Even/Client_even_Dockerfile .
docker build -t akshar-client-odd -f Client_Odd/Client_odd_Dockerfile .
```

### 4. Apply Kubernetes Deployments
```sh
kubectl apply -f K8s/server_deployment.yaml -n akshar
kubectl apply -f K8s/client_even_deployment.yaml -n akshar
kubectl apply -f K8s/client_odd_deployment.yaml -n akshar
kubectl apply -f K8s/server_service.yaml -n akshar
```

### 5. Monitor Logs
```sh
kubectl logs -l app=server -n akshar --follow
kubectl logs -l app=client-even -n akshar --follow
kubectl logs -l app=client-odd -n akshar --follow
```

---

## Contributing
Feel free to submit issues or create pull requests to improve this project.

---

## License
This project is open-source and available under the MIT License.
