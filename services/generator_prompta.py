[Insert Strict System-Level Prompt]

Generate the full, unabridged code for `services/generator.py`.
This module must use `reportlab` or a similar robust library to generate beautiful, highly clean, ATS-compliant PDFs from raw JSON data.

Requirements:
- Ensure font embedding, exact margin controls (0.75-inch standard), and zero decorative elements that break ATS parsers.
- Implement a method to package multiple formats (PDF, DOCX text file, Cover Letter) into a compressed, streaming `.zip` archive.
- Include a strict validation step confirming file sizes and bytes before returning the payload.
