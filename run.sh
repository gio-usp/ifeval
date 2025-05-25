#!/bin/bash
docker run --rm \
  -v "$(pwd)/responses.jsonl:/app/responses.jsonl" \
  -v "$(pwd)/output:/app/output" \
  ifeval