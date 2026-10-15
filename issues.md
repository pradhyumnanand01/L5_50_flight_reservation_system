# Lab 5: Static Code Analysis — Issues and Fixes

**Student:** Pradhyumn Anand  
**SRN:** PES2UG24CS358  
**Repository:** L5_50_flight_reservation_system

## Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe use of eval | Security | 426–432 | Evaluates an expression supplied as a function argument, which can execute arbitrary Python code. | Replace expression evaluation with a safe, explicitly defined baggage-fee calculation. |
| Shell command injection risk | Security | 442–449 | Builds a shell command using a filename and executes it through `os.system()`. | Remove the shell invocation and use safe Python file operations. |
| Hardcoded secret | Security | 463–482 | A secret-like token is embedded in the source and printed to the output. | Remove the hardcoded token and avoid printing secrets. |
| Mutable default argument | Bug | 380–397 | `baggage_tags=[]` reuses the same list across function calls. | Use `None` as the default and initialize a new list inside the function. |
| Bare exception handler | Reliability | 399–409 | `except:` silently catches all exceptions and hides failures. | Catch the specific expected exception and handle it appropriately. |
| Unsafe file handling | Reliability | 442–447 | The file is opened without a context manager, so cleanup depends on explicit close logic. | Use `with open(...)` to manage the file safely. |
| Weak passenger hash | Security | 434–436 | MD5 is not suitable for security-sensitive hashing. | Avoid MD5 for security purposes; use an appropriate modern approach if a security hash is genuinely required. |

**Note:** Recheck the line numbers against the file you actually edited. Add the actual tool finding or code observation for each issue and mark the issues that you have verified as fixed.
## Verification

After applying the fixes, I reran Pylint, Bandit, and Flake8 on `flight_reservation_system.py`. I reviewed the updated reports and checked that the program still ran.

Final Pylint score: [Enter the score from pylint_report.txt]

Remaining Pylint findings: [Enter actual findings or None]

Remaining Bandit findings: [Enter actual findings or None]

Remaining Flake8 findings: [Enter actual findings or None]
