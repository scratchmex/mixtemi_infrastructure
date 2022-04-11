#! /bin/sh
kubeseal \
    --controller-namespace sealed-secrets-ns \
    --scope cluster-wide \
    -o yaml \
| sed "/null/d"