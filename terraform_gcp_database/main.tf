# main.tf
terraform {
  required_version = ">= 0.14"

  required_providers {
    # Cloud Run support was added on 3.3.0
    google = ">= 3.3"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}


# #############################################
# #          GCP Bucket & Big Query           #
# #############################################
# Create GCS Bucket
resource "google_storage_bucket" "storagebucket" {
  name          = format("%s-traffic-crash-data", var.project_id)
  location      = var.region
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# Create BigQuery Dataset
resource "google_bigquery_dataset" "bigquerydataset" {
  dataset_id = var.bq_dataset_name
  location   = var.region
  delete_contents_on_destroy = true
}