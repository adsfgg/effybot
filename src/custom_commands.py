import discord

# custom commands
ALLOWED_CHANNELS_ID = []

#TODO: Make this use embeds
#TODO: Make bot remember channels between restarts

async def on_cmd_channel(ctx):
  arg = ctx.args[0] #there should only be one argument for this cmd
  cid = ctx.channel.id
  
  if arg == "start":
    if not cid in ALLOWED_CHANNELS_ID:
      ALLOWED_CHANNELS_ID.append(cid)
      return await ctx.send("Now listening in this channel for commands. :blush:")
    else:
      return await ctx.send("I'm already listening in this channel :wink:")
  elif arg == "stop":
    if cid in ALLOWED_CHANNELS_ID:
      ALLOWED_CHANNELS_ID.remove(cid)
      return await ctx.send("Stopped listening in this channel for commands. :sob:")
    else:
      return await ctx.send("I'm not listening in this channel :blush:")

async def on_cmd_channels(ctx):
  cid = ctx.channel.id
  channels_list = []
  
  for channel_id in ALLOWED_CHANNELS_ID:
    channels_list.append(ctx.guild.get_channel(channel_id).name)
  
  msg = discord.Embed(title="Channels", description=str(channels_list), color=0xFFFFFF)
  await ctx.send(embed=msg)

bot_commands = [
                
                # Channel
                {
                "name": "channel",
                "has_args": True,
                "num_args": 1,
                "valid_args": [
                               "start",
                               "stop"
                               ],
                "on_command": on_cmd_channel,
                "owner_only": True
                },
                
                # Channels
                {
                "name": "channels",
                "has_args": False,
                "on_command": on_cmd_channels,
                "owner_only": True
                }
]

def set_allowed_channels(allowed_channels):
  global ALLOWED_CHANNELS_ID
  ALLOWED_CHANNELS_ID = allowed_channels

def get_allowed_channels():
  return ALLOWED_CHANNELS_ID
