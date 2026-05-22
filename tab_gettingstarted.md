---
title: gettingstarted
displaytext: Getting Started
layout: null
tab: true
order: 3
type: documentation
level: 2
tags: docksec
---

# Getting Started with DockSec

Follow these steps to start securing your Docker environments with AI-powered insights.

## Prerequisites

- **Python 3.12+**
- **Docker** (required for image scanning)
- **API Key** (Optional, for AI features. Supports OpenAI, Anthropic, Google, and Ollama)

## Installation

```bash
# Install via pip
pip install docksec

# Install external scanners (Trivy and Hadolint)
python -m docksec.setup_external_tools
```

## Basic Usage

### GitHub Action

Integrate DockSec into your GitHub Actions workflow:

```yaml
- name: Run DockSec AI Scanner
  uses: OWASP/DockSec@main
  with:
    dockerfile: 'Dockerfile'
    openai_api_key: ${{ secrets.OPENAI_API_KEY }}
```

### CLI Usage

### 1. Scan a Dockerfile
Analyze a Dockerfile for security best practices and common misconfigurations.

```bash
docksec Dockerfile
```

### 2. Full Analysis (Dockerfile + Image)
Combine static Dockerfile analysis with dynamic image vulnerability scanning.

```bash
docksec Dockerfile -i myapp:latest
```

### 3. Image-Only Scan
Scan a Docker image without needing the original Dockerfile.

```bash
docksec --image-only -i nginx:latest
```

## AI Configuration

To enable AI-powered explanations and remediation steps, set your preferred provider's API key:

```bash
# For OpenAI (Default)
export OPENAI_API_KEY="your-key-here"

# For Anthropic Claude
export ANTHROPIC_API_KEY="your-key-here"
export LLM_PROVIDER="anthropic"
# Note: Defaults to claude-haiku-4-5 (cheapest/fastest)

# For Google Gemini
export GOOGLE_API_KEY="your-key-here"
export LLM_PROVIDER="google"
```

## Generating Reports

DockSec automatically generates professional reports in multiple formats (HTML, PDF, JSON, CSV) for every scan.

By default, all reports are saved to:
`~/.docksec/results/`

You can override this location using an environment variable:
```bash
export DOCKSEC_RESULTS_DIR="/path/to/your/reports"
```

### Quick Scan (No AI)
If you want a lightning-fast scan without AI analysis:

```bash
# Scan only the Dockerfile
docksec Dockerfile --scan-only

# Scan only an image
docksec --image-only -i nginx:latest
```
