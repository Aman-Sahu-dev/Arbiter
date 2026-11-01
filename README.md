# Arbiter

A configurable, rule-based credit assessment engine that evaluates credit applications against policies and produces decisions with explanations.

## Overview

Arbiter evaluates credit applications using configurable policies. Each policy defines assessment criteria, scoring rules, and decision thresholds.

Users can create, view, update, and delete policies without modifying the application's source code. The assessment engine applies a selected policy to an application, evaluates its answers, calculates a score, and determines the resulting decision.

The project starts as a command-line application and will evolve incrementally.

## Core Features

### Policy Management
- Create, view, update, and delete policies.
- Enable or disable policies.
- Configure assessment criteria, scoring rules, and decision thresholds.
- Add, modify, and remove criteria within a policy.

### Credit Assessment
- Collect application information and answers.
- Evaluate applications against a selected policy.
- Calculate scores using policy-defined rules.
- Apply decision thresholds and mandatory conditions.
- Produce decisions with explanations.

### Persistence and History
- Store policies and criteria in SQLite.
- Store applications and their assessment results.
- Preserve historical assessment results when policies change.
- Retrieve previous assessments.

## Planned Features

- [ ] Policy management (CRUD operations)
- [ ] Configurable assessment criteria and scoring rules
- [ ] MCQ-based application assessment
- [ ] Rule-based scoring and decision evaluation
- [ ] Configurable decision thresholds
- [ ] Mandatory conditions and policy restrictions
- [ ] Written justifications for assessment results
- [ ] SQLite persistence
- [ ] Application and assessment history
- [ ] Policy versioning
- [ ] Automated tests for policy evaluation and scoring
- [ ] Optional AI-assisted analysis

## Design Principles

- **Policy-driven:** Assessment criteria and scoring rules are defined by policies rather than hardcoded into the engine.
- **Deterministic:** Identical inputs evaluated against the same policy version produce consistent results.
- **Separation of concerns:** Policy management, assessment logic, persistence, and user interaction remain independent.
- **Explainability:** Each assessment provides a traceable explanation of its score and decision.
- **Extensibility:** New rule types can be introduced without rewriting the core engine.
- **Minimal dependencies:** Prefer Python's standard library unless an external dependency provides a clear benefit.
- **Incremental development:** Implement and test core functionality before introducing additional complexity.
- **Historical integrity:** Changes to policies must not silently alter previous assessment results.
- **Security:** Policy evaluation must not require executing arbitrary user-supplied code.

## Tech Stack

- **Language:** Python
- **Project management:** uv
- **Database:** SQLite
- **Testing:** Python `unittest` or `pytest` (to be decided)
- **AI integration:** Optional, future consideration

## Project Structure

The initial source layout is planned as follows:

    Arbiter/
    ├── src/
    │   └── arbiter/
    │       ├── __init__.py
    │       ├── main.py
    │       ├── models.py
    │       ├── policy_manager.py
    │       ├── assessment.py
    │       └── database.py
    ├── tests/
    │   ├── test_policy_manager.py
    │   └── test_assessment.py
    ├── pyproject.toml
    ├── README.md
    └── .gitignore

## Assessment Workflow

1. A user creates or selects a policy.
2. The policy defines the criteria, evaluation rules, and scoring thresholds.
3. An application provides the information required by the policy.
4. The assessment engine evaluates the application against the policy.
5. The engine calculates the score and applies mandatory conditions.
6. Arbiter produces a decision with an explanation.
7. The application and assessment result can be stored for future reference.

## Project Status

**Early development.**

Initial development will focus on policy management and a deterministic assessment engine. Persistent application history, advanced rule types, and optional AI integration will follow as the core functionality matures.

## Disclaimer

Arbiter is a software project for implementing policy-based credit assessment. Its output does not establish creditworthiness on its own. Real-world lending decisions require validated assessment criteria, appropriate safeguards, and compliance with applicable laws and regulations.
