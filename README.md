# Locust K8S Demo

## Building Image

```sh
docker build -t locust-k8s-demo .
```

## Running the Demo

```sh
kubectl apply -f ./k8s/
```

## Port Forward

```sh
kubectl port-forward svc/locust-master 8089:8089 --namespace locust-k8s-demo
```

## Test

Go to `http://localhost:8089` in your preferred web browser. The Locust Web UI should be visible there and 4 workers should be connected. The example test sending request to the `echo-server` hosted within the same Kubernetes cluster should be able to start successfully.

## Next Steps

For a more production like deployment an ingress controller should be used instead of just doing `port-forward`. The choice of ingress depends on the cloud provider and there's multiple alternatives. The most common choice is usually to use the AWS ALB Ingress Controller: [Kubernetes Ingress with ALB Ingress Controller](https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/)


