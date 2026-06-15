#!/usr/bin/env python3
"""
Sovereign Enterprise System - Universal Meta-Builder
File: builder.py
Purpose: Reads a structural system JSON blueprint and systematically compiles
         unabridged production-grade source code files straight to local disk.
"""

import os
import json
import sys
from google import genai
from google.genai import types

def load_blueprint(blueprint_path: str) -> dict:
    """Loads and validates the structural JSON blueprint file."""
    if not os.path.exists(blueprint_path):
        print(f"[-] Error: Blueprint file matching path '{blueprint_path}' not found.")
        sys.exit(1)
    try:
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[-] Error: Blueprint contains invalid JSON strings. Details: {e}")
        sys.exit(1)

def clean_model_response(raw_text: str) -> str:
    """
    Strips markdown code fences (```python ... 
```) if returned by the model
    to ensure only valid, executable source code is saved to disk.
    """
    lines = raw_text.strip().split('\n')
    if lines and lines[0].startswith('```'):
        lines.pop(0)
    if lines and lines[-1].startswith('
```'):
        lines.pop()
    return '\n'.join(lines).strip()

def run_meta_builder():
    # 1. Initialize client using the 2026 google-genai SDK standard layout
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[-] Error: GEMINI_API_KEY environment variable is not set.")
        print("[*] Please set it using: export GEMINI_API_KEY='your_key'")
        sys.exit(1)
        
    client = genai.Client(api_key=api_key)
    
    # 2. Select the target blueprint configuration file
    blueprint_file = "enterprise_blueprint.json"
    print(f"[*] Initializing local architecture build sequence via: {blueprint_file}")
    blueprint = load_blueprint(blueprint_file)
    
    project_name = blueprint.get("project_name", blueprint.get("enterprise_name", "Sovereign_Project"))
    modules = blueprint.get("modules", [])
    output_base_dir = os.path.join(os.getcwd(), "output", project_name)
    
    print(f"[*] Target Directory Base: {output_base_dir}")
    print(f"[*] Detected Modules to compile: {len(modules)}")
    print("-" * 60)

    # 3. Define the absolute system-level engineering prompt boundaries
    system_instruction = (
        "You are an expert Principal Software Architect specializing in production-grade, "
        "high-performance backend architectures, micro-agents, and modern enterprise systems.\n\n"
        "ABSOLUTE CONSTRAINTS:\n"
        "1. NO PLACEHOLDERS: Writing '// TODO', '# implement logic here', or leaving files truncated "
        "is a fatal violation. Every single import, class, execution loop, method, routing hook, and "
        "defensive error-handling try-catch block must be explicitly fully typed out.\n"
        "2. 2026 ARCHITECTURE: Code must use native asynchronous execution execution blocks (async/await), "
        "explicit type hinting, structured native logging, and secure cryptographic layers.\n"
        "3. EXCLUSIVE ISOLATION: Focus solely on generating the exact file path requested. Do not speculate, "
        "do not output introductory text, and do not provide conversational explanations. Output ONLY valid code."
    )

    # 4. Process the system modules linearly file-by-file
    for module_idx, module in enumerate(modules, start=1):
        module_name = module.get("module_name", f"module_{module_idx}")
        files = module.get("files", [])
        
        print(f"\n[+] Compiling Module [{module_idx}/{len(modules)}]: {module_name}")
        
        for file_info in files:
            relative_file_path = file_info.get("path")
            file_purpose = file_info.get("purpose")
            
            # Compute full system save paths
            full_target_path = os.path.join(output_base_dir, relative_file_path)
            target_directory = os.path.dirname(full_target_path)
            
            # Ensure local directories exist
            os.makedirs(target_directory, exist_ok=True)
            
            print(f"    └─► Generating: {relative_file_path}")
            print(f"        Purpose: {file_purpose}")
            
            # Formulate the targeted execution instruction
            generation_prompt = (
                f"Generate the full, unabridged source code for the file path: '{relative_file_path}'.\n"
                f"Core Purpose of this file: {file_purpose}\n\n"
                f"Ensure the implementation completely fulfills this role with robust logic, full parameters, "
                f"and error processing. Do not truncate the code block."
            )
            
            try:
                # Direct API call to the fast, massive context gemini-2.5-pro model
                response = client.models.generate_content(
                    model='gemini-2.5-pro',
                    contents=generation_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.2, # Low temperature forces structural stability and engineering consistency
                    ),
                )
                
                # Clean code blocks and remove markdown wrapper syntax
                clean_source_code = clean_model_response(response.text)
                
                # Write the output directly onto your hard drive
                with open(full_target_path, 'w', encoding='utf-8') as code_file:
                    code_file.write(clean_source_code)
                
                print(f"        [✓] Saved successfully ({len(clean_source_code)} bytes).")
                
            except Exception as error:
                print(f"        [X] Error generating file {relative_file_path}: {error}")
                print("        [*] Aborting run to protect system integrity.")
                sys.exit(1)

    print("\n" + "="*60)
    print(f"[✓] ENTERPRISE COMPILATION COMPLETE: {project_name}")
    print(f"[✓] All modules have been built directly inside: {output_base_dir}")
    print("="*60)

if __name__ == "__main__":
    run_meta_builder()
