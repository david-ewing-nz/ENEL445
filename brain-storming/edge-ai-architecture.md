# Edge AI Architecture — GX10 + Pi Cluster

## Overview

A hierarchical inference architecture inspired by AlphaFold's two-representation model.
Claude (or any frontier LLM) plays no runtime role — it is a **build-time development tool only**.
The production stack is fully local and private.

---

## Hardware

| Device | Role |
|--------|------|
| ASUS Ascent GX10 (NVIDIA GB10 Grace Blackwell, 128 GB) | Aggregation, LLM inference, orchestration |
| Sipeed NanoCluster × 7 (CM4/CM5) | Edge inference nodes |

---

## Two-Tensor Design (AlphaFold-inspired)

### Single Representation (Edge Tensor)
- Runs **on each Pi node** independently
- Encodes local state: sensor data, local environment, task context
- Lightweight — INT8 or FP16 quantised, fits CM5 compute budget
- No inter-node communication required at this layer

### Pair Representation (Aggregation Tensor)
- Runs **on the GX10**
- Encodes cross-node relationships — what node A knows about node B's context
- Receives compressed feature vectors from each Pi
- Drives cross-attention / reasoning across the cluster

---

## Inference Flow

```
Pi Node 1 ──┐
Pi Node 2 ──┤  single tensors (local features)
Pi Node 3 ──┤─────────────────────────────► GX10
Pi Node 4 ──┤  (compressed, low bandwidth)   ├─ pair tensor (cross-node reasoning)
Pi Node 5 ──┤                                ├─ LLM / orchestration layer
Pi Node 6 ──┤                                └─ decision / task dispatch back to nodes
Pi Node 7 ──┘
```

---

## Key Design Principles

- **Hierarchical** — heavy compute stays on GX10; Pis do only local inference
- **Private** — no data leaves the local network at runtime
- **Cost-free at runtime** — no API calls to Anthropic or any cloud service
- **Claude's role** — development assistant only (writing orchestration code, K3S manifests, agent logic, ML pipelines)

---

## Next Steps (from 01 July 2026)

1. Receive Sipeed NanoCluster (order ref NZO574203: Woolworths Church Corner)
2. Flash CM4/CM5 nodes, set up K3S cluster
3. Deploy edge tensor inference on Pi nodes (TensorFlow Lite or ONNX Runtime)
4. Implement aggregation layer on GX10
5. Integrate LLM orchestration (local model — Llama 3 / Mistral class)
6. Use Claude Code (CLI over SSH to GX10) for development iteration
