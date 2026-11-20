import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_inputs(root=ROOT):
    return {p.stem: json.loads(p.read_text(encoding='utf-8'))
            for p in sorted((root / 'data').glob('*.json'))}


if __name__ == '__main__':
    for name, value in read_inputs().items():
        count = len(value) if isinstance(value, list) else 1
        print(f'{name}：{count} 条')
