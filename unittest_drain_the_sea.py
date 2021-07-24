#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock
import drain_the_sea

###############################################################################
# deploy_wall_x_to_y
class Test_deploy_wall_x_to_y(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_01(self):
        start_x = 0
        start_y = 1
        start_z = 2
        inc_x = 3
        inc_y = 3
        block_name = "minecraft:air"
        # deploy_mode = 
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_result = "fill {x} {y} {z} {x} {y} {z} {block_name} {deploy_mode}".format(
                                x=2, y=3, z=2, block_name="minecraft:air", deploy_mode="replace"
                            )
        actually_result = drain_the_sea.deploy_wall_x_to_y(start_x, start_y, start_z, inc_x, inc_y, block_name)
        
        self.assertEqual(expected_result, actually_result)

    def test_case_02(self):
        start_x = 0
        start_y = 1
        start_z = 2
        inc_x = 3
        inc_y = 3
        block_name = "minecraft:air"
        deploy_mode = "destroy"
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_result = "fill {x} {y} {z} {x} {y} {z} {block_name} {deploy_mode}".format(
                                x=2, y=3, z=2, block_name="minecraft:air", deploy_mode="destroy"
                            )
        actually_result = drain_the_sea.deploy_wall_x_to_y(start_x, start_y, start_z, inc_x, inc_y, block_name, deploy_mode)
        
        self.assertEqual(expected_result, actually_result)

###############################################################################
# deploy_wall_y_to_z
class Test_deploy_wall_y_to_z(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_01(self):
        start_x = 0
        start_y = 1
        start_z = 2
        inc_y = 3
        inc_z = 3
        block_name = "minecraft:air"
        # deploy_mode = 
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_result = "fill {x} {y} {z} {x} {y} {z} {block_name} {deploy_mode}".format(
                                x=0, y=3, z=4, block_name="minecraft:air", deploy_mode="replace"
                            )
        actually_result = drain_the_sea.deploy_wall_y_to_z(start_x, start_y, start_z, inc_y, inc_z, block_name)
        
        self.assertEqual(expected_result, actually_result)

    def test_case_02(self):
        start_x = 0
        start_y = 1
        start_z = 2
        inc_y = 3
        inc_z = 3
        block_name = "minecraft:air"
        deploy_mode = "destroy"
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_result = "fill {x} {y} {z} {x} {y} {z} {block_name} {deploy_mode}".format(
                                x=0, y=3, z=4, block_name="minecraft:air", deploy_mode="destroy"
                            )
        actually_result = drain_the_sea.deploy_wall_y_to_z(start_x, start_y, start_z, inc_y, inc_z, block_name, deploy_mode)
        
        self.assertEqual(expected_result, actually_result)

###############################################################################
# deploy_blocks_x_y_z
class Test_deploy_blocks_x_y_z(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_01(self):
        start_x = 0
        start_y = 1
        start_z = 2
        inc_x = 3
        inc_y = 3
        inc_z = 3
        target_block = "minecraft:air"
        deploy_block = "minecraft:torch"
        # deploy_mode = 
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_result = "execute if block {x} {y} {z} {target_block} run fill {x} {y} {z} {x} {y} {z} {deploy_block} {deploy_mode}".format(
                                x=2, y=3, z=4, target_block="minecraft:air", deploy_block="minecraft:torch", deploy_mode="replace"
                            )
        actually_result = drain_the_sea.deploy_blocks_x_y_z(start_x, start_y, start_z, inc_x, inc_y, inc_z, target_block, deploy_block)
        
        self.assertEqual(expected_result, actually_result)

    def test_case_02(self):
        start_x = 0
        start_y = 1
        start_z = 2
        inc_x = 3
        inc_y = 3
        inc_z = 3
        target_block = "minecraft:air"
        deploy_block = "minecraft:torch"
        deploy_mode = "destroy"
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_result = "execute if block {x} {y} {z} {target_block} run fill {x} {y} {z} {x} {y} {z} {deploy_block} {deploy_mode}".format(
                                x=2, y=3, z=4, target_block="minecraft:air", deploy_block="minecraft:torch", deploy_mode="destroy"
                            )
        actually_result = drain_the_sea.deploy_blocks_x_y_z(start_x, start_y, start_z, inc_x, inc_y, inc_z, target_block, deploy_block, deploy_mode)
        
        self.assertEqual(expected_result, actually_result)

###############################################################################
# _filter_list
class Test_filter_list(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_01(self):
        start = 0
        end = 10
        denominator = 4
        expected_result = [0, 4, 8]
        actually_result = drain_the_sea._filter_list(start, end, denominator)

        self.assertEqual(expected_result, actually_result)

###############################################################################
# deploy_torch
class Test_deploy_torch(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case_01(self):
        start_x = 0
        start_y = 1
        start_z = 3
        inc_x = 11
        inc_y = 11
        inc_z = 11
        # deploy_mode = 
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_run_command = (
            "execute "
            + "if block {x} {y} {z} {target_block} "
            + "unless block {x} {negative_y} {z} {deploy_block} "
            + "unless block {x} {negative_y} {z} {target_block} "
            + "run fill {x} {y} {z} {x} {y} {z} {deploy_block} {deploy_mode}")
        expected_result = expected_run_command.format(
                                x=8, y=11, negative_y=10, z=12,
                                target_block="minecraft:air",
                                deploy_block="minecraft:torch", 
                                water_block  = "minecraft:water",
                                deploy_mode="replace"
                            )
        actually_result = drain_the_sea.deploy_torch(start_x, start_y, start_z, inc_x, inc_y, inc_z)
        
        self.assertEqual(expected_result, actually_result)

    def test_case_02(self):
        start_x = 0
        start_y = 1
        start_z = 3
        inc_x = 11
        inc_y = 11
        inc_z = 11
        deploy_mode = "destroy"
        drain_the_sea.MCRconWrapper = mock.Mock()
        drain_the_sea.MCRconWrapper.run_command = mock.Mock(return_value="run result")
        expected_run_command = (
            "execute "
            + "if block {x} {y} {z} {target_block} "
            + "unless block {x} {negative_y} {z} {deploy_block} "
            + "unless block {x} {negative_y} {z} {target_block} "
            + "unless block {x} {negative_y} {z} {water_block} "
            + "run fill {x} {y} {z} {x} {y} {z} {deploy_block} {deploy_mode}")
        expected_result = expected_run_command.format(
                                x=8, y=11, negative_y=10, z=12,
                                target_block="minecraft:air",
                                eploy_block="minecraft:torch",
                                water_block="minecraft:water",
                                deploy_mode="destroy"
                            )
        actually_result = drain_the_sea.deploy_torch(start_x, start_y, start_z, inc_x, inc_y, inc_z, deploy_mode)
        
        self.assertEqual(expected_result, actually_result)

if __name__ == "__main__":
    unittest.main()
