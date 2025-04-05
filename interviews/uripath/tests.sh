#!/bin/bash

BINARY="./uripath"

function run_test() {
    input="$1"
    echo "Running: $input"
    $BINARY $input
    echo "------------------------"
}

run_test "https://user:pass@example.com:8080/path/to/resource?query=1#fragment"
run_test "ftp://ftp.example.com/resource.txt"
run_test "/home/test/file.txt"
run_test "./README.md"
run_test "notauriwithslashes"
run_test "http://[2001:db8::1]:80/path"
run_test "http://user@host.com"
run_test "http://user:pass@host.com"
