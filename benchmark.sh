#!/usr/bin/env sh

duration=5m
results_dir=results
server_name=$1
host=$2

for endpoint in cache db; do
  echo "Starting tests for $endpoint endpoint..."
	curl -s $host/$endpoint >/dev/null
	for connections in 1 10 50 100; do
    echo "$connections connections..."
		mkdir -p $results_dir/$server_name/$endpoint
		bombardier --connections=$connections --duration=$duration --timeout=10s --print=result --format=json $host/$endpoint | jq >$results_dir/$server_name/$endpoint/$connections.json
	done
done

echo "Done."
