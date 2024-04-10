#!/bin/bash

SUCCESSFUL_CASES=(
    "martincastro@gmail.com"
    "martincastro105@gmail.com"
    "martin-castro.10.5@gmail.com"
    "martin_castro@mail.google.com"
    "martincastro.10.5@mail.google.com"
    "martincastro+1@gmail.com"
    "martincastro.10.5+1@gmail.com"
    "martincastro.10.5+1@gmail.com.es"
    "martin-castro.10.5+1@gmail.com.ar"
    "martincastro@gmail.net"
    "martin.castro@gmail.com"
    "martincastro@Gmail.com"
)

UNSUCCESSFUL_CASES=(
    "martincastro"
    "martincastrogmail.com"
    "martincastro@gmail"
    "martincastro@@gmail.com"
    "martincastro@gmail.com."
    ".martincastro@gmail.com"
    "martin castro@gmail.com"
    "martin-castro/@gmail.com"
    "martincastro@/gmail.com"
    "martin_castro@gmailcom"
    "martincastro.@gmail.com"
    "martin--castro@gmail.com"
)

PYTHON_SCRIPT="emailAfn.py"

check_email() {
    email=$1
    type=$2
    python3 "$PYTHON_SCRIPT" "$email" >/dev/null 2>&1
    exit_status=$?
    if [[ "$type" == "success" && $exit_status -ne 0 ]]; then
        echo "Test failed for expected successful case: $email"
    elif [[ "$type" == "fail" && $exit_status -eq 0 ]]; then
        echo "Test failed for expected unsuccessful case: $email"
    elif [[ "$type" == "fail" ]]; then
        echo "Email '$email' rejected as expected."
    else
        echo "Email '$email' accepted as expected."
    fi
}

for email in "${SUCCESSFUL_CASES[@]}"; do
  check_email "$email" "success"
done

for email in "${UNSUCCESSFUL_CASES[@]}"; do
  check_email "$email" "fail"
done
