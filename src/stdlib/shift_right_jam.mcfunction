#tellraw @a {"score": {"name": "$jam", "objective": "namespace"}}
#tellraw @a {"score": {"name": "$jamby", "objective": "namespace"}}
execute if score $jamby namespace matches 31.. store result score $jammed namespace unless score $jam namespace matches 0
execute unless score $jamby namespace matches 31.. run function namespace:shift_right_jam2
#say jammed:
#tellraw @a {"score": {"name": "$jammed", "objective": "namespace"}}