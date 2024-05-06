#!/bin/bash

if [ -f .env ]; then
    echo ".env already exists"
else
    cat <<EOF > .env
ENV=dev
PROJECT_NAME=arxivapi
BACKEND_CORS_ORIGINS="http://localhost,http://localhost:8000"

# Database
DB_USER=arxivapi
DB_PASSWORD=$(openssl rand -hex 16)
DB_DB=arxivapi
DB_HOST=db
DB_PORT=5432

# Nginx
NGINX_HOST=localhost
UPSTREAMS=/:backend:8000
ENABLE_SSL=
CERTBOT_EMAIL=
DOMAIN_LIST=
EOF
    echo "Generated .env file with random DB_PASSWORD"
fi
