import discord, asyncio, os, botinfo, sqlite3, random, math, praw
from discord.ext import commands
import gamedata as gdata
from game import create_game, GameState, Card, Deck, Player, Monster
from functions import RandomChamp
from datetime import datetime, timedelta
from database_setup import setup_database
from opggscraper import get_player_stats_from_url, check_solo_duo_rank
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os


# --- BOT SETTINGS AND PRESET VARS --- #

# Define intents
intents = discord.Intents.all()
intents.message_content = True  # This is required to read message content

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Game sessions dictionary created
game_sessions = {}

# Setup Database
setup_database()

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="Replace", # Replace with your Reddit Client ID
    client_secret="Replace", # Replace with your Reddit Client Secret
    user_agent="discord-meme-bot"   # Replace with a descriptive name, e.g., "discord-meme-bot"
)

# --- Phased out keys (No longer in use) --- #
'''
# Humor API Settings
HUMOR_API_KEY = "Replace"
HUMOR_API_URL = "https://api.humorapi.com/memes/random"
'''
# --- BOT COMMANDS --- #

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Ping Command (Replies with 'Pong!')
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Echo Text
@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# --- Image Related Commands --- #
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

# --- Roll Related Commands --- #
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
    await ctx.send(f'D1: {roll} D2: {roll2} Total: {total}')

@bot.command()
async def randomchamp(ctx):
    roll = RandomChamp()
    await ctx.send(roll)

# --- Basic Arithmetic --- #
# Helper function to format results
def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

# Command to add two numbers
@bot.command()
async def add(ctx, a: float = None, b: float = None):
    if a is None or b is None:
        await ctx.send("Usage: !add <number1> <number2>")
    else:
        result = a + b
        formatted_a = format_result(a)
        formatted_b = format_result(b)
        formatted_result = format_result(result)
        await ctx.send(f"{formatted_a} + {formatted_b} = {formatted_result}")

# Command to subtract two numbers
@bot.command()
async def subtract(ctx, a: float = None, b: float = None):
    if a is None or b is None:
        await ctx.send("Usage: !subtract <number1> <number2>")
    else:
        result = a - b
        formatted_a = format_result(a)
        formatted_b = format_result(b)
        formatted_result = format_result(result)
        await ctx.send(f"{formatted_a} - {formatted_b} = {formatted_result}")

# Command to multiply two numbers
@bot.command()
async def multiply(ctx, a: float = None, b: float = None):
    if a is None or b is None:
        await ctx.send("Usage: !multiply <number1> <number2>")
    else:
        result = a * b
        formatted_a = format_result(a)
        formatted_b = format_result(b)
        formatted_result = format_result(result)
        await ctx.send(f"{formatted_a} * {formatted_b} = {formatted_result}")

# Command to divide two numbers
@bot.command()
async def divide(ctx, a: float = None, b: float = None):
    if a is None or b is None:
        await ctx.send("Usage: !divide <number1> <number2>")
    elif b == 0:
        await ctx.send("You cannot divide by zero.")
    else:
        result = a / b
        formatted_a = format_result(a)
        formatted_b = format_result(b)
        formatted_result = format_result(result)
        await ctx.send(f"{formatted_a} / {formatted_b} = {formatted_result}")

# --- Error Handling --- #
# Error handler for invalid argument type
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Invalid input. Please provide valid numbers.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Usage: {ctx.prefix}{ctx.command} <number1> <number2>")
    else:
        await ctx.send("An error occurred. You may have input an invalid command.")

# Command to perform a countdown and post a random emoji
@bot.command()
async def random_emoji(ctx):
    """Counts down from 5 and posts a random emoji with a specific message."""
    try:
        # Define interjecting messages from different bot personalities
        interjecting_messages = [
            # ChatGPT-like messages
            "Patience is key—it's almost here!",
            "Let's stay calm and see what happens next!",
            "I hope this ends well for you. 😊",
            # JimBot-like messages
            "Don't get your hopes up; this might be hilarious.",
            "Calling it now—it's gonna be 💩.",
            "Why are we even doing this? Oh, right—because it's funny.",
            # KawaiiBot-like messages
            "Ooh, I'm so excited! This is so fun! ✨",
            "What if it's the BEST outcome?! Let's hope! 😊",
            "Kawaii suspense is the best kind of suspense! 💖"
        ]

        # List of emojis with corresponding messages
        emoji_messages = {
            "💩": "Lmao you got shit! 💩",
            "🎉": "Congrats, you're a winner! 🎉",
            "😎": "Cool as ice! You got the sunglasses emoji! 😎",
            "😢": "Oh no, it's a sad day! 😢 But don't worry, better luck next time!",
            "🍕": "Yum! Pizza party time! 🍕 You're a slice above the rest!",
        }

        # Perform the countdown
        for i in range(5, 0, -1):
            await ctx.send(f"{i}...")
            await asyncio.sleep(1)

            # Add interjecting messages between countdown ticks
            if i > 1:  # Avoid sending suspense message after the last tick
                suspense_message = random.choice(interjecting_messages)
                await ctx.send(suspense_message)
                await asyncio.sleep(1)  # Short pause after the message

        # Randomly choose an emoji
        emoji = random.choice(list(emoji_messages.keys()))
        message = emoji_messages[emoji]

        # Send the corresponding message
        await ctx.send(message)

    except Exception as e:
        # Handle unexpected errors gracefully
        await ctx.send("Something went wrong during the countdown. Please try again later.")
        print(f"Error during countdown: {e}")

