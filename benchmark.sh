#!/usr/bin/env sh

duration=2s
results_dir=results

for port in 3001 3002 3003 3004; do
  echo "Starting tests for server in port $port..."
  for endpoint in db cache; do
    for connections in 1 10 50 100; do
      mkdir -p $results_dir/$port/$endpoint
      bombardier --connections=$connections --duration=$duration --print=result --format=json localhost:$port/$endpoint | jq > $results_dir/$port/$endpoint/$connections.json
    done
  done
  echo "Done."
done
