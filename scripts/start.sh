#!/bin/bash
echo $SMTP_EMAIL
PROJECT_NAME=mlops \
  MAGE_CODE_PATH=/home/src \
  SMTP_EMAIL=$SMTP_EMAIL \
  SMTP_PASSWORD=$SMTP_PASSWORD \
  docker compose up
