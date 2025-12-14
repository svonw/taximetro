from trip import Trip
import time
import pytest

@pytest.fixture(autouse=True)
def reset_trip():
    """Resetear Trip antes de cada test """
    Trip.trip_activate = False
    Trip.start_time = 0
    Trip.stopped_time = 0
    Trip.moving_time = 0
    Trip.state = None
    Trip.state_start_time = 0


# TEST 1
def test_start_activates_trip():

    """Verifica que start() activa el viaje correctamente"""
    Trip.start("start")
    assert Trip.trip_activate == True
    assert Trip.state == "stopped"

# TEST 2
def test_stop_move_change_state():

    """Verifica que stop_move() cambia entre stopped y moving"""
    Trip.start("start")
    Trip.stop_move("move")
    assert Trip.state == "moving"
    Trip.stop_move("stop")
    assert Trip.state == "stopped"

# TEST 3
def test_stop_move_adds_time():

    """Verifica que stop_move() acumula tiempo correctamente"""
    Trip.start("start")
    time.sleep(1)
    Trip.stop_move("move")
    assert Trip.stopped_time >= 1

# TEST 4
def test_finish_deactivate_trip():

    """Verifica que finish() desactiva el viaje y acumula tiempo final"""
    Trip.start("start")
    time.sleep(1)
    Trip.finish("finish")
    assert Trip.trip_activate == False
    assert Trip.stopped_time >= 1

# TEST 5
def test_start_twice_not_allowed():

    """Verifica que no puedes hacer start() si ya hay un viaje activo"""
    Trip.start("start")
    viajes_antes = Trip.trip_activate
    Trip.start("start")
    assert Trip.trip_activate == viajes_antes

#TEST 6
def test_completed_trip():

    """Verifica calculos de tiempo de viaje completo"""
    Trip.start("start")
    time.sleep(3)
    Trip.stop_move("move")
    time.sleep(2)
    Trip.finish("finish")
    assert Trip.stopped_time == 3
    assert Trip.moving_time == 2