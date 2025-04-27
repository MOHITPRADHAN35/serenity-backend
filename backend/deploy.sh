#!/bin/bash

# Step 1: Set your Cloud Run service name
SERVICE_NAME="serenity-backend"

# Step 2: Set your region
REGION="us-central1"

# Step 3: Deploy using current directory
gcloud run deploy $SERVICE_NAME \
    --source . \
    --region $REGION \
    --platform managed \
    --allow-unauthenticated \
    --port 8080

