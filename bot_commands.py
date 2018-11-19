BOT_CENTRAL_ID = 446243019205640212
ALLOWED_CHANNELS_ID = [BOT_CENTRAL_ID]

#TODO: Make this use embeds
#TODO: Make bot remember channels between restarts

async def on_cmd_channel(ctx):
  arg = ctx.args[0] #there should only be one argument for this cmd
  cid = ctx.channel.id

  if arg == "add":
    if not cid in ALLOWED_CHANNELS_ID:
      ALLOWED_CHANNELS_ID.append(cid)
      return await ctx.send("Now listening in this channel for commands. :blush:")
    else:
      return await ctx.send("I'm already listening in this channel :wink:")
  elif arg == "remove":
    if cid in ALLOWED_CHANNELS_ID:
      ALLOWED_CHANNELS_ID.remove(cid)
      return await ctx.send("Stopped listening in this channel for commands. :sob:")
    else:
      return await ctx.send("I'm not listening in this channel :blush:")
  elif arg == "list":
    return await ctx.send("not in yet ;)")

bot_commands = [
  {
    "name": "channel",
    "has_args": True,
    "max_args": 1,
    "min_args": 1,
    "valid_args": [
      "add",
      "remove",
      "list"
    ],
    "on_command": on_cmd_channel
  }
]
