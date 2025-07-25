# InfraDevOps Automation

This repository ([m3hr4nn/infradevops-automation](https://github.com/m3hr4nn/infradevops-automation)) provides a ready-to-use automation framework for deploying and monitoring multi-site infrastructure using **Python**, **Bash**, **Ansible**, and **GitLab CI/CD**.

---

## **Project Overview**

This project is designed to:
- Perform **health checks** on multiple sites (via a list of URLs).
- Automate **provisioning and configuration** of infrastructure (e.g., NGINX installation).
- Integrate with **CI/CD pipelines** (GitLab CI/CD) for fully automated deployments.

The default setup includes **4 sample sites**:
```
https://dc1.myservice.com
https://dc2.myservice.com
https://dc3.myservice.com
https://dc4.myservice.com
```
You can modify these to fit your environment.

---

## **Repository Structure**
```
InfraDevOps-Automation/
├── input/
│   └── site_vips.txt       # List of site VIP URLs
├── scripts/
│   ├── check_sites.py      # Python health check script
│   └── deploy.sh           # Bash script for orchestrating checks and deployment
├── ansible/
│   ├── inventory.ini       # Inventory of target servers
│   └── site.yml            # Ansible playbook for provisioning
├── .gitlab-ci.yml          # GitLab CI/CD pipeline configuration
└── README.md               # Project documentation
```

---

## **Quick Start**

### **1. Update Your URLs**
Edit `input/site_vips.txt` to include your site URLs:
```txt
https://yourdomain1.com
https://yourdomain2.com
```

### **2. Configure Ansible Inventory**
Edit `ansible/inventory.ini` to add your servers:
```ini
[sites]
server1.yourdomain.com
server2.yourdomain.com

[all:vars]
ansible_user=your_ssh_user
ansible_ssh_private_key_file=~/.ssh/id_rsa
```

### **3. Run Health Checks**
```bash
cd scripts
python3 check_sites.py
```

### **4. Deploy Infrastructure**
```bash
./scripts/deploy.sh
```
This script will:
- Run the health checks.
- Trigger the Ansible playbook for provisioning.

### **5. Enable CI/CD**
Push this repository to your GitLab instance (or fork this repo if you want to adapt it for GitHub Actions).  
The `.gitlab-ci.yml` will automatically run the health check and deployment stages.

---

## **Key Files to Modify**
- `input/site_vips.txt` → Add your target site URLs.
- `ansible/inventory.ini` → Update server addresses, SSH user, and key.
- `ansible/site.yml` → Adjust tasks for your application or infrastructure.
- `.gitlab-ci.yml` → Update for your CI/CD requirements or environment.

---

## **Tech Stack**
- **Python 3.x** for monitoring.
- **Bash** for automation scripts.
- **Ansible** for configuration management.
- **GitLab CI/CD** for automated pipelines.

---

## **Planned Improvements**
- Add **GitHub Actions workflows** for users on GitHub.
- Extend monitoring (e.g., SSL expiry checks, latency thresholds).
- Add Ansible roles for custom applications.

---

## **License**
This project is released under the MIT License.

---

## **Maintainer**
- **Author:** Mehran Naderizadeh
- GitHub: [m3hr4nn](https://github.com/m3hr4nn)
