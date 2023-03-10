# Apache Airflow in Kubernetes

All credit goes to Yuyu Lin

## Zero to Hero Installation on execution on Windows (WSL) and Mac

### Installation on WSL

1. Install Ubuntu 22.04 https://learn.microsoft.com/en-us/windows/wsl/install
2. Install VSCode https://code.visualstudio.com/docs/remote/wsl
3. Install minikube 
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start
```
4. Install helm
```
snap install helm --classic
wget https://get.helm.sh/helm-v3.8.2-linux-amd64.tar.gz
tar xvf helm-*-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin
```
5. Change the values.yaml to reflect your flow repository
```
vi values.yaml
helm install airflow .
```
6. Run VSCode
```
code .
```
7. Forward the port
```
kubectl port-forward --namespace default svc/airflow 8080:8080 &
```
8. Bring up Apache Airflow Kubernetes visualizations http://localhost:8080/home
