#!/bin/bash

# AI Pentest Agent with Open WebUI - Quick Start Script
# تشغيل سريع لنظام AI Pentest Agent مع واجهة Open WebUI

echo "🔒 AI Pentest Agent with Open WebUI"
echo "=================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    echo "Visit: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p custom
mkdir -p mongo-init
mkdir -p logs
mkdir -p data/mongodb
mkdir -p data/redis
mkdir -p data/openwebui

# Set permissions
chmod +x start-openwebui.sh
chmod 755 custom/
chmod 755 mongo-init/

echo "✅ Directories created successfully"
echo ""

# Check if configuration files exist
echo "🔧 Checking configuration files..."

if [ ! -f "custom/openai_config.json" ]; then
    echo "❌ custom/openai_config.json not found"
    echo "Please ensure all configuration files are in place"
    exit 1
fi

if [ ! -f "custom/pentest-theme.css" ]; then
    echo "❌ custom/pentest-theme.css not found"
    exit 1
fi

if [ ! -f "custom/functions.py" ]; then
    echo "❌ custom/functions.py not found"
    exit 1
fi

echo "✅ All configuration files found"
echo ""

# Stop any existing containers
echo "🛑 Stopping existing containers..."
docker-compose down 2>/dev/null || true

# Pull latest images
echo "📥 Pulling latest Docker images..."
docker-compose pull

# Build and start services
echo "🚀 Starting AI Pentest Agent with Open WebUI..."
docker-compose up -d

# Wait for services to start
echo "⏳ Waiting for services to start..."
sleep 10

# Check service status
echo "🔍 Checking service status..."
echo ""

# Check Open WebUI
if curl -s http://localhost:3000 > /dev/null; then
    echo "✅ Open WebUI is running at: http://localhost:3000"
else
    echo "❌ Open WebUI failed to start"
fi

# Check API Backend
if curl -s http://localhost:8000 > /dev/null; then
    echo "✅ API Backend is running at: http://localhost:8000"
else
    echo "❌ API Backend failed to start"
fi

# Check MongoDB
if docker exec ai-pentest-mongo mongosh --eval "db.adminCommand('ping')" > /dev/null 2>&1; then
    echo "✅ MongoDB is running at: localhost:27017"
else
    echo "❌ MongoDB failed to start"
fi

# Check Redis
if docker exec ai-pentest-redis redis-cli ping > /dev/null 2>&1; then
    echo "✅ Redis is running at: localhost:6379"
else
    echo "❌ Redis failed to start"
fi

echo ""
echo "🎉 AI Pentest Agent with Open WebUI is ready!"
echo ""
echo "📱 Access Points:"
echo "   • Open WebUI:    http://localhost:3000"
echo "   • API Backend:   http://localhost:8000"
echo "   • MongoDB:       localhost:27017"
echo "   • Redis:         localhost:6379"
echo ""
echo "📚 Quick Start Guide:"
echo "   1. Open http://localhost:3000 in your browser"
echo "   2. Create a new account or sign in"
echo "   3. Select 'AI Pentest Agent' model"
echo "   4. Start your penetration testing session!"
echo ""
echo "🛠️ Management Commands:"
echo "   • View logs:     docker-compose logs -f"
echo "   • Stop services: docker-compose down"
echo "   • Restart:       docker-compose restart"
echo "   • Update:        docker-compose pull && docker-compose up -d"
echo ""
echo "⚠️  Security Reminder:"
echo "   Use this tool responsibly and only on authorized targets!"
echo ""

# Show container status
echo "📊 Container Status:"
docker-compose ps

# Optional: Open browser automatically
if command -v xdg-open &> /dev/null; then
    echo ""
    read -p "🌐 Open browser automatically? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        xdg-open http://localhost:3000
    fi
elif command -v open &> /dev/null; then
    echo ""
    read -p "🌐 Open browser automatically? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open http://localhost:3000
    fi
fi

echo ""
echo "✨ Setup complete! Happy penetration testing!"
