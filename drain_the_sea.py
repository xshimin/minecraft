#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcrcon import MCRcon
import time

minecraft_address = "127.0.0.1"
minecraft_port = 28016
minecraft_pasword = "testing"

class MCRconWrapper:
    def __init__(self):
        self.mcr = MCRcon(minecraft_address, minecraft_pasword, minecraft_port)
        self.mcr.connect()
    
    def disconnect(self):
        self.mcr.disconnect()

    def run_command(self, cmd) -> str:
        resp = self.mcr.command(cmd)
        print("Executed command: '{cmd}'".format(cmd=cmd))
        print("> " + resp)
        return resp

# Z座標を軸としてX-Y座標を任意のブロックで置き換える
def deploy_wall_x_to_y(start_x, start_y, start_z, inc_x, inc_y, block_name, deploy_mode="replace"):
    end_x, end_y, end_z       = start_x + inc_x, start_y + inc_y, start_z + 0
    mcrwrap = MCRconWrapper()
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            run_command = "fill {x} {y} {z} {x} {y} {z} {block_name} {deploy_mode}".format(
                x=x, y=y, z=end_z, block_name=block_name, deploy_mode=deploy_mode
            )
            mcrwrap.run_command(run_command)
    mcrwrap.disconnect()
    return run_command

# X座標を軸としてY-Z座標を任意のブロックで置き換える
def deploy_wall_y_to_z(start_x, start_y, start_z, inc_y, inc_z, block_name, deploy_mode="replace"):
    end_x, end_y, end_z       = start_x + 0, start_y + inc_y, start_z + inc_z
    mcrwrap = MCRconWrapper()
    for z in range(start_z, end_z):
        for y in range(start_y, end_y):
            run_command = "fill {x} {y} {z} {x} {y} {z} {block_name} {deploy_mode}".format(
                x=end_x, y=y, z=z, block_name=block_name, deploy_mode=deploy_mode
            )
            mcrwrap.run_command(run_command)
    mcrwrap.disconnect()
    return run_command

# XYZ座標全てについて対象とするブロックを任意のブロックで置き換える
def deploy_blocks_x_y_z(start_x, start_y, start_z, inc_x, inc_y, inc_z, target_block, deploy_block, deploy_mode="replace"):
    end_x, end_y, end_z       = start_x + inc_x, start_y + inc_y, start_z + inc_z
    mcrwrap = MCRconWrapper()
    for x in range(start_x, end_x):
        for z in range(start_z, end_z):
            for y in range(start_y, end_y):
                run_command = "execute if block {x} {y} {z} {target_block} run fill {x} {y} {z} {x} {y} {z} {deploy_block} {deploy_mode}".format(
                    target_block=target_block, x=x, y=y, z=z, deploy_block=deploy_block, deploy_mode=deploy_mode
                )
                mcrwrap.run_command(run_command)
    mcrwrap.disconnect()
    return run_command

# rangeで生成されるリストのうち指定された整数で割り切れる数字のみをリストの要素として返す
def _filter_list(start, end, denominator) -> list:
    return list(filter(lambda x : x % denominator == 0, range(start, end)))

# Y座標を軸として以下の条件を全て満たす場合のみ空気ブロック上に松明を配置する
# (1) 対象ブロックが空気ブロックであること
# (2) 対象ブロックのY座標-1ブロックが松明以外であること
# (3) 対象ブロックのY座標-1ブロックが空気ブロック以外であること
def deploy_torch(start_x, start_y, start_z, inc_x, inc_y, inc_z, deploy_mode="replace"):
    end_x, end_y, end_z       = start_x + inc_x, start_y + inc_y, start_z + inc_z
    target_block = "minecraft:air"
    deploy_block = "minecraft:torch"
    command_base = (
        "execute "
        # 条件(1)
        + "if block {x} {y} {z} {target_block} "
        # AND 条件(2)
        + "unless block {x} {negative_y} {z} {deploy_block} "
        # AND 条件(3)
        + "unless block {x} {negative_y} {z} {target_block} "
        # ブロック配置
        + "run fill {x} {y} {z} {x} {y} {z} {deploy_block} {deploy_mode}")
    mcrwrap = MCRconWrapper()
    for x in _filter_list(start_x, end_x, 4):
        for z in _filter_list(start_z, end_z, 4):
            for y in range(start_y, end_y):
                negative_y = y - 1
                run_command = command_base.format(
                    x=x, y=y, negative_y=negative_y, z=z,
                    target_block = target_block,
                    deploy_block = deploy_block,
                    deploy_mode = deploy_mode
                )
                mcrwrap.run_command(run_command)
    mcrwrap.disconnect()
    return run_command

def main():
    base_x, base_y, base_z = 235, 15, -2015
    inc_x, inc_y, inc_z    = 80,  52,    80

    try:
        # 海の一部をガラスブロックの壁で囲む
        deploy_wall_x_to_y(base_x,         base_y, base_z +        0, inc_x, inc_y, "minecraft:glass")
        deploy_wall_x_to_y(base_x,         base_y, base_z + inc_z -1, inc_x, inc_y, "minecraft:glass")
        deploy_wall_y_to_z(base_x +     0, base_y, base_z,            inc_y, inc_z, "minecraft:glass")
        deploy_wall_y_to_z(base_x + inc_x, base_y, base_z,            inc_y, inc_z, "minecraft:glass")
        # 壁の上にシーランタンを配置する
        deploy_wall_x_to_y(base_x,         base_y + inc_y, base_z +        0, inc_x,     1, "minecraft:sea_lantern")
        deploy_wall_x_to_y(base_x,         base_y + inc_y, base_z + inc_z -1, inc_x,     1, "minecraft:sea_lantern")
        deploy_wall_y_to_z(base_x +     0, base_y + inc_y, base_z,                1, inc_z, "minecraft:sea_lantern")
        deploy_wall_y_to_z(base_x + inc_x, base_y + inc_y, base_z,                1, inc_z, "minecraft:sea_lantern")
        # 水ブロックをスポンジブロックで置き換える -> 濡れたスポンジブロックが生成される
        deploy_blocks_x_y_z(base_x, base_y, base_z, inc_x, inc_y, inc_z, "minecraft:water", "minecraft:sponge")
        # 濡れたスポンジブロックを空気ブロックで置き換える
        deploy_blocks_x_y_z(base_x, base_y, base_z, inc_x, inc_y, inc_z, "minecraft:wet_sponge", "minecraft:air")
        # 松明を置いて湧き潰しを行う
        deploy_torch(base_x, base_y, base_z, inc_x, inc_y, inc_z)
    except:
        raise

if __name__ == "__main__":
    main()