# --- Game Related --- #
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

# Command to check balance
@bot.command()
async def bal(ctx):
    balance = get_balance(ctx.author.id)
    if balance is None:
        await ctx.send("You don't have an account yet. Use !daily to create an account and get your daily credits.")
    else:
        await ctx.send(f"{ctx.author.mention}, your current balance is {balance} credits.")

# Command to claim daily credits
@bot.command()
async def daily(ctx):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT balance, last_daily FROM user_balances WHERE user_id = ?', (ctx.author.id,))
    result = c.fetchone()

    if result:
        balance, last_daily = result
        now = datetime.now()
        if last_daily is not None and (now - datetime.strptime(last_daily, '%Y-%m-%d %H:%M:%S')).days < 1:
            await ctx.send(f"{ctx.author.mention}, you have already claimed your daily credits. Try again later.")
            conn.close()
            return

        new_balance = balance + 500
        c.execute('UPDATE user_balances SET balance = ?, last_daily = ? WHERE user_id = ?', (new_balance, now.strftime('%Y-%m-%d %H:%M:%S'), ctx.author.id))
    else:
        new_balance = 500
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c.execute('INSERT INTO user_balances (user_id, balance, last_daily) VALUES (?, ?, ?)', (ctx.author.id, new_balance, now))

    conn.commit()
    conn.close()
    await ctx.send(f"{ctx.author.mention}, you have received 500 daily credits! Your new balance is {new_balance} credits.")

# Gambling
# Dictionaries to keep track of the winning streak and total streak bonus for each user
winning_streaks = {}
streak_bonuses = {}

