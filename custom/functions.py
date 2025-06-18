"""
Custom functions for AI Pentest Agent in Open WebUI
"""

import json
import re
import requests
from typing import Dict, List, Any
from datetime import datetime

class PentestAgentFunctions:
    """
    Custom functions for AI Pentest Agent
    """
    
    def __init__(self):
        self.deepseek_api_key = "sk-1bd5de3f31db429cb8cbe73875537c5c"
        self.deepseek_api_url = "https://api.deepseek.com/v1/chat/completions"
        
    def extract_domain(self, text: str) -> str:
        """Extract domain from user input"""
        domain_pattern = r'(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        match = re.search(domain_pattern, text)
        return match.group(1) if match else "target.com"
    
    def generate_pentest_plan(self, user_message: str) -> Dict[str, Any]:
        """
        Generate penetration testing plan using DeepSeek API
        """
        try:
            target_domain = self.extract_domain(user_message)
            
            system_prompt = {
                "role": "system",
                "content": """You are an AI penetration testing assistant. Convert the user's request into a structured penetration testing plan.

IMPORTANT: You must respond with ONLY a valid JSON object in this exact format:
{
  "plan": [
    {
      "tool": "tool_name",
      "command": "full_command_here",
      "description": "description_of_what_this_does",
      "risk_level": "low|medium|high",
      "category": "network|web|infrastructure|social"
    }
  ],
  "target": "domain_or_ip",
  "assessment_type": "comprehensive|focused|quick",
  "estimated_time": "time_estimate",
  "prerequisites": ["list", "of", "requirements"],
  "warnings": ["security", "warnings"]
}

Available tools include: nmap, sqlmap, nikto, dirb, gobuster, hydra, john, metasploit, burpsuite, etc.
Make sure commands are realistic and safe for testing environments.
Always include the target domain/IP in commands where applicable.
Do not include any text outside the JSON response."""
            }
            
            messages = [
                system_prompt,
                {"role": "user", "content": user_message}
            ]
            
            response = requests.post(
                self.deepseek_api_url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.deepseek_api_key}"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": messages,
                    "max_tokens": 2000,
                    "temperature": 0.7
                }
            )
            
            if response.status_code == 200:
                ai_response = response.json()
                ai_content = ai_response.get("choices", [{}])[0].get("message", {}).get("content", "")
                
                # Parse JSON response
                try:
                    json_match = re.search(r'\{[\s\S]*\}', ai_content)
                    json_string = json_match.group(0) if json_match else ai_content
                    plan_data = json.loads(json_string)
                    return plan_data
                except json.JSONDecodeError:
                    return self.get_fallback_plan(target_domain)
            else:
                return self.get_fallback_plan(target_domain)
                
        except Exception as e:
            print(f"Error generating pentest plan: {e}")
            return self.get_fallback_plan(target_domain)
    
    def get_fallback_plan(self, target_domain: str) -> Dict[str, Any]:
        """Fallback plan if AI service fails"""
        return {
            "plan": [
                {
                    "tool": "nmap",
                    "command": f"nmap -sV -sC -T4 -p- {target_domain}",
                    "description": "Comprehensive port scan with service detection",
                    "risk_level": "low",
                    "category": "network"
                },
                {
                    "tool": "nikto",
                    "command": f"nikto -h {target_domain}",
                    "description": "Web server vulnerability scan",
                    "risk_level": "low",
                    "category": "web"
                },
                {
                    "tool": "sqlmap",
                    "command": f"sqlmap -u 'http://{target_domain}/page?id=1' --batch",
                    "description": "SQL injection vulnerability testing",
                    "risk_level": "medium",
                    "category": "web"
                }
            ],
            "target": target_domain,
            "assessment_type": "basic",
            "estimated_time": "2-4 hours",
            "prerequisites": ["Network access to target", "Proper authorization"],
            "warnings": ["Ensure you have permission to test the target", "Some tests may impact system performance"]
        }
    
    def format_plan_for_display(self, plan_data: Dict[str, Any]) -> str:
        """Format the plan for display in Open WebUI"""
        if not plan_data or "plan" not in plan_data:
            return "❌ Failed to generate penetration testing plan."
        
        output = []
        
        # Header
        output.append("# 🔒 AI Penetration Testing Plan")
        output.append(f"**Target:** `{plan_data.get('target', 'Unknown')}`")
        output.append(f"**Assessment Type:** {plan_data.get('assessment_type', 'Standard')}")
        output.append(f"**Estimated Time:** {plan_data.get('estimated_time', 'Variable')}")
        output.append("")
        
        # Warnings
        if plan_data.get('warnings'):
            output.append("## ⚠️ Security Warnings")
            for warning in plan_data['warnings']:
                output.append(f"- {warning}")
            output.append("")
        
        # Prerequisites
        if plan_data.get('prerequisites'):
            output.append("## 📋 Prerequisites")
            for prereq in plan_data['prerequisites']:
                output.append(f"- {prereq}")
            output.append("")
        
        # Testing Plan
        output.append("## 🛠️ Testing Plan")
        
        for i, tool in enumerate(plan_data['plan'], 1):
            risk_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(tool.get('risk_level', 'medium'), "🟡")
            category_emoji = {
                "network": "🌐",
                "web": "🌍", 
                "infrastructure": "🏗️",
                "social": "👥"
            }.get(tool.get('category', 'network'), "🔧")
            
            output.append(f"### {i}. {category_emoji} {tool.get('tool', 'Unknown Tool').upper()} {risk_emoji}")
            output.append(f"**Command:**")
            output.append(f"```bash")
            output.append(f"{tool.get('command', 'No command specified')}")
            output.append(f"```")
            output.append(f"**Description:** {tool.get('description', 'No description available')}")
            output.append(f"**Risk Level:** {tool.get('risk_level', 'medium').title()}")
            output.append("")
        
        # Footer
        output.append("---")
        output.append("*Generated by AI Pentest Agent - Use responsibly and only on authorized targets*")
        
        return "\n".join(output)

# Initialize the functions
pentest_functions = PentestAgentFunctions()

def process_pentest_request(user_input: str) -> str:
    """
    Main function to process penetration testing requests
    """
    plan_data = pentest_functions.generate_pentest_plan(user_input)
    return pentest_functions.format_plan_for_display(plan_data)

# Function registry for Open WebUI
FUNCTIONS = {
    "process_pentest_request": {
        "function": process_pentest_request,
        "description": "Generate AI-powered penetration testing plans",
        "parameters": {
            "user_input": {
                "type": "string",
                "description": "User's penetration testing request"
            }
        }
    }
}
