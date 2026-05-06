"""Cross-platform path resolution for SifabAS.

Use these instead of `os.environ['USERPROFILE']` so the same scripts work on
Windows (Sondre's PC, Tom's PC) and macOS (Mac mini).

Usage in any tool:
    from _paths import SHARED, HOME
    quote = SHARED / 'Zigma360' / 'Projects' / 'SP-01415 ...'
"""

from pathlib import Path

HOME: Path = Path.home()


def _resolve_shared_drive() -> Path:
    """Find the SifabAS shared OneDrive folder ('Dokumenter - Felles').

    Windows: ~/OneDrive - Sifab AS/Dokumenter - Felles
    macOS:   ~/Library/CloudStorage/OneDrive-SifabAS/Dokumenter - Felles
             or ~/Library/CloudStorage/OneDrive-SharedLibraries-SifabAS/Dokumenter - Felles
             or (older OneDrive) ~/OneDrive - Sifab AS/Dokumenter - Felles
    """
    candidates = [
        HOME / 'OneDrive - Sifab AS' / 'Dokumenter - Felles',
        HOME / 'Library' / 'CloudStorage' / 'OneDrive-SifabAS' / 'Dokumenter - Felles',
        HOME / 'Library' / 'CloudStorage' / 'OneDrive-SharedLibraries-SifabAS' / 'Dokumenter - Felles',
    ]
    for p in candidates:
        if p.exists():
            return p
    # No path exists yet — return the most likely one for the current OS so
    # callers that build paths but don't read can still proceed.
    return candidates[0]


SHARED: Path = _resolve_shared_drive()


if __name__ == '__main__':
    print(f'HOME:   {HOME}')
    print(f'SHARED: {SHARED}')
    print(f'  exists: {SHARED.exists()}')
