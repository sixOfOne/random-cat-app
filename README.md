cat > README.md << 'EOF'
# Random Cat App 🐱

A super simple Flask web app that shows a random cat from [http.cat](https://http.cat) every time you refresh the page.

Built as a lightweight example using:
- Python + Flask
- Docker
- Kubernetes (Minikube because local)

## Features
- Random HTTP status cat images
- Fully containerized
- Easy local Kubernetes deployment

## Quick Start

### Local Development
```bash
docker build -t random-cat-app .
docker run -p 8080:8080 random-cat-app
