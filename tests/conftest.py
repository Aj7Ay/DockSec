"""Pytest configuration and fixtures."""

import os
import shutil
import tempfile
import json
from datetime import datetime

import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    test_dir = tempfile.mkdtemp()
    yield test_dir
    shutil.rmtree(test_dir)


@pytest.fixture
def sample_dockerfile(temp_dir):
    """Create a sample Dockerfile for testing."""
    dockerfile_path = os.path.join(temp_dir, "Dockerfile")
    with open(dockerfile_path, "w") as f:
        f.write("FROM ubuntu:latest\nRUN echo 'test'\n")
    return dockerfile_path


@pytest.fixture
def sample_vulnerabilities():
    return [
        {
            "VulnerabilityID": "CVE-2023-1234",
            "Severity": "CRITICAL",
            "PkgName": "openssl",
            "InstalledVersion": "1.0.0",
            "Title": "Buffer overflow in openssl",
            "CVSS": 9.8,
            "Status": "fixed",
            "Target": "python:3.9-slim",
            "PrimaryURL": "https://nvd.nist.gov/vuln/detail/CVE-2023-1234",
        }
    ]


@pytest.fixture
def sample_scan_info():
    return {
        "image": "python:3.9-slim",
        "scan_date": "2024-01-01T00:00:00",
        "scanner": "trivy",
    }


@pytest.fixture
def sample_scan_results(temp_dir, sample_vulnerabilities):
    """Create sample scan results for testing."""
    return {
        'dockerfile_scan': {
            'success': True,
            'output': None
        },
        'image_scan': {
            'success': True,
            'output': 'Scan completed'
        },
        'json_data': sample_vulnerabilities,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'image_name': 'test:latest',
        'dockerfile_path': os.path.join(temp_dir, 'Dockerfile'),
        'scan_mode': 'full'
    }


@pytest.fixture
def mock_cache_file(temp_dir):
    """Create a mock cache file for testing."""
    cache_data = {
        "abc123def456": {
            "image": "test:latest",
            "timestamp": datetime.now().isoformat(),
            "results": {
                "image_name": "test:latest",
                "json_data": []
            }
        }
    }
    cache_path = os.path.join(temp_dir, ".docksec_cache.json")
    with open(cache_path, 'w') as f:
        json.dump(cache_data, f)
    return cache_path


@pytest.fixture
def long_dockerfile():
    """Create a long Dockerfile for truncation testing."""
    content = "FROM ubuntu:latest\n"
    for i in range(100):
        content += f"RUN echo 'line {i}' && echo 'some very long command here that should be truncated'\n"
    return content


@pytest.fixture
def mixed_severity_vulnerabilities():
    """Create vulnerabilities with mixed severity levels."""
    return [
        {
            "VulnerabilityID": f"CVE-2023-{i:04d}",
            "Severity": severity,
            "PkgName": f"package{i}",
            "InstalledVersion": "1.0.0",
            "Title": f"Issue {i}",
            "CVSS": 5 + i * 0.5,
        }
        for i, severity in enumerate(['CRITICAL', 'CRITICAL', 'HIGH', 'HIGH', 'MEDIUM', 'LOW'])
    ]


@pytest.fixture
def dockerfile_with_multiple_sections():
    """Create a Dockerfile with multiple sections for AI analysis."""
    return """FROM ubuntu:latest

# System packages
RUN apt-get update && apt-get install -y \\
    curl \\
    wget \\
    git

# Application code
COPY app /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Environment variables
ENV API_KEY=default_key
ENV DEBUG=true

# Expose port
EXPOSE 8080

# Run application
CMD ["python", "app.py"]
"""

