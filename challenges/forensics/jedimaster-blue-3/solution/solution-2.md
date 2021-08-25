# Introduction
This is not a fully fledged solution guide as I never actually attempted this solution. That being
said, it would likely be possible if you could find/build the tools to do it.

# Solution
It so happened that the flag for this challenge was stored on a sign. While the user didn't know this, 
sign data can be incredibly valueable when performing any kind of minecraft forensices for several
reasons:
- Signs don't generate naturally, so they are a good sign of some kind of player interaction
- They can contain text, which can often be hints or instructions of some kind.
- In rare cases like this one, they may contain a plaintext flag.

It may be possible to parse the region files and pull out all the sign data, including information
such as location and contents. Even just the locations of the flags can sometimes be helpful as you
can then teleport to that location to see it in the real world.

While researching this solution, I could not find a tool that could actually do this, however there
may be a couple repositories and/or mods that have this capability. Even without this, it may be
possible to quickly build such a tool.

If anyone continues to explore this possibility of a solution, let me know. I'd love to know if
more extensive research happens to find a way to complete this solution.
