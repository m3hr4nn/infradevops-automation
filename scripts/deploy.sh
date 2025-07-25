#!/bin/bash
set -e
echo "[+] Starting Deployment..."

echo "[+] Checking site health..."
python3 scripts/check_sites.py

echo "[+] Running Ansible Playbook..."
ansible-playbook -i ansible/inventory.ini ansible/site.yml

echo "[+] Deployment Completed."
