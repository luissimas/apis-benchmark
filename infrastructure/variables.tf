variable "project" {
  description = "GCP project id."
  type        = string
}

variable "credentials_file" {
  description = "GCP service account credentials file path."
  type        = string
}

variable "region" {
  type        = string
  description = "GCP region for all resources."
  default     = "southamerica-east1"
}

variable "zone" {
  type        = string
  description = "GCP zone for all resources."
  default     = "southamerica-east1-b"
}

variable "db_user" {
  description = "Database user."
  type        = string
  default     = "postgres"
}

variable "db_password" {
  description = "Database password."
  type        = string
}

variable "local_ip" {
  description = "Local machine IP address."
  type        = string
}
