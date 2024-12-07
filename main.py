import discord, asyncio, os, botinfo, sqlite3, random, math
from discord.ext import commands
import gamedata as gdata
from game import create_game, GameState, Card, Deck, Player, Monster
from functions import RandomChamp
from datetime import datetime, timedelta
from database_setup import setup_database

# Define intents
intents = discord.Intents.all()
intents.message_content = True  # This is required to read message content

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Game sessions dictionary created
game_sessions = {}

# Setup Database
setup_database()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Basic Text Stuff
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# Pokemon Image
@bot.command()
async def randompokemon(ctx):
    # Specify the directory where your images are stored
    image_folder = 'DiscordBot/pokemon/images'

    # Get a list of all files in the directory
    images = os.listdir(image_folder)

    # Filter out only files with image extensions
    images = [img for img in images if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]

    # Check if there are any images in the folder
    if not images:
        await ctx.send("No images found in the folder.")
        return

    # Pick a random image
    random_image = random.choice(images)
    random_image_path = os.path.join(image_folder, random_image)
    file_name = os.path.splitext(random_image)[0].capitalize()

    # Send the image and the file name
    await ctx.send(f"A wild {file_name} has appeared!\n", file=discord.File(random_image_path))

# Roll
@bot.command()
async def roll(ctx):
    roll = random.randrange(1, 101)
    await ctx.send(roll)

@bot.command()
async def rolldice(ctx):
    roll = random.randrange(1, 7)
    await ctx.send(roll)

@bot.command()
async def rolldice2(ctx):
    roll = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    total = roll + roll2
    await ctx.send(f'D1: {roll}, D2:{roll2} Total: {total}')

@bot.command()
async def randomchamp(ctx):
    roll = RandomChamp()
    await ctx.send(roll)

# Game Related
# Command: Store Data
@bot.command()
async def store(ctx, *, data):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('REPLACE INTO user_data (user_id, data) VALUES (?, ?)', (ctx.author.id, data))
    conn.commit()
    conn.close()
    await ctx.send(f'Stored data for {ctx.author}: {data}')

# Command: Retrieve Data
@bot.command()
async def retrieve(ctx):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT data FROM user_data WHERE user_id = ?', (ctx.author.id,))
    row = c.fetchone()
    conn.close()
    data = row[0] if row else "No data found"
    await ctx.send(f'Data for {ctx.author}: {data}')

@bot.command()
async def checklevel(ctx):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT PlayerLevel FROM user_data WHERE user_id = ?', (ctx.author.id,))
    row = c.fetchone()
    conn.close()
    data = row[0] if row else "No data found"
    await ctx.send(f'Player level for {ctx.author}: {data}')

@bot.command()
async def checkatts(ctx):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM player_data WHERE user_id = ?', (ctx.author.id,))
    row = c.fetchone()
    conn.close()
    if row:
        data = f"Class: {row[1]}, HitPoints: {row[2]}, Strength: {row[3]}, Intelligence: {row[4]}, Agility: {row[5]}, Speed: {row[6]}"
    else:
        data = "No data found"
    await ctx.send(f'Attributes\n{data}')

async def gamelevel1(ctx):
    stage1mob = random.choice(gdata.monsters_grasslands)
    await ctx.send('Map 1 Stage 1\n'
                   f'Monster: {stage1mob}'
                   )

async def gamestartintro(ctx):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('REPLACE INTO user_data (user_id, PlayerLevel) VALUES (?, ?)', (ctx.author.id, 1))
    c.execute('REPLACE INTO player_data (user_id, HitPoints, Strength, Intelligence, Agility, Speed) VALUES (?, ?, ?, ?, ?, ?)', (ctx.author.id, 25, 5, 5, 5, 5))
    conn.commit()
    c.execute('SELECT * FROM player_data WHERE user_id = ?', (ctx.author.id,))
    row = c.fetchone()
    conn.close()
    if row:
        data = f"HitPoints: {row[2]}    Strength: {row[3]}    Intelligence: {row[4]}    Agility: {row[5]}    Speed: {row[6]}"
    else:
        data = "No data found"
    await ctx.send(f"\nNew Run Started\nCurrent Attributes\n{data}")
    choose_class = await ctx.send(
        '\nWhat class would you like to play?\n'
        "1️⃣ Warrior\n"
        "2️⃣ Rogue\n"
        "3️⃣ Mage\n"
    )
    
    emojis = ['1️⃣', '2️⃣', '3️⃣']

    for emoji in emojis:
        await choose_class.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in emojis

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('You took too long to respond!')
    else:
        conn = sqlite3.connect('DiscordBot/database/user_data.db')
        c = conn.cursor()
        if str(reaction.emoji) == '1️⃣':
            c.execute('UPDATE player_data SET Class = ? WHERE user_id = ?', ('Warrior', ctx.author.id))
            conn.commit()
            conn.close()
            await gamelevel1(ctx)
        elif str(reaction.emoji) == '2️⃣':
            c.execute('UPDATE player_data SET Class = ? WHERE user_id = ?', ('Rogue', ctx.author.id))
            conn.commit()
            conn.close()
            await gamelevel1(ctx)
        elif str(reaction.emoji) == '3️⃣':
            c.execute('UPDATE player_data SET Class = ? WHERE user_id = ?', ('Mage', ctx.author.id))
            conn.commit()
            conn.close()
            await gamelevel1(ctx)

