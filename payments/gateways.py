[Insert Strict System-Level Prompt]

Generate the full, production-grade code for `payments/gateways.py`.
This file manages commercial checkouts and financial state securely.

Requirements:
- Implement a dual-gateway factory wrapper: PayFast/Ozow (ZAR processing via signatures and security passphrases) and Stripe (Global processing via webhooks and payment intents).
- Include strict server-side cryptographic hashing for PayFast parameters to prevent transaction tampering.
- Include localized currency conversion fallbacks and explicit error catching for payment failure states.
