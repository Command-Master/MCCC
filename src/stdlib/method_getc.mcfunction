scoreboard players set $r0 namespace -1
execute if data storage namespace:main input[-1] store result score $r0 namespace run data get storage namespace:main input[-1]
execute if data storage namespace:main input[-1] run data remove storage namespace:main input[-1]