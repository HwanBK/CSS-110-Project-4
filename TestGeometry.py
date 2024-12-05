# CSC110
# Project 4 - Test code file
# Hwansu Kim (billy)
# 10/19/2021


import unittest
import geometry


class CalculationTest(unittest.TestCase):

    def test_circleCircum(self):
        self.assertAlmostEqual(37.69911184,  geometry.circleCircum(6),     4)
        self.assertAlmostEqual(0,            geometry.circleCircum(0),     4)
        self.assertAlmostEqual(-62.83185307, geometry.circleCircum(-10),   4)
        self.assertAlmostEqual(189.9406918,  geometry.circleCircum(30.23), 4)
        self.assertAlmostEqual(-9.110618695, geometry.circleCircum(-1.45), 4)

    def test_circleArea(self):
        self.assertAlmostEqual(50.26548246, geometry.circleArea(4),        4)
        self.assertAlmostEqual(0,           geometry.circleArea(0),        4)
        self.assertAlmostEqual(1256.637061, geometry.circleArea(-20),      4)
        self.assertAlmostEqual(290779.2213, geometry.circleArea(304.2333), 4)
        self.assertAlmostEqual(.6082123377, geometry.circleArea(-0.44),    4)

    def test_sphereVolume(self):
        self.assertAlmostEqual(523.5987756,  geometry.sphereVolume(5),       4)
        self.assertAlmostEqual(0,            geometry.sphereVolume(0),       4)
        self.assertAlmostEqual(-7238.229474, geometry.sphereVolume(-12),     4)
        self.assertAlmostEqual(373.5731144,  geometry.sphereVolume(4.46782), 4)
        self.assertAlmostEqual(-3412.944594, geometry.sphereVolume(-09.34),  4)

    def test_sphereSurfArea(self):
        self.assertAlmostEqual(2123.716634,  geometry.sphereSurfArea(13),        4)
        self.assertAlmostEqual(0,            geometry.sphereSurfArea(0),         4)
        self.assertAlmostEqual(12867.96351,  geometry.sphereSurfArea(-32),       4)
        self.assertAlmostEqual(29366.96679,  geometry.sphereSurfArea(48.342),    4)
        self.assertAlmostEqual(0.0067707221, geometry.sphereSurfArea(-0.023212), 4)

    def test_squarePerim(self):
        self.assertAlmostEqual(212,         geometry.squarePerim(53),         4)
        self.assertAlmostEqual(0,           geometry.squarePerim(0),          4)
        self.assertAlmostEqual(-1368,       geometry.squarePerim(-342),       4)
        self.assertAlmostEqual(51.797204,   geometry.squarePerim(12.949301),  4)
        self.assertAlmostEqual(-152.051016, geometry.squarePerim(-38.012754), 4)

    def test_squareArea(self):
        self.assertAlmostEqual(900,         geometry.squareArea(30),        4)
        self.assertAlmostEqual(0,           geometry.squareArea(0),         4)
        self.assertAlmostEqual(1936,        geometry.squareArea(-44),       4)
        self.assertAlmostEqual(455.4966292, geometry.squareArea(21.342367), 4)
        self.assertAlmostEqual(2.227347305, geometry.squareArea(-1.49243),  4)

    def test_cubeVolume(self):
        self.assertAlmostEqual(125000,       geometry.cubeVolume(50),         4)
        self.assertAlmostEqual(0,            geometry.cubeVolume(0),          4)
        self.assertAlmostEqual(-804357,      geometry.cubeVolume(-93),        4)
        self.assertAlmostEqual(917326.8347,  geometry.cubeVolume(97.1645923), 4)
        self.assertAlmostEqual(-833854.8651, geometry.cubeVolume(-94.12323),  4)

    def test_cubeSurfArea(self):
        self.assertAlmostEqual(92256,       geometry.cubeSurfArea(124),        4)
        self.assertAlmostEqual(0,           geometry.cubeSurfArea(0),          4)
        self.assertAlmostEqual(11094,       geometry.cubeSurfArea(-43),        4)
        self.assertAlmostEqual(648.0463365, geometry.cubeSurfArea(10.3926764), 4)
        self.assertAlmostEqual(31510.97058, geometry.cubeSurfArea(-72.4695),   4)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()