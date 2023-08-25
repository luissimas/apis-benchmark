#!/usr/bin/env sh

duration=5m
results_dir=results_cloud_sql_round_2
host=34.95.137.134
server_name=python-async

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
