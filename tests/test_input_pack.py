import json
import unittest

from inspect_inputs import ROOT, read_inputs


class InputPackTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_inputs()
        cls.manifest = json.loads((ROOT / 'data-manifest.json').read_text(encoding='utf-8'))

    def test_declared_tables_and_record_fields(self):
        self.assertEqual(self.data.keys(), self.manifest.keys())
        for name, records in self.data.items():
            rows = records if isinstance(records, list) else [records]
            with self.subTest(table=name):
                self.assertEqual(len(rows), self.manifest[name]['records'])
                for row in rows:
                    self.assertEqual(set(row), set(self.manifest[name]['fields']))

    def test_explicit_time_intervals_are_ordered(self):
        for name, records in self.data.items():
            if not isinstance(records, list):
                continue
            for row in records:
                for start, end in [('start_min','end_min'), ('from_day','until_day'), ('from_hour','until_hour')]:
                    if row.get(start) is not None and row.get(end) is not None:
                        with self.subTest(table=name, start=start, record=row):
                            self.assertLessEqual(row[start], row[end])
