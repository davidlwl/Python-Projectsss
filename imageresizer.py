from PIL import Image
catIm = Image.open(r'C:\Users\Davidlwl\Desktop\zophie.png')
catIm.size
width, height = catIm.size
svelteIm = catIm.resize((width, height + 9000))
svelteIm.save('svelte.png')
