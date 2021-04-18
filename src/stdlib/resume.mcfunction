# tellraw @a {"nbt":"rec", "storage": "namespace:main"}
execute store result score $rectemp namespace run data get storage namespace:main rec[-1]
function namespace:tree/recover
execute if data storage namespace:main rec[0] run function namespace:resume