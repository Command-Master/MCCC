#tellraw @a {"text":"ERROR: ADD MAGS2 ISN'T IMPLEMENTED!!!", "color": "red"}
execute store result score $sign namespace if score $aval namespace matches ..-1
scoreboard players operation $siga namespace *= $64 namespace
scoreboard players operation $sigb namespace *= $64 namespace
execute if score $expdiff namespace matches ..-1 run function namespace:add_mags21
execute unless score $expdiff namespace matches ..-1 run function namespace:add_mags22
scoreboard players set $sig namespace 536870912
scoreboard players operation $sig namespace += $siga namespace
scoreboard players operation $sig namespace += $sigb namespace
# jank food?
execute if score $sig namespace matches 0..1073741823 run scoreboard players remove $exp namespace 1
# execute store result score $thing namespace if score $sig namespace matches ..1073741823
execute if score $sig namespace matches 0..1073741823 run scoreboard players operation $sig namespace *= $2 namespace
# tellraw @a {"score": {"name": "$exp", "objective": "namespace"}}