from .models import InteractEvent

def test_interact_event():
    event = InteractEvent(user_id=1, movie_id=2, event="click")
    assert event.user_id == 1
    assert event.movie_id == 2
    assert event.event == "click"
