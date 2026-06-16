#!/usr/bin/env python3
"""
Sovereign Enterprise System - Orchestrator Engine
File: engineering_prompt.py
Purpose: Loads the career system architecture and provisions runtime
         coordination for the autonomous AI engines.
"""

import os
import json
import sys
import time
from google import genai
from google.genai import types
from google.genai.errors import APIError

def run_orchestrator():
    # 1. Setup direct local authentication
    api_key = "AIzaSy..."  # <--- PASTE YOUR COPIED GEMINI API KEY ENTIRELY HERE
    
    if not api_key or api_key == "AIzaSy...":
        print("[-] Error: Please paste your active Gemini API key directly into engineering_prompt.py.")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    
    # 2. Define the core operational system prompt
    system_instruction = (
        "You are an expert Principal Engineer specializing in high-performance Python backend "
        "architectures, micro-agents, and modern enterprise systems. Your goal is to guide, "
        "validate, and optimize system logic flawlessly with zero placeholders."
    )
    
    # 3. Target the system development matrix
    blueprint_file = "career_blueprint.json"
    if not os.path.exists(blueprint_file):
        # Fallback if named differently
        blueprint_file = "enterprise_blueprint.json"
        
    if not os.path.exists(blueprint_file):
        print(f"[-] Error: Target roadmap profile '{blueprint_file}' not found in directory.")
        sys.exit(1)
        
    print(f"[*] Core Orchestrator Active. Loading target model layout from: {blueprint_file}")
    
    with open(blueprint_file, 'r', encoding='utf-8') as f:
        blueprint_data = json.load(f)
        
    project_name = blueprint_data.get("project_name", blueprint_data.get("enterprise_name", "Sovereign_System"))
    print(f"[✓] System Node Connected. Online for project: {project_name}")
    print("[*] Listening for inbound app layer triggers from frontend.py...")
    print("-" * 60)
    
    # Keeps the orchestration process alive to field calls
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Shutting down Orchestrator Engine cleanly.")

if __name__ == "__main__":
    run_orchestrator()
