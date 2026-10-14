# Implement tic-tac-toe tasks

> [09\_tic\_tac\_toe](Sem5/SE/Lab4/09_tic_tac_toe/)&#x20;
> this is a simple project with a readme describing what is to be done
> implement the given tasks, only implement it, i will test it myself

<details><summary>6 previous messages</summary>

> I’ll inspect the project README and existing code, then implement only the requested tasks without running or modifying unrelated files.
>
> <details><summary>Ran 3 commands</summary>
>
> - Ran `Get-ChildItem -Recurse -File | Select-Object -ExpandProperty FullName; Write-Output '--- README candidates ---'; Get-ChildItem -Recurse -File -Filter README* | Select-Object -ExpandProperty FullName`
> - Ran `Get-Content -Raw README.md; Write-Output '--- files ---'; Get-ChildItem -Recurse -File | Select-Object FullName; Write-Output '--- main.py ---'; Get-Content -Raw tic-tac-toe/main.py`
> - Ran `Get-Content -Raw game/game_engine.py; Write-Output '--- rules ---'; Get-Content -Raw game/rules.py; Write-Output '--- ai ---'; Get-Content -Raw game/ai.py; Write-Output '--- renderer ---'; Get-Content -Raw game/renderer.py`
>
> </details>
>
> The project is a compact Pygame implementation with the intended gaps isolated in `game_engine.py`, `rules.py`, and `renderer.py`. I’m implementing the fixes there, including persistent scores and keyboard controls: `R` for round restart, `M` for match reset, and `X`/`O` to choose who starts next round.
>
> <details><summary>Edited 4 files, ran a command</summary>
>
> - Wrote `./Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/game_engine.py` (+55 -24)
> - Wrote `./Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/renderer.py` (+2 -2)
> - Wrote `./Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/rules.py` (+4 -3)
> - Wrote `./Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/game_engine.py` (+1 -1)
> - Ran `python -m py_compile main.py game/*.py; git diff -- game/game_engine.py game/rules.py game/renderer.py`
>
> </details>
>
> The implementation is complete. One shell-specific compile command didn’t expand the wildcard on PowerShell, so I’m doing a direct syntax check on the three Python modules and reviewing the final diff now.
>
> <details><summary>Ran a command</summary>
>
> - Ran `python -m py_compile main.py game/game_engine.py game/rules.py game/ai.py game/renderer.py; git status --short`
>
> </details>
</details>

Implemented all requested tasks in:

- [game_engine.py](C:/Users/Anmol%20Vyas/OneDrive/Desktop/anmol's%20programming/Fun/Pesu/Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/game_engine.py)
- [rules.py](C:/Users/Anmol%20Vyas/OneDrive/Desktop/anmol's%20programming/Fun/Pesu/Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/rules.py)
- [renderer.py](C:/Users/Anmol%20Vyas/OneDrive/Desktop/anmol's%20programming/Fun/Pesu/Sem5/SE/Lab4/09_tic_tac_toe/tic-tac-toe/game/renderer.py)

Added diagonal detection, correct win/draw ordering, move validation, round-end protection, persistent scoreboard, first-player selection, and separate controls:

- `R`: restart round
- `M`: reset match and scoreboard
- `X`: X starts next round
- `O`: O starts next round

Python syntax validation passed.
