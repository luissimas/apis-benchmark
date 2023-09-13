output "server_ip" {
  value = google_compute_instance.server_instance.network_interface.0.access_config.0.nat_ip
}

output "client_ip" {
  value = google_compute_instance.client_instance.network_interface.0.access_config.0.nat_ip
}

output "database_ip" {
  value = google_sql_database_instance.database_instance.ip_address.0.ip_address
}
