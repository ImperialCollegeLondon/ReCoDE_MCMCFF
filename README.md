<h1 align="center">🎲 ⛓️ 👉 🧪 Markov Chain Monte Carlo for fun and profit</h1>
<p align="center">
    <em>Using random numbers to do all the things.</em>
</p>

<p align="center">
<img src="https://github.com/Imperial-CMTH/koala/actions/workflows/ci.yml/badge.svg"/>
<a href="https://zenodo.org/badge/latestdoi/422218038">
    <img src="https://zenodo.org/badge/422218038.svg"/>
</a>
<a href="https://wfxr.mit-license.org/2017">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg"/>
</a>
</p>

This is an exemplar project designed to showcase best practices in developing scientific software as part of the ReCode Project at Imperial College London. 

**You do not need to know or care about Markov Chain Monte Carlo for this to be useful to you.**

Rather this project is primarily designed to showcase the tools and practices available to you when developing scientific softare projects. Maybe you are a PhD student just starting or a researcher just about to embark on a larger scale softare project there should be something intersting here for you.

## How to use this repo

Take a look at a the table of contents below and see if there are any topics that might be useful to you. The actual code lives in `./code` and the documentation in `./learning`

## Table of contents
1. [A short introduction][intro]
2. The problem
3. A quick and dirty solution
4. Planning out a larger software project
5. Python development environnments: Pip, Conda, setup.py and all that.
6. Test driven development: it's fun.
7. Using Jupyter Notebooks during development
8. Documentation
9. Software Reproducability
10. Citing software in a publication: CITATION.cff

## The map
``` bash
.
├── CITATION.cff #This file describes how to cite the work contained in this repository.
├── LICENSE # Outlines what legal rights you have to use this software.
├── README.md # You are here!
├── code 
│   ├── README.md # Human readable information about the little python package in here
│   ├── pyproject.toml # Machine readable information about that same package
│   ├── setup.cfg # Tells Pip how to install this package
│   ├── src
│   │   └── MCFF # The actual code lives in here!
│   └── tests # automated tests for the code
└── learning # Supporting documentation
    └── Untitled.ipynb
```




[TDD]: http://placeholder_link.com/
[intro]: http://placeholder_link.com/