@bot.command()
async def gamestart(ctx):
    menu_message = await ctx.send(
        "\nMain Menu:\n"
        "1️⃣ New Game\n"
        "2️⃣ Continue\n"
        "3️⃣ Quit\n"
    )

    emojis = ['1️⃣', '2️⃣', '3️⃣']

    for emoji in emojis:
        await menu_message.add_reaction(emoji)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in emojis

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('You took too long to respond!')
    else:
        if str(reaction.emoji) == '1️⃣':
            new_game_menu = await ctx.send(
                "Any previous saves will be lost, is that okay?\n"
                "1️⃣ Yes\n"
                "2️⃣ No\n"
            )
            new_game_emojis = ['1️⃣', '2️⃣']
            for emoji in new_game_emojis:
                await new_game_menu.add_reaction(emoji)

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('You took too long to respond!')
            else:
                if str(reaction.emoji) == '1️⃣':
                    await gamestartintro(ctx)
                else:
                    await gamestart(ctx)
        elif str(reaction.emoji) == '2️⃣':
            await ctx.send('No Previous Save Found')
        elif str(reaction.emoji) == '3️⃣':
            await menu_message.delete()

@bot.command()
async def start(ctx):
    game_state = create_game(ctx.author.name)
    game_sessions[ctx.author.id] = game_state
    await ctx.send(f"A wild {', '.join(monster.name for monster in game_state.monsters)} appear!\n{game_state.display_health()}\nYour hand:\n" + "\n".join([f"{i + 1}: {card}" for i, card in enumerate(game_state.player.hand)]))

@bot.command()
async def play(ctx, card_index: int = None, target_index: int = None):
    if ctx.author.id not in game_sessions:
        await ctx.send("You don't have an active game. Use !start to begin a new game.")
        return

    if card_index is None or target_index is None:
        await ctx.send("You need to choose a card and a target. Use the command like this: `!play <card_number> <target_number>`.")
        return

    game_state = game_sessions[ctx.author.id]
    if game_state.is_combat_over():
        await ctx.send("The game is over. Use !start to begin a new game.")
        return

    card_index -= 1
    target_index -= 1
    if card_index < 0 or card_index >= len(game_state.player.hand):
        await ctx.send("Invalid card choice. Please choose a valid card.")
        return

    if target_index < 0 or target_index >= len(game_state.monsters):
        await ctx.send("Invalid target choice. Please choose a valid target.")
        return

    result = game_state.player_turn(card_index, target_index)
    if game_state.is_combat_over():
        await ctx.send(result + "\n" + game_state.display_health() + "\n" + game_state.combat_result())
        del game_sessions[ctx.author.id]
        return

    monster_result = game_state.monster_turn()
    if game_state.is_combat_over():
        await ctx.send(result + "\n" + monster_result + "\n" + game_state.display_health() + "\n" + game_state.combat_result())
        del game_sessions[ctx.author.id]
        return

    await ctx.send(result + "\n" + monster_result + "\n" + game_state.display_health() + "\nYour hand:\n" + "\n".join([f"{i + 1}: {card}" for i, card in enumerate(game_state.player.hand)]))

# Gambling/Balance/Credit
# Function to get user balance from the database
def get_balance(user_id):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT balance FROM user_balances WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

# Function to set user balance in the database
def set_balance(user_id, balance):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO user_balances (user_id, balance) VALUES (?, ?)', (user_id, balance))
    conn.commit()
    conn.close()

# Function to update last_daily timestamp in the database
def update_last_daily(user_id):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('UPDATE user_balances SET last_daily = ? WHERE user_id = ?', (datetime.now(), user_id))
    conn.commit()
    conn.close()

# Function to get last_daily timestamp from the database
def get_last_daily(user_id):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT last_daily FROM user_balances WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    if result and result[0]:
        return datetime.fromisoformat(result[0])
    else:
        return None

