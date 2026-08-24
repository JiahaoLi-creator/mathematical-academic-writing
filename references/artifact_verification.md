# Artifact Verification

Use this reference when the deliverable includes a notebook, code output, TeX source, HTML preview, or PDF.

## Verification levels

| Level | Inspect | Permitted claim |
| --- | --- | --- |
| Text-bound | source prose, formulas, notation, internal links | internally consistent or identified textual issue |
| Source-bound | designated references and theorem or citation locations | agrees or conflicts with the governing source |
| Execution-bound | fresh execution, outputs, seeds, tolerances, dependencies | runs successfully and reproduces the inspected outputs |
| Render-bound | exported HTML, PDF, or notebook preview | visible artifact renders as described |

Report the deepest level reached. File existence, stale output, or source inspection alone does not establish successful execution or rendering.

## Notebook checks

1. Verify the exact notebook path and, for fixture work, cell IDs and hashes.
2. Confirm that code, parameters, seeds, and mathematical prose describe the same experiment.
3. Restart and run all cells when execution verification is required.
4. Inspect tracebacks, warnings that affect conclusions, missing outputs, and nondeterministic state.
5. Export the intended preview from the executed notebook.
6. Inspect equations, tables, captions, axes, legends, units, and code-visibility requirements in the preview.

Hidden code in a reader preview must not remove code from the source notebook. An output created before the latest source change is stale until regenerated.

## TeX and PDF checks

- Compile from the current source and inspect the compiler result.
- Check undefined references, citation failures, overfull content that hides mathematics, and equation numbering.
- Render representative and high-risk pages: dense displays, theorem blocks, tables, figures, and bibliography.
- Confirm that extracted text and visible glyphs preserve symbols, minus signs, subscripts, and delimiters.

## Mathematical rendering checks

Inspect especially:

- inline delimiters around expressions such as `$f\in C^2(\mathbb R)$`;
- display delimiters and balanced environments;
- backslashes that HTML or JSON escaping may consume;
- table cells containing MathJax, where column layout can shift formulas;
- macros unsupported by the target renderer;
- equation labels and links after export.

A correct source formula with a broken preview is a rendering failure, not a mathematical correction opportunity.

## Evidence and freshness

Bind claims to current artifacts with paths, timestamps, or hashes when release or regression work needs reproducibility. Recompute hashes after regeneration. If source, output, and preview have different freshness, treat the oldest dependent layer as stale.
