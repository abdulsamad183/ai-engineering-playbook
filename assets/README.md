# Assets

> Diagrams, images, screenshots, slides, and downloadable resources.

---

## Organization

```
assets/
├── diagrams/                    # Mermaid and diagram source files
│   ├── flowcharts/              # Decision and process flows
│   ├── sequence/                # API and agent interaction sequences
│   ├── architecture/            # System architecture diagrams
│   ├── class/                   # Data models and class diagrams
│   ├── er/                      # Entity-relationship diagrams
│   ├── workflows/               # AI workflow orchestration
│   └── agent-interactions/      # Multi-agent communication
├── images/                      # Static images organized by domain
│   ├── llm-engineering/
│   ├── rag/
│   ├── agents/
│   └── deployment/
├── screenshots/                 # UI and tool screenshots
├── slides/                      # Presentation materials
└── resources/                   # Downloadable files (PDFs, configs)
```

---

## Conventions

See [Mermaid Conventions](../meta/mermaid-conventions.md) for diagram standards and [Naming Conventions](../meta/naming-conventions.md) for file naming.

### Quick Rules

| Asset Type | Location | Naming |
|------------|----------|--------|
| Mermaid source | `diagrams/{type}/` | `{type}-{subject}-v{N}.mmd` |
| Images | `images/{domain}/` | `{domain}-{topic}-{descriptor}.png` |
| Screenshots | `screenshots/` | `{tool}-{description}.png` |
| Slides | `slides/` | `{topic}-slides.{ext}` |

### Image Guidelines

- Keep images under 500 KB when possible.
- Use PNG for screenshots, SVG for icons and simple graphics.
- Always include alt text in documents that reference images.
- Reference images with relative paths from the document.

### Diagram Guidelines

- Simple diagrams (< 15 nodes): embed inline in documents.
- Complex diagrams: standalone `.mmd` files in `diagrams/`.
- Version diagrams on semantic changes: `-v1`, `-v2`.

---

## See Also

- [Mermaid Conventions](../meta/mermaid-conventions.md)
- [Style Guide](../meta/style-guide.md#image-organization)
