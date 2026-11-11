terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # O backend state deve ficar remoto (ex: S3 + DynamoDB) fora do repositório
  backend "s3" {
    bucket = "fiap-citizens-tfstate-bucket"
    key    = "boca-de-lobo/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "boca_lobo_sg" {
  name        = "boca-lobo-sg-prod"
  description = "Security group restrito para o MVP Boca de Lobo"

  # Porta HTTP publica para a API do Cidadão
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # SSH restrito estritamente a um IP seguro (NUNCA 0.0.0.0/0)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.admin_ip_secured] 
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance "app_server" {
  ami                    = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.boca_lobo_sg.id]

  tags = {
    Name = "CitizenTech-BocaDeLobo-MVP"
  }
}