# magic sign thing:
execute store result score $sa namespace if score $aval namespace matches ..-1
execute store result score $sb namespace if score $bval namespace matches ..-1
execute if score $sa namespace matches 0 if score $sb namespace matches 1 run function namespace:float_add1
scoreboard players operation $sa namespace += $sb namespace
scoreboard players operation $sa namespace %= $2 namespace
#magic sign end - sa is sub/add


tellraw @a[tag=fdebug] ["adding: ", {"score": {"name": "$aval", "objective": "namespace"}}]
tellraw @a[tag=fdebug] ["adding: ", {"score": {"name": "$bval", "objective": "namespace"}}]
execute if score $sa namespace matches 1 run function namespace:sub_mags
execute if score $sa namespace matches 0 run function namespace:add_mags