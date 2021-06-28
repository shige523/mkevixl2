import unittest


class MkevixiTest(unittest.TestCase):
    # @unittest.skip("初期動確用テスト")
    def test_mkevixl_validation_ok(self):
        from mkevixl2.core import mkevixl2

        sheet = ("test1", "test2")
        self.assertTrue(mkevixl2("test", sheet))

    def test_mkevixl_validation_ng_empty_tuple(self):
        from mkevixl2.core import mkevixl2

        sheet = ()
        self.assertFalse(mkevixl2("test", sheet))
