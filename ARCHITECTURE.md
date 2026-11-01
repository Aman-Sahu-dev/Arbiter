intended architecture
arbiter/
├── pyproject.toml
├── README.md
├── src/arbiter/
│   ├── __main__.py            # entry point, only starts the CLI
│   ├── cli/                   # presentation layer
│   │   ├── app.py             # menu loop, command routing
│   │   ├── prompts.py         # input helpers and validation
│   │   └── views.py           # output formatting
│   ├── services/              # application layer (use cases)
│   │   ├── policy_service.py
│   │   └── assessment_service.py
│   ├── engine/                # evaluation, pure functions
│   │   ├── evaluator.py       # assess(policy_version, application) -> Assessment
│   │   ├── scoring.py
│   │   └── explain.py         # builds the explanation from rule results
│   ├── domain/                # data and rules, no I/O
│   │   ├── models.py          # Policy, PolicyVersion, Criterion, Application, Assessment
│   │   ├── rules.py           # rule types plus registry
│   │   └── errors.py
│   └── storage/               # persistence layer
│       ├── base.py            # repository interfaces (Protocol)
│       ├── memory.py          # first implementation
│       └── sqlite.py          # added later
└── tests/                     # mirrors src: engine/, domain/, services/
