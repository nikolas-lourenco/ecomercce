# IAM roles and policies
# Uncomment and modify the below content according to your needs
# resource "aws_iam_role" "my_role" {
#   name = "my-role"
#   assume_role_policy = jsonencode({
#     Version = "2012-10-17"
#     Statement = [
#       {
#         Action = "sts:AssumeRole"
#         Effect = "Allow"
#         Principal = {
#           Service = "ec2.amazonaws.com"
#         }
#       }
#     ]
#   })
# }
