from linguist import (
    user_create, user_get_by_id, user_update_name, user_change_password, user_delete_by_id,
    deck_create, deck_get_by_id, deck_update, deck_delete_by_id,
    card_create, card_get_by_id, card_filter, card_update, card_delete_by_id
)

def test_user_crud():
    print("Testing User CRUD...")
    # Create
    u1 = user_create("Alice", "alice@test.com", "pass123")
    assert u1.id == 1
    assert u1.name == "Alice"
    
    # Read
    u1_fetch = user_get_by_id(1)
    assert u1_fetch is u1
    assert user_get_by_id(999) is None

    # Update Name
    u1_updated = user_update_name(1, "Alice M.")
    assert u1_updated.name == "Alice M."
    
    # Change Password
    assert user_change_password(1, "wrongpass", "newpass") is False
    assert user_change_password(1, "pass123", "newpass") is True
    assert u1_updated.password == "newpass"
    
    # Delete
    assert user_delete_by_id(1) is True
    assert user_get_by_id(1) is None
    assert user_delete_by_id(1) is False

def test_deck_crud():
    print("Testing Deck CRUD...")
    u1 = user_create("Bob", "bob@test.com", "pass123")
    
    # Create
    d1 = deck_create("English Basics", u1.id)
    assert d1.id == 1
    assert d1.name == "English Basics"
    assert d1.user_id == u1.id
    
    # Read
    deck_fetch = deck_get_by_id(d1.id)
    assert deck_fetch is d1
    assert deck_get_by_id(999) is None

    # Update
    deck_updated = deck_update(d1.id, "English Intermediate")
    assert deck_updated.name == "English Intermediate"
    
    # Delete
    assert deck_delete_by_id(d1.id) is True
    assert deck_get_by_id(d1.id) is None

def test_card_crud():
    print("Testing Card CRUD...")
    u1 = user_create("Charlie", "charlie@test.com", "pass123")
    
    # Create
    c1 = card_create(u1.id, "Apple", "Яблуко", "A red fruit")
    c2 = card_create(u1.id, "Banana", "Банан", "A yellow fruit")
    assert c1.id == 1
    assert c2.word == "Banana"
    
    # Read
    c1_fetch = card_get_by_id(c1.id)
    assert c1_fetch is c1
    
    # Filter
    results = card_filter("fruit")
    assert len(results) == 2
    
    results_apple = card_filter("apple")
    assert len(results_apple) == 1
    
    results_ukr = card_filter("Банан")
    assert len(results_ukr) == 1

    # Update
    c1_updated = card_update(c1.id, word="Red Apple", tip="Sweet red fruit")
    assert c1_updated.word == "Red Apple"
    assert c1_updated.translation == "Яблуко" # Should not change
    assert c1_updated.tip == "Sweet red fruit"
    
    # Delete
    assert card_delete_by_id(c1.id) is True
    assert card_get_by_id(c1.id) is None
    assert len(card_filter("fruit")) == 1

if __name__ == "__main__":
    test_user_crud()
    test_deck_crud()
    test_card_crud()
    print("All tests passed successfully!")
