"""Tests for ReferenceManager."""

import re
import pytest
from ipynb_pdf.utils.reference_manager import ReferenceManager

@pytest.fixture
def manager():
    return ReferenceManager()

def test_reference_removal_simple(manager):
    """Test simple reference section removal."""
    text = """Texte avant les références.

---
**Références :**

<a id="ref1"></a>[1] Mitzenmacher, M., & Upfal, E. (2005). *Probability and Computing*. Cambridge University Press.

<!-- PAGE_BREAK -->"""
    
    result = manager.remove_reference_section(text)
    assert "Texte avant les références." in result
    assert "**Références :**" not in result
    assert "Mitzenmacher" not in result
    # Note: The current implementation removes everything after the separator, 
    # so the PAGE_BREAK at the end is also removed if it's AFTER the references.
    # This is expected behavior for page breaks INSIDE the reference section.

def test_reference_removal_complex(manager):
    """Test removal with complex content (from RandomAlgorithms)."""
    text = """---

### Ouvertures

Ce travail ouvre la voie à plusieurs approfondissements essentiels :

* **Le Paradigme Monte-Carlo :** Il serait pertinent de s'attaquer au paradigme Monte-Carlo (résultat approximatif, temps borné). L'analyse de l'**algorithme de Karger** [[1]](#ref1) pour la coupe minimale, serait un cas d'étude fascinant, nécessitant de calculer non pas une espérance de coût, mais une probabilité de succès (ex: $P(succ \ge 2/n^2)$) et les techniques d'**amplification** (répétition) nécessaires pour la rendre fiable.

---
**Références :**

<a id="ref1"></a>[1] Mitzenmacher, M., & Upfal, E. (2005). *Probability and Computing*. Cambridge University Press.
"""
    result = manager.remove_reference_section(text)
    assert "### Ouvertures" in result
    assert "pour la rendre fiable." in result
    assert "**Références :**" not in result
    assert "Mitzenmacher" not in result

def test_page_break_preservation(manager):
    """Test that PAGE_BREAK before references is preserved."""
    text = """Some content.
<!-- PAGE_BREAK -->
---
**Références :**
[1] Ref 1
"""
    result = manager.remove_reference_section(text)
    assert "Some content." in result
    assert "<!-- PAGE_BREAK -->" in result
    assert "**Références :**" not in result

def test_page_break_inside_reference_definition(manager):
    """Test that PAGE_BREAK inside a reference definition is NOT preserved (it's part of the ref)."""
    text = """Some content.
---
**Références :**
[1] Ref 1
<!-- PAGE_BREAK -->
[2] Ref 2
"""
    result = manager.remove_reference_section(text)
    assert "Some content." in result
    assert "<!-- PAGE_BREAK -->" not in result

