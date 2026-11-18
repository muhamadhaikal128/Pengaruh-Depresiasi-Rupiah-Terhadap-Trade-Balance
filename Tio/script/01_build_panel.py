from pathlib import Path
import runpy
p=Path(__file__).resolve().parent/"python"
runpy.run_path(str(p/"01_build_hs6.py"),run_name="__main__")
runpy.run_path(str(p/"02_prepare_cases.py"),run_name="__main__")
runpy.run_path(str(p/"03_audit_classification_time.py"),run_name="__main__")
