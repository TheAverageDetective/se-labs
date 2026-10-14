Issues:

   | Issue | Type | Line(s) | Description | Fix Approach |
   |-------|------|---------|-------------|--------------|
   | Weak hash | Security | 25 | MD5 hashes are considered weak | Use a different algorithm |
   | File security | Security | 55 | The file mode is too permissive | Reduce file permissions |
   | Mutable default argument | Code quality | 9 | A list is used as a default argument and can retain state between calls | Use None and initialize the list inside the function |
   | Resource handling | Code quality | 28, 33 | Files are opened without context managers or explicit encoding | Use with statements and specify UTF-8 encoding |
   | Readability | Code | 9 | Less blank lines and few long lines | Add more blank lines and reduce line size |
   | Docstring | Code | 1 | Missing docstring at the top | Add a docstring |



