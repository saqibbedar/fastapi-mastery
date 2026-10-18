# Local Deployment Pipeline

```bash
# build docker image
docker build -t fastapi-project-5:v1 . # or: (ubuntu) docker build --network=host -t fastapi-project-5:v1 .

# run docker image
docker run --rm -it --network=host --env-file .env fastapi-project-5:v1

# create kind cluster
kind create cluster --name local-cluster

# 1. Push your built image into the cluster memory space
kind load docker-image fastapi-project-5:v1 --name local-cluster

# 1.1 verify the image is present in the KinD node
docker exec -it local-cluster-control-plane crictl images | grep fastapi-project-5

# 2. Deploy your application pods to the cluster
kubectl apply -f deployment.yaml

# 2.1 Check the pods status
kubectl get pods -l app=fastapi-project-5         # you should see 2 pods with status running

# 2.2 check logs to ensure the database connected
kubectl logs -l app=fastapi-project-5 --tail=50

# 3. Create a temporary bridge to access it locally on port 8000
kubectl port-forward deployment/fastapi-project-5-deployment 8000:8000
```