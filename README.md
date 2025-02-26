# GausSMILES
A chemistry program used to convert SMILES to cartesian coordinates with a connectivity matrix for use in Gaussian and other molecular viewing software

Just run and input a smiles. ex.: C1CCCCC1 for cyclohexane.

You will get something that looks like this:
```
C1CCCCC1

0 1
 C    0.315203  -1.385625  -0.314350
 C    1.460570  -0.356793  -0.219389
 C    0.980088   1.069206   0.119788
 C   -0.436774   1.328689  -0.402415
 C   -1.460569   0.356793   0.219389
 C   -0.858516  -1.012271   0.596977
 H   -0.048168  -1.440887  -1.364342
 H    0.696302  -2.392402  -0.037791
 H    2.184229  -0.681830   0.559650
 H    2.004733  -0.341464  -1.188865
 H    1.681002   1.811666  -0.319298
 H    0.988353   1.211215   1.223120
 H   -0.732262   2.375561  -0.174228
 H   -0.439153   1.212660  -1.508808
 H   -2.291811   0.207020  -0.503686
 H   -1.897150   0.816276   1.132901
 H   -0.501033  -0.982990   1.650032
 H   -1.645042  -1.794825   0.531316

 1 2 1.0 6 1.0 7 1.0 8 1.0
 2 1 1.0 3 1.0 9 1.0 10 1.0
 3 2 1.0 4 1.0 11 1.0 12 1.0
 4 3 1.0 5 1.0 13 1.0 14 1.0
 5 4 1.0 6 1.0 15 1.0 16 1.0
 6 5 1.0 1 1.0 17 1.0 18 1.0
 7 1 1.0
 8 1 1.0
 9 2 1.0
 10 2 1.0
 11 3 1.0
 12 3 1.0
 13 4 1.0
 14 4 1.0
 15 5 1.0
 16 5 1.0
 17 6 1.0
 18 6 1.0
```

You may obtain SMILES from a program like ChemDraw and may open this .inp file in a program like ChemCraft and should see cyclohexane.

For use in Gaussian for calculations, you have to do the typical slurm and inp setups though, which you may find use from AutoSlurm? 
