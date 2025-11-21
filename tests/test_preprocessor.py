"""Tests for preprocessing rules."""

from __future__ import annotations

import nbformat

from ipynb_pdf.preprocessor import preprocess_notebook


def _make_notebook():
	nb = nbformat.v4.new_notebook()
	nb.cells = [
		nbformat.v4.new_markdown_cell("Paragraph " * 20),
		nbformat.v4.new_code_cell("import math"),
		nbformat.v4.new_code_cell("x = 1\nprint(x)", metadata={"tags": ["hide_code"]}),
	]
	return nb


def test_markdown_reflow_and_hide_code():
	nb = _make_notebook()
	config = {
		"reflow_markdown": True,
		"max_line_length": 40,
		"hide_code_with_tag": ["hide_code"],
		"remove_cells_with_tag": [],
		"hide_code_by_default": False,
		"detect_long_code_lines": True,
		"long_line_threshold": 80,
		"hide_import_only_cells": True,
	}
	processed = preprocess_notebook(nb, config)

	assert len(processed.cells) == 3
	md_lines = processed.cells[0].source.splitlines()
	assert all(len(line) <= 40 for line in md_lines if line)
	
	# Check that the cell is marked for input removal instead of having empty source
	assert "remove_input" in processed.cells[1].metadata.get("tags", [])
	# Source should remain intact
	assert processed.cells[1].source == 'import math'
	
	# Same for the third cell (import only)
	assert "remove_input" in processed.cells[2].metadata.get("tags", [])


def test_remove_cell_by_tag():
	nb = nbformat.v4.new_notebook()
	nb.cells = [
		nbformat.v4.new_markdown_cell("keep me"),
		nbformat.v4.new_markdown_cell("remove me", metadata={"tags": ["remove"]}),
	]
	processed = preprocess_notebook(nb, {"remove_cells_with_tag": ["remove"]})
	assert len(processed.cells) == 1
	assert processed.cells[0].source == "keep me"
