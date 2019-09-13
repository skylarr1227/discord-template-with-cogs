from libneko.extras import superuser
import discord
from discord.ext import commands

class WhitelistedOwnerSuperuserCog(commands.Cog):
    
    owners = [1856271517491511531, 4325824835683126527, 21512642468346835632]
    async def owner_check(self, ctx):
        return ctx.author.id in self.owners
    
    
    bot.add_cog(WhitelistedOwnerSuperuserCog())
