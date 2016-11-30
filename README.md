# fieldguide
# TENTATIVE DOCUMENT
plant identification program

About
=========
Plant identification programs available right now rely on the standard
approach to image recognition: feed a neural net a ton of labeled photos
of plant species, then verify it works on some unlabeled data. The idea
here is to use a convolutional neural net to recognize common structures
in plants, then identify the unique traits to these structures that mark
it as a particular species, similar to how a biologist would identify a
plant. This approach has its limits. Plants are too diverse to rely on this
for general-purpose recognition, but I just want to see if I can do it.

Plan
=========
First, build a simple image classifier -- a hello world of deep learning.

Next, build a convolutional neural net.

Now the real work begins.

Design the nodes to pick up on key plant structures (shape of blade, midrib
design, etc.). A leaf is far from universal, but common and diverse enough
that I think it will be a good starting point.

Establish scope. For now, just a few local plants will do. The important
thing is that it works.

Get as much training data as possible. Consider what kinds of photos the
user will be taking of plants. Guidelines can be provided, but the training
set should be robust.

Train it. Test it. Fix it. Repeat.
