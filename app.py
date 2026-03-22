from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Your tarot cards
card_meanings = {

    "The Fool": "New beginnings, adventure, innocence",
    "The Magician": "Skill, resourcefulness, power",
    "The High Priestess": "Intuition, mystery, secrets",
    "The Empress": "Abundance, nurturing, fertility",
    "The Emperor": "Authority, structure, control",
    "The Hierophant": "Tradition, guidance, spirituality",
    "The Lovers": "Relationships, choices, union",
    "The Chariot": "Determination, willpower, victory",
    "Strength": "Courage, patience, control",
    "The Hermit": "Reflection, solitude, guidance",
    "Wheel of Fortune": "Cycles, destiny, change",
    "Justice": "Fairness, truth, law",
    "The Hanged Man": "Pause, surrender, letting go",
    "Death": "Transformation, endings, new beginnings",
    "Temperance": "Balance, moderation, harmony",
    "The Devil": "Bondage, temptation, materialism",
    "The Tower": "Sudden change, upheaval, revelation",
    "The Star": "Hope, inspiration, serenity",
    "The Moon": "Illusion, fear, intuition",
    "The Sun": "Success, joy, vitality",
    "Judgement": "Reflection, reckoning, awakening",
    "The World": "Completion, achievement, travel",

    # Minor Arcana - Wands

    "Ace of Wands": "inspiration, power, creation, beginnings",
    "Two of Wands": "decisions, negotiation, obstacles",
    "Three of Wands": "preperation, group energy, fate, luck",
    "Four of Wands": "celebration, harmony, marriage, holiday, relaxtion",
    "Five of Wands": "irritation, competition, strife",
    "Six of Wands": "recognition, good news, victory, progress",
    "Seven of Wands": "challenge, good results, valor",
    "Eight of Wands": "passion, speed, flight, activation",
    "Nine of Wands": "persistance, courage, advantage, stability",
    "Ten of Wands": "accomplishment, stress, excess activity, oppression",
    "Page of Wands": "message incoming, ambition, enthusiasm, pure intention, helpful information",
    "Knight of Wands": "excitement, energy, flexible intution, adventure",
    "Queen of Wands": "courage, determination, passion, joy",
    "King of Wands": "big picture, leadership, overcoming challenges",

    # Minor Arcana - Swords

    "Ace of Swords": "new ideas, clear communication, mental clarity",
    "Two of Swords": "indecision, stalemate, difficult choices",
    "Three of Swords": "heartbreak, sorrow, grief",
    "Four of Swords": "rest, recovery, contemplation",
    "Five of Swords": "conflict, tension, betrayal",
    "Six of Swords": "transition, moving forward, healing",
    "Seven of Swords": "deception, strategy, cunning",
    "Eight of Swords": "movement, speed, action",
    "Nine of Swords": "resiliencem persistence, stamina",
    "Ten of Swords": "burden, responsibility, hard work",
    "Page of Swords": "exploration, enthusiasm, discovery",
    "Knight of Swords": "adventure, impulsiveness, energy",
    "Queen of Swords": "confidence, determination, vibrance",
    "King of Swords": "leadership, vision, honor",

    # Minor Arcana - Cups

    "Ace of Cups": "new emotions, love, compassion",
    "Two of Cups": "partnership, attraction, connection",
    "Three of Cups": "celebration, friendship, community",
    "Four of Cups": "apathy, contemplation, reevaluation",
    "Five of Cups": "loss, regret, disappointment",
    "Six of Cups": "nostalgia, childhood, memories",
    "Seven of Cups": "choices, imagination, illusions",
    "Eight of Cups": "leaving behind, moving on, introspection",
    "Nine of Cups": "wish fulfillment, contentment, satisfaction",
    "Ten of Cups": "emotional fulfillment, happiness, family",
    "Page of Cups": "curiousity, messages, new feelings",
    "Knight of Cups": "romance, charm, following the heart",
    "Queen of Cups": "compassion, caring, emotional security",
    "King of Cups": "balance, control, generosity of emotion",

    #Minor Arcana - Pentacles

    "Ace of Pentacles": "new financial opportunities, prosperity",
    "Two of Pentacles": "balance, adaptability, juggling resposibilities",
    "Three of Pentacles": "teamwork, collaboration, skill",
    "Four of Pentacles": "stability, conversation, control",
    "Five of Pentacles": "financial loss, struggle, insecurity",
    "Six of Pentacles": "generosity, charity, sharing wealth",
    "Seven of Pentacles": "patience, assessment, long-term planning",
    "Eight of Pentacles": "skill development, apprenticeship, development",
    "Nine of Pentacles": "self-sufficiency, luxury, accomplishment",
    "Ten of Pentacles": "wealth, family, long-term success",
    "Page of Pentacles": "study, manifestation,curiousity",
    "Knight of Pentacles": "responsibility, efficiency, routine",
    "Queen of Pentacles": "nurturing, practicality, prosperity",
    "King of Pentacles": "authority, intellect, truth",
}

# Single Card
@app.route('/single', methods=['GET', 'POST'])
def single_card():
    if request.method == 'POST':
        question = request.form['question']
        card = random.choice(list(card_meanings.keys()))
        reversed_card = random.choice([True, False])
        if reversed_card:
            card_name = card + " (Reversed)"
            meaning = card_meanings[card] + " (Reversed may indicate blockage or opposite energy.)"
        else:
            card_name = card
            meaning = card_meanings[card]
        return render_template('result.html', card=card_name, meaning=meaning, question=question)
    return render_template('single.html')

# Daily Pull
@app.route('/daily')
def daily_pull():
    card = random.choice(list(card_meanings.keys()))
    reversed_card = random.choice([True, False])
    if reversed_card:
        card_name = card + " (Reversed)"
        meaning = card_meanings[card] + " (Reversed may indicate blockage or opposite energy.)"
    else:
        card_name = card
        meaning = card_meanings[card]
    return render_template('daily.html', card=card_name, meaning=meaning)

# 3-Card Spread
@app.route('/three')
def three_card():
    spread = random.sample(list(card_meanings.keys()), 3)
    positions = ["Past", "Present", "Future"]
    results = []
    for pos, card in zip(positions, spread):
        reversed_card = random.choice([True, False])
        if reversed_card:
            card_name = card + " (Reversed)"
            meaning = card_meanings[card] + " (Reversed may indicate blockage or opposite energy.)"
        else:
            card_name = card
            meaning = card_meanings[card]
        results.append({'position': pos, 'card': card_name, 'meaning': meaning})
    return render_template('three.html', results=results)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)