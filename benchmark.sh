#!/usr/bin/env sh

duration=5m
results_dir=results_cloud_sql
host=35.199.81.182
server_name=python-async

for endpoint in db; do
  echo "Starting tests for $endpoint endpoint..."
	curl -s $host/$endpoint >/dev/null
	for connections in 1 10 50 100; do
    echo "$connections connections..."
		mkdir -p $results_dir/$server_name/$endpoint
		bombardier --connections=$connections --duration=$duration --timeout=10s --print=result --format=json $host/$endpoint | jq >$results_dir/$server_name/$endpoint/$connections.json
	done
done

echo "Done."
