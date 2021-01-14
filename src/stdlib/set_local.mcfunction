execute store result score $search1 namespace run scoreboard players operation $search2 namespace = $index namespace
scoreboard players remove $search1 namespace 1610612736
scoreboard players operation $search1 namespace /= $1024 namespace
scoreboard players operation $search1 namespace *= $1024 namespace
scoreboard players operation $search2 namespace %= $1024 namespace
execute if score $search1 namespace > $stackSize namespace run say AHHAAHHAHAHAHAHAH errorororoor attempting to dereference deallocated memoryryryry@!!!!!!
execute if score $search1 namespace = $stackSize namespace run function namespace:tree/local_set
execute if score $search1 namespace < $stackSize namespace run function namespace:tree/local_copy
execute if score $search1 namespace < $stackSize namespace run function namespace:tree/templ_set
execute if score $search1 namespace < $stackSize namespace run function namespace:tree/local_paste