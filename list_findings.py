#!/usr/bin/env python3
import json, subprocess, os, re
SPACE = "as-9507ba26-9fbf-43a1-9d3b-383d61b72d0b"
JOB = "pj-d7c6ded2-6ee8-4542-92d7-268ab21e2f9d"

REGION = os.environ.get("AWS_REGION", "us-east-1")
def aws(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 else None
resp = aws(["aws", "securityagent", "list-findings",
            "--agent-space-id", SPACE, "--pentest-job-id", JOB, 
            "--region", REGION, "--output", "json"])
findings = resp.get("findingsSummaries", [])

print(f"\uCD1D {len(findings)}\uAC1C Finding\\n")
for f in findings:
    print(f"{f.get('riskType'):<30}|{f.get('riskLevel'):<12}|{f.get('name')}")
