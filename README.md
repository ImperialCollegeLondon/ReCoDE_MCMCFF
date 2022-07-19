<h1 align="center">🎲 ⛓️ 👉 🧪 Markov Chain Monte Carlo for fun and profit</h1>
<p align="center">
    <em>Using random numbers to do all the things.</em>
</p>

<p align="center">
<!-- <img src="https://github.com/Imperial-CMTH/koala/actions/workflows/ci.yml/badge.svg"/> -->
<!-- <a href="https://zenodo.org/badge/latestdoi/422218038">
    <img src="https://zenodo.org/badge/422218038.svg"/>
</a> -->
<a href="https://wfxr.mit-license.org/2017">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg"/>
</a>
<a href="https://mybinder.org/v2/gh/TomHodson/ReCoDE_MCMCFF/HEAD">
        <img src="https://mybinder.org/badge_logo.svg"/>
</a>
</p>

## Description

This is an exemplar project designed to showcase best practices in developing scientific software as part of the ReCoDE Project at Imperial College London.

**You do not need to know or care about Markov Chain Monte Carlo for this to be useful to you.**

Rather this project is primarily designed to showcase the tools and practices available to you when developing scientific software projects. Maybe you are a PhD student just starting, or a researcher just about to embark on a larger scale software project - there should be something interesting here for you.

## Learning Outcomes

- Creating virtual environments using Anaconda
- Plotting data using Matplotlib
- Improving code performance with `numba` and Just-in-time compilation
- Packaging Python projects into modules
- Writing a simple Monte Carlo simulation using `numba` and `numpy`
- Using Test Driven Development (TDD) to test your code
- Creating unittests with `pytest`
- Calculating the `coverage` of your codebase
- Visualising coarse and detailed views of the `coverage` in your codebase
- Creating property-based tests with `hypothesis`
- Creating regression tests
- Using autoformatters like `black` and other development tools
- Improving performance using `generators` and `yield`
- Making a reproducible Python environment using Anaconda
- Documenting your code using `sphinx`
- Writing docstrings using a standardised format

## Requirements

### Academic

Entry level researcher with basic knowledge of Python.

**Complementary Resources to the exemplar:**

- [The Turing Way](https://the-turing-way.netlify.app/) has tons of great resources on the topics discussed here.
- [Intermediate Research Software Development in Python](https://carpentries-incubator.github.io/python-intermediate-development/index.html)

### System

| Language                                                   | Version |
| ---------------------------------------------------------- | ------- |
| [Python](https://www.python.org/downloads/)                | >= 3.7  |
| [Anaconda](https://www.anaconda.com/products/distribution) | >= 4.1  |

## Getting Started

Take a look at the table of contents below and see if there are any topics that might be useful to you. The actual code lives in `src` and the documentation in `docs/learning` in the form of Jupyter notebooks.

When you're ready to dive in you have 4 options:

### 1. Launch the notebooks in Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ImperialCollegeLondon/ReCoDE_MCMCFF/HEAD?urlpath=lab%2Ftree%2Fdocs%2Flearning%2F01%20Introduction.ipynb)

_NOTE: Performance might be a bit slow_.

### 2. Clone the repo and run the Jupyter notebooks locally

```bash
git clone https://github.com/ImperialCollegeLondon/ReCoDE_MCMCFF mcmc
cd mcmc
pip install .[dev]
jupyter lab
```

_NOTE: Better performance but requires you have Python and Jupyter installed_.

### 3. View the Jupyter notebooks non-interactively via the online documentation

You can read all the Jupyter notebooks online and non-interactively in the official **[Documentation](https://recode-mcmcff.readthedocs.io/)**.

### 4. View the Jupyter notebooks non-interactively on GitHub

Click [here](https://github.com/ImperialCollegeLondon/ReCoDE_MCMCFF/tree/main/docs/learning)
to view the individual Jupyter notebooks.

## Project Structure

```bash
.
├── CITATION.cff # This file describes how to cite the work contained in this repository.
├── LICENSE # Outlines what legal rights you have to use this software.
├── README.md # You are here!
├── docs
│   ├── ... #Files to do with making the documentation
│   └── learning
│       └── #The Jupyter notebooks that form the main body of this project
│
├── pyproject.toml # Machine readable information about the MCFF package
├── readthedocs.yaml # Tells readthedocs.com how to build the documentation
├── requirements.txt # What packages MCFF requires
├── setup.cfg # Machine readable information about the MCFF package
├── src
│   └── MCFF # The actual code!
│
└── tests # automated tests for the code
```
