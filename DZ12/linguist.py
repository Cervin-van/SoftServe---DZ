__users = {}
__decks = {}
__cards = {}

__user_id_seq = 1
__deck_id_seq = 1
__card_id_seq = 1

class User:
    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

class Deck:
    def __init__(self, deck_id: int, name: str, user_id: int):
        self.id = deck_id
        self.name = name
        self.user_id = user_id

class Card:
    def __init__(self, card_id: int, user_id: int, word: str, translation: str, tip: str):
        self.id = card_id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

# === USER FUNCTIONS ===

def user_create(name: str, email: str, password: str) -> User:
    """Creates a new user and returns the User object."""
    global __user_id_seq
    new_user = User(user_id=__user_id_seq, name=name, email=email, password=password)
    __users[__user_id_seq] = new_user
    __user_id_seq += 1
    return new_user

def user_get_by_id(user_id: int) -> User:
    """Retrieves a user by their ID and returns the User object."""
    return __users.get(user_id)

def user_update_name(user_id: int, name: str) -> User:
    """Updates the name of a user and returns the User object."""
    user = user_get_by_id(user_id)
    if user:
        user.name = name
    return user

def user_change_password(user_id: int, old_password: str, new_password: str) -> bool:
    """Changes the password of a user and returns a Boolean value indicating success or failure."""
    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        return True
    return False

def user_delete_by_id(user_id: int) -> bool:
    """Deletes a user by their ID and returns a Boolean value indicating success or failure."""
    if user_id in __users:
        del __users[user_id]
        return True
    return False

# === DECK FUNCTIONS ===

def deck_create(name: str, user_id: int) -> Deck:
    """Creates a new deck belonging to a user and returns the Deck object."""
    global __deck_id_seq
    # Optionally checking if user exists:
    if user_id not in __users:
        raise ValueError("User does not exist")
        
    new_deck = Deck(deck_id=__deck_id_seq, name=name, user_id=user_id)
    __decks[__deck_id_seq] = new_deck
    __deck_id_seq += 1
    return new_deck

def deck_get_by_id(deck_id: int) -> Deck:
    """Retrieves a deck by its ID and returns the Deck object."""
    return __decks.get(deck_id)

def deck_update(deck_id: int, name: str) -> Deck:
    """Updates the name of a deck and returns the Deck object."""
    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
    return deck

def deck_delete_by_id(deck_id: int) -> bool:
    """Deletes a deck by its ID and returns a Boolean value indicating success or failure."""
    if deck_id in __decks:
        del __decks[deck_id]
        return True
    return False

# === CARD FUNCTIONS ===

def card_create(user_id: int, word: str, translation: str, tip: str) -> Card:
    """Creates a new flashcard and returns the Card object."""
    global __card_id_seq
    if user_id not in __users:
        raise ValueError("User does not exist")

    new_card = Card(card_id=__card_id_seq, user_id=user_id, word=word, translation=translation, tip=tip)
    __cards[__card_id_seq] = new_card
    __card_id_seq += 1
    return new_card

def card_get_by_id(card_id: int) -> Card:
    """Retrieves a flashcard by its ID and returns the Card object."""
    return __cards.get(card_id)

def card_filter(sub_word: str) -> tuple[Card]:
    """Retrieves all flashcards containing a substring in either the word, translation, or tip fields."""
    matched_cards = []
    sub_word_lower = sub_word.lower()
    for card in __cards.values():
        if (sub_word_lower in card.word.lower() or 
            sub_word_lower in card.translation.lower() or 
            sub_word_lower in card.tip.lower()):
            matched_cards.append(card)
    return tuple(matched_cards)

def card_update(card_id: int, word: str = None, translation: str = None, tip: str = None) -> Card:
    """Updates the fields of a flashcard and returns the Card object."""
    card = card_get_by_id(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
    return card

def card_delete_by_id(card_id: int) -> bool:
    """Deletes a flashcard by its ID and returns a Boolean value indicating success or failure."""
    if card_id in __cards:
        del __cards[card_id]
        return True
    return False
