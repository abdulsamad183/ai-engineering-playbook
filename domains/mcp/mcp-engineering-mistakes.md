---
title: "MCP Engineering Mistakes"
description: "Troubleshooting — invalid schemas, transport failures, stale capabilities, sessions, retry storms."
domain: mcp
tags: [mcp, mistakes, troubleshooting, debugging, phase-9]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - production-mcp.md
  - mcp-security.md
keywords: [MCP debugging, troubleshooting, anti-patterns]
author: hp
---

# MCP Engineering Mistakes

## Overview

Section **19** of Phase 9 — troubleshooting playbook.

## Issue Catalog

### Invalid Schemas

| | |
|---|---|
| **Symptoms** | `tools/call` fails; model generates bad args |
| **Root cause** | Loose or missing JSON Schema |
| **Diagnosis** | Validate schema with examples; log rejected args |
| **Fix** | Tighten `required`, `enum`, `maxLength` |
| **Prevention** | Schema review checklist |

### Transport Failures

| | |
|---|---|
| **Symptoms** | Connection reset, hung client |
| **Root cause** | STDIO buffer deadlock, HTTP proxy timeout |
| **Diagnosis** | Capture raw frames; check server stderr |
| **Fix** | Flush logs to stderr not stdout; increase proxy timeout |
| **Prevention** | Health checks; keep-alive |

### Stale Capabilities

| | |
|---|---|
| **Symptoms** | Tool not found after server deploy |
| **Root cause** | Client cached `tools/list` |
| **Diagnosis** | Compare cache age vs deploy time |
| **Fix** | Handle `tools/list_changed`; re-list |
| **Prevention** | TTL on capability cache |

### Broken Sessions

| | |
|---|---|
| **Symptoms** | Requests hang after server restart |
| **Root cause** | Client did not re-`initialize` |
| **Diagnosis** | Log initialize state |
| **Fix** | Reconnect pipeline on transport error |
| **Prevention** | Session watchdog |

### Resource Leakage

| | |
|---|---|
| **Symptoms** | User A sees User B data |
| **Root cause** | Shared server without tenant filter |
| **Diagnosis** | Audit `resources/read` by principal |
| **Fix** | Per-tenant URIs + ACL |
| **Prevention** | Integration tests per tenant |

### Retry Storms

| | |
|---|---|
| **Symptoms** | Downstream API overload |
| **Root cause** | Aggressive retry on 5xx for write tools |
| **Diagnosis** | Spike in `tools/call` metrics |
| **Fix** | Exponential backoff; circuit breaker |
| **Prevention** | Mark idempotent tools explicitly |

### Version Mismatches

| | |
|---|---|
| **Symptoms** | `initialize` fails |
| **Root cause** | Client/server protocol version drift |
| **Diagnosis** | Log negotiated versions |
| **Fix** | Upgrade SDK; pin versions in deploy |
| **Prevention** | CI compatibility tests |

## Navigation

- [Real-World Architectures](mcp-real-world-architectures.md) · [Debugging Cheat Sheet](../../cheat-sheets/mcp-debugging-checklist.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 9 Section 19 |
