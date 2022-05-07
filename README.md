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

## dns naming scheme

we name each server via a unique short name (e.g. pluto, ceres). Then, we add for each environment:

- `dev`: Development
- `test`: Testing
- `stag`: Staging
- `prod`: Production

There could be special apps, mostly org related, like git, uptime, etc; that we can put in the first level. If the app is server related, then is behind the level of the server name, probaly we would have a wildcard.

At the end we add the unique project name. If multiple deployments for the same app, we add the `-#` suffix. If we need different deployments for api, web, etc, we add it also as a suffix `-api`.

The records of each app points to a server via `CNAME` record. Each server is a `A` record.

examples:
```
pluto.domain.tld    A    123.4.5.6
ceres.domain.tld    A    123.9.9.9

git.domain.tld    CNAME    pluto.domain.tld.

# monitor.pluto.domain.tld    CNAME    pluto.domain.tld.
# traefik.ceres.domain.tld    CNAME    ceres.domain.tld.
*.pluto.domain.tld    CNAME    pluto.domain.tld.
*.ceres.domain.tld    CNAME    ceres.domain.tld.

empanada.dev.domain.tld    CNAME    ceres.domain.tld.
empanada-api.dev.domain.tld    CNAME    ceres.domain.tld.

empanada-2.prod.domain.tld    CNAME    pluto.domain.tld.
empanada-2-api.prod.domain.tld    CNAME    pluto.domain.tld.
```

This way our certificates only will need to be issued with this schema:

```
domain.tld
*.domain.tld
*.pluto.domain.tld
*.dev.domain.tld
*.prod.domain.tld
```


refs:
- [A Proper Server Naming Scheme](https://mnx.io/blog/a-proper-server-naming-scheme/)
- [Naming Schemes](https://namingschemes.com)


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