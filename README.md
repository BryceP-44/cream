**Without using any path following algorithm and just using the output of blaze ai, the turtle is able to follow along a pre trained route after finding it by itself.**
<br />
<br />
Here is a single  loop I tried to draw. The turtle did pretty well following it
![cream](https://github.com/BryceP-44/cream/blob/main/cream2.png)
<br />
<br />
Here are a few random loops I drew and you can see the turtle gets lost many times but always finds its way back to one of the trained loops.
![cream](https://github.com/BryceP-44/cream/blob/main/cream4.png)

<br />
The ai only has 4 inputs and 4 outputs which is impressive it is able to actually work. 
<br /><br />
First, pip install keyboard if you don't have it. Then run the program. You get to jetpack around to make a path. Then, press "p" to stop and let blaze ai run. 

The future purpose of blaze ai is to basically reduce the number of data points by clustering and then replacing tight clusters with singular points. 

The blaze ai basically looks around at all the points and thinks "what would the human do in this scenario?" and then does literally the closest thing to
what the human would do. 

It is sort of janky for sure, but as a very first proof of concept I would say this is successful. It would benefit to search for closest points in a
bounding box which would speed it up during  both the training and inferencing. Also, just like in differential equations, my turtle tends to overestimate
the curves around big cricles. 
This is in part due to dt being something like (.0001), but the biggest reasoning is because of the lack of input and output parameters.
<br />
Right now, the 4 inputs are 2 position coordinates and 2 velocity coordinates. The 4 outputs are the 4 arrow keys to control the turtle. If you train an oval,
chances are that the inferencing turtle will make a bigger and bigger oval. This is because when really far away, the turtle is doing it's best job to follow the human behavior. However, the human behavior is based on different conditions, i.e. a very different location corresponding to the same outputs the turtle is trying to replicate.
<br />
<br />
![cream](https://github.com/BryceP-44/cream/blob/main/cream2.png)
