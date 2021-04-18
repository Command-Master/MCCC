execute if score $siga namespace matches 0 run tellraw @a {"text": "division by 0!", "color": "red"}
scoreboard players set $r namespace 1
tellraw @a {"text": "subnormal floats not yet supported for division!", "color": "red"}