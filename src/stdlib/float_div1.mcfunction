execute if score $siga namespace matches 0 run scoreboard players set $out namespace 0
execute if score $siga namespace matches 0 run scoreboard players set $r namespace 1
execute if score $r namespace matches 0 run tellraw @a {"text": "subnormal floats not yet supported for division!", "color": "red"}