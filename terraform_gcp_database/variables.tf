variable "project_id" {
  type        = string
  description = "The name of the project"
}

variable "region" {
  type        = string
  description = "The default compute region"
}

variable "zone" {
  type        = string
  description = "The default compute zone"
}

variable "bq_dataset_name" {
  type = string
  description = "BigQuery Dataset"
  default = "processed_data"
}
