#! /bin/sh
kubectl create secret generic SECRET_NAME_____CHANGE_ME \
    -n NAMESPACE_____CHANGE_ME \
    --dry-run=client \
    -o yaml \
    --from-env-file=/dev/stdin \
| sed "/null/d"