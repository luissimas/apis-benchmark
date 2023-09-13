terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project     = var.project
  credentials = file(var.credentials_file)
  region      = var.region
  zone        = var.zone
}

resource "google_compute_instance" "server_instance" {
  name         = "server-instance"
  machine_type = "n1-standard-1"

  metadata_startup_script = file("server_setup.sh")

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  tags = ["allow-http"]
}

resource "google_compute_instance" "client_instance" {
  name         = "client-instance"
  machine_type = "n1-highcpu-4"

  metadata_startup_script = file("client_setup.sh")

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
}

resource "google_sql_database" "database" {
  name     = "database"
  instance = google_sql_database_instance.database_instance.name
}

resource "google_sql_database_instance" "database_instance" {
  name             = "database-instance"
  database_version = "POSTGRES_15"

  settings {
    tier      = "db-custom-4-8192"
    disk_size = 10

    ip_configuration {
      authorized_networks {
        name  = "server"
        value = google_compute_instance.server_instance.network_interface.0.access_config.0.nat_ip
      }

      authorized_networks {
        name  = "local"
        value = var.local_ip
      }
    }
  }

  deletion_protection = false
}

resource "google_sql_user" "example" {
  instance = google_sql_database_instance.database_instance.name
  name     = var.db_user
  password = var.db_password
}

resource "google_compute_firewall" "allow_http_firewall" {
  name    = "allow-http-firewall"
  network = "default"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["allow-http"]
}