# Gambling
# Dictionaries to keep track of the winning streak and total streak bonus for each user
winning_streaks = {}
streak_bonuses = {}

# Winstreak check
@bot.command()
async def winstreak(ctx):
    if ctx.author.id in winning_streaks:
        streak = winning_streaks[ctx.author.id]
        await ctx.send(f"Your current winning streak is {streak}.")
    else:
        await ctx.send(f"You do not have an active winning streak.")

# Gambling commands
@bot.command()
async def gamble(ctx, gamble_type: str = None, amount: int = None, choice: str = None):
    if gamble_type != 'cf' or amount is None or choice not in ['h', 't']:
        await ctx.send("Invalid command. Use !gamble cf (amount) h or !gamble cf (amount) t")
        return

    if amount <= 1:
        await ctx.send("The minimum bet for a coin flip is 2 credits.")
        return

    balance = get_balance(ctx.author.id)
    if balance is None:
        await ctx.send("You don't have an account yet. Use !daily to create an account and get your daily credits.")
        return

    if amount > balance:
        await ctx.send("You don't have enough credits to gamble that amount.")
        return

    await perform_coin_flip(ctx, amount, choice)

async def perform_coin_flip(ctx, amount, choice):
    balance = get_balance(ctx.author.id)
    result = random.choice(['h', 't'])
    win = (result == choice)
    
    # Send the result image
    image_folder = 'DiscordBot/Images/Coinflip'
    image_path = os.path.join(image_folder, 'dcoinheads.png' if result == 'h' else 'dcointails.png')

    if win:
        winnings = math.floor(amount * 0.9)
        new_balance = balance + winnings
        winnings_balance = winnings + amount
        streak_bonus = 0

        # Update or reset winning streak
        if ctx.author.id in winning_streaks:
            winning_streaks[ctx.author.id] += 1
            streak_bonuses[ctx.author.id] += math.floor(new_balance * 0.01)
        else:
            winning_streaks[ctx.author.id] = 1
            streak_bonuses[ctx.author.id] = 0
        
        if winning_streaks[ctx.author.id] > 1:
            streak_bonus = streak_bonuses[ctx.author.id]

        new_balance += streak_bonus
        set_balance(ctx.author.id, new_balance)
        result_message = (f"You won! The coin landed on {'heads' if result == 'h' else 'tails'}.\n"
                          f"You have won {winning_streaks[ctx.author.id]} times in a row and have won {winnings_balance} credits.\nYou also got {streak_bonus} credits for a streak bonus.\n"
                          f"Your new balance is {new_balance} credits.")
        result_message += "\nReact with 🎲 to push your luck or 💵 to cash out."

        message = await ctx.send(result_message, file=discord.File(image_path))

        # Add reactions
        await message.add_reaction('🎲')
        await message.add_reaction('💵')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['🎲', '💵']

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You took too long to respond! Cashing out automatically.')
            winning_streaks[ctx.author.id] = 1  # Reset streak on timeout
            streak_bonuses[ctx.author.id] = 0  # Reset streak bonus on timeout
        else:
            if str(reaction.emoji) == '🎲':
                if new_balance <= 1:
                    await ctx.send("You need more than 1 credit to continue gambling. Cashing out automatically.")
                    winning_streaks[ctx.author.id] = 1  # Reset streak if they can't continue
                    streak_bonuses[ctx.author.id] = 0  # Reset streak bonus if they can't continue
                else:
                    await perform_coin_flip(ctx, winnings_balance, choice)
            else:
                await ctx.send(f"You won {winnings_balance} credits and {streak_bonus} credits for a streak bonus. You now have {new_balance} credits.")
                winning_streaks[ctx.author.id] = 1  # Reset streak on cash out
                streak_bonuses[ctx.author.id] = 0  # Reset streak bonus on cash out
    else:
        new_balance = balance - amount
        total_streak_bonus = streak_bonuses.get(ctx.author.id, 0)
        result_message = (f"You lost! The coin landed on {'heads' if result == 'h' else 'tails'}. "
                          f"You lost {amount} credits and {total_streak_bonus} credits of streak bonus. Your new balance is {new_balance} credits.")

        # Reset winning streak and streak bonus
        if ctx.author.id in winning_streaks:
            del winning_streaks[ctx.author.id]
        if ctx.author.id in streak_bonuses:
            del streak_bonuses[ctx.author.id]

        set_balance(ctx.author.id, new_balance)

        await ctx.send(result_message, file=discord.File(image_path))


try:
    bot.run(botinfo.key)
except discord.LoginFailure:
    print("Invalid token. Please check your bot token.")
except Exception as e:
    print(f"An error occurred: {e}")
