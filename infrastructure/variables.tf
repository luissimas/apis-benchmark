variable "project" {
  type = string
}

variable "credentials_file" {
  type = string
}

variable "region" {
  type    = string
  default = "southamerica-east1"
}

variable "zone" {
  type    = string
  default = "southamerica-east1-b"
}

variable "db_user" {
  type = string
}

variable "db_password" {
  type = string
}

variable "local_ip" {
  type = string
}
