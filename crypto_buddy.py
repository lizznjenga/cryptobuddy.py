crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },

    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

print("👋 Hey there! I’m CryptoBuddy—your AI crypto sidekick. Ask me about crypto trends or sustainability!")

while True:
    user_query = input("You: ").lower()

     if "exit" in user_query or "quit" in user_query:
        print("CryptoBuddy: 👋 Bye! Remember—crypto is risky. Always do your own research!")
        break

     elif "profitable" in user_query or "growth" in user_query or "trending" in user_query:
        best = None
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                best = coin
                break

            if best:
            print(f"CryptoBuddy: 🚀 {best} is rising in price and has strong market cap!")
        else:
            print("CryptoBuddy: Hmm 🤔 I couldn’t find a top profitable crypto at the moment.")

            elif "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 {best} is the most sustainable option with score {crypto_db[best]['sustainability_score']*10}/10.")

         elif any(coin.lower() in user_query for coin in crypto_db):
        for coin in crypto_db:
            if coin.lower() in user_query:
                data = crypto_db[coin]
                print(f"CryptoBuddy: {coin} info → Trend: {data['price_trend']}, Market Cap: {data['market_cap']}, Energy Use: {data['energy_use']}, Sustainability: {data['sustainability_score']*10}/10.")
    
    else:
        print("CryptoBuddy: 🤖 I didn’t catch that. Try asking about profitability, sustainability, or a specific crypto.")