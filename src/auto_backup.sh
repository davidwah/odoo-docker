#!/bin/bash

# variabel
BACKUP_DIR=~/Downloads/odoo-backup
ODOO_DATABASE={db_odoo}
ADMIN_PASSWORD={db_pass}

# Buat direktori data-backup
mkdir -p ${BACKUP_DIR}

# Membuat backup
curl -X POST \
    -F "master_pwd=${ADMIN_PASSWORD}" \
    -F "name=${ODOO_DATABASE}" \
    -F "backup_format=zip" \
    -o ${BACKUP_DIR}/${ODOO_DATABASE}.$(date +%F_%T).zip \
    http://localhost:8069/web/database/backup
