# 📄 ipynb-pdf

**Transformez vos Notebooks Jupyter en documents PDF professionnels et académiques.**

`ipynb-pdf` est un outil de conversion avancé conçu pour les scientifiques, les chercheurs et les data scientists qui souhaitent produire des rapports, des articles ou des thèses directement depuis Jupyter, sans passer par LaTeX manuellement.

---

## 🚀 Pourquoi utiliser ipynb-pdf ?

* **📚 Gestion Intelligente des Références** : Centralise automatiquement vos citations, dédoublonne les entrées et génère une bibliographie propre en fin de document.
* **🎨 Typographie Premium** : Utilise des polices de haute qualité (Charter, Lato, Fira Code) et une mise en page soignée (marges, interlignage, césure).
* **🙈 Contrôle Granulaire** : Masquez le code, les sorties ou certaines cellules spécifiques grâce à un système de tags simple (`hide_code`, `internal`, `remove_input`).
* **➗ Support Mathématique** : Rendu impeccable des équations LaTeX.
* **⚙️ 100% Configurable** : Adaptez tout via un simple fichier YAML (marges, polices, comportements).

---

## 📦 Installation

### Prérequis

Ce projet utilise `weasyprint` pour la génération PDF.

* **Windows** : Vous aurez besoin de GTK3. Suivez les instructions officielles de WeasyPrint pour Windows.
* **Linux/macOS** : Installez les librairies graphiques nécessaires (ex: `pango`, `gdk-pixbuf`).

### 🚀 Installation rapide (PyPI)

C'est la méthode recommandée. Ouvrez votre terminal et lancez :

```bash
pip install ipynb-pdf
```

Une fois installé, la commande `ipynb-pdf` est disponible partout dans votre système.

### 🔧 Installation depuis les sources (Développement)

Si vous souhaitez contribuer ou tester la dernière version non publiée :

```bash
git clone https://github.com/KpihX/ipynb-pdf.git
cd ipynb-pdf
pip install .
```

---

## 🛠️ Utilisation

### Commande de base

Convertissez un notebook en une seule ligne de commande :

```bash
ipynb-pdf mon_notebook.ipynb
```

### Avec configuration personnalisée

Pour un contrôle total sur le rendu, utilisez un fichier de configuration :

```bash
ipynb-pdf mon_notebook.ipynb --config config.yaml --output rapport_final.pdf
```

---

## 📂 Exemples

Le dossier `examples/` contient tout ce qu'il faut pour démarrer :

### 1. Cas Simple (`examples/simple_case/`)

Une démonstration des fonctionnalités de base : masquage de code, tags, et formatage simple.

```bash
ipynb-pdf examples/simple_case/feature_demo.ipynb --config examples/simple_case/config.yaml
```

### 2. Cas Complexe (`examples/complex_case/`)

Un exemple réel de papier académique ("Algorithmes Randomisés") avec :

* Formules mathématiques complexes
* Figures et graphiques
* Bibliographie et citations croisées
* Mise en page stricte

```bash
ipynb-pdf examples/complex_case/RandomAlgorithms.ipynb --config examples/complex_case/config_RandomAlgorithms.yaml
```

---

## ⚙️ Configuration

Créez un fichier `config.yaml` pour surcharger les paramètres par défaut. Voici les options principales :

```yaml
# === Apparence ===
pdf_margin_top: 2.5cm
pdf_margin_bottom: 2.5cm
text_font_family: "Charter, serif"
code_font_size: 9pt

# === Comportement ===
hide_code_by_default: false       # Masquer tout le code par défaut ?
hide_execution_count: true        # Masquer les [1]: ?
reflow_markdown: true             # Reformater le texte Markdown ?

# === Tags Spéciaux ===
remove_cells_with_tag: ['remove', 'internal']
hide_code_with_tag: ['hide_code', 'secret']
partial_code_with_tag: ['partial'] # Montre seulement le début/fin du code

# === Bibliographie ===
centralize_references: true       # Regrouper les références à la fin ?
```

---

## 🏗️ Structure du Projet

```text
ipynb-pdf/
├── ipynb_pdf/              # 🐍 Code source du package
│   ├── css/                # 🎨 Feuilles de style CSS (Base, Typo, Code)
│   ├── templates/          # 📝 Templates HTML (Jinja2)
│   ├── utils/              # 🔧 Utilitaires (Preprocessing, Refs, Logs)
│   ├── cli.py              # 💻 Point d'entrée ligne de commande
│   └── config.py           # ⚙️ Gestion de la configuration
├── examples/               # 💡 Exemples (Simple & Complexe)
├── tests/                  # 🧪 Tests unitaires (Pytest)
├── pyproject.toml          # 📦 Métadonnées du projet
└── README.md               # 📖 Ce fichier
```

---

## 🧪 Développement

Pour lancer la suite de tests et vous assurer que tout fonctionne :

```bash
pytest tests/
```

---

## 👤 Auteur

### KpihX

* [GitHub Profile](https://github.com/KpihX)

## 📄 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, le modifier et le distribuer.
