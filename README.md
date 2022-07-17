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

This is an exemplar project designed to showcase best practices in developing scientific software as part of the ReCoDE Project at Imperial College London.

**You do not need to know or care about Markov Chain Monte Carlo for this to be useful to you.**

Rather this project is primarily designed to showcase the tools and practices available to you when developing scientific software projects. Maybe you are a PhD student just starting, or a researcher just about to embark on a larger scale software project - there should be something interesting here for you.

## Table of contents
1. [Introduction](docs/learning/01%20Introduction.ipynb)
1. [Packaging It Up](docs/learning/02%20Packaging%20It%20Up.ipynb)
1. [Writing a Markov Chain Monte Carlo Sampler](docs/learning/03%20Writing%20a%20Markov%20Chain%20Monte%20Carlo%20Sampler.ipynb)
1. [Testing](docs/learning/04%20Testing.ipynb)
1. [Adding Functionality](docs/learning/05%20Adding%20Functionality.ipynb)
1. [Speeding It Up](docs/learning/06%20Speeding%20It%20Up.ipynb)
1. [Producing Research Outputs](docs/learning/07%20Producing%20Research%20Outputs.ipynb)
1. [Doing Reproducible Science](docs/learning/08%20Doing%20Reproducible%20Science.ipynb)
1. [Adding Documentation](docs/learning/09%20Adding%20Documentation.ipynb)

## How to use this repository

Take a look at a the table of contents below and see if there are any topics that might be useful to you. The actual code lives in `./code` and the documentation in `./docs/learning`

When you're ready to dive in you have three options:
### 1. Launch them in Binder (easiest but a bit slow)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ImperialCollegeLondon/ReCoDE_MCMCFF/HEAD?urlpath=lab%2Ftree%2Fdocs%2Flearning%2F01%20Introduction.ipynb)

### 2. Clone the repo and run the jupyter notebooks locally. (Faster but requires you have python/jupyter installed)

```
git clone
cd
pip install -r requirements.txt
jupyter lab
```

### 3. View them non-interactively in GitHub via the links in the table of contents


## The map
```bash
.
├── CITATION.cff # This file describes how to cite the work contained in this repository.
├── LICENSE # Outlines what legal rights you have to use this software.
├── README.md # You are here!
├── docs
│   ├── ... #Files to do with making the documentation
│   └── learning
│       └── #The Jupyer notebooks that form the main body of this project
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

## External Resources
- [The Turing Way](https://the-turing-way.netlify.app/) has tons of great resources on the topics discussed here.
- [Intermediate Research Software Development in Python](https://carpentries-incubator.github.io/python-intermediate-development/index.html)



[TDD]: learning/01%20Introduction.ipynb
[intro]: learning/01%20Introduction.ipynb
[packaging]: learning/02%20Packaging%20it%20up.ipynb
[testing]: learning/02%20Testing.ipynb
