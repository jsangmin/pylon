# Development Guide

## Recommended Workflow (Fastest Loop)
For daily development (coding, debugging), use the **Hybrid Approach**:

1.  **Database**: Run via Docker Compose.
    ```bash
    docker-compose up -d
    ```
    - Provides a consistent, isolated database environment.
    - No need to install PostgreSQL on your host machine.

2.  **Application**: Run Locally (Python).
    ```bash
    source venv/bin/activate
    uvicorn app.main:app --reload
    ```
    - **Pros**:
        - **Hot Reload**: Changes are reflected instantly.
        - **Debugging**: IDE debuggers work natively.
        - **Speed**: No image build time.

## Verification & Deployment Workflow
Use **Kubernetes (k8s)** when you want to verify the deployment configuration or simulate production.

1.  **Build Image**:
    ```bash
    docker build -t fastapi-example:latest .
    ```

2.  **Deploy to local k8s**:
    ```bash
    kubectl apply -f k8s/
    ```

## Comparison

| Feature | Local + Docker DB | Full Docker/k8s |
| :--- | :--- | :--- |
| **Code Changes** | Instant (Hot Reload) | Slow (Rebuild & Redeploy) |
| **Debugging** | Easy (IDE Support) | Harder (Remote Debug) |
| **Environment** | Host Dependencies | Isolated |
| **Use Case** | **Development** | **Staging/Production** |
