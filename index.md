---
layout: col-sidebar
title: OWASP DockSec
tags: docker, security, ai, scanner, devsecops, owasp
level: 2
type: documentation
---

[![GitHub Repo stars](https://img.shields.io/github/stars/OWASP/DockSec?style=flat)](https://github.com/OWASP/DockSec)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/docksec.svg)](https://pypi.org/project/docksec/)
[![Python Version](https://img.shields.io/pypi/pyversions/docksec.svg)](https://pypi.org/project/docksec/)
[![OWASP Incubator](https://img.shields.io/badge/OWASP-Incubator%20Project-48A646?logo=owasp)](https://owasp.org/www-project-docksec/)

<div align="center">
  <img src="https://raw.githubusercontent.com/OWASP/DockSec/main/images/docksec-logo-II.png" alt="DockSec" height="120">
  
  <h1>DockSec</h1>
  <p><strong>AI-powered Docker security scanner that explains vulnerabilities in plain English</strong></p>
</div>

---

## What is DockSec?

DockSec is an **OWASP Incubator Project** that bridges the gap between complex security scan results and actionable developer fixes. It integrates industry-standard scanners (Trivy, Hadolint, Docker Scout) with advanced AI to provide **context-aware security analysis**. 

Instead of overwhelming you with a list of 200+ CVEs, DockSec:

- **Prioritizes** what actually affects your specific container setup.
- **Explains** vulnerabilities in plain English, not just security jargon.
- **Suggests** specific, line-by-line fixes for your Dockerfile.
- **Generates** professional, interactive security reports for your team.

Think of it as having a security expert sitting right next to you, reviewing your Dockerfiles in real-time.

### Why OWASP Recognition Matters

Being recognized as an [OWASP Incubator Project](https://owasp.org/www-project-docksec/) means:
- ✅ **Vetted** by security professionals for quality and impact.
- ✅ **Community-driven** development and open governance.
- ✅ **Trusted** by enterprises and security teams worldwide.
- ✅ **Transparent** security practices and open-source maintenance.

---

## How It Works

<div align="center">
  <img src="https://raw.githubusercontent.com/OWASP/DockSec/main/images/workflow.png" alt="DockSec Workflow" width="800">
  <p><em>DockSec workflow: From scanning to actionable insights</em></p>
</div>

DockSec follows a robust four-stage pipeline:
1. **Scan**: Runs Trivy, Hadolint, and Docker Scout locally on your environment.
2. **Analyze**: AI correlates findings across all scanners to remove noise and assess real-world impact.
3. **Recommend**: Generates human-readable explanations and specific remediation steps.
4. **Report**: Exports actionable results in JSON, PDF, HTML, or Markdown formats.

---

## Quick Start

```bash
# Install DockSec
pip install docksec

# Scan a Dockerfile (AI-powered)
docksec Dockerfile

# Scan Dockerfile + Docker image
docksec Dockerfile -i myapp:latest

# Scan without AI (offline mode, no API key needed)
docksec Dockerfile --scan-only
```

---

## Features

- **Smart Analysis**: AI explains what vulnerabilities mean for *your* specific setup.
- **Multi-LLM Support**: Use OpenAI, Anthropic Claude, Google Gemini, or local models via Ollama.
- **Deep Integration**: Combines Trivy (vulnerabilities), Hadolint (linting), and Docker Scout.
- **Security Scoring**: Get a 0-100 score to track your security posture over time.
- **Rich Reporting**: Professional exports in HTML (interactive), PDF, JSON, and CSV.
- **Privacy First**: All scanning happens locally. Only scan metadata is sent to AI providers.
- **CI/CD Ready**: Designed for easy integration into GitHub Actions and build pipelines.

---

## Installation

### 1. Install via Pip
Requires **Python 3.12+** and **Docker** (for image scanning).

```bash
pip install docksec
```

### 2. Configure AI Provider (Optional)
Choose your preferred LLM provider by setting the appropriate environment variable:

#### OpenAI (Default)
```bash
export OPENAI_API_KEY="your-key-here"
```

#### Anthropic Claude
```bash
export ANTHROPIC_API_KEY="your-key-here"
export LLM_PROVIDER="anthropic"
export LLM_MODEL="claude-3-5-sonnet-20241022"
```

#### Google Gemini
```bash
export GOOGLE_API_KEY="your-key-here"
export LLM_PROVIDER="google"
export LLM_MODEL="gemini-1.5-pro"
```

#### Ollama (Local Models - No API Key Needed)
```bash
# Install Ollama from https://ollama.ai
export LLM_PROVIDER="ollama"
export LLM_MODEL="llama3.1"
```

### 3. Install External Scanners (Optional)
To enable full vulnerability and linting support:

```bash
# Automatically install Trivy and Hadolint
python -m docksec.setup_external_tools
```

---

## Usage

### Common Commands

```bash
# Basic Dockerfile analysis
docksec Dockerfile

# Full analysis (Dockerfile + Image)
docksec Dockerfile -i nginx:latest

# Image-only scan (no Dockerfile needed)
docksec --image-only -i nginx:latest

# Use a specific AI model
docksec Dockerfile --provider anthropic --model claude-3-5-sonnet-20241022

# Save report to a custom path
docksec Dockerfile -o my_report.html
```

---

## Roadmap

- [x] Multi-LLM support (OpenAI, Anthropic, Google, Ollama)
- [x] Professional HTML/PDF report generation
- [ ] Docker Compose multi-service scanning
- [ ] Kubernetes manifest analysis
- [ ] GitHub Action for automated PR reviews
- [ ] Custom security policy enforcement

---

## Recognition & Community

<div align="center">
  <a href="https://owasp.org/www-project-docksec/">
    <img src="https://raw.githubusercontent.com/OWASP/DockSec/main/images/owasp-logo.png" alt="OWASP" height="80">
  </a>
</div>

DockSec is proud to be an **OWASP Incubator Project**. Our mission is to make container security accessible, understandable, and actionable for every developer.

### Links
- **OWASP Project Page**: [owasp.org/www-project-docksec/](https://owasp.org/www-project-docksec/)
- **PyPI**: [pypi.org/project/docksec/](https://pypi.org/project/docksec/)
- **Issues**: [Report a bug](https://github.com/OWASP/DockSec/issues)
- **Discussions**: [Join the community](https://github.com/OWASP/DockSec/discussions)

---

<div align="center">
  <strong>If DockSec helps you, give it a ⭐ to help others discover it!</strong><br>
  Built with ❤️ by <a href="https://github.com/advaitpatel">Advait Patel</a> and the OWASP community.
</div>
