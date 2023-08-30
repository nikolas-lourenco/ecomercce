# Glue Crawlers and Athena Workgroups
# Uncomment and modify the below content according to your needs
# resource "aws_glue_catalog_database" "my_db" {
#   name = "my-db"
# }
# resource "aws_glue_crawler" "my_crawler" {
#   database_name = aws_glue_catalog_database.my_db.name
#   role          = aws_iam_role.my_role.arn
#   ...
# }
