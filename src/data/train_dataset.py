from pathlib import Path
import shutil
import kagglehub

source_path = Path(kagglehub.dataset_download("uciml/red-wine-quality-cortez-et-al-2009"))

# Asumiendo que el script está en src/data/
project_root = Path(__file__).resolve().parents[2]
dest_path = project_root / "data" / "raw"

dest_path.mkdir(parents=True, exist_ok=True)

for file in source_path.iterdir():
    if file.is_file():
        shutil.move(str(file), str(dest_path / file.name))

print(f"Dataset copiado a: {dest_path}")
