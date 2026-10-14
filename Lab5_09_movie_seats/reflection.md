1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues were the missing docstrings, extra blank lines, long lines,
and the unsafe file permission value. These could be fixed directly by adding
documentation, reformatting the code, and changing the permission mode. The
hardest issue was replacing the mutable default argument and removing the
global assignment while preserving the existing reservation behavior. These
required understanding how state was shared between function calls and how
the loaded data updated the global `shows` dictionary.

2. Did the static analysis tools report any false positives? If so, describe one example.

No clear false positives were reported. The warnings were applicable to the
code: MD5 was a weak hash choice, `0o777` was too permissive, the bare
`except` could hide unexpected errors, and the file handles were not managed
explicitly. Some style warnings, such as the naming warning for
`printSeatingSummary`, were subjective, but changing the name to
`print_seating_summary` improved consistency with Python conventions.

3. How would you integrate static analysis tools into your actual software development workflow?

I would run tools such as Flake8, Pylint, and Bandit locally before committing
code, using a consistent configuration shared by the project. I would also
run them automatically in a CI pipeline for every pull request. Critical
security findings and errors would block the merge, while less serious style
warnings could be reviewed and fixed as part of normal maintenance.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code became easier to read because it now has module and function
docstrings, consistent naming, f-strings, proper spacing, and shorter lines.
The mutable default argument no longer risks retaining data across calls.
Explicit exception handling avoids hiding unrelated errors, and context
managers ensure files are closed correctly. UTF-8 encoding makes file access
explicit, while SHA-256 and restrictive file permissions improve security.
