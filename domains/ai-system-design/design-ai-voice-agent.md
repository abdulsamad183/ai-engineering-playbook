---
title: "Design: AI Voice Agent"
description: "Voice AI — STT, VAD, streaming, TTS, interruptions, real-time tools."
domain: ai-system-design
tags: [system-design, voice, stt, tts, realtime, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../llm-engineering/llm-streaming.md
keywords: [voice agent, STT, TTS, VAD, interruptions]
author: hp
---

# Design: AI Voice Agent

## Problem Statement

Real-time spoken conversation with <500ms perceived latency and barge-in support.

## Architecture

```mermaid
flowchart LR
    MIC[Audio in] --> VAD[Voice activity detection]
    VAD --> STT[Speech-to-text stream]
    STT --> AGENT[Dialog agent]
    AGENT --> TOOLS[Tools]
    AGENT --> TTS[Text-to-speech stream]
    TTS --> SPK[Audio out]
```

## Components

| Component | Role |
|-----------|------|
| **VAD** | Detect speech start/end; reduce STT cost |
| **Streaming STT** | Partial transcripts |
| **Agent** | Short responses; tool calls |
| **Streaming TTS** | Start speak before full text |
| **Interruptions** | Stop TTS on user speak; cancel LLM |

## Latency Optimization

- Pipeline overlap: STT partial → LLM → TTS chunk
- Edge deployment for media
- Smaller models for dialog routing

## Tradeoffs

| Full duplex WebRTC | Turn-based |
|--------------------|------------|
| Natural | Simpler |

## Navigation

- [Scaling AI Systems](scaling-ai-systems.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 14 |
