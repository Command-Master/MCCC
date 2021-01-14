# magic sign thing:
execute store result score $sa namespace if score $aval namespace matches ..-1
execute store result score $sb namespace if score $bval namespace matches ..-1
scoreboard players operation $sa namespace += $sa namespace
scoreboard players operation $sb namespace += $sb namespace
scoreboard players remove $sa namespace 1
scoreboard players remove $sb namespace 1
scoreboard players operation $sa namespace *= $sb namespace
#magic sign end - sa is sub/add

tellraw @a[tag=fdebug] ["subing: ", {"score": {"name": "$aval", "objective": "namespace"}}]
tellraw @a[tag=fdebug] ["subing: ", {"score": {"name": "$bval", "objective": "namespace"}}]
execute if score $sa namespace matches -1 run function namespace:add_mags
execute if score $sa namespace matches 1 run function namespace:sub_mags