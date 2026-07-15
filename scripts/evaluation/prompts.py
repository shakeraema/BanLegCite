# prompts.py
# stage: Phase 3 Shadow Work — Evaluation Harness

STANDARD_PROMPT = """
You are a legal citation verification assistant. Your task is to verify if the following citation is REAL or FABRICATED.

A citation is REAL if it exists in the designated reporter volume and page, and matches the legal holding.
A citation is FABRICATED if it does not exist, references the wrong volume/page, or makes false claims.

Context Paragraph: {context}
Citation to Verify: {citation}
Purported Source: {source}

Output your analysis in this exact format:
Verdict: [REAL or FABRICATED]
Confidence: [1 to 5]
Reasoning: [Brief explanation of your verdict]
"""

AGENTIC_PROMPT = """
You are a legal citation verification assistant with access to verified legal references.
Use the following retrieved background information to evaluate if the citation is REAL or FABRICATED.

Background Reference:
{retrieved_info}

Context Paragraph to Verify:
{context}
Citation to Verify: {citation}
Purported Source: {source}

Output your analysis in this exact format:
Verdict: [REAL or FABRICATED]
Confidence: [1 to 5]
Reasoning: [Brief explanation referencing the background document]
"""
