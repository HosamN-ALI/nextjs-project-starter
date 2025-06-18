// MongoDB Initialization Script for AI Pentest Agent

// Switch to the ai_pentest database
db = db.getSiblingDB('ai_pentest');

// Create collections
db.createCollection('pentest_sessions');
db.createCollection('audit_logs');
db.createCollection('user_preferences');
db.createCollection('pentest_reports');
db.createCollection('tool_configurations');

// Create indexes for better performance
db.pentest_sessions.createIndex({ "user_id": 1, "created_at": -1 });
db.pentest_sessions.createIndex({ "session_id": 1 }, { unique: true });
db.audit_logs.createIndex({ "timestamp": -1 });
db.audit_logs.createIndex({ "user_id": 1, "action": 1 });
db.pentest_reports.createIndex({ "session_id": 1 });
db.pentest_reports.createIndex({ "target_domain": 1, "created_at": -1 });

// Insert default tool configurations
db.tool_configurations.insertMany([
    {
        "tool_name": "nmap",
        "category": "network",
        "risk_level": "low",
        "default_options": "-sV -sC -T4",
        "description": "Network discovery and security auditing",
        "documentation_url": "https://nmap.org/docs.html",
        "created_at": new Date()
    },
    {
        "tool_name": "sqlmap",
        "category": "web",
        "risk_level": "medium",
        "default_options": "--batch --crawl=2",
        "description": "Automatic SQL injection and database takeover tool",
        "documentation_url": "https://sqlmap.org/",
        "created_at": new Date()
    },
    {
        "tool_name": "nikto",
        "category": "web",
        "risk_level": "low",
        "default_options": "-h",
        "description": "Web server scanner",
        "documentation_url": "https://cirt.net/Nikto2",
        "created_at": new Date()
    },
    {
        "tool_name": "gobuster",
        "category": "web",
        "risk_level": "low",
        "default_options": "dir -w /usr/share/wordlists/dirb/common.txt",
        "description": "Directory/File, DNS and VHost busting tool",
        "documentation_url": "https://github.com/OJ/gobuster",
        "created_at": new Date()
    },
    {
        "tool_name": "hydra",
        "category": "authentication",
        "risk_level": "high",
        "default_options": "-L users.txt -P passwords.txt",
        "description": "Network logon cracker",
        "documentation_url": "https://github.com/vanhauser-thc/thc-hydra",
        "created_at": new Date()
    },
    {
        "tool_name": "metasploit",
        "category": "exploitation",
        "risk_level": "high",
        "default_options": "",
        "description": "Penetration testing framework",
        "documentation_url": "https://docs.metasploit.com/",
        "created_at": new Date()
    },
    {
        "tool_name": "burpsuite",
        "category": "web",
        "risk_level": "medium",
        "default_options": "",
        "description": "Web application security testing platform",
        "documentation_url": "https://portswigger.net/burp/documentation",
        "created_at": new Date()
    },
    {
        "tool_name": "sslscan",
        "category": "infrastructure",
        "risk_level": "low",
        "default_options": "",
        "description": "SSL/TLS scanner",
        "documentation_url": "https://github.com/rbsec/sslscan",
        "created_at": new Date()
    }
]);

// Insert sample user preferences
db.user_preferences.insertOne({
    "user_id": "default_user",
    "preferences": {
        "theme": "dark",
        "default_risk_level": "medium",
        "auto_save_sessions": true,
        "notification_settings": {
            "email_reports": false,
            "browser_notifications": true
        },
        "favorite_tools": ["nmap", "sqlmap", "nikto"],
        "custom_wordlists": [],
        "api_settings": {
            "timeout": 30,
            "max_retries": 3
        }
    },
    "created_at": new Date(),
    "updated_at": new Date()
});

// Create sample audit log entry
db.audit_logs.insertOne({
    "user_id": "system",
    "action": "database_initialized",
    "details": {
        "collections_created": [
            "pentest_sessions",
            "audit_logs", 
            "user_preferences",
            "pentest_reports",
            "tool_configurations"
        ],
        "indexes_created": 6,
        "default_data_inserted": true
    },
    "timestamp": new Date(),
    "ip_address": "127.0.0.1",
    "user_agent": "MongoDB Init Script"
});

print("✅ AI Pentest Agent database initialized successfully!");
print("📊 Collections created: pentest_sessions, audit_logs, user_preferences, pentest_reports, tool_configurations");
print("🔍 Indexes created for optimal performance");
print("🛠️ Default tool configurations inserted");
print("👤 Default user preferences created");
print("📝 Initial audit log entry added");
