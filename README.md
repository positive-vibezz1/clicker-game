## miniature-parakeet
### a clicker game made in pygame

a project i started to help me get better with python and game develepment.

the progression with the game halted when i lost motivation and interest, but i will try to push out two more versions

- [x] `first update - code clean up and removing unnecessary code`

- [x] `second update - adding classes and further code cleanup, and maybe more features`
 
- the game shouldn't be to hard to expand upon, and to make the game look prettier


### to add more cubes or upgrades, create a new instance of the class like this

```
upgrade_button_X = Button((600, 300), (50, 50), button_color_red, clicker)

if upgrade_button_X.is_clicked((mousex, mousey), mousepress):
    button functionality code here 

upgrade_button_X.button_render()
```


### to add more text, create a new instance of the class like this
```
text = text((500, 200), "next upgrade in: " + str(your variable here), font2)

#then call your text inside the button class`

if button class:
    button functaionalit)
    text.text = "next upgrade in: " + str(next_upgrade_X)

text.textrender(clicker)
```
