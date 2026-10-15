# Lab 5: Static Code Analysis — Reflection

**Student:** Pradhyumn Anand  
**SRN:** PES2UG24CS358

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, insecure coding practices, and style violations early in development. It improves maintainability and reduces the likelihood of problems reaching users.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks overall Python code quality, including naming, unused variables, and design issues. Bandit focuses on common security vulnerabilities. Flake8 checks style and other code issues, including violations of Python's PEP 8 conventions. Using all three provides complementary checks.

## 3. What issues did you find, and how did you fix them?

The original program included unsafe expression evaluation, shell command execution, a hardcoded secret, a mutable default argument, and a broad exception handler. I replaced unsafe expression evaluation with a validated numeric calculation, removed shell execution and the hardcoded secret, initialized mutable data safely, and improved exception handling and file management.

## 4. What did you learn, and what are the limitations of static analysis?

I learned that static analysis can detect many potential problems before a program runs. However, a clean report does not prove that a program is completely secure or functionally correct. Functional testing and code review are also necessary. I reran the analysis tools after modifying the program to verify the changes.
