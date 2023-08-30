output "dev" {
  value = aws_instance.dev[0].public_ip
}
