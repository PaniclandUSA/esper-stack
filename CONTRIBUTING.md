# Contributing to **Esper-Stack**

Thank you for your interest in contributing to **Esper-Stack**, the unified architecture that connects:

- **Vector-Space Esperanto (VSE)** — semantic algebra and intent calculus  
- **PICTOGRAM** — compact visual meaning language (glyph + modifier system)  
- **ChronoCore** — temporal-causal narrative kernel  

Esper-Stack provides a cross-model, cross-lingual, cross-architecture substrate for meaning.  
This repository orchestrates the three interoperating layers.

---

# 🌐 Repository Topology

Esper-Stack is a **meta-repository** that references three sibling codebases:

esper-stack/ │ ├── vse/          → semantic algebra, operators, modifiers, axiom engine
├── pictogram/    → glyph sets, modifier algebra, compositor
├── chronocore/   → narrative kernel, temporal engine, context crystallization
│ └── docs/         → cross-layer documentation, proofs, inscriptions, tutorials

Each layer is versioned independently and published under the same license.

---

# ✨ Contribution Philosophy

Esper-Stack is built on two guiding principles:

### **VENERATE (Axiom 11)**  
Begin contributions with respect for lineage — prior work, collaborators, and clarity.

### **STACCATO (Axiom 12)**  
Work in crisp, discrete bursts. Keep PRs small, reviewable, and semantically clean.

---

# 🔧 Where to Contribute

### **Contribute to VSE if your work touches:**
- semantic operators  
- modifier algebra  
- axiom definitions  
- convergence or divergence proofs  
- canonical syntax changes  
- English ↔ VSE transformation logic  

### **Contribute to PICTOGRAM if your work touches:**
- glyph designs  
- modifier families  
- semantic compression  
- layout, line rules, interpreter logic  

### **Contribute to ChronoCore if your work touches:**
- temporal scaffolding  
- narrative engine internals  
- crystallization steps  
- causal graph validation  
- time-axis manipulation functions  

### **Contribute to Esper-Stack root repo if your work touches:**
- cross-layer integrations  
- tutorials  
- documentation  
- pipeline examples  
- ecosystem-wide validation  
- community coordination  

If unsure where your change belongs: **open a discussion first**.

---

# 📚 Documentation Standards

All documentation must follow:

- clear section headings  
- reproducible examples  
- no external links without context  
- VSE code blocks labeled with `vse`  
- PICTOGRAM glyphs represented as text until SVG layer is added  
- cross-repo references must include version numbers

---

# 🧪 Testing & Validation

Esper-Stack depends on **cross-model semantic convergence**, validated with N=148 test cases.

Validation lives at:

data/cross-model-validation/

When updating operators, modifiers, or rules:

1. Run the full test suite.  
2. Add new test cases for novel operators.  
3. Document observable convergence or failures in  
   `docs/validation-results.md`.

---

# 🔀 Branching & Workflow

We use a lightweight semantic workflow:

### **Branches**
- `main` — release-stable  
- `develop` — integration branch  
- `feature/<name>` — scoped contributions  
- `docs/<name>` — documentation-focused PRs  

### **Commit Style**
Use semantic prefixes:

feat:    new feature
fix:     bug fix
docs:    documentation
refactor: restructure, no behavior change
test:    adds or updates tests
chore:   non-impacting maintenance

### **Pull Requests**
- keep PRs under 400 lines when possible  
- describe impact on each layer  
- reference any axioms modified  
- include “Before / After” examples  

---

# 🤝 Code of Conduct

Be kind. Be curious.  
Esper-Stack is a collaborative project bridging humans and AI systems.  
Respect diversity of thought, background, and approach.  
All voices are welcome.

---

# 🜂 Closing Ritual

As per **Axiom 11 (VENERATE)**, contributors may (optionally) include:

Gratitude

I thank those whose prior work made this contribution possible.

This is not required, but traditional.

Thank you for helping build Esper-Stack.
