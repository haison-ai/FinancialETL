resource "aws_s3_bucket" "raw_data" {
  bucket = "bucket_aplha_vin"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
    project     = "Etl project"
  }
}
