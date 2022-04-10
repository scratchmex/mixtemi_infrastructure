#! /bin/sh
kubeseal \
    --controller-namespace sealed-secrets-ns \
    -o yaml \
| sed "/null/d"