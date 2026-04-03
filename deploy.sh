#!/usr/bin/env bash
set -euo pipefail

cd /var/www/InaDigiWay

sudo -u deploy git pull origin main
sudo -u deploy bash -lc '
  cd /var/www/InaDigiWay
  set -a
  source /var/www/InaDigiWay/.env
  set +a
  /var/www/InaDigiWay/venv/bin/pip install -r requirements.txt
  /var/www/InaDigiWay/venv/bin/python manage.py migrate
  /var/www/InaDigiWay/venv/bin/python compile_messages.py
  /var/www/InaDigiWay/venv/bin/python manage.py collectstatic --noinput
'
systemctl restart inadigiway-dev.service
systemctl --no-pager --full status inadigiway-dev.service | sed -n '1,30p'
