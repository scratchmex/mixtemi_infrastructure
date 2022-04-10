# Mixtemi Infrastructure

```
|-- apps    <-- apps to deploy
|-- clusters    <-- fluxcd definitions
|-- infra-apps    <-- commons apps for cluster operation: traefik, service mesh, metrics
|-- infra-config    <-- Pulumi config for: dns
```


## apps

```
apps
|-- base
|   |-- <appname>.yaml    <-- includes: repo, namespace, release
|   |-- kustomization.yaml
|-- prod
|   |-- <app-releasename>-values.yaml    <-- patch specific values
|   |-- kustomization.yaml
|-- dev
|   |-- <app-releasename>-values.yaml    <-- patch specific values
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
|-- <appname>.yaml    <-- includes: namespace, release, values
|-- repos.yaml    <-- all repos/sources
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
