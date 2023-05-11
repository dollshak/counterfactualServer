import unittest


class TestAlgorithmController(unittest.TestCase):

    def test_restore_algorithm(self):
        # TODO
        # at the start of the test, the db should contain an algorithm the system does not have
        # by calling get_all_algorithms -> should create the unexisting algorithm in system
        assert False

    def test_server_restart(self):
        # TODO remove all algorithm from server
        # validate get_all_algorithms restore all algorithms to system
        assert False

    def test_run_from_system(self):
        # TODO
        # this test validate that if a selected algorithm is already in the system, does not call db
        assert False
