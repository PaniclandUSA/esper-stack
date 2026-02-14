# Esper Stack — Quick Start

**The complete pipeline in five minutes.**

---

## What You're About to Do

Run meaning through all four layers of the Esper Stack:

```
Natural Language
      ↓
VSE (encode meaning as semantic packet)
      ↓
ChronoCore™ (execute with temporal coherence)
      ↓
PICTOGRAM-256 (inscribe as stable glyphs)
      ↓
PivotGuard / PSH-256 (seal cryptographically)
      ↓
PIVOTGRAM-92 (audit drift across the pipeline)
```

---

## Prerequisites

Python 3.9 or higher.

```bash
git clone https://github.com/PaniclandUSA/vse
git clone https://github.com/PaniclandUSA/chronocore
git clone https://github.com/PaniclandUSA/pictogram
git clone https://github.com/PaniclandUSA/pivotgram
git clone https://github.com/PaniclandUSA/PivotGuard
```

---

## Step 1: Encode Meaning in VSE

VSE represents meaning as a semantic packet — not a sentence, but a
structured coordinate in 12-dimensional motif space.

```python
# A VSE semantic packet
packet = {
    "text": "Teaching a neighbor to read is a labor of love.",
    "phi_1": +0.82,   # Polarity: warm
    "phi_2": -0.61,   # Direction: dreaming
    "phi_3": +0.74,   # Stance: together
    "phi_4": -0.43,   # Confidence: wondering
    "tau": 0,         # Temporal: eternal now
    "motifs": [
        "SOLIDARITY", "STEWARDSHIP", "CARE",
        "DIGNITY", "RESTORATION", "HOPE"
    ],
    "resonance": 0.913
}
```

The Esperpiler compiles natural language into this form automatically.
The resonance score (0.913) measures how faithfully the packet
captures the original intent. Above 0.9 is considered stable.

**What VSE guarantees:** the same text, run through the Esperpiler
twice, produces packets with distance ≤ ε under the semantic metric.
This is ε-bounded determinism — the ISA property of the stack.

---

## Step 2: Execute with ChronoCore™

ChronoCore sequences the VSE packet through temporal physics,
producing a glyph-state audit log.

```python
from chronocore import ChronoCore

core = ChronoCore()
log = core.execute(packet)

print(log.glyph_trace)
# Output: [◯⟲∿] — low-pressure cyclic organic flow
# Meaning: stable, continuous, living motion

print(log.coherence_score)
# Output: 0.97 — temporal coherence maintained

print(log.divergence)
# Output: 0.003 — within ε-bounds, no drift detected
```

ChronoCore is the CPU layer. It does not interpret meaning —
it executes the VSE instruction sequence and records state transitions.
Every step is auditable.

---

## Step 3: Inscribe with PICTOGRAM-256

PICTOGRAM converts the semantic state into stable, cryptographically
bound glyphs. These are the persistent form of meaning — the storage layer.

```python
from pictogram import PictogramHasher, compose

# Map VSE motifs to PICTOGRAM glyphs
glyph_sequence = compose([
    "E029",  # SOLIDARITY
    "E02A",  # STEWARDSHIP
    "E031",  # CARE
    "E030",  # DIGNITY
    "E02B",  # RESTORATION
    "E0DB",  # HOPE
])

# Compute PSH-256 hash for each glyph
hasher = PictogramHasher()
for glyph in glyph_sequence:
    result = hasher.compute_psh256(glyph)
    print(f"{glyph.name}: {result.psh256[:16]}...")
```

**What PSH-256 guarantees:** each glyph's hash is invariant under
rotation, scaling, and redrawing, as long as its topology is preserved.
This is how meaning survives across time, culture, and substrate.

---

## Step 4: Seal with PivotGuard

PivotGuard creates a cryptographic attestation of the semantic state
at this moment — a timestamped, chain-linked proof of integrity.

