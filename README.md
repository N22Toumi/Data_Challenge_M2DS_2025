# Predicting Energy Consumption in a Building

[![Build status](https://github.com/ramp-kits/template-kit/actions/workflows/test.yml/badge.svg)](https://github.com/ramp-kits/template-kit/actions/workflows/test.yml)

## Introduction

This challenge is based on the paper [Data driven prediction models of energy use of appliances in a low-energy house](https://www.sciencedirect.com/science/article/pii/S0378778816308970?fr=RR-2&ref=pdf_download&rr=91bc15f83edb04a0). This study investigates the feasibility of predicting the energy consumption of appliances in a low-energy house.

The dataset comes from a wireless sensor network installed in a house, collecting temperature and humidity data from different rooms. It also includes weather data from a nearby airport station and recorded energy usage of lighting fixtures and appliances.

The goal is to develop predictive models that accurately estimate household energy consumption based on the available data. By identifying key factors that influence energy use, participants will refine their models to enhance prediction accuracy and uncover meaningful patterns. Understanding and predicting energy use is key to reducing waste, cutting costs, and supporting sustainability. Better energy management helps improve home automation, use resources more efficiently, and reduce environmental impact. Insights from this challenge can lead to new ideas and solutions, helping homeowners, energy providers, and policymakers create a greener and more efficient future.

The challenge in this RAMP is to design an algorithm that generates well on unseen season. Particularly, the train set available for the competitors detailed data from winter and the test set for the competition contained spring data.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, we provide an `environment.yml` file for similar
usage.

### Challenge description

Get started on this RAMP with the
[dedicated notebook](template_starting_kit.ipynb).

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

You may need to download the data first:
```bash
python download_data.py
```

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)
