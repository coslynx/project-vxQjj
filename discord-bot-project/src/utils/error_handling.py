class ErrorHandling:
    @staticmethod
    async def handle_error(error):
        print(f"An error occurred: {error}")
        # Add custom error handling logic here

    @staticmethod
    async def handle_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Invalid command. Use !help to see available commands.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required arguments. Use !help command_name for more info.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have the required permissions to execute this command.")
        else:
            await ctx.send("An error occurred while executing the command. Please try again later.")

    @staticmethod
    async def handle_moderation_error(ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Invalid user provided. Please mention a valid user.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the required permissions to perform this action.")
        else:
            await ctx.send("An error occurred while performing the moderation action. Please try again later.")