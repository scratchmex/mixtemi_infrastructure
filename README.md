# Mixtemi Infrastructure

```
|-- apps    <-- apps to deploy
|-- clusters    <-- fluxcd definitions
|-- infra-apps    <-- commons apps for cluster operation: traefik, service mesh, metrics
|-- infra-config    <-- Pulumi config for: dns
|-- scripts    <-- utils
```


# apps

base resources definitions should point to `default` namespace to monitor leaked apps without proper patches

```
apps
|-- base
|   |-- <appname>
|   |   |-- resources.yaml    <-- includes: repo, release
|   |   |-- kustomization.yaml
|-- prod
|   |-- <appname>
|       |-- values.yaml    <-- patch specific values
|       |-- namespace.yaml    <-- specific namespace definition
|       |-- kustomization.yaml
|   |-- kustomization.yaml
|-- dev
|   |-- <appname>
|       |-- values.yaml    <-- patch specific values
|       |-- namespace.yaml    <-- specific namespace definition
|       |-- kustomization.yaml
|   |-- kustomization.yaml
```


# clusters

```
clusters
|-- main    <-- only cluster for now
    |-- flux-system    <-- fluxcd installation
    |-- releases.yaml    <-- releases specific to the cluster
```


# infra-apps

```
infra-apps
|-- <appname>.yaml    <-- includes: namespace, release, values, repos/sources
|-- <namespace>
|   |-- <appname>.yaml    <-- includes: release, values, repos/sources. Unwrap resources as needed (e.g. common repos)
|   |-- namespace.yaml
|   |-- kustomization.yaml
|-- kustomization.yaml
```


# infra-config

```
infra-config
|-- Pulumi.yaml
|-- Pulumi.main.yaml
|-- dns.py
|-- __main__.py
|-- requirements.txt
```


# scripts

## creation of sealed secrets

```console
cat .env | scripts/create-secret.sh | scripts/seal-secret.sh
```
or
```console
echo "VAR1=VALUE1\n VAR2=VALUE2" | scripts/create-secret.sh | scripts/seal-secret.sh
```


# references

- [Flux v2 Everything that you wanted to know but were afraid to ask (Stefan Prodan)](https://www.youtube.com/watch?v=nGLpUCPX8JE)
- [Manage your Kubernetes clusters with Flux2](https://medium.com/alterway/manage-your-kubernetes-clusters-with-flux2-82dd1cfe2a6a)
- [flux2-kustomize-helm-example](https://github.com/fluxcd/flux2-kustomize-helm-example)