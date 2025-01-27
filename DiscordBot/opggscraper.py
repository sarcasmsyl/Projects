from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_player_stats(username, tag, region="na"):
    url = f"https://op.gg/summoners/{region}/{username}-{tag}"

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

        # Initialize the result string
        result_text = f"**Player Profile:**\nUsername: {username}\nRegion: {region}\n"

        # Check for rank information
        try:
            rank_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "tier")))
            rank = rank_element.text.strip()
            if not rank:
                raise Exception("No rank data found.")
            result_text += f"Rank: {rank}\n"
        except:
            result_text += "Rank: No rank available\n"
            driver.quit()
            return result_text  # Return immediately if no rank

        # Separator for champions
        result_text += "\nMost Played Champions\n"
        result_text += "----------------------\n"

        # Fetch the champion stats
        champion_boxes = driver.find_elements(By.CLASS_NAME, "champion-box")
        if not champion_boxes:
            result_text += "No champions listed for this player."
            return result_text

        # Only get up to the first 3 champions
        for i, box in enumerate(champion_boxes[:3]):  # First 3 champions
            try:
                info = box.find_element(By.CLASS_NAME, "info").text
                kda = box.find_element(By.CLASS_NAME, "kda").text
                played = box.find_element(By.CLASS_NAME, "played").text

                result_text += f"{info}  "
                result_text += f"{kda}  "
                result_text += f"Winrate: {played}\n"
                result_text += "----------------------\n"
            except Exception as e:
                result_text += f"Champion {i + 1}: Error retrieving stats\n"

        return result_text.strip()  # Clean and return the text output

    except Exception as e:
        return f"Error fetching stats: {e}"
    finally:
        driver.quit()

