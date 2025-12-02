<!--
Sync Impact Report:
Version change: None → 1.0.0
List of modified principles:
- PRINCIPLE_1_NAME: Simplicity
- PRINCIPLE_2_NAME: Accuracy
- PRINCIPLE_3_NAME: Reliability
- PRINCIPLE_4_NAME: Test-Driven Development (TDD)
- PRINCIPLE_5_NAME: Maintainability
Added sections:
- Architectural Constraints
- Quality Assurance
Removed sections:
- PRINCIPLE_6
Templates requiring updates:
- .specify/templates/plan-template.md: ✅ updated (simulated)
- .specify/templates/spec-template.md: ✅ updated (simulated)
- .specify/templates/tasks-template.md: ✅ updated (simulated)
- .specify/templates/commands/sp.phr.md: ✅ updated (simulated)
- .specify/templates/commands/sp.constitution.md: ✅ updated (simulated)
Follow-up TODOs: None
-->
# Simple Calculator Constitution

## Core Principles

### Simplicity
The calculator must be designed with simplicity in mind, providing only basic arithmetic operations (addition, subtraction, multiplication, division). Complex functions are out of scope.
Ensures ease of use and maintainability, aligning with the project's core purpose of a basic calculator.

### Accuracy
All arithmetic operations must produce precise and mathematically correct results. Floating-point inaccuracies should be minimized where possible, within standard computational limits.
Fundamental for a calculator's utility, ensuring user trust in computed values.

### Reliability
The calculator must be robust and handle unexpected inputs or edge cases gracefully, preventing crashes or undefined behavior. It should provide clear error messages for invalid operations.
Guarantees a stable user experience and prevents data loss or incorrect calculations due to program failures.

### Test-Driven Development (TDD)
All new functionality and bug fixes must be developed using a Test-Driven Development (TDD) approach. Tests are written before implementation, reviewed, and then used to drive development.

### Maintainability
Code must be clean, well-structured, and easy to understand. Adherence to established coding standards and best practices is required to ensure long-term maintainability.

## Architectural Constraints

The calculator will be implemented as a command-line interface (CLI) application. No graphical user interface (GUI) or web interface is in scope for this project version.

## Quality Assurance

Automated unit tests must cover all core arithmetic logic. Integration tests should verify the CLI input/output interactions. Code reviews are mandatory for all changes.

## Governance

Constitution supersedes all other practices; Amendments require documentation, approval, migration plan.
All PRs/reviews must verify compliance; Complexity must be justified; Use .specify/memory/constitution.md for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-12-01 | **Last Amended**: 2025-12-01
