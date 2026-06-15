[Insert Strict System-Level Prompt]

Generate the complete source code for `compliance/poopia_gdpr.py`.
This module acts as an inline middleware validator for all user inputs.

Requirements:
- Implement strict PII (Personally Identifiable Information) scrubbing functions targeting South African ID numbers, phone numbers, email strings, and home addresses.
- Enforce transient session storage processing: data must be purged entirely from memory the moment a PDF is generated and downloaded.
- Include logging hooks that audit data-destruction confirmations without saving the underlying personal data.