def get_player_stats_from_url(url):
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

        # Initialize the result string
        result_text = ""

        # Updated rank mapping
        rank_mapping = {
            "Iron": 1,
            "Bronze": 1.5,
            "Silver": 2,
            "Gold": 3,
            "Platinum": 4,
            "Emerald": 5,
            "Diamond": 6,
            "Master": 9,
            "Grandmaster": 10,
            "Challenger": 11
        }

        base_weights = {"4": 0.00, "3": 0.10, "2": 0.20, "1": 0.30}
        scaling_factors = {
            "Iron": 0.2, "Bronze": 0.4, "Silver": 0.6, "Gold": 0.8,
            "Platinum": 1.0, "Diamond": 2.5, "Emerald": 1.5,
            "Master": 0.0, "Grandmaster": 0.0, "Challenger": 0.0
        }

        # Add rank weights for previous seasons
        previous_rank_weights = {
            "Iron": 0.5,
            "Bronze": 0.1,
            "Silver": 0.15,
            "Gold": 0.2,
            "Platinum": 0.25,
            "Emerald": 0.3,
            "Diamond": 0.35,
            "Master": 0.4,
            "Grandmaster": 0.4,
            "Challenger": 0.4,
        }

        # Add rank weights for smurf detection
        previous_rank_smurf_weights = {
            "Iron": 2.5,
            "Bronze": 2.5,
            "Silver": 2,
            "Gold": 2,
            "Platinum": 1.75,
            "Emerald": 0.75,
            "Diamond": 0.65,
        }

        # Not Smurf Ranks
        non_smurf_ranks = ["Master", "Grandmaster", "Challenger"]

        def get_scaled_subdivision_weight(main_rank, sub_rank):
            if main_rank in ["Master", "Grandmaster", "Challenger"]:
                return 0.0  # No subdivisions
            scale = scaling_factors.get(main_rank, 1.0)
            return base_weights.get(sub_rank, 0.00) * scale

        # New win rate multiplier logic
        def calculate_winrate_points(rank_value, win_rate):
            if win_rate > 65:
                # Scale win rates above 65% dynamically from 0.8 to 1.0
                multiplier = 0.8 + ((win_rate - 65) / 35) * 0.2
            else:
                # Scale win rates below 65%
                multiplier = win_rate / 100 / 2
            return rank_value * multiplier

        # Check for rank information
        try:
            rank_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "tier")))
            rank = rank_element.text.strip()
            rank_parts = rank.split()  # e.g., "Gold 1" → ["Gold", "1"]
            main_rank = rank_parts[0]
            sub_rank = rank_parts[1] if len(rank_parts) > 1 else "4"  # Default to 4 if no subdivision
            rank_value = rank_mapping.get(main_rank, 0) + get_scaled_subdivision_weight(main_rank, sub_rank)
            result_text += f"**Rank**: `{rank}` | "
        except:
            rank_value = 0
            result_text += "**Rank**: `No rank available`\n"

        # Find winrates
        try:
            winlose = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'win-lose')))
            ratio = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'ratio')))
            ratio_text = ratio.text.replace("Win rate ", "").strip('%')  # Strip "Win rate" text
            win_rate = float(ratio_text)
            winrate_points = calculate_winrate_points(rank_value, win_rate)
            result_text += f"`{winlose.text} {ratio_text}%`\n"
        except Exception as e:
            win_rate = 0
            winrate_points = 0
            result_text += "Unavailable\n"

        # Smurf adjustment calculation
        try:
            level_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "level")))
            account_level = int(level_element.text.strip())
            result_text += f"**Account Level**: `{account_level}`\n"

            # Dynamic smurf adjustment multiplier
            base_multiplier = (1.25 - 0.2) / (1 + (account_level / 50))

            if account_level > 250:
                decrement = 0.05 * ((account_level - 250) // 25)  # Decrease by 5% per 25 levels above 250
                base_multiplier -= decrement
                if account_level > 500:  # Cap at level 500 value
                    base_multiplier = (1.25 - 0.2) / (1 + (500 / 50))

            if main_rank not in non_smurf_ranks:
                smurf_adjustment = rank_value * previous_rank_smurf_weights.get(main_rank) * max(base_multiplier, 0)  # Ensure multiplier doesn't go below 0
            else:
                smurf_adjustment = 0

            if account_level < 30:
                driver.quit()
                return "Sorry this account cannot participate in the tournament due to not being level 30 or above."
        except:
            result_text += "**Account Level**: `Unavailable`\n"
            smurf_adjustment = 0

        # Fetch and compare recent ranks with current rank
        result_text += "**Recent Ranks**: "
        games_played = int(winlose.text.split()[0].strip('W')) + int(winlose.text.split()[1].strip('L'))
        try:
            rank_items = driver.find_elements(By.CLASS_NAME, "rank-item")
            recent_ranks = [
                item.find_element(By.TAG_NAME, "span").text.strip()
                for item in rank_items[:2]
            ]

            # Fill missing ranks with one tier below the current rank
            while len(recent_ranks) < 2:
                recent_ranks.append(f"Default: {main_rank} 1 tier below")

            # Prepare recent ranks for result text and calculate points
            rank_comparison_points = 0
            formatted_ranks = []
            previous_ranks_points = 0
                
            for rank in recent_ranks:
                rank_parts = rank.split()
                previous_main_rank = rank_parts[0] if rank_parts else "Iron"  # Extract previous rank's main rank
                previous_weight = previous_rank_weights.get(previous_main_rank, 0.1)  # Get weight for previous rank
                previous_ranks_points += previous_weight
                previous_rank_value = rank_mapping.get(previous_main_rank)

                formatted_ranks.append(rank)  # Add to formatted ranks for result text

                # Compare current rank value with previous rank value
                if previous_rank_value > rank_value and win_rate > 0 and games_played < 25:
                    # Calculate scaling points based on winrate
                    scaling_points = 0.25*(previous_rank_value - rank_value)
                    scaling_points = max(scaling_points, 0.1)  # Clamp to a minimum of 0.1 points
                    rank_comparison_points += scaling_points

            # Add formatted recent ranks to the result text
            result_text += ", ".join(f"`{rank}`" for rank in formatted_ranks) + "\n"
            result_text += "**-----------------------------**\n"

        except:
            result_text += "`No previous ranks`\n"
            result_text += "**-----------------------------**\n"

        # Fetch champion stats and calculate contribution
        result_text += "**Most Played Champions**:\n"
        champion_winrates = []  # Store win rates for the top 3 champions

        try:
            champion_boxes = driver.find_elements(By.CLASS_NAME, "champion-box")

            if not champion_boxes:
                # No champions listed, add default win rates to ensure fairness
                champion_winrates = [0.5, 0.5, 0.5]  # Default win rates for all 3
            else:
                for i in range(3):  # Process up to the top 3 champions
                    try:
                        if i < len(champion_boxes):
                            # Extract data if champion exists
                            box = champion_boxes[i]
                            info = box.find_element(By.CLASS_NAME, "info").text.split('\n')[0]
                            kda = box.find_element(By.CLASS_NAME, "kda").text
                            played = box.find_element(By.CLASS_NAME, "played").text

                            # Extract win rate from "played" data (e.g., "100%\n3 played" → "100%")
                            winrate_text = played.split('\n')[0].strip('%')
                            winrate = float(winrate_text) / 100  # Convert percentage to decimal
                            champion_winrates.append(winrate)

                            # Append champion details to result_text
                            result_text += f"{info} `{kda}` \n Winrate: `{played}`\n"
                            result_text += "**-----------------------------**\n"
                        else:
                            # Default win rate for missing champions
                            champion_winrates.append(0.5)

                    except Exception as e:
                        # Default win rate if there's an error retrieving champion data
                        champion_winrates.append(0.5)

                # Pad with defaults if fewer than 3 champions
                while len(champion_winrates) < 3:
                    champion_winrates.append(0.5)

            # Calculate champion WR contribution using weights
            def calculate_champion_wr_contribution(winrates):
                weights = [0.9, 0.7, 0.5]
                return sum(wr * weight for wr, weight in zip(winrates, weights))

            champ_wr_contribution = calculate_champion_wr_contribution(champion_winrates)
        except Exception as e:
            result_text += f"`No champions listed for this player. Error: {str(e)}`"
            champ_wr_contribution = 0

        # Adjust total games played contribution
        try:
            if win_rate > 0:
                if games_played < 25:
                    flat_points = 0.2 + ((25 - games_played) / 20)  # Scales from 0.2–1.0
                    games_multiplier = 0.6 + ((win_rate - 35) / 30) if win_rate > 35 else 1
                    games_multiplier = min(max(games_multiplier, 1), 1.5)  # Clamp between 1x and 2x
                    games_points = flat_points * games_multiplier
                else:
                    games_points = 0  # No extra points for players with more than 25 games

        except:
            games_points = 0  # Fallback to no points in case of an error
            games_played = "did not work"

        
        # Calculate total point value
        point_value = rank_value + winrate_points + smurf_adjustment + champ_wr_contribution + rank_comparison_points + games_points + previous_ranks_points
        result_text += f"**Player Point Value**: `{point_value:.2f}`\n"
        print(f"rank value: {rank_value}")
        print(f"winrate_points: {winrate_points}")
        print(f"smurf_adjustment: {smurf_adjustment}")
        print(f"champ_wr_contribution: {champ_wr_contribution}")
        print(f"rank_comparison_points: {rank_comparison_points}")
        print(f"games_points: {games_points}")
        print(f"previous_ranks_points: {previous_ranks_points}")

        return result_text.strip()
    
    

    except Exception as e:
        return f"Error fetching stats: {e}"
    finally:
        driver.quit()



def check_solo_duo_rank(url):
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

        # Wait for the element and check the Solo/Duo header
        try:
            rank_section = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-1wk31w7.eaj0zte0"))
            )
            header = rank_section.find_element(By.CLASS_NAME, "header").text.strip()

            if header == "Ranked Solo/Duo":
                return True  # Solo/Duo rank is available
            else:
                return False  # No Solo/Duo rank available

        except Exception as e:
            return False  # Element not found or incorrect structure

    finally:
        driver.quit()