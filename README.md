<img src="./assets/discord.svg" width=200 style="padding-right:8px;"/><img src="./assets/python.svg" width=160/>

# Azure's Discord Webhook Library

A one-file library that you can drop into any project that you wish to have Webhook support! Only relies on the `requests` library, which is already included with many python runtimes.

## Example Usage

See [example.py](./example.py) for more examples.

```py
import discordlib

URL = "https://discord.com/api/webhooks/..."

webhook = DiscordWebhook(URL)
webhook.send_plain("This is a test message!")
```

## License

This file is distributed under the GNU GPLv3 license. *I offer no promises that this project will be maintained into the future. :thumbsup:*

A full copy of the license can be found in [LICENSE](./LICENSE).

---

*Copyright (C) 2023 Andrew "Azure-Agst" Augustine*