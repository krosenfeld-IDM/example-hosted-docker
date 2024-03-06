# README

You need to update the `DOCK_PACK` variable to match what Jenkins pipeline produced.

Use Python 3.10 and install requirements:
```
pip install -r requirements.txt --index-url=https://packages.idmod.org/api/pypi/pypi-production/simple
```
and then launch the example:
```
python run_local.py
```

This will run the `run_remote.py` script and download the result to `output.txt`.

