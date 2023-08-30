variable "ami" {
  type = "string"
  default = "ami-026c8acd92718196b"
}

variable "cdirs_acesso_remoto" {
  type = "list"
  default = ["191.32.154.79/32", "192.32.154.79/32"]
}

variable "key_name" {
  default = "terraform-aws"
}