```python
from pivotguard import PivotGuardAttestor

attestor = PivotGuardAttestor()

attestation = attestor.attest_moment(
    milieu={
        "packet": packet,
        "glyph_sequence": [g.code for g in glyph_sequence],
    },
    gravitas={},
    ambience={},
)

print(attestation.hash.hex())
# Output: 5ba0e3783b35cb0c9caed0b36df3ad49...
# This is the canonical attestation for "Teaching a neighbor to read..."
```

The attestation is embedded in the compiled artifact's padding bytes —
zero storage overhead, 100% backward compatible.

If the semantic state changes, the hash breaks. Tampering is
mathematically detectable.

---

## Step 5: Audit with PIVOTGRAM-92

PIVOTGRAM-92 measures whether meaning moved during the pipeline —
and by how much.

```python
from pivotgram import DriftMeasure

# Measure drift from input to output
origin_coord = {
    "temporal": 0.0,     # eternal now
    "orientation": 0.82, # warm, directed outward
    "scope": 0.74,       # communal, together
    "duty": 0.61,        # obligation claimed (labor of love)
}

output_coord = {
    "temporal": 0.0,
    "orientation": 0.81,
    "scope": 0.73,
    "duty": 0.60,
}

drift = DriftMeasure.compute(origin_coord, output_coord)
print(f"∇I = {drift:.4f}")
# Output: ∇I = 0.0141

# ∇I < 0.05 means meaning was conserved.
# ∇I = 0.0 would mean perfect preservation.
# ∇I > 0.10 triggers review.
```

PIVOTGRAM-92 does not judge whether the meaning is correct.
It measures whether it moved. Human judgment remains sovereign.

---

## Complete Pipeline Output

```
Input:   "Teaching a neighbor to read is a labor of love."

VSE:     Φ₁=+0.82 Φ₂=-0.61 Φ₃=+0.74 Φ₄=-0.43 τ=0
         Resonance: 0.913

Trace:   [◯⟲∿] — coherence: 0.97

Glyphs:  E029 E02A E031 E030 E02B E0DB
         (SOLIDARITY · STEWARDSHIP · CARE · DIGNITY · RESTORATION · HOPE)

Seal:    5ba0e3783b35cb0c9caed0b36df3...

Audit:   ∇I = 0.0141 — meaning conserved ✓
```

---

## What Just Happened

You ran a sentence through a semantic computer:

| Stage | Layer | Role |
|-------|-------|------|
| Esperpiler | VSE (ISA) | Compiled language into instruction set |
| ChronoCore | CPU | Executed with temporal coherence |
| PICTOGRAM | I/O + Storage | Inscribed as stable, hashable glyphs |
| PivotGuard | Memory | Sealed with cryptographic attestation |
| PIVOTGRAM-92 | Audit | Measured semantic drift: ∇I = 0.0141 |

The sentence entered as natural language.
It exited as a cryptographically sealed, auditable semantic state.
The meaning was conserved within ε-bounds.

That is semantic computation.

---

## Implementation Status

| Component | Status |
|-----------|--------|
| VSE specification | Complete |
| Esperpiler | Specified; reference implementation in progress |
| ChronoCore | Specified; core modules active |
| PICTOGRAM-256 | Complete — 256 glyphs, font ready |
| PSH-256 | Specified; reference implementation complete |
| PivotGuard | Specified; canonical test vector verified |
| PIVOTGRAM-92 | Complete — 92 glyphs, master sheet canonical |

Code examples above reflect the intended API.
Some modules are at specification stage with implementations in progress.
See individual repositories for current build status.

---

## Next Steps

- **Literacy application**: See `docs/literacy_pipeline.md`
- **CYRANO integration**: See `docs/cyrano_pipeline.md`
- **Academic documentation**: See `VON_NEUMANN_MAPPING.md`
- **Validation record**: See `VALIDATION_APPENDIX.md`
- **Glyph reference**: See `GLYPHS.md` in the PIVOTGRAM-92 repository

---

*"Teaching a neighbor to read is a labor of love."*
*— The Cyrano de Bergerac Foundation*
