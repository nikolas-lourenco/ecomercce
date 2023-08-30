terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "your-organization-name"

    workspaces {
      name = "your-workspace-name"
    }
  }
}