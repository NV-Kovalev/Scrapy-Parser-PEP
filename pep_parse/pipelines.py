import csv
import datetime as dt
from collections import defaultdict

from .settings import DATETIME_FORMAT, BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.stats = defaultdict(int)
        self.result_dir = BASE_DIR / 'results'

    def process_item(self, item, spider):
        self.stats[item['status']] += 1
        return item

    def close_spider(self, spider):
        results = [('Статус', 'Количество')]
        results.extend(self.stats.items())
        results.append(('Total', sum(self.stats.values())))

        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_path = f'{self.result_dir}/status_summary_{now_formatted}.csv'
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
