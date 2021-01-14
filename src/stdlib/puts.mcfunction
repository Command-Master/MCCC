function namespace:get_heap
# value
execute unless score $value namespace matches 10 unless score $value namespace matches 0 run function namespace:tree/putc
execute if score $value namespace matches 10 run tellraw @a {"nbt":"ibuffer", "storage":"namespace:main", "interpret": true}
execute if score $value namespace matches 10 run data modify storage namespace:main ibuffer set value []
scoreboard players add $index namespace 1
execute unless score $value namespace matches 0 run function namespace:puts