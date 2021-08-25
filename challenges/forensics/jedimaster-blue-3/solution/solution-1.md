# Background
A little background on world generation. Minecraft doesn't put in the effort to generate and save the world until
someone has travelled to a specific location. When it does generate the world, it does it in pieces called "chunks"
which are 16x256x16 "blocks" (blocks are the smalled unit we will discuss here). It then saves these generated
chunks into files called "Region files". Every single one of these has it's own coordinate system with (0,0) being
the center of the world in all three models.

In all three models:
- x represents east to west (from -60,000,000 to 60,000,000)
- y represents height (from 0 to 256)
- z represents south to north (from -60,000,000 to 60,000,000)

When discussing coordinates for both chunks and regions, there is no y axis, as a chunk (and region) will always span
the whole range of the y axis (from 0 to 256).

So, how do these all fit together (exactly):
1 block = smallest unit (technically is supposed to represent one meter in the real world)
1 chunk = 16 x 256 x 16 blocks
1 region = 32 x 32 chunks

This can also be used to convert from one coordinate system to another. For example, (insert coordinate example)

# Solution
Looking at the region directories, it is pretty readily obvious that the region generation that exists in the World
save is a little a-typical. There are a large number of region files that exist way outside the bounds of what we would
typically expect. This should be oddly suspisious. How did these region files get generated? Why are they there?

From here, there are two paths that can be taken.
- The longer (and more standard path) is to visit each of the strange regions and explore to see if there is anything
unusual about these locations.
- The second option is a slight modification of the first. Looking at the region files, one of the groupings of region
files containers more region files and more raw data than the others. This is a strong indication that some player
activity may have occurred there.
- Both of these stratagies can be made more efficient by attempting to find the centermost region file before
exploration. The reason this is helpful is because the most likely cause of the extra region files is user teleportation.
Since chunks are generated in a square around the user, teleporting to the center is most likely to give you
a better picture of the world.

Upon travelling to these chunks, an exploring a little, eventually a beacon will be found, and at the base of the
beacon, there are a number of signs, one of which has the flag on it.

This solution can be assisted with tools such as NBT Explorer.

# Helpful Tools
- [NBT Explorer](https://github.com/jaquadro/NBTExplorer/releases)
- [Dinnerbone Coordinate Tools](https://dinnerbone.com/minecraft/tools/coordinates/)
