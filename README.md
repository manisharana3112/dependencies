# SWAN custom environment (Venv) — example repository

This repository contains a minimal layout you can point SWAN to when creating a
Custom Environment with the Venv builder. It's intended as a starting point to
run Python workloads on swan.cern.ch using the new JupyterLab interface.

Files
- `requirements.txt` — Python packages to install (used by SWAN's Venv builder).
- `setup.sh` — optional helper to create a local venv and install requirements.
- `test_env.py` — small verification script to run inside the SWAN session.

Recommended SWAN UI settings (when creating the session)
- Try the new JupyterLab interface (experimental): enable
- Source: LCG
- Environment type: Custom Environment
- Repository: `https://gitlab.cern.ch/<your-username>/<your-repo>` (replace)
- Builder: Venv
- CPU: 2
- Memory: 4 GB (recommended); increase to 8 GB if you plan to load large datasets

Notes about the repository
- Keep `requirements.txt` updated with the Python packages you need. Pin versions
  if reproducibility is important.
- For extra system-level dependencies not available via pip, include install steps
  in `setup.sh` (be careful: installing apt packages may not be allowed in SWAN).

Verifying the environment inside SWAN
1. Open the terminal in the SWAN JupyterLab session or a notebook cell.
2. Check Python and pip:

```bash
python --version
pip --version
pip list | head -n 40
```

3. Run the quick verifier:

```bash
python test_env.py
```

Troubleshooting
- If SWAN fails to clone the repo: check visibility (private repos require credentials)
  and the URL. Use a deploy token or personal access token if needed.
- If packages fail to install: inspect the session logs in SWAN (the UI shows builder
  output), and consider pinning package versions or adding wheels where possible.

Further improvements
- Add a `requirements-dev.txt` for test/dev-only packages.
- Add CI to push tags or trigger rebuilds when you update requirements.
