#!/usr/bin/env python3
"""Simple helper to inspect JWT claims without verifying signature.
Usage:
  python inspect_jwt.py <token>
"""
import sys
import json
from jose import jwt
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: inspect_jwt.py <token>", file=sys.stderr)
    sys.exit(1)

token = sys.argv[1]
try:
    payload = jwt.get_unverified_claims(token)
except Exception as e:
    print("Failed to decode token:", e)
    sys.exit(2)

print(json.dumps(payload, indent=2))
if 'exp' in payload:
    print("exp:", payload['exp'], "->", datetime.utcfromtimestamp(payload['exp']).isoformat() + "Z")
if 'iss' in payload:
    print("iss:", payload['iss'])
if 'aud' in payload:
    print("aud:", payload['aud'])
if 'permissions' in payload:
    print("permissions:", payload['permissions'])
