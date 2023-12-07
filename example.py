#!/usr/bin/env python3

from datetime import datetime
from discordlib import DiscordWebhook, DiscordMessage, DiscordEmbed

# Replace this with an actual webhook URL
# Preferably for a channel with no-one else in it but you
TEST_URL = "https://discord.com/api/webhooks/..."


def main():
    hook = DiscordWebhook(TEST_URL)

    # plain message
    plain = hook.send_plain("This is a plain message!")
    print(plain)

    # embed message
    rich = hook.send_rich(DiscordMessage(
        content="This is a rich message!",
        embeds=[
            DiscordEmbed(
                title="Test Embed",
                description="Basic embed with a picture and a footer!",
                image="https://picsum.photos/300",
                footer="Image courtesy of picsum.photos",
            ),
            DiscordEmbed(
                title="Test Embed 2",
                description="This is another embed with a different color and a timestamp!",
                color=DiscordEmbed.Colors.SECONDARY,
                timestamp=str(datetime.utcnow().isoformat())
            )
        ]
    ))
    print(rich)

    # update message
    edit_msg = hook.send_plain("This message should be replaced later on!")
    print(edit_msg)
    edit_msg.content = "This is the message that will replace the original!"
    hook.update(edit_msg)
    print(edit_msg)

    # allowed mentions
    hook.send_plain(
        "@everyone <@&role-id> <@user-id>\nWithout flags, all mentions parse!"
    )
    hook.send_plain(
        "@everyone <@&role-id> <@user-id>\nThis should be a silent message!",
        flags=DiscordMessage.Flags.SILENT_MESSAGE
    )
    hook.send_plain(
        "@everyone <@&role-id> <@user-id>\nThis should only ping the user!",
        flags=DiscordMessage.Flags.ALLOW_MENTION_USER | DiscordMessage.Flags.ALLOW_MENTION_USER
    )


if __name__ == "__main__":
    exit(main())