def get_streak_data(user_id):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('SELECT winning_streak, streak_bonus FROM user_streaks WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    if result:
        return result
    else:
        return 0, 0

def set_streak_data(user_id, winning_streak, streak_bonus):
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()
    c.execute('INSERT OR REPLACE INTO user_streaks (user_id, winning_streak, streak_bonus) VALUES (?, ?, ?)', (user_id, winning_streak, streak_bonus))
    conn.commit()
    conn.close()

def reset_streak_data(user_id):
    set_streak_data(user_id, 0, 0)

# Get winstreak Data
@bot.command()
async def winstreak(ctx):
    winning_streak, streak_bonus = get_streak_data(ctx.author.id)
    if winning_streak > 0:
        await ctx.send(f"Your current winning streak is {winning_streak} with a streak bonus of {streak_bonus} credits.")
    else:
        await ctx.send(f"You do not have an active winning streak.")

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
        winnings_balance = winnings + amount

        # Get or update winning streak
        winning_streak, streak_bonus = get_streak_data(ctx.author.id)
        winning_streak += 1
        
        if winning_streak > 1:
            streak_bonus += math.floor(winnings * 0.1)  # Calculate streak bonus based on winnings

        new_balance = balance + winnings + streak_bonus
        set_balance(ctx.author.id, new_balance)
        set_streak_data(ctx.author.id, winning_streak, streak_bonus)

        result_message = (f"You won! The coin landed on {'heads' if result == 'h' else 'tails'}.\n"
                          f"You have won {winning_streak} times in a row and have won {winnings_balance} credits.\n"
                          f"You also got {streak_bonus} credits for a streak bonus.\n"
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
            reset_streak_data(ctx.author.id)  # Reset streak on timeout
        else:
            if str(reaction.emoji) == '🎲':
                if new_balance <= 1:
                    await ctx.send("You need more than 1 credit to continue gambling. Cashing out automatically.")
                    reset_streak_data(ctx.author.id)  # Reset streak if they can't continue
                else:
                    await perform_coin_flip(ctx, winnings_balance, choice)
            else:
                await ctx.send(f"You won {winnings_balance} credits and {streak_bonus} credits for a streak bonus. You now have {new_balance} credits.")
                reset_streak_data(ctx.author.id)  # Reset streak on cash out
    else:
        winning_streak, streak_bonus = get_streak_data(ctx.author.id)
        total_streak_bonus = streak_bonus
        new_balance = balance - amount - total_streak_bonus
        result_message = (f"You lost! The coin landed on {'heads' if result == 'h' else 'tails'}. "
                          f"You lost {amount} credits and {total_streak_bonus} credits of streak bonus. Your new balance is {new_balance} credits.")

        # Reset winning streak and streak bonus
        reset_streak_data(ctx.author.id)

        set_balance(ctx.author.id, new_balance)

        await ctx.send(result_message, file=discord.File(image_path))

# --- Flow OPGG Points Calculation --- #
@bot.command()
async def points(ctx, url: str):
    # Validate the URL
    if not url.startswith("https://www.op.gg/summoners/"):
        await ctx.send("Invalid URL. Please provide a valid OP.GG profile URL (must include 'www'). \n Usage: !points <op.gg url> \n ex: !points https://www.op.gg/summoners/na/Sarcasm-Lol")
        return

    # Check for Solo/Duo rank
    if not check_solo_duo_rank(url):
        await ctx.send(
            "Sorry but this account can not participate in the Tournament due to having no Solo/Duo rank"
        )
        return

    # Fetch player stats
    try:
        result = get_player_stats_from_url(url)
        await ctx.send(result)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send("Usage: !points <op.gg url>")

# Command to test scraping elements
@bot.command()
async def scrapetest(ctx, url: str, element_class: str):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.140 Safari/537.36")
    chrome_options.add_argument("--headless=new")

    chrome_service = Service("opggscraper\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.get(url)

    try:
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Attempt to find the specified element
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, element_class)))
            await ctx.send(f"Element with class `{element_class}` found:\n`{element.text}`")
        except:
            await ctx.send(f"Element with class `{element_class}` not found.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
    finally:
        driver.quit()

# --- Commands with API Requests --- #
# Command to fetch memes from a subreddit
@bot.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")  # Choose a meme subreddit
    posts = list(subreddit.hot(limit=50))  # Get top 50 hot posts

    # Choose a random meme post
    post = random.choice(posts)

    # Ensure it's an image post
    if post.url.endswith(("jpg", "jpeg", "png", "gif")) or "imgur.com" in post.url:
        await ctx.send(f"**{post.title}**\n{post.url}")
    else:
        await ctx.send("Couldn't find an image meme, try again!")

# Command to fetch posts from pcmasterrace
@bot.command()
async def pcmasterrace(ctx):
    subreddit = reddit.subreddit("pcmasterrace")  # Choose a meme subreddit
    posts = list(subreddit.hot(limit=50))  # Get top 50 hot posts

    # Choose a random meme post
    post = random.choice(posts)

    # Ensure it's an image post
    if post.url.endswith(("jpg", "jpeg", "png", "gif")) or "imgur.com" in post.url:
        await ctx.send(f"**{post.title}**\n{post.url}")
    else:
        await ctx.send("Couldn't find an image meme, try again!")

# Command to fetch posts from webcomics
@bot.command()
async def webcomics(ctx):
    subreddit = reddit.subreddit("webcomics")  # Choose a meme subreddit
    posts = list(subreddit.hot(limit=50))  # Get top 50 hot posts

    # Choose a random meme post
    post = random.choice(posts)

    # Ensure it's an image post
    if post.url.endswith(("jpg", "jpeg", "png", "gif")) or "imgur.com" in post.url:
        await ctx.send(f"**{post.title}**\n{post.url}")
    else:
        await ctx.send("Couldn't find an image meme, try again!")

# More memes command selecting from multiple subreddits
@bot.command()
async def morememes(ctx):
    meme_subreddits = [
        "memes",
        "dankmemes",
        "funny",
        "wholesomememes",
        "me_irl",
        "historymemes",
        "techsupportgore",
        "programmerhumor",
        "terriblefacebookmemes",
        "webcomics",
        "pcmasterrace",
        "WTF"
    ]

    chosen_subreddit = random.choice(meme_subreddits)

    try:
        subreddit = reddit.subreddit(chosen_subreddit)
        found_meme = None

        for submission in subreddit.hot(limit=20):
            if not submission.stickied and submission.url.endswith(("jpg", "jpeg", "png", "gif")) or "imgur.com" in submission.url:
                if found_meme is None:
                    found_meme = submission.url  # Store the first valid meme
                else:
                    await ctx.send(f"r/{chosen_subreddit} \n **{submission.title}** \n {submission.url}")
                    return

        if found_meme:
            await ctx.send(f"r/{chosen_subreddit} \n {found_meme}")
        else:
            await ctx.send("Couldn't find a meme at the moment.")

    except Exception as e:
        await ctx.send(f"Error fetching meme: {e}")
        print(f"Error fetching meme: {e}")

try:
    bot.run(botinfo.key)
except discord.LoginFailure:
    print("Invalid token. Please check your bot token.")
except Exception as e:
    print(f"An error occurred: {e}")
