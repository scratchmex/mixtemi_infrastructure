# Mixtemi Infrastructure

```
|-- apps    <-- apps to deploy
|-- clusters    <-- fluxcd definitions
|-- infra-apps    <-- commons apps for cluster operation: traefik, service mesh, metrics
|-- infra-config    <-- Pulumi config for: dns
```


## apps

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


## clusters

```
clusters
|-- main    <-- only cluster for now
    |-- flux-system    <-- fluxcd installation
    |-- releases.yaml    <-- releases specific to the cluster
```


## infra-apps

```
infra-apps
|-- <appname>.yaml    <-- includes: namespace, release, values, repos/sources
|-- kustomization.yaml
```


## infra-config

```
infra-config
|-- Pulumi.yaml
|-- Pulumi.main.yaml
|-- dns.py
|-- __main__.py
|-- requirements.txt
```


# references

- [Flux v2 Everything that you wanted to know but were afraid to ask (Stefan Prodan)](https://www.youtube.com/watch?v=nGLpUCPX8JE)
