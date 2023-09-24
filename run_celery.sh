#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

# Replace * with name of Django Project
su -m myuser -c "celery -A FileUploader worker -l INFO -P solo"