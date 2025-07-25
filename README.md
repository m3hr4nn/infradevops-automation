# InfraDevOps Automation

Automated provisioning and monitoring system for multi-site deployment using Python, Bash, Ansible, and GitLab CI/CD.

## Features

- Python script to check availability and response time of each site.
- Ansible playbook to install & start NGINX on each target host.
- Bash script to run health checks and deploy in sequence.
- GitLab CI/CD pipeline for automation.

## Requirements

- Python 3.x
- Ansible
- GitLab Runner (optional for CI)
- SSH access to all sites with key-based auth

## Usage

1. Add your site URLs in `input/site_vips.txt`
2. Run manually:
   ```bash
   ./scripts/deploy.sh
   ```
3. Or commit to GitLab for CI/CD auto-deployment.

## License

MIT
