from datetime import datetime, timezone, timedelta
from os.path import dirname, abspath

import requests
import json
import yaml

import sys
args = sys.argv

now = datetime.now(timezone(timedelta(hours=9)))
base_dir = dirname(abspath(__file__))
print(base_dir)
with open(base_dir + '/config.yml') as yml:
    config = yaml.safe_load(yml)

print(config['SEND_DISCORD_WEB_HOOK_URL'])

#POST送信
response = requests.post(
    config['SEND_DISCORD_WEB_HOOK_URL'],
    headers = {'Content-Type': 'application/json'},
    data = json.dumps({
      "content": "",
      "embeds": [
        {
          "title": "Error Handling",
          "description": "プログラム上でエラーを感知しました。",
          "color": 14158346,
          "fields": [
            {
              "name": "Error Dir",
              "value": args[1]
            },
            {
              "name": "Error File",
              "value": args[2]
            },
            {
              "name": "Execution Date",
              "value": args[3]
            },
            {
              "name": "Error Log",
              "value": args[4]
            }
          ],
          "timestamp": str(now)
        }
      ],
      "attachments": []
  })
)