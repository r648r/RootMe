#!/bin/bash

site="$1"

methods=("GET" "POST" "PUT" "DELETE" "OPTIONS" "PATCH")

for method in "${methods[@]}"
do
    response=$(curl -X "$method" -sL -w "%{http_code}" "$site")
    grep_result="$(grep "Mot de passe / password" <<< "$response")"
    if [[ -n $grep_result ]]; then
        echo "METHODE HTTP : $method  $grep_result"
    fi
done
